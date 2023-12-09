
class Token():

  def __init__(self, value: str, start: int, end: int):
     self.value = value
     self.start = start
     self.end = end
     self.row = None
     self.column = None
     self.color = 'grey'
     self.width = 5

  def __eq__(self, other):
     if not isinstance(other, self.__class__):
        return False
     if self.__dict__ == other.__dict__:
        return True
     return False


class Empty(Token):

    def __init__(self, value: str, start: int, end: int):
        Token.__init__(self, value, start, end)

    def convert(self, tokenType):
        return self


class Node(Token):

    def __init__(self, value: str, start: int, end: int):
        Token.__init__(self, value, start, end)

    def convert(self, tokenType):
       oReturn = tokenType(self.value, self.start, self.end)
       oReturn.row = self.row
       oReturn.column = self.column
       return oReturn


class SingleNode(Node):

    def __init__(self, value: str, start: int, end: int):
        Node.__init__(self, value, start, end)


class TopNode(Node):

    def __init__(self, value: str, start: int, end: int):
        Node.__init__(self, value, start, end)


class MiddleNode(Node):

    def __init__(self, value: str, start: int, end: int):
        Node.__init__(self, value, start, end)


class BottomNode(Node):

    def __init__(self, value: str, start: int, end: int):
        Node.__init__(self, value, start, end)


class Arrow(Token):

    def __init__(self, value: str, start: int, end: int):
        Token.__init__(self, value, start, end)

    def convert(self, tokenType):
       oReturn = tokenType(self.value, self.start, self.end)
       oReturn.row = self.row
       oReturn.column = self.column
       return oReturn


class SingleArrow(Arrow):

    def __init__(self, value: str, start: int, end: int):
        Token.__init__(self, value, start, end)


class StartArrow(Arrow):

    def __init__(self, value: str, start: int, end: int):
        Arrow.__init__(self, value, start, end)


class MiddleArrow(Arrow):

    def __init__(self, value: str, start: int, end: int):
        Arrow.__init__(self, value, start, end)


class EndArrow(Arrow):

    def __init__(self, value: str, start: int, end: int):
        Arrow.__init__(self, value, start, end)


def extract_nodes(line: str) -> list:
    lReturn = []
    nodeIndexes = get_node_indexes(line)
    for startBar in range(0, len(nodeIndexes), 2):
        startIndex, endIndex, name = extract_indexes_and_name(nodeIndexes, startBar, line)
        lReturn.append(Node(name, startIndex, endIndex))
    return lReturn


def extract_arrows(line: str) -> list:
    lReturn = []
    arrowIndexes = get_arrow_indexes(line)

    for startBar in range(0, len(arrowIndexes), 2):
        startIndex, endIndex, name = extract_indexes_and_name(arrowIndexes, startBar, line)
        if name == '':
            lReturn.append(Empty(name, startIndex + 1, endIndex - 1))
        else:
            lReturn.append(Arrow(name, startIndex + 1, endIndex - 1))
    return lReturn


def extract_indexes_and_name(arrowIndexes, startBar, line):
    startIndex = arrowIndexes[startBar]
    endIndex = arrowIndexes[startBar + 1]
    name = line[startIndex + 1:endIndex].strip()
    return startIndex, endIndex, name


def get_node_indexes(line: str) -> list:
    return get_indexes_of_bars(line)


def get_arrow_indexes(line: str) -> list:
    indexes = get_indexes_of_bars(line)
    del indexes[0]
    del indexes[-1]
    return indexes


def get_indexes_of_bars(line: str) -> list:
    lReturn = []
    for iChar, sChar in enumerate(line):
        if sChar == '|':
            lReturn.append(iChar)
    return lReturn


def tokenize(line: str) -> list:
    lReturn = []
    lReturn.extend(extract_nodes(line))
    lReturn.extend(extract_arrows(line))
    return lReturn
