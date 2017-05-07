"""Testiranje i iscrtavanje"""
from implementmodule import Vertex, breadth_first_search, depth_first_search, print_path

#Knjiga BFS graph
VERTEXR = Vertex('R')
VERTEXV = Vertex('V')
VERTEXS = Vertex('S')
VERTEXW = Vertex('W')
VERTEXT = Vertex('T')
VERTEXU = Vertex('U')
VERTEXY = Vertex('Y')
VERTEXX = Vertex('X')
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
