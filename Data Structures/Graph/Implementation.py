"""
Implementation of a Graph Data Structure in python using adjacency list, this is an undirected and unweighted graph data
structure. There is no default graph data structure in python.

The graph data structure can be implemented using Edge List, Adjacent List or Adjacent Matrix strategies with each
having its pros and cons.
"""


class Graph:
    def __init__(self):
        self.number_of_nodes = 0
        self.adjacency_list = {}

    def add_vertex(self, node):
        self.adjacency_list[node] = []
        self.number_of_nodes += 1

    def add_edge(self, node_1, node_2):
        temp = list(self.adjacency_list.get(node_1))
        temp.append(node_2)
        self.adjacency_list[node_1] = temp

    def show_connections(self):
        pass


# Initialization
my_graph = Graph()
my_graph.add_vertex(10)
my_graph.add_vertex(11)
my_graph.add_vertex(15)
my_graph.add_vertex(12)
my_graph.add_vertex(3)
my_graph.add_edge(10, 11)
my_graph.add_edge(11, 15)
my_graph.add_edge(15, 3)
my_graph.add_edge(15, 12)
my_graph.add_edge(12, 3)
my_graph.add_edge(12, 15)
my_graph.add_edge(3, 15)
my_graph.add_edge(3, 12)
print(my_graph.adjacency_list)
