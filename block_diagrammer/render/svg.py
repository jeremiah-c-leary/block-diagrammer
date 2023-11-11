
from block_diagrammer import token


class New():

    def __init__(self, diagram: object):
        self.diagram = diagram
        self.max_x = 0
        self.max_y = 0
        self.row_height = 40
        self.row_buffer = 2
        self.column_width = 40
        self.rendered = []

    def add_marker(self):
        self.rendered.append('  <defs>')
        self.rendered.append('    <!-- A marker to be used as an arrowhead -->')
        self.rendered.append('    <marker')
        self.rendered.append('      id="arrow"')
        self.rendered.append('      viewBox="0 0 10 10"')
        self.rendered.append('      refX="5"')
        self.rendered.append('      refY="5"')
        self.rendered.append('      markerWidth="6"')
        self.rendered.append('      markerHeight="6"')
        self.rendered.append('      orient="auto-start-reverse">')
        self.rendered.append('      <path d="M 0 0 L 10 5 L 0 10 z" />')
        self.rendered.append('    </marker>')
        self.rendered.append('  </defs>')

    def add_svg_header(self):
        sString = f'<svg viewBox="0 0 {self.max_x} {self.max_y}" xmlns="http://www.w3.org/2000/svg">'
        self.rendered.insert(0, sString)

    def add_svg_footer(self):
        sString = f'</svg>'
        self.rendered.append(sString)

    def draw_multirow_node(self, oToken: object, NodeTopRow: int, row: int, column: int):
        x = column * self.column_width
        y = NodeTopRow * self.row_height + self.row_buffer
        height = (row + 1 - NodeTopRow) * self.row_height - (2 * self.row_buffer)
        fill = get_color_of_node(oToken)
        sString = f'  <rect x="{x}" y="{y}" width="{self.column_width}" height="{height}" fill="{fill}"/>'
        self.rendered.append(sString)
        self.draw_node_text(oToken, NodeTopRow, column)
#        sValue = oToken.value
#        x = x + (self.column_width / 2)
#        y = y - self.row_buffer + (self.row_height / 2)
#        sString = f'  <text x="{x}" y="{y}" dominant-baseline="middle" text-anchor="middle">{sValue}</text>'
#        self.rendered.append(sString)

    def draw_single_node(self, oToken: object, row: int, column: int):
        x = column * self.column_width
        y = row * self.row_height + self.row_buffer
        height = self.row_height - (2 * self.row_buffer)
        fill = get_color_of_node(oToken)
        sString = f'  <rect x="{x}" y="{y}" width="{self.column_width}" height="{height}" fill="{fill}"/>'
        self.rendered.append(sString)
        self.draw_node_text(oToken, row, column)

    def draw_node_text(self, oToken: object, row: int, column: int):
        x = column * self.column_width
        y = row * self.row_height + self.row_buffer
        sValue = oToken.value
        x = x + (self.column_width / 2)
        y = y - self.row_buffer + (self.row_height / 2)
        sString = f'  <text x="{x}" y="{y}" dominant-baseline="middle" text-anchor="middle" fill="white" font-family="Verdana, sans-serif" font-size="6px">{sValue}</text>'
        self.rendered.append(sString)

    def draw_nodes(self):
        for column in self.diagram.get_node_columns():
            lTokens = self.diagram.get_tokens_from_column(column)
            self.max_x = column * self.column_width + self.column_width
            NodeTopRow = 0
            for row in range(0, self.diagram.get_number_of_rows()):
                self.max_y = row * self.row_height + self.row_height
                oToken = lTokens[row]
                if isinstance(oToken, token.TopNode):
                    NodeTopRow = row
                    topNode = oToken
                if isinstance(oToken, token.SingleNode):
                    self.draw_single_node(oToken, row, column)
                if isinstance(oToken, token.BottomNode):
                    self.draw_multirow_node(topNode, NodeTopRow, row, column)

    def draw_left_port(self, row: int, column: int):
        x = column * self.column_width
        y = row * self.row_height + (self.row_height / 2) - 5 
        height = 10
        width = 5 
        sString = f'  <rect x="{x}" y="{y}" width="{width}" height="{height}" fill="black" />'
        self.rendered.append(sString)

    def draw_right_port(self, row: int, column: int):
        x = column * self.column_width + self.column_width - 5
        y = row * self.row_height + (self.row_height / 2) - 5 
        height = 10
        width = 5
        sString = f'  <rect x="{x}" y="{y}" width="{width}" height="{height}" fill="black" />'
        self.rendered.append(sString)

    def has_start_arrow(self, row: int, column: int):
        oToken = self.diagram.map[row][column]
        if oToken.value.startswith('<'):
            return True
        return False

    def has_end_arrow(self, row: int, column: int):
        oToken = self.diagram.map[row][column]
        if oToken.value.endswith('>'):
            return True
        return False

    def draw_single_arrow(self, row: int, column: int):
        x1 = column * self.column_width + 5
        x2 = column * self.column_width + self.column_width - 5
        y = row * self.row_height + (self.row_height / 2)
        sString = f'  <line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="black"'
        if self.has_start_arrow(row, column):
            sString += ' marker-start="url(#arrow)"'
        if self.has_end_arrow(row, column):
            sString += ' marker-end="url(#arrow)"'
        sString += ' />'
        self.rendered.append(sString)

    def draw_multi_arrow(self, row: int, firstColumn: int, secondColumn):
        x1 = firstColumn * self.column_width + 5
        x2 = secondColumn * self.column_width + self.column_width - 5
        y = row * self.row_height + (self.row_height / 2)
        sString = f'  <line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="black"'
        if self.has_start_arrow(row, firstColumn):
            sString += ' marker-start="url(#arrow)"'
        if self.has_end_arrow(row, secondColumn):
            sString += ' marker-end="url(#arrow)"'
        sString += ' />'
        self.rendered.append(sString)

    def draw_ports(self):
        self.rendered.append('  <!-- Ports -->')
        for row in range(0, self.diagram.get_number_of_rows()):
            lTokens = self.diagram.get_tokens_from_row(row)
            NodeLeftColumn = 0
#            print(lTokens)
            for column in range(1, self.diagram.get_number_of_columns() - 1):
                oToken = lTokens[column]
                if isinstance(oToken, token.SingleArrow):
                    self.draw_left_port(row, column)
                    self.draw_single_arrow(row, column)
                    self.draw_right_port(row, column)
                elif isinstance(oToken, token.StartArrow):
                    self.draw_left_port(row, column)
                    NodeLeftColumn = column
                elif isinstance(oToken, token.EndArrow):
                    self.draw_multi_arrow(row, NodeLeftColumn, column)
                    self.draw_right_port(row, column)


    def render(self):
        self.add_marker()
        self.draw_nodes()
        self.draw_ports()
        self.add_svg_header()
        self.add_svg_footer()
        return self.rendered


def get_color_of_node(oToken: object):
    return oToken.color
