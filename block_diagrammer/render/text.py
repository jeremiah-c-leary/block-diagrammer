
from block_diagrammer import token


class New():

    def __init__(self, diagram: object):
        self.diagram = diagram
        self.columns = []
        self.rendered = None

    def expand_arrow(self, oToken: object):
#E        print(f'::{oToken.value}::')
        lExpanded = []
        add_blank_line(lExpanded)
        if oToken.value.isspace():
            add_blank_line(lExpanded)
        else:
            sValue = oToken.value.strip()
             
            sLeft = sValue[0]
            sRight = sValue[-1] 
            lExpanded.append(f']{sLeft}---{sRight}[')
        add_blank_line(lExpanded)
        return lExpanded

    def expand_each_column(self):
        for column in range(0, self.diagram.get_number_of_columns()):
            self.columns.append([])
            for oToken in self.diagram.get_tokens_from_column(column):
                lTemp = self.expand_token(oToken)
                self.columns[column].extend(lTemp)

    def merge_nodes_in_column(self):
        for column in range(0, self.diagram.get_number_of_columns(), 2):
            sPreviousRow = ''
            iLastRow = len(self.columns[column]) - 1
            for row in range(0, len(self.columns[column])):
                sRow = self.columns[column][row]
                if row == 0 and sRow == '|     |':
 #                   print('Got Here')
                    self.columns[column][row] = '+-----+'
                elif row == iLastRow and sRow == '|     |':
                    self.columns[column][row] = '+-----+'
                else:
                    if sRow == '+-----+' and sPreviousRow == '|     |':
                        self.columns[column][row] = '|     |'
                    if sRow == '|     |' and sPreviousRow == '+-----+' and row > 1:
                        self.columns[column][row - 1] = '|     |'
                sPreviousRow = self.columns[column][row]

    def expand_blank_node(self, oToken):
        lExpanded = []
        lExpanded.append('|     |')
        lExpanded.append('|     |')
        lExpanded.append('|     |')
        return lExpanded

    def expand_node(self, oToken: object):
        if oToken.value.isspace():
            return self.expand_blank_node(oToken)
        else:
            return self.expand_value_node(oToken)

    def expand_token(self, oToken: object):
        if isinstance(oToken, token.Node):
            return self.expand_node(oToken)
        elif isinstance(oToken, token.Arrow):
            return self.expand_arrow(oToken)
        else:
            return self.expand_empty()

    def expand_empty(self):
        lExpanded = []
        lExpanded.append('       ')
        lExpanded.append('       ')
        lExpanded.append('       ')
        return lExpanded

    def expand_value_node(self, oToken):
        lExpanded = []
        lExpanded.append('+-----+')
        lExpanded.append(f'|  {oToken.value}  |')
        lExpanded.append('+-----+')
        return lExpanded

    def render_by_row(self):
        self.rendered = []
        for row in range(0, len(self.columns[0])):
            sRow = ''
            for column in range(0, len(self.columns)):
                sRow += self.columns[column][row]
            self.rendered.append(sRow)

    def render(self):
        self.expand_each_column()
#        self.merge_nodes_in_column()
        self.render_by_row()
        return self.rendered



def add_blank_line(lines: list):
    lines.append('       ')


class Cell():

    def __init__(self):
        lines = []

