
import unittest

from block_diagrammer import diagram
from block_diagrammer.render import text


class test(unittest.TestCase):

    def test_node_expansion(self):
        lLines = ['|A| ----> |B|']
        oDiagram = diagram.New(lLines)
        oRenderer = text.New(oDiagram)

        lExpected = []
        lExpected.append('+-----+')
        lExpected.append('|  A  |')
        lExpected.append('+-----+')

        lActual = oRenderer.expand_node(oDiagram.get_tokens_from_column(0)[0])
        self.assertEqual(lExpected, lActual)

        lExpected = []
        lExpected.append('+-----+')
        lExpected.append('|  B  |')
        lExpected.append('+-----+')

        lActual = oRenderer.expand_node(oDiagram.get_tokens_from_column(2)[0])
        self.assertEqual(lExpected, lActual)

    def test_left_arrow_expansion(self):
        lLines = ['|A| ----> |B|']
        oDiagram = diagram.New(lLines)
        oRenderer = text.New(oDiagram)

        lExpected = []
        lExpected.append('       ')
        lExpected.append(']---->[')
        lExpected.append('       ')

        lActual = oRenderer.expand_arrow(oDiagram.get_tokens_from_column(1)[0])
        self.assertEqual(lExpected, lActual)

    def test_right_arrow_expansion(self):
        lLines = ['|A| <---- |B|']
        oDiagram = diagram.New(lLines)
        oRenderer = text.New(oDiagram)

        lExpected = []
        lExpected.append('       ')
        lExpected.append(']<----[')
        lExpected.append('       ')

        lActual = oRenderer.expand_arrow(oDiagram.get_tokens_from_column(1)[0])
        self.assertEqual(lExpected, lActual)

    def test_bidir_arrow_expansion(self):
        lLines = ['|A| <---> |B|']
        oDiagram = diagram.New(lLines)
        oRenderer = text.New(oDiagram)

        lExpected = []
        lExpected.append('       ')
        lExpected.append(']<--->[')
        lExpected.append('       ')

        lActual = oRenderer.expand_arrow(oDiagram.get_tokens_from_column(1)[0])
        self.assertEqual(lExpected, lActual)

    def test_two_nodes_with_one_arrow(self):
        lLines = ['|A| ----> |B|']
        oDiagram = diagram.New(lLines)
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
        lExpected.append('|     |]---->[|  B  |')
        lExpected.append('|  A  |       +-----+')
        lExpected.append('|     |       +-----+')
        lExpected.append('|     |]<----[|  C  |')
        lExpected.append('+-----+       +-----+')

        lActual = oRenderer.render()
        self.assertEqual(lExpected, lActual)

    def test_one_3_high_node_with_one_2_high_node_and_one_1_high_node(self):
        lLines = []
        lLines.append('|A| ----> |B|')
        lLines.append('| |       |B|')
        lLines.append('|A| <---- |C|')
        oDiagram = diagram.New(lLines)
        oRenderer = text.New(oDiagram)

        lExpected = []
        lExpected.append('+-----+       +-----+')
        lExpected.append('|     |]---->[|     |')
        lExpected.append('|     |       |     |')
        lExpected.append('|     |       |     |')
        lExpected.append('|  A  |       |  B  |')
        lExpected.append('|     |       +-----+')
        lExpected.append('|     |       +-----+')
        lExpected.append('|     |]<----[|  C  |')
        lExpected.append('+-----+       +-----+')

        lActual = oRenderer.render()
        self.assertEqual(lExpected, lActual)

