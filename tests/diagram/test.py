import unittest

from block_diagrammer import diagram
from block_diagrammer import token

from tests import utils


class test(unittest.TestCase):

    def test_diagram_tokenizes_single_line(self):

        lLines = ['|A| ----> |B| <----> |C|']

        lExpected = []
        lExpected.append(token.SingleNode('A', 0, 2))
        lExpected.append(token.SingleArrow('---->', 3, 9))
        lExpected.append(token.SingleNode('B', 10, 12))
        lExpected.append(token.SingleArrow('<---->', 13, 20))
        lExpected.append(token.SingleNode('C', 21, 23))
        for oToken in lExpected:
            oToken.row = 0
        lExpected[0].column = 0
        lExpected[1].column = 1
        lExpected[2].column = 2
        lExpected[3].column = 3
        lExpected[4].column = 4

        oDiagram = diagram.New(utils.create_diagram_dict(lLines))

        lActual = oDiagram.get_tokens_from_row(0)

        self.assertEqual(lExpected, lActual)
        self.assertEqual(1, oDiagram.rows)
        self.assertEqual(5, oDiagram.columns)

    def test_diagram_tokenizes_two_lines(self):

        lLines = []
        lLines.append('|A| ----> |B| <----> |C|')

        lFirstRow = []
        lFirstRow.append(token.SingleNode('A', 0, 2))
        lFirstRow.append(token.SingleArrow('---->', 3, 9))
        lFirstRow.append(token.TopNode('B', 10, 12))
        lFirstRow.append(token.SingleArrow('<---->', 13, 20))
        lFirstRow.append(token.TopNode('C', 21, 23))
        for oToken in lFirstRow:
            oToken.row = 0
        lFirstRow[0].column = 0
        lFirstRow[1].column = 1
        lFirstRow[2].column = 2
        lFirstRow[3].column = 3
        lFirstRow[4].column = 4

        lLines.append('          |B| <----> |C|')
        lSecondRow = []
        lSecondRow.append(token.Empty('', 0, 0))
        lSecondRow.append(token.Empty('', 0, 0))
        lSecondRow.append(token.BottomNode('B', 10, 12))
        lSecondRow.append(token.SingleArrow('<---->', 13, 20))
        lSecondRow.append(token.BottomNode('C', 21, 23))
        for oToken in lSecondRow[2::]:
            oToken.row = 1
        lSecondRow[2].column = 2
        lSecondRow[3].column = 3 
        lSecondRow[4].column = 4 

        oDiagram = diagram.New(utils.create_diagram_dict(lLines))

        lActual = oDiagram.get_tokens_from_row(0)
        self.assertEqual(lFirstRow, lActual)

        lActual = oDiagram.get_tokens_from_row(1)

        self.assertEqual(lSecondRow, lActual)

        self.assertEqual(2, oDiagram.rows)
        self.assertEqual(5, oDiagram.columns)

    def test_diagram_tokenizes_three_lines(self):

        lLines = []
        lLines.append('|A| ----> |B| <----> |C|')

        lFirstRow = []
        lFirstRow.append(token.SingleNode('A', 0, 2))
        lFirstRow.append(token.SingleArrow('---->', 3, 9))
        lFirstRow.append(token.TopNode('B', 10, 12))
        lFirstRow.append(token.SingleArrow('<---->', 13, 20))
        lFirstRow.append(token.TopNode('C', 21, 23))
        lFirstRow.append(token.Empty('', 0, 0))
        lFirstRow.append(token.Empty('', 0, 0))

        lFirstRow[0].row = 0
        lFirstRow[1].row = 0
        lFirstRow[2].row = 0
        lFirstRow[3].row = 0
        lFirstRow[4].row = 0

        lFirstRow[0].column = 0
        lFirstRow[1].column = 1
        lFirstRow[2].column = 2
        lFirstRow[3].column = 3
        lFirstRow[4].column = 4

        lLines.append('          | | <----> | |')
        lSecondRow = []
        lSecondRow.append(token.Empty('', 0, 0))
        lSecondRow.append(token.Empty('', 0, 0))
        lSecondRow.append(token.MiddleNode('B', 10, 12))
        lSecondRow.append(token.SingleArrow('<---->', 13, 20))
        lSecondRow.append(token.BottomNode('C', 21, 23))
        lSecondRow.append(token.Empty('', 0, 0))
        lSecondRow.append(token.Empty('', 0, 0))

        lSecondRow[2].row = 1
        lSecondRow[3].row = 1
        lSecondRow[4].row = 1

        lSecondRow[2].column = 2
        lSecondRow[3].column = 3
        lSecondRow[4].column = 4

        lLines.append('|D| ----> | | <----> |E| ----> |F|')

        lThirdRow = []
        lThirdRow.append(token.SingleNode('D', 0, 2))
        lThirdRow.append(token.SingleArrow('---->', 3, 9))
        lThirdRow.append(token.BottomNode('B', 10, 12))
        lThirdRow.append(token.SingleArrow('<---->', 13, 20))
        lThirdRow.append(token.SingleNode('E', 21, 23))
        lThirdRow.append(token.SingleArrow('---->', 24, 30))
        lThirdRow.append(token.SingleNode('F', 31, 33))

        for oToken in lThirdRow:
            oToken.row = 2
        lThirdRow[0].column = 0
        lThirdRow[1].column = 1
        lThirdRow[2].column = 2
        lThirdRow[3].column = 3
        lThirdRow[4].column = 4
        lThirdRow[5].column = 5
        lThirdRow[6].column = 6

        lExpected = []
        lExpected.extend(lFirstRow)
        lExpected.extend(lSecondRow)
        lExpected.extend(lThirdRow)

        oDiagram = diagram.New(utils.create_diagram_dict(lLines))

        lActual = oDiagram.get_tokens_from_row(0)
        self.assertEqual(lFirstRow, lActual)
        
        lActual = oDiagram.get_tokens_from_row(1)
        self.assertEqual(lSecondRow, lActual)

        lActual = oDiagram.get_tokens_from_row(2)
        self.assertEqual(lThirdRow, lActual)

        self.assertEqual(3, oDiagram.rows)
        self.assertEqual(7, oDiagram.columns)

    def test_diagram_get_tokens_from_column_method(self):

        lLines = []
        lLines.append('|A| ----> |B| <----> |C|')

        lFirstRow = []
        lFirstRow.append(token.SingleNode('A', 0, 2))
        lFirstRow.append(token.SingleArrow('---->', 3, 9))
        lFirstRow.append(token.TopNode('B', 10, 12))
        lFirstRow.append(token.SingleArrow('<---->', 13, 20))
        lFirstRow.append(token.TopNode('C', 21, 23))
        for oToken in lFirstRow:
            oToken.row = 0
        lFirstRow[0].column = 0
        lFirstRow[1].column = 1
        lFirstRow[2].column = 2
        lFirstRow[3].column = 3
        lFirstRow[4].column = 4

        lLines.append('          | | <----> | |')
        lSecondRow = []
        lSecondRow.append(token.Empty('', 0, 0))
        lSecondRow.append(token.Empty('', 0, 0))
        lSecondRow.append(token.MiddleNode('B', 10, 12))
        lSecondRow.append(token.SingleArrow('<---->', 13, 20))
        lSecondRow.append(token.BottomNode('C', 21, 23))
        for oToken in lSecondRow[2::]:
            oToken.row = 1
        lSecondRow[2].column = 2
        lSecondRow[3].column = 3
        lSecondRow[4].column = 4

        lLines.append('|D| ----> | | <----> |E| ----> |F|')

        lThirdRow = []
        lThirdRow.append(token.SingleNode('D', 0, 2))
        lThirdRow.append(token.SingleArrow('---->', 3, 9))
        lThirdRow.append(token.BottomNode('B', 10, 12))
        lThirdRow.append(token.SingleArrow('<---->', 13, 20))
        lThirdRow.append(token.SingleNode('E', 21, 23))
        lThirdRow.append(token.SingleArrow('---->', 24, 30))
        lThirdRow.append(token.SingleNode('F', 31, 33))
        for oToken in lThirdRow:
            oToken.row = 2
        lThirdRow[0].column = 0
        lThirdRow[1].column = 1
        lThirdRow[2].column = 2
        lThirdRow[3].column = 3
        lThirdRow[4].column = 4
        lThirdRow[5].column = 5
        lThirdRow[6].column = 6

        oDiagram = diagram.New(utils.create_diagram_dict(lLines))

        ## Test column 0
        lActual = oDiagram.get_tokens_from_column(0)

        lExpectedColumn0 = []
        lExpectedColumn0.append(lFirstRow[0])
        lExpectedColumn0.append(token.Empty('', 0, 0))
        lExpectedColumn0.append(lThirdRow[0])
        self.assertEqual(lExpectedColumn0, lActual)

        ## Test column 1
        lActual = oDiagram.get_tokens_from_column(1)

        lExpectedColumn0 = []
        lExpectedColumn0.append(lFirstRow[1])
        lExpectedColumn0.append(token.Empty('', 0, 0))
        lExpectedColumn0.append(lThirdRow[1])
        self.assertEqual(lExpectedColumn0, lActual)

        ## Test column 6
        lActual = oDiagram.get_tokens_from_column(6)

        lExpectedColumn0 = []
        lExpectedColumn0.append(token.Empty('', 0, 0))
        lExpectedColumn0.append(token.Empty('', 0, 0))
        lExpectedColumn0.append(lThirdRow[6])
        self.assertEqual(lExpectedColumn0, lActual)

