
from block_diagrammer import token


class New():

    def __init__(self, diagram: object):
        self.diagram = diagram
        self.columns = []
        self.rendered = None

    def expand_arrow(self, oToken: object):
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

    def expand_start_arrow(self, oToken: object):
        lExpanded = []
        add_blank_line(lExpanded)
        if oToken.value.isspace():
            add_blank_line(lExpanded)
        else:
            sValue = oToken.value.strip()
             
            sLeft = sValue[0]
            lExpanded.append(f']{sLeft}-----')
        add_blank_line(lExpanded)
        return lExpanded

    def expand_middle_arrow(self, oToken: object):
        lExpanded = []
        add_blank_line(lExpanded)
        if oToken.value.isspace():
            add_blank_line(lExpanded)
        else:
            sValue = oToken.value.strip()
             
            lExpanded.append(f'-------')
        add_blank_line(lExpanded)
        return lExpanded

    def expand_end_arrow(self, oToken: object):
        lExpanded = []
        add_blank_line(lExpanded)
        if oToken.value.isspace():
            add_blank_line(lExpanded)
        else:
            sValue = oToken.value.strip()
             
            sRight = sValue[-1] 
            lExpanded.append(f'-----{sRight}[')
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

    def expand_top_node(self, oToken):
        lExpanded = []
        lExpanded.append('+-----+')
        lExpanded.append(f'|  {oToken.value}  |')
        lExpanded.append('|     |')
        return lExpanded

    def expand_bottom_node(self, oToken):
        lExpanded = []
        lExpanded.append('|     |')
        lExpanded.append('|     |')
        lExpanded.append('+-----+')
        return lExpanded

    def expand_node(self, oToken: object):
        if oToken.value.isspace():
            return self.expand_blank_node(oToken)
        else:
            return self.expand_value_node(oToken)

    def expand_token(self, oToken: object):
        if isinstance(oToken, token.TopNode):
            return self.expand_top_node(oToken)
        elif isinstance(oToken, token.MiddleNode):
            return self.expand_blank_node(oToken)
        elif isinstance(oToken, token.BottomNode):
            return self.expand_bottom_node(oToken)
        elif isinstance(oToken, token.Node):
            return self.expand_node(oToken)
        elif isinstance(oToken, token.StartArrow):
            return self.expand_start_arrow(oToken)
        elif isinstance(oToken, token.MiddleArrow):
            return self.expand_middle_arrow(oToken)
        elif isinstance(oToken, token.EndArrow):
            return self.expand_end_arrow(oToken)
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
        self.render_by_row()
        return self.rendered



def add_blank_line(lines: list):
    lines.append('       ')


class Cell():

    def __init__(self):
        lines = []

