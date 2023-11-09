
from block_diagrammer import token


class New():

    def __init__(self, diagram: object):
        self.diagram = diagram
        self.columns = []
        self.rendered = None

    def expand_arrow(self, oToken: object, width: int):
        lExpanded = []
        lExpanded.append(empty_line(width))

        sLeft = oToken.value[0]
        sRight = oToken.value[-1]
        lExpanded.append(']' + sLeft + '-' * (width - 2) + sRight + '[')

        lExpanded.append(empty_line(width))
        return lExpanded

    def expand_start_arrow(self, oToken: object, width: int):
        lExpanded = []
        lExpanded.append(empty_line(width))

        sLeft = oToken.value[0]

        lExpanded.append(']' + sLeft + '-' * width)
        lExpanded.append(empty_line(width))

        return lExpanded

    def expand_middle_arrow(self, oToken: object, width: int):
        lExpanded = []
        lExpanded.append(empty_line(width))

        lExpanded.append('-' + '-' * width + '-')
        lExpanded.append(empty_line(width))
        return lExpanded

    def expand_end_arrow(self, oToken: object, width: int):
        lExpanded = []
        lExpanded.append(empty_line(width))
        sRight = oToken.value[-1]
        lExpanded.append('-' * width + sRight + '[')
        lExpanded.append(empty_line(width))
        return lExpanded

    def expand_each_column(self):
        for column in range(0, self.diagram.get_number_of_columns()):
            self.columns.append([])
            for oToken in self.diagram.get_tokens_from_column(column):
                lTemp = self.expand_token(oToken, column)
                self.columns[column].extend(lTemp)

    def expand_blank_node(self, oToken, width: int):
        lExpanded = []
        lExpanded.append(empty_node_line(width))
        lExpanded.append(empty_node_line(width))
        lExpanded.append(empty_node_line(width))
        return lExpanded

    def expand_top_node(self, oToken, width: int):
        lExpanded = []
        lExpanded.append(bar_node_line(width))
        lExpanded.append(value_node_line(width, oToken.value))
        lExpanded.append(empty_node_line(width))
        return lExpanded

    def expand_bottom_node(self, oToken, width: int):
        lExpanded = []
        lExpanded.append(empty_node_line(width))
        lExpanded.append(empty_node_line(width))
        lExpanded.append(bar_node_line(width))
        return lExpanded

    def expand_node(self, oToken: object, width: int):
        return self.expand_value_node(oToken, width)

    def expand_token(self, oToken: object, column: int):
        column_width = self.diagram.get_column_width(column)
        if isinstance(oToken, token.TopNode):
            return self.expand_top_node(oToken, column_width)
        elif isinstance(oToken, token.MiddleNode):
            return self.expand_blank_node(oToken, column_width)
        elif isinstance(oToken, token.BottomNode):
            return self.expand_bottom_node(oToken, column_width)
        elif isinstance(oToken, token.Node):
            return self.expand_node(oToken, column_width)
        elif isinstance(oToken, token.StartArrow):
            return self.expand_start_arrow(oToken, column_width)
        elif isinstance(oToken, token.MiddleArrow):
            return self.expand_middle_arrow(oToken, column_width)
        elif isinstance(oToken, token.EndArrow):
            return self.expand_end_arrow(oToken, column_width)
        elif isinstance(oToken, token.Arrow):
            return self.expand_arrow(oToken, column_width)
        else:
            return self.expand_empty(column_width)

    def expand_empty(self, width: int):
        lExpanded = []
        lExpanded.append(empty_line(width))
        lExpanded.append(empty_line(width))
        lExpanded.append(empty_line(width))
        return lExpanded

    def expand_value_node(self, oToken: object, width: int):
        lExpanded = []
        lExpanded.append(bar_node_line(width))
        lExpanded.append(value_node_line(width, oToken.value))
        lExpanded.append(bar_node_line(width))
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


def empty_line(width: int):
    return ' ' + ' ' * width + ' '


def empty_node_line(width: int):
    return '|' + ' ' * width + '|'


def bar_node_line(width: int):
    return '+' + '-' * width + '+'


def value_node_line(width: int, value: str):
    return '|' + value.center(width) + '|'
