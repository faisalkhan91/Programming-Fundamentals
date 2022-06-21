"""
Implementation of a Graph Data Structure in python using adjacency list, this is an undirected and unweighted graph data
structure. There is no default graph data structure in python.

The graph data structure can be implemented using Edge List, Adjacent List or Adjacent Matrix strategies with each
having its pros and cons.
"""


# Definition of the graph class data structure
class Graph:
    # Initialization of the constructor.
    def __init__(self):
        self.number_of_nodes = 0  # Variable to keep track of vertices in the graph.
        self.adjacency_list = {}  # Initialization of the dictionary to store the vertices and edges.

    # Method to add vertices to the graph. Keys in graph are unique by default.
    def add_vertex(self, node):
        self.adjacency_list[node] = []  # Set the key in the dictionary (adjacency list) to empty list (array).
        self.number_of_nodes += 1  # Increment the tracker by 1.

    # Initial attempt to add edges to the graph
    def add_edge_initial(self, node_1, node_2):
        temp = list(self.adjacency_list.get(node_1))  # Store the list of the first node in a temporary declaration.
        temp.append(node_2)  # Append the new node to the list.
        self.adjacency_list[node_1] = temp  # Make the new list as the value of the key.
        temp = list(self.adjacency_list.get(node_2))  # Same as above
        temp.append(node_1)
        self.adjacency_list[node_2] = temp

    # Since the graph is undirected we need to add edges to both the nodes. So node 1 and node 2 will have to have the
    # vertices to be added to their respective adjacency list.
    def add_edge(self, node_1, node_2):
        if node_1 not in self.adjacency_list[node_2]:
            self.adjacency_list[node_1].append(node_2)  # Append the vertex to the first nodes list.
            self.adjacency_list[node_2].append(node_1)  # Append the vertex to the second nodes list.
        else:
            print("This edge already exists.")

    # Method to print all the connections of the graph.
    def show_connections(self):
        all_nodes = self.adjacency_list.keys()  # Get all the nodes in the graph.
        for node in all_nodes:
            node_connections = self.adjacency_list[node]  # Get all the edges for respective node in the adjacent list.
            connections = ""
            for vertex in node_connections:
                connections += vertex + " "  # Create a string 'connections' with all the edge connections in the list.
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
