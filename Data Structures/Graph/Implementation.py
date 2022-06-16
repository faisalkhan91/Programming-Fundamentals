"""
Implementation of a Graph Data Structure in python using adjacency list. There is no default graph data structure in
python.

The graph data structure can be implemented using Edge List, Adjacent List or Adjacent Matrix strategies with each
having its pros and cons.
"""


class Graph:
    def __init__(self):
        self.number_of_nodes = 0
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        self.adjacency_list[self.number_of_nodes] = vertex
        self.number_of_nodes += 1

    def add_edge(self):
        

    def show_connections(self):
        pass


# Initialization
my_graph = Graph()
my_graph.add_vertex(10)
my_graph.add_vertex(11)
my_graph.add_vertex(15)
my_graph.add_vertex(12)
my_graph.add_vertex(3)
print(my_graph.adjacency_list)
