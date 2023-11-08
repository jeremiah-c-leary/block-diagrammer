
from block_diagrammer.render import text
from block_diagrammer import diagram

renderers = {}
renderers['text'] = text


def execute(cla):
    oDiagram = diagram.New(cla.fileDict['diagram']['lines'])

    oRenderer = renderers[cla.renderer].New(oDiagram)
    lLines = oRenderer.render()
    for line in lLines:
        print(line)

