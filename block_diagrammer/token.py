
class Token():

  def __init__(self, value: str, start: int, end: int):
     self.value = value
     self.start = start
     self.end = end
     self.row = None
     self.column = None

  def __eq__(self, other):
     if not isinstance(other, self.__class__):
        return False
     if self.__dict__ == other.__dict__:
        return True
     return False


class Empty(Token):

    def __init__(self, value: str, start: int, end: int):
        Token.__init__(self, value, start, end)


class Node(Token):

    def __init__(self, value: str, start: int, end: int):
        Token.__init__(self, value, start, end)


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


def extract_nodes(line: str) -> list:
    lReturn = []
    bNodeFound = False
    for iChar, sChar in enumerate(line):
        if sChar == '|' and bNodeFound:
            bNodeFound = False
            lReturn.append(Node(sName, iStart, iChar))
            continue
        if bNodeFound:
            sName += sChar
        if sChar == '|' and not bNodeFound:
            bNodeFound = True
            iStart = iChar
            sName = ''
    return lReturn


def extract_arrows(line: str) -> list:
    lReturn = []
    bNodeFound = False
    sName = ''
    iStart = None
    iEnd = None
    for iChar, sChar in enumerate(line):
        if sChar == '|' and bNodeFound:
            bNodeFound = False
            iStart = iChar + 1
            continue
        if sChar == '|' and not bNodeFound:
            bNodeFound = True
            iEnd = iChar - 1
            if iStart is not None:
                lReturn.append(Arrow(sName, iStart, iEnd))
            sName = ''
        if not bNodeFound:
            sName += sChar
    return lReturn


def tokenize(line: str) -> list:
    lReturn = []
    lReturn.extend(extract_nodes(line))
    lReturn.extend(extract_arrows(line))
    return lReturn
