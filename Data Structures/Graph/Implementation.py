"""
Implementation of a Graph Data Structure in python using adjacency list, this is an undirected and unweighted graph data
structure. There is no default graph data structure in python.

The graph data structure can be implemented using Edge List, Adjacent List or Adjacent Matrix strategies with each
having its pros and cons.
"""


# Graph class
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
        all_nodes = self.adjacency_list.keys()
        for node in all_nodes:
            node_connections = self.adjacency_list[node]
            connections = ""
            for vertex in node_connections:
                connections += vertex + " "
            print(node + '-->' + connections)


# Initialization
my_graph = Graph()
# my_graph.add_vertex(10)
# my_graph.add_vertex(11)
# my_graph.add_vertex(15)
# my_graph.add_vertex(12)
# my_graph.add_vertex(3)
# my_graph.add_edge(10, 11)
# my_graph.add_edge(11, 15)
# my_graph.add_edge(15, 3)
# my_graph.add_edge(15, 12)
# my_graph.add_edge(12, 3)
# my_graph.add_edge(12, 15)
# my_graph.add_edge(3, 15)
# my_graph.add_edge(3, 12)
my_graph.add_vertex('0')
my_graph.add_vertex('1')
my_graph.add_vertex('2')
my_graph.add_vertex('3')
my_graph.add_vertex('4')
my_graph.add_vertex('5')
my_graph.add_vertex('6')
my_graph.add_edge('3', '1')
my_graph.add_edge('3', '4')
my_graph.add_edge('4', '2')
my_graph.add_edge('4', '5')
my_graph.add_edge('1', '2')
my_graph.add_edge('1', '0')
my_graph.add_edge('0', '2')
my_graph.add_edge('6', '5')
print(my_graph.adjacency_list)
my_graph.show_connections()
