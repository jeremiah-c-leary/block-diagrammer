
from block_diagrammer import token


class New():

    def __init__(self, lines: list):
        self.tokens = []
        self.generate_tokens(lines) 
        self.rows = get_max_row_number(self.tokens) + 1
        self.columns = get_max_column_number(self.tokens) + 1

    def generate_tokens(self, lines: list):
        for row, line in enumerate(lines):
            tokens = token.tokenize(line)
            assign_row_to_tokens(tokens, row)
            self.tokens.extend(tokens)
        assign_column(self.tokens)

    def get_tokens_from_column(self, column: int):
        lReturn = []
        for row in range(0, self.rows):
            for token in self.tokens:
                 if token.row == row and token.column == column:
                     lReturn.append(token)
                     break
            else:
                lReturn.append(None)
        return lReturn


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
