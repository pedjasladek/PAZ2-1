"""Testiranje i iscrtavanje"""
from implementmodule import Vertex, breadth_first_search, depth_first_search, print_path

VERTEXR = Vertex('R')
VERTEXV = Vertex('V')
VERTEXS = Vertex('S')
VERTEXW = Vertex('W')
VERTEXT = Vertex('T')
VERTEXU = Vertex('U')
VERTEXY = Vertex('Y')
VERTEXX = Vertex('X')
VERTEXZ = Vertex('Z')
#BFS graph (book)
BFSG = {
    VERTEXS: [VERTEXR, VERTEXW],
    VERTEXR: [VERTEXS, VERTEXV],
    VERTEXV: [VERTEXR],
    VERTEXW: [VERTEXS, VERTEXT, VERTEXX],
    VERTEXT: [VERTEXW, VERTEXX, VERTEXU],
    VERTEXX: [VERTEXT, VERTEXW, VERTEXY],
    VERTEXU: [VERTEXT, VERTEXX, VERTEXY],
    VERTEXY: [VERTEXT, VERTEXX, VERTEXU]
    }

breadth_first_search(BFSG, VERTEXT)
# This calls BFD on BFSG graph
print_path(BFSG, VERTEXS, VERTEXW)
#KDFS graph (book)
DFSG = {
    VERTEXU: [VERTEXX, VERTEXV],
    VERTEXX: [VERTEXV],
    VERTEXV: [VERTEXY],
    VERTEXY: [VERTEXX],
    VERTEXW: [VERTEXY, VERTEXS],
    VERTEXS: [VERTEXS]
}
# This calls DFS on DFSG graph
print_path(DFSG, VERTEXU, VERTEXY, True)
# This calls BFS on DFSG graph
print_path(DFSG, VERTEXU, VERTEXY)
depth_first_search(DFSG, VERTEXU)
print(DFSG.keys())