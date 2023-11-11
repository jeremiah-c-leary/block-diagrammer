
from block_diagrammer import diagram

from block_diagrammer.render import svg
from block_diagrammer.render import text

renderers = {}
renderers['text'] = text
renderers['svg'] = svg


def execute(cla):
    oDiagram = diagram.New(cla.fileDict)

    oRenderer = renderers[cla.renderer].New(oDiagram)
    lLines = oRenderer.render()
    for line in lLines:
        print(line)

