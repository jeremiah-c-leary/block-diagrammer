
import unittest

from block_diagrammer import diagram
from block_diagrammer.render import svg


class test(unittest.TestCase):

    def test_two_nodes_with_one_arrow(self):
        lLines = ['|A| ----> |B|']

        dDiagram = {}
        dDiagram['diagram'] = {}
        dDiagram['diagram']['lines'] = lLines

        oDiagram = diagram.New(dDiagram)

        oRenderer = text.New(oDiagram)

        lExpected = []
        lExpected.append('+-----+       +-----+')
        lExpected.append('|  A  |]---->[|  B  |')
        lExpected.append('+-----+       +-----+')

        lActual = oRenderer.render()
        self.assertEqual(lExpected, lActual)

    def test_three_nodes_with_two_arrow(self):
        lLines = ['|A| ----> |B| <---> |C|']
        oDiagram = diagram.New(lLines)
        oRenderer = text.New(oDiagram)

        lExpected = []
        lExpected.append('+-----+       +-----+       +-----+')
        lExpected.append('|  A  |]---->[|  B  |]<--->[|  C  |')
        lExpected.append('+-----+       +-----+       +-----+')

        lActual = oRenderer.render()
        self.assertEqual(lExpected, lActual)

    def test_four_nodes_with_two_arrow(self):
        lLines = []
        lLines.append('|A| ----> |B|')
        lLines.append('|C| <---- |D|')
        oDiagram = diagram.New(lLines)
        oRenderer = text.New(oDiagram)

        lExpected = []
        lExpected.append('+-----+       +-----+')
        lExpected.append('|  A  |]---->[|  B  |')
        lExpected.append('+-----+       +-----+')
        lExpected.append('+-----+       +-----+')
        lExpected.append('|  C  |]<----[|  D  |')
        lExpected.append('+-----+       +-----+')

        lActual = oRenderer.render()
        self.assertEqual(lExpected, lActual)

    def test_one_2_high_node_with_two_1_high_nodes(self):
        lLines = []
        lLines.append('|A| ----> |B|')
        lLines.append('|A| <---- |C|')
        oDiagram = diagram.New(lLines)
        oRenderer = text.New(oDiagram)

        lExpected = []
        lExpected.append('+-----+       +-----+')
        lExpected.append('|  A  |]---->[|  B  |')
        lExpected.append('|     |       +-----+')
        lExpected.append('|     |       +-----+')
        lExpected.append('|     |]<----[|  C  |')
        lExpected.append('+-----+       +-----+')

        lActual = oRenderer.render()
        self.assertEqual(lExpected, lActual)

    def test_one_3_high_node_with_one_2_high_node_and_one_1_high_node_with_bounded_values(self):
        lLines = []
        lLines.append('|A| ----> |B|')
        lLines.append('| |       |B|')
        lLines.append('|A| <---- |C|')
        oDiagram = diagram.New(lLines)
        oRenderer = text.New(oDiagram)

        lExpected = []
        lExpected.append('+-----+       +-----+')
        lExpected.append('|  A  |]---->[|  B  |')
        lExpected.append('|     |       |     |')
        lExpected.append('|     |       |     |')
        lExpected.append('|     |       |     |')
        lExpected.append('|     |       +-----+')
        lExpected.append('|     |       +-----+')
        lExpected.append('|     |]<----[|  C  |')
        lExpected.append('+-----+       +-----+')

        lActual = oRenderer.render()
        self.assertEqual(lExpected, lActual)

    def test_one_3_high_node_with_one_2_high_node_and_one_1_high_node(self):
        lLines = []
        lLines.append('|A| ----> |B|')
        lLines.append('| |       | |')
        lLines.append('| | <---- |C|')
        oDiagram = diagram.New(lLines)
        oRenderer = text.New(oDiagram)

        lExpected = []
        lExpected.append('+-----+       +-----+')
        lExpected.append('|  A  |]---->[|  B  |')
        lExpected.append('|     |       |     |')
        lExpected.append('|     |       |     |')
        lExpected.append('|     |       |     |')
        lExpected.append('|     |       +-----+')
        lExpected.append('|     |       +-----+')
        lExpected.append('|     |]<----[|  C  |')
        lExpected.append('+-----+       +-----+')

        lActual = oRenderer.render()
        self.assertEqual(lExpected, lActual)

    def test_multiple_nodes_version1(self):
        lLines = []
        lLines.append("|A| ----> |B| <---> |C|")
        lLines.append("          | | <---> |C|")
        lLines.append("|D| <---> | |          ")
        lLines.append("          |B| <---- |E|")
        lLines.append("          |F| ----->|E|")
        oDiagram = diagram.New(lLines)
        oRenderer = text.New(oDiagram)

        lExpected = []
        lExpected.append('+-----+       +-----+       +-----+')
        lExpected.append('|  A  |]---->[|  B  |]<--->[|  C  |')
        lExpected.append('+-----+       |     |       |     |')
        lExpected.append('              |     |       |     |')
        lExpected.append('              |     |]<--->[|     |')
        lExpected.append('              |     |       +-----+')
        lExpected.append('+-----+       |     |              ')
        lExpected.append('|  D  |]<--->[|     |              ')
        lExpected.append('+-----+       |     |              ')
        lExpected.append('              |     |       +-----+')
        lExpected.append('              |     |]<----[|  E  |')
        lExpected.append('              +-----+       |     |')
        lExpected.append('              +-----+       |     |')
        lExpected.append('              |  F  |]---->[|     |')
        lExpected.append('              +-----+       +-----+')

        lActual = oRenderer.render()
        self.assertEqual(lExpected, lActual)

    def test_expanding_arrows_across_columns(self):
        lLines = []
        lLines.append("|A| ----> |B| <---> |C|       |X|")
        lLines.append("|A| --------------> |C| <---> | |")
        lLines.append("|D| <-------------> |E|")
        lLines.append("          |Y| <---- | | <---> |W|")
        lLines.append("|Z| ------------------------> |W|")
        oDiagram = diagram.New(lLines)
        oRenderer = text.New(oDiagram)

        lExpected = []
        lExpected.append('+-----+       +-----+       +-----+       +-----+')
        lExpected.append('|  A  |]---->[|  B  |]<--->[|  C  |       |  X  |')
        lExpected.append('|     |       +-----+       |     |       |     |')
        lExpected.append('|     |                     |     |       |     |')
        lExpected.append('|     |]------------------>[|     |]<--->[|     |')
        lExpected.append('+-----+                     +-----+       +-----+')
        lExpected.append('+-----+                     +-----+              ')
        lExpected.append('|  D  |]<----------------->[|  E  |              ')
        lExpected.append('+-----+                     |     |              ')
        lExpected.append('              +-----+       |     |       +-----+')
        lExpected.append('              |  Y  |]<----[|     |]<--->[|  W  |')
        lExpected.append('              +-----+       +-----+       |     |')
        lExpected.append('+-----+                                   |     |')
        lExpected.append('|  Z  |]-------------------------------->[|     |')
        lExpected.append('+-----+                                   +-----+')

        lActual = oRenderer.render()
        self.assertEqual(lExpected, lActual)

