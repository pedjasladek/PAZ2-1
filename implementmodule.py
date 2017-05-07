"""Vertex structures"""
import queue
from enum import Enum
from typing import Dict, List

class Vertex:
    """Graph vertex"""
    def __init__(self, name):
        self.name = name
        self.color = Color.WHITE
        self.parent = None
        self.data = {
            # used for graph when vertex is discovered
            'Start': None,
            # used for graph when vertex is completed
            'End': None
            }

    def __repr__(self):
        colorstring = ""
        parentstring = ""
        startstring = ""
        endstring = ""
        if self.color is Color.BLACK:
            colorstring = 'BLACK'
        elif self.color is Color.GRAY:
            colorstring = 'GRAY'
        else:
            colorstring = 'WHITE'
        if self.parent is None:
            parentstring = " "
        else:
            parentstring = self.parent.name
        if self.data['Start'] is None:
            startstring = ''
        else:
            startstring = "\n\t{}".format(self.data['Start'])
        if self.data['End'] is None:
            endstring = ''
        else:
            endstring = "/{}".format(self.data['End'])
        return "{0}:\n\tColor: {1}{2}{3}\n\t[{4}]\n"\
        .format(self.name, colorstring, startstring, endstring, parentstring)

    def reset(self):
        """Reset Vertex"""
        self.color = Color.WHITE
        self.parent = None
        self.data = {
            'Start': None,
            'End': None
        }

    def init_start(self):
        """init start time"""
        if self.data['Start'] is None:
            self.data['Start'] = 0

    def init_end(self):
        """init end time"""
        if self.data['End'] is None:
            self.data['End'] = 0


class Color(Enum):
    """Colors used to denote vertex states"""
    BLACK = 0
    GRAY = 127
    WHITE = 255


def depth_first_search(graph: Dict[Vertex, List[Vertex]],
                       vertex: Vertex,
                       toplist: List[Vertex]=None):
    """DFS Implement additional arg is for topological sort"""
    for vertex in graph.keys():
        vertex.reset()
    # Don't use globals
    time = 0
    for vertex in graph.keys():
        if vertex.color is Color.WHITE:
            time = dfs_visit(graph, vertex, time, toplist)


def dfs_visit(graph: Dict[Vertex, List[Vertex]], element: Vertex,
              time: int, toplist: List[Vertex]=None):
    """Part of dfs for depth"""
    time += 1
    element.data['Start'] = time
    element.color = Color.GRAY
    for vertex in graph[element]:
        if vertex.color is Color.WHITE:
            vertex.parent = element
            time = dfs_visit(graph, vertex, time, toplist)
    element.color = Color.BLACK
    time += 1
    element.data['End'] = time
    if toplist is not None:
        toplist.insert(0, element)
    return time

def _print_path(source: Vertex, destination: Vertex):
    """Prints elemts between source and destination vertices"""
    ret = False
    if source == destination:
        print(source.name)
        ret = True
        return ret
    elif destination.parent is None:
        print('No path')
        return ret
    else:
        ret = _print_path(source, destination.parent)
        print(destination.name)
        return ret

def print_path(graph: Dict[Vertex, List[Vertex]],
               source: Vertex, destination: Vertex,
               option: bool=False):
    """prints path and distancance aditional arg for bfs(false,default) or dfs(true)"""
    if not option:
        breadth_first_search(graph, source)
    else:
        depth_first_search(graph, source)
    _print_path(source, destination)
    print()

def breadth_first_search(graph: Dict[Vertex, Vertex], source: Vertex):
    """BFS Implementation"""
    source.reset()
    vertexqueue = queue.Queue()
    for vertex in graph.keys():
        if vertex != source:
            vertex.reset()
    source.color = Color.GRAY
    source.init_start()
    source.parent = None
    vertexqueue.put(source)
    while not vertexqueue.empty():
        vertexsource = vertexqueue.get()
        for vertex in graph[vertexsource]:
            if vertex.color is Color.WHITE:
                vertex.color = Color.GRAY
                vertex.parent = vertexsource
                vertexqueue.put(vertex)
                vertex.data['Start'] = vertexsource.data['Start'] + 1
        vertexsource.color = Color.BLACK
