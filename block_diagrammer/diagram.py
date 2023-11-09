
from block_diagrammer import token


class New():

    def __init__(self, lines: list):
        self.map = []
        self.column_widths = []
        self.generate_tokens(lines) 

    def generate_tokens(self, lines: list):
        lTokens = tokenize_lines(lines)
        assign_column(lTokens)
        self.populate_map(lTokens)
        self.calculate_column_widths()
        self.merge_nodes()
        self.expand_arrows_across_columns()


    def populate_map(self, tokens: list):
        self.rows = get_max_row_number(tokens) + 1
        self.columns = get_max_column_number(tokens) + 1
        for row in range(0, self.rows):
            lRow = []
            for column in range(0, self.columns):
                for oToken in tokens:
                    if oToken.row == row and oToken.column == column:
                        lRow.append(oToken)
                        break
                else:
                    lRow.append(token.Empty('', 0, 0))
            self.map.append(lRow)

    def get_column_width(self, column: int):
        return self.column_widths[column]

    def get_tokens_from_column(self, column: int):
        lReturn = []
        for row in range(0, self.rows):
            lReturn.append(self.map[row][column])

        return lReturn

    def get_tokens_from_row(self, row: int):
        return self.map[row]

    def get_number_of_columns(self):
        return self.columns

    def calculate_column_widths(self):
        for column in range(0, self.columns):
            self.column_widths.append(5)
            for row in range(0, self.rows):
                if column % 2 == 0:
                    self.column_widths[column] = max(self.column_widths[column], len(self.map[row][column].value) + 2)
                else:
                    self.column_widths[column] = 5

    def expand_arrows_across_columns(self):
        for row in range(0, self.rows):
            for column in range(1, self.columns - 1):
                if previous_column_is_node(self, row, column) and current_column_is_arrow(self, row, column) and next_column_is_empty(self, row, column):
                    convert_current_token_to_starting_arrow(self, row, column)
                    convert_next_token_to_ending_arrow(self, row, column)
                elif previous_column_is_arrow(self, row, column) and current_column_is_arrow(self, row, column) and next_column_is_empty(self, row, column):
                    convert_current_token_to_middle_arrow(self, row, column)
                    convert_next_token_to_ending_arrow(self, row, column)

    def merge_nodes(self):
        if map_has_single_row(self.map):
            for column in range(0, len(self.map[0]), 2):
                for row in range(0, len(self.map)):
                    self.map[row][column] = self.map[row][column].convert(token.SingleNode)
        else:
            for column in range(0, len(self.map[0]), 2):
                lColumn = self.get_tokens_from_column(column)
                for row in range(0, len(self.map)):
                    if row == 0:
                        if row_below_is_empty(self, row, column):
                            convert_token_to_single(self, row, column)
                        elif row_below_matches_value(self, row, column):
                            convert_token_to_top(self, row, column)
                        elif row_below_has_blank_value(self, row, column):
                            convert_token_to_top(self, row, column)
                            self.map[row+1][column].value = self.map[row][column].value
                    elif row == len(self.map) - 1:
                        if isinstance(self.map[row][column], token.Empty):
                            continue
                        elif row_above_matches_value(self, row, column):
                            convert_token_to_bottom(self, row, column)
                        else:
                            convert_token_to_single(self, row, column)
                    else:

                        if isinstance(self.map[row][column], token.Empty):
                            continue
                        elif row_above_is_empty(self, row, column) and row_below_is_empty(self, row, column):
                            convert_token_to_single(self, row, column)
                        elif row_above_matches_value(self, row, column) and row_below_is_empty(self, row, column):
                            convert_token_to_bottom(self, row, column)
                        elif not row_above_matches_value(self, row, column) and row_below_is_empty(self, row, column):
                            convert_token_to_single(self, row, column)
                        elif row_above_matches_value(self, row, column) and row_below_has_blank_value(self, row, column):
                            convert_token_to_middle(self, row, column)
                            self.map[row+1][column].value = self.map[row][column].value
                        elif row_above_matches_value(self, row, column) and row_below_matches_value(self, row, column):
                            convert_token_to_middle(self, row, column)
                        elif row_above_matches_value(self, row, column) and not row_below_matches_value(self, row, column):
                            convert_token_to_bottom(self, row, column)
                        elif not row_above_matches_value(self, row, column) and row_below_has_blank_value(self, row, column):
                            convert_token_to_top(self, row, column)
                            self.map[row+1][column].value = self.map[row][column].value
                        elif not row_above_matches_value(self, row, column) and row_below_matches_value(self, row, column):
                            convert_token_to_top(self, row, column)


