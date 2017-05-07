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
#Knjiga BFS graph
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
breadth_first_search(BFSG, VERTEXS)
print(BFSG.keys())

#Knjiga DFS graph
DFSG = {
    VERTEXU: [VERTEXX, VERTEXU],
    VERTEXX: [VERTEXV],
    VERTEXV: [VERTEXY],
    VERTEXY: [VERTEXX],
    VERTEXW: [VERTEXY, VERTEXS],
    VERTEXS: [VERTEXS]
}
