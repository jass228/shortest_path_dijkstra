class Graph():
    def __init__(self, nodes, initial_graph):
        """
        Description:
        ------------
        Initializes the Graph class.

        Params:
        ------------
        nodes (list): A list of nodes in the graph.
        initial_graph (dict): A dictionary containing the edges and weights of the graph.
        """
        self.nodes = nodes
        self.graph = initial_graph

    def construct_graph(self):
        """
        Description:
        ------------
        Constructs the graph by adding missing nodes and edges.

        Return:
        ------------
        dict: The completed graph with all nodes and edges.
        """
        graph = {}
        for node in self.nodes:
            graph[node] = {}

        graph.update(self.graph)

        for node, edges in graph.items():
            for adjacent_node, value in edges.items():
                if graph[adjacent_node].get(node, False) == False:
                    graph[adjacent_node][node] = value

        return graph

    def get_nodes(self):
        """
        Description:
        ------------
        Returns the nodes in the graph.

        Return:
        ------------
        list: A list of nodes in the graph.
        """
        return self.nodes

    def get_neighbor_nodes(self, node):
        """
        Description:
        ------------
        Returns the neighboring nodes of a node.

        Params:
        ------------
        node (str): The node whose neighbors have to be found.

        Return:
        ------------
        list: List of nodes to which the input node has neighbors.
        """
        connections = []
        for out_node in self.nodes:
            if self.graph[node].get(out_node, False) != False:
                connections.append(out_node)
        return connections

    def get_weights_nodes(self, first_node, second_node):
        """
        Description:
        ------------
        Returns the weight of the edge between two nodes.

        Params:
        ------------
        first_node (str): The starting node of the edge.
        second_node (str): The ending node of the edge.

        Return:
        ------------
        int or str: The weight of the edge between the two nodes, or a message indicating that there is no connection.
        """
        try:
            return self.graph[first_node][second_node]
        except KeyError:
            print(
                f'There is no connection between {first_node} and {second_node}')
