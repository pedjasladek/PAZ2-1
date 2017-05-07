"""Random graph generations and plot"""
from typing import Dict, List
import random
#import time
#import matplotlib.pyplot as plt
from implementmodule import Vertex, breadth_first_search, depth_first_search

def sum_edges(graph: Dict[Vertex, List[Vertex]]):
    """Returns number of aall edges of a graph"""
    suma = 0
    for keys in graph.keys():
        suma += len(graph[keys])
    return suma

def sum_vertexes(graph: Dict[Vertex, List[Vertex]]):
    """Returns all number of vertexes in graph"""
    return len(graph.keys())

def random_vertices(size, elements):
    """Generate a list of random vertices"""
    verticesnames = random.sample(range(1, size+1), elements)
    vertices = []
    for item in verticesnames:
        #Make a vertex out of every random int
        vertices.append(Vertex(item))
    return vertices

def generate_graph(size: int):
    """Returns randomly generated graph of omitted size
    maximum size is 10000"""
    graph = dict()
    #Generate size number of verticies
    vertices = random_vertices(10000, size)
    #Init graph
    for item in vertices:
        #Put every vertex into the graph
        graph[item] = []
    for item in graph:
        #generate random edges for every vertex
        edgenumber = random.randint(0, size)
        random.shuffle(vertices)
        #assign the edges to the graphs vertex
        graph[item] = vertices[0:edgenumber]
    #return the random graph
    return graph

def first_source(graph: Dict[Vertex, List[Vertex]]):
    """Return a the first vertex in the dictionary"""
    for item in graph:
        return item


TESTGRAPH = generate_graph(10)
print(sum_edges(TESTGRAPH))
print(sum_vertexes(TESTGRAPH))

breadth_first_search(TESTGRAPH, first_source(TESTGRAPH))
depth_first_search(TESTGRAPH, first_source(TESTGRAPH))
print(TESTGRAPH.keys())
