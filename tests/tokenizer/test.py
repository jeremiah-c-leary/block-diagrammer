
import unittest

from block_diagrammer import token


class test(unittest.TestCase):

    def test_tokens_are_equal(self):
        self.assertEqual(token.Token('A', 0, 2), token.Token('A', 0, 2))

    def test_tokens_are_not_equal(self):
        self.assertNotEqual(token.Token('A', 0, 2), token.Token('B', 0, 2))
        self.assertNotEqual(token.Token('A', 0, 2), token.Token('A', 1, 2))
        self.assertNotEqual(token.Token('A', 0, 2), token.Token('A', 0, 3))

    def test_nodes_are_not_equal_to_arrows(self):
        self.assertNotEqual(token.Node('A', 0, 2), token.Arrow('A', 0, 2))

    def test_extract_nodes_with_two_nodes_and_one_arrow(self):
        sLine = '|A| ----> |B|'

        lExpected = []

        lExpected.append(token.Node('A', 0, 2))
        lExpected.append(token.Node('B', 10, 12))

        lActual = token.extract_nodes(sLine)

        self.assertEqual(lExpected, lActual)

    def test_extract_nodes_with_three_nodes_and_two_arrows(self):
        sLine = '|A| ----> |B| <----> |C|'

        lExpected = []

        lExpected.append(token.Node('A', 0, 2))
        lExpected.append(token.Node('B', 10, 12))
        lExpected.append(token.Node('C', 21, 23))

        lActual = token.extract_nodes(sLine)

        self.assertEqual(lExpected, lActual)

    def test_extract_arrows_with_two_nodes_and_one_arrow(self):
        sLine = '|A| ----> |B|'

        lExpected = []

        lExpected.append(token.Arrow(' ----> ', 3, 9))

        lActual = token.extract_arrows(sLine)

        self.assertEqual(lExpected, lActual)

    def test_extract_arrows_with_three_nodes_and_two_arrows(self):
        sLine = '|A| ----> |B| <----> |C|'

        lExpected = []

        lExpected.append(token.Arrow(' ----> ', 3, 9))
        lExpected.append(token.Arrow(' <----> ', 13, 20))

        lActual = token.extract_arrows(sLine)

        self.assertEqual(lExpected, lActual)

    def test_extract_arrows_with_leading_spaces_before_first_node(self):
        sLine = '          |B| <----> |C|'

        lExpected = []

        lExpected.append(token.Arrow(' <----> ', 13, 20))

        lActual = token.extract_arrows(sLine)

        self.assertEqual(lExpected, lActual)

    def test_tokenize_with_three_nodes_and_two_arrows(self):
        sLine = '|A| ----> |B| <----> |C|'

        lExpected = []

        lExpected.append(token.Node('A', 0, 2))
        lExpected.append(token.Node('B', 10, 12))
        lExpected.append(token.Node('C', 21, 23))
        lExpected.append(token.Arrow(' ----> ', 3, 9))
        lExpected.append(token.Arrow(' <----> ', 13, 20))

        lActual = token.tokenize(sLine)

        self.assertEqual(lExpected, lActual)

    def test_tokenize_with_leading_spaces_three_nodes_and_two_arrows(self):
        sLine = '          |B| <----> |C|'

        lExpected = []

        lExpected.append(token.Node('B', 10, 12))
        lExpected.append(token.Node('C', 21, 23))
        lExpected.append(token.Arrow(' <----> ', 13, 20))

        lActual = token.tokenize(sLine)

        self.assertEqual(lExpected, lActual)

