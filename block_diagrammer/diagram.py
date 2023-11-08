
from block_diagrammer import token


class New():

    def __init__(self, lines: list):
        self.map = []
        self.generate_tokens(lines) 

    def generate_tokens(self, lines: list):
        lTokens = tokenize_lines(lines)
        assign_column(lTokens)
        self.populate_map(lTokens)

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

    def get_tokens_from_column(self, column: int):
        lReturn = []
        for row in range(0, self.rows):
            lReturn.append(self.map[row][column])

        return lReturn

    def get_tokens_from_row(self, row: int):
        return self.map[row]

    def get_number_of_columns(self):
        return self.columns


def assign_row_to_tokens(tokens: list, row: int):
    for token in tokens:
        token.row = row
        

def assign_column(tokens: list):
#    print('Hello')
    dIndexes = {}
    for oToken in tokens:
        dIndexes[oToken.start] = []    
#    print(dIndexes)
    for oToken in tokens:
        dIndexes[oToken.start].append(oToken)
#    print(dIndexes)
    lIndexes = list(dIndexes.keys())
    lIndexes.sort()
#    print(lIndexes)
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

