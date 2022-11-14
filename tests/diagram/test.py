
import unittest

from block_diagrammer import diagrams
from block_diagrammer import token


class test(unittest.TestCase):

    def test_diagram_tokenizes_single_line(self):

        lLines = ['|A| ----> |B| <----> |C|']

        lExpected = []
        lExpected.append(token.Node('A', 0, 2))
        lExpected.append(token.Node('B', 10, 12))
        lExpected.append(token.Node('C', 21, 23))
        lExpected.append(token.Arrow(' ----> ', 3, 9))
        lExpected.append(token.Arrow(' <----> ', 13, 20))
        for oToken in lExpected:
            oToken.row = 0
        lExpected[0].column = 0
        lExpected[1].column = 2
        lExpected[2].column = 4
        lExpected[3].column = 1
        lExpected[4].column = 3


        oDiagram = diagrams.New(lLines)
        lActual = oDiagram.tokens

        self.assertEqual(lExpected, lActual)
        self.assertEqual(1, oDiagram.rows)
        self.assertEqual(5, oDiagram.columns)

    def test_diagram_tokenizes_two_lines(self):

        lLines = []
        lLines.append('|A| ----> |B| <----> |C|')

        lFirstRow = []
        lFirstRow.append(token.Node('A', 0, 2))
        lFirstRow.append(token.Node('B', 10, 12))
        lFirstRow.append(token.Node('C', 21, 23))
        lFirstRow.append(token.Arrow(' ----> ', 3, 9))
        lFirstRow.append(token.Arrow(' <----> ', 13, 20))
        for oToken in lFirstRow:
            oToken.row = 0
        lFirstRow[0].column = 0
        lFirstRow[1].column = 2
        lFirstRow[2].column = 4
        lFirstRow[3].column = 1
        lFirstRow[4].column = 3

        lLines.append('          |B| <----> |C|')
        lSecondRow = []
        lSecondRow.append(token.Node('B', 10, 12))
        lSecondRow.append(token.Node('C', 21, 23))
        lSecondRow.append(token.Arrow(' <----> ', 13, 20))
        for oToken in lSecondRow:
            oToken.row = 1
        lSecondRow[0].column = 2
        lSecondRow[1].column = 4
        lSecondRow[2].column = 3

        lExpected = []
        lExpected.extend(lFirstRow)
        lExpected.extend(lSecondRow)

        oDiagram = diagrams.New(lLines)
        lActual = oDiagram.tokens

        self.assertEqual(lExpected, lActual)
        self.assertEqual(2, oDiagram.rows)
        self.assertEqual(5, oDiagram.columns)

    def test_diagram_tokenizes_three_lines(self):

        lLines = []
        lLines.append('|A| ----> |B| <----> |C|')

        lFirstRow = []
        lFirstRow.append(token.Node('A', 0, 2))
        lFirstRow.append(token.Node('B', 10, 12))
        lFirstRow.append(token.Node('C', 21, 23))
        lFirstRow.append(token.Arrow(' ----> ', 3, 9))
        lFirstRow.append(token.Arrow(' <----> ', 13, 20))
        for oToken in lFirstRow:
            oToken.row = 0
        lFirstRow[0].column = 0
        lFirstRow[1].column = 2
        lFirstRow[2].column = 4
        lFirstRow[3].column = 1
        lFirstRow[4].column = 3

        lLines.append('          | | <----> | |')
        lSecondRow = []
        lSecondRow.append(token.Node(' ', 10, 12))
        lSecondRow.append(token.Node(' ', 21, 23))
        lSecondRow.append(token.Arrow(' <----> ', 13, 20))
        for oToken in lSecondRow:
            oToken.row = 1
        lSecondRow[0].column = 2
        lSecondRow[1].column = 4
        lSecondRow[2].column = 3

        lLines.append('|D| ----> | | <----> |E| ----> |F|')

        lThirdRow = []
        lThirdRow.append(token.Node('D', 0, 2))
        lThirdRow.append(token.Node(' ', 10, 12))
        lThirdRow.append(token.Node('E', 21, 23))
        lThirdRow.append(token.Node('F', 31, 33))
        lThirdRow.append(token.Arrow(' ----> ', 3, 9))
        lThirdRow.append(token.Arrow(' <----> ', 13, 20))
        lThirdRow.append(token.Arrow(' ----> ', 24, 30))
        for oToken in lThirdRow:
            oToken.row = 2
        lThirdRow[0].column = 0
        lThirdRow[1].column = 2
        lThirdRow[2].column = 4
        lThirdRow[3].column = 6
        lThirdRow[4].column = 1
        lThirdRow[5].column = 3
        lThirdRow[6].column = 5

        lExpected = []
        lExpected.extend(lFirstRow)
        lExpected.extend(lSecondRow)
        lExpected.extend(lThirdRow)

        oDiagram = diagrams.New(lLines)
        lActual = oDiagram.tokens

        self.assertEqual(lExpected, lActual)
        self.assertEqual(3, oDiagram.rows)
        self.assertEqual(7, oDiagram.columns)

    def test_diagram_get_tokens_from_column_method(self):

        lLines = []
        lLines.append('|A| ----> |B| <----> |C|')

        lFirstRow = []
        lFirstRow.append(token.Node('A', 0, 2))
        lFirstRow.append(token.Node('B', 10, 12))
        lFirstRow.append(token.Node('C', 21, 23))
        lFirstRow.append(token.Arrow(' ----> ', 3, 9))
        lFirstRow.append(token.Arrow(' <----> ', 13, 20))
        for oToken in lFirstRow:
            oToken.row = 0
        lFirstRow[0].column = 0
        lFirstRow[1].column = 2
        lFirstRow[2].column = 4
        lFirstRow[3].column = 1
        lFirstRow[4].column = 3

        lLines.append('          | | <----> | |')
        lSecondRow = []
        lSecondRow.append(token.Node(' ', 10, 12))
        lSecondRow.append(token.Node(' ', 21, 23))
        lSecondRow.append(token.Arrow(' <----> ', 13, 20))
        for oToken in lSecondRow:
            oToken.row = 1
        lSecondRow[0].column = 2
        lSecondRow[1].column = 4
        lSecondRow[2].column = 3

        lLines.append('|D| ----> | | <----> |E| ----> |F|')

        lThirdRow = []
        lThirdRow.append(token.Node('D', 0, 2))
        lThirdRow.append(token.Node(' ', 10, 12))
        lThirdRow.append(token.Node('E', 21, 23))
        lThirdRow.append(token.Node('F', 31, 33))
        lThirdRow.append(token.Arrow(' ----> ', 3, 9))
        lThirdRow.append(token.Arrow(' <----> ', 13, 20))
        lThirdRow.append(token.Arrow(' ----> ', 24, 30))
        for oToken in lThirdRow:
            oToken.row = 2
        lThirdRow[0].column = 0
        lThirdRow[1].column = 2
        lThirdRow[2].column = 4
        lThirdRow[3].column = 6
        lThirdRow[4].column = 1
        lThirdRow[5].column = 3
        lThirdRow[6].column = 5

        oDiagram = diagrams.New(lLines)

        ## Test column 0
        lActual = oDiagram.get_tokens_from_column(0)

        lExpectedColumn0 = []
        lExpectedColumn0.append(lFirstRow[0])
        lExpectedColumn0.append(None)
        lExpectedColumn0.append(lThirdRow[0])
        self.assertEqual(lExpectedColumn0, lActual)

        ## Test column 1
        lActual = oDiagram.get_tokens_from_column(1)

        lExpectedColumn0 = []
        lExpectedColumn0.append(lFirstRow[3])
        lExpectedColumn0.append(None)
        lExpectedColumn0.append(lThirdRow[4])
        self.assertEqual(lExpectedColumn0, lActual)

        ## Test column 6
        lActual = oDiagram.get_tokens_from_column(6)

        lExpectedColumn0 = []
        lExpectedColumn0.append(None)
        lExpectedColumn0.append(None)
        lExpectedColumn0.append(lThirdRow[3])
        self.assertEqual(lExpectedColumn0, lActual)