def convert_token_to_middle(self, row: int, column: int):
    self.map[row][column] = self.map[row][column].convert(token.MiddleNode)


def convert_token_to_top(self, row: int, column: int):
    self.map[row][column] = self.map[row][column].convert(token.TopNode)


def convert_token_to_bottom(self, row: int, column: int):
    self.map[row][column] = self.map[row][column].convert(token.BottomNode)


def convert_token_to_single(self, row: int, column: int):
    self.map[row][column] = self.map[row][column].convert(token.SingleNode)


def convert_current_token_to_starting_arrow(self, row: int, column: int):
    self.map[row][column] = self.map[row][column].convert(token.StartArrow)


def convert_next_token_to_ending_arrow(self, row: int, column: int):
    self.map[row][column+1] = self.map[row][column].convert(token.EndArrow)


def convert_current_token_to_middle_arrow(self, row: int, column: int):
    self.map[row][column] = self.map[row][column].convert(token.MiddleArrow)


def row_above_matches_value(self, row: int, column: int):
    if self.map[row-1][column].value == self.map[row][column].value:
        return True
    return False                


def row_below_matches_value(self, row: int, column: int):
    if self.map[row+1][column].value == self.map[row][column].value:
        return True
    return False                


def row_below_has_blank_value(self, row: int, column: int):
    if self.map[row+1][column].value == '':
        return True
    return False


def row_above_is_empty(self, row: int, column: int):
    if isinstance(self.map[row-1][column], token.Empty):
        return True
    return False                


def row_below_is_empty(self, row: int, column: int):
    if isinstance(self.map[row+1][column], token.Empty):
        return True
    return False                


def map_has_single_row(tokenMap: list):
    if len(tokenMap) == 1:
        return True
    return False


def assign_row_to_tokens(tokens: list, row: int):
    for token in tokens:
        token.row = row


def previous_column_is_node(self, row: int, column: int):
    if isinstance(self.map[row][column-1], token.Node):
        return True
    return False


def previous_column_is_arrow(self, row: int, column: int):
    if isinstance(self.map[row][column-1], token.Arrow):
        return True
    return False


def current_column_is_arrow(self, row: int, column: int):
    if isinstance(self.map[row][column], token.Arrow):
        return True
    return False


def next_column_is_empty(self, row: int, column: int):
    if isinstance(self.map[row][column+1], token.Empty):
        return True
    return False


def assign_column(tokens: list):
    dIndexes = {}
    for oToken in tokens:
        dIndexes[oToken.start] = []    
    for oToken in tokens:
        dIndexes[oToken.start].append(oToken)
    lIndexes = list(dIndexes.keys())
    lIndexes.sort()
    for iColumn, iIndex in enumerate(lIndexes):
        for oToken in dIndexes[iIndex]:
            oToken.column = iColumn 


def get_max_column_number(tokens: list):
    return get_max_dict_value(tokens, 'column')


def get_max_row_number(tokens: list):
    return get_max_dict_value(tokens, 'row')


def get_max_dict_value(tokens: list, attribute_name: str):
    iMax = 0
    for token in tokens:
        iMax = max(iMax, token.__dict__[attribute_name])
    return iMax


def tokenize_lines(lines: list):
    lReturn = []
    for row, line in enumerate(lines):
        tokens = token.tokenize(line)
        assign_row_to_tokens(tokens, row)
        lReturn.extend(tokens)
    return lReturn
