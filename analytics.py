"""Random graph generations and plot"""
from typing import Dict, List
import random
import time
import matplotlib.pyplot as plt
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

def time_measure(graph: Dict[Vertex, List[Vertex]], bfs: bool=False):
    """Returns how long it took for dfs (default) or bfs (set aditonal argument to True)"""
    time_start = 0
    time_end = 0
    if not bfs:
        time_start = time.clock()
        depth_first_search(graph, first_source(graph))
        time_end = time.clock()
    else:
        time_start = time.clock()
        breadth_first_search(graph, first_source(graph))
        time_end = time.clock()
    return time_end - time_start

def analyse():
    """Extracts runing times. New graph will be made for every value in runnsize.
     modify runnsize for different size of graphs"""
    vertices = [5, 25, 50]
    exectimebfs = []
    exectimedfs = []
    edges = []
    for item in vertices:
        temp_graph = generate_graph(item)
        # number of edges
        edges.append(sum_edges(temp_graph))
        # extract time for bfs
        exectimebfs.append(time_measure(temp_graph, True))
        # extract time for dfs
        exectimedfs.append(time_measure(temp_graph))
    plot_graph_stats(vertices, edges, exectimebfs, 'Breath-First-Search')
    plot_graph_stats(vertices, edges, exectimedfs, 'Depth-First-Search')

def plot_graph_stats(vertices: List[int], edges: List[int], exec_time: List[int], label: str):
    """Makes plot of graph structure"""
    input_data = []
    for index, item in enumerate(vertices):
        input_data.append(item + edges[index])
    plt.plot(input_data, exec_time, label=label)
    plt.xlabel('V + E [n]')
    plt.ylabel('T[S]')
    plt.legend()
    print(label)
    for index, item in enumerate(vertices):
        print("Number of vertecies: {} Number of edges: {} Time: {}"\
        .format(item, edges[index], exec_time[index]))

analyse()
plt.show()
