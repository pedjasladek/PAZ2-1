"""Vertex structures"""
import queue
from enum import Enum
from typing import Dict, List

TIME = 0


class Vertex:
    """Cvor grafa"""
    def __init__(self, name):
        self.name = name
        self.color = Color.WHITE
        self.parent = None
        self.data = {
            'Start': None,
            'End': None
            }

    def __repr__(self):
        return "{}:{} Data: {}".format(self.color, self.data, self.name)

    def reset(self):
        """Reset Vertex"""
        self.color = Color.WHITE
        self.parent = None
        self.data = {
            'Discovery': None,
            'Finish': None
        }

    def increment(self, vertex):
        """Increase data"""
        self.data = vertex.data + 1


class Color(Enum):
    """Colors used to denote vertex states"""
    BLACK = 0
    GRAY = 127
    WHITE = 255


# ZADATAK3


def depth_first_search(graph: Dict[Vertex, List[Vertex]], toplist: List[Vertex] = None):
    """DFS Implement"""
    for vertex in graph.keys():
        vertex.reset()
    global TIME
    TIME = 0
    for vertex in graph.keys():
        if vertex.color is Color.WHITE:
            dfs_visit(graph, vertex, toplist)


def dfs_visit(graph: Dict[Vertex, List[Vertex]], element: Vertex, toplist: List[Vertex] = None):
    """Part of dfs for depth"""
    global TIME
    TIME = TIME + 1
    element.data['Discovery'] = TIME
    element.color = Color.GRAY
    for vertex in graph[element]:
        if vertex.color is Color.WHITE:
            vertex.parent = element
            dfs_visit(graph, vertex, toplist)
    element.color = Color.BLACK
    TIME = TIME + 1
    element.data['Finish'] = TIME
    if toplist is not None:
        toplist.insert(0, element)


def print_path(source: Vertex, destination: Vertex):
    """Print path between to vertexes"""
    if source == destination:
        print(source)
    elif destination.parent is None:
        print('Na path found')
    else:
        print_path(source, destination.parent)
        print(destination)


def breadth_first_search(graph: Dict[Vertex, Vertex], source: Vertex):
    """BFS Implement"""
    source.reset()
    vertexqueue = queue.Queue()
    for vertex in graph.keys():
        if vertex != source:
            vertex.reset()
    source.color = Color.GRAY
    time = 0
    source.data['Discovery'] = time
    source.parent = None
    vertexqueue.put(source)
    while not vertexqueue.empty():
        vertexsource = vertexqueue.get()
        for vertex in graph[vertexsource]:
            if vertex.color is Color.WHITE:
                vertex.color = Color.GRAY
                vertex.parent = vertexsource
                vertexqueue.put(vertex)
                time += 1
                vertex.data['Discovery'] = time
        time += 1
        vertexsource.color = Color.BLACK
        vertexsource.data['Finish'] = time
