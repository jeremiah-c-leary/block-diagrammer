
def create_diagram_dict(lines: list):
    dDiagram = {}
    dDiagram['diagram'] = {}
    dDiagram['diagram']['lines'] = lines
    dDiagram['diagram']['nodes'] = {}
    dDiagram['diagram']['columns'] = {}
    return dDiagram
