class Dijkstra():
    def __init__(self, graph):
        """
        Description:
        ------------
        Initializes the Dijkstra class with the graph, initial node, and end node.

        Params:
        ------------
        graph (dict): The graph represented as a dictionary with nodes as keys and their neighbors and corresponding weights as values.
        """
        self.graph = graph

    def get_current_node(self, visited, currentDistances):
        """
        Description:
        ------------
        Returns the unvisited node with the smallest distance from the source node.

        Params:
        ------------
        visited (set): A set of visited nodes.
        currentDistances (dict): A dictionary containing the current distances to each node.

        Return:
        ------------
        str: The unvisited node with the smallest distance from the source node.
        """
        initial_distance = float('inf')  # Set minimum distance to infinity
        current_node = None
        for node in currentDistances:
            if node not in visited:
                if currentDistances[node] < initial_distance:
                    initial_distance = currentDistances[node]
                    current_node = node
        return current_node

    def shortest_path(self, initial_node, end_node):
        """
        Description:
        ------------
        Implements Dijkstra's shortest path algorithm to find the shortest path between the initial node and the end node.

        Params:
        -----------
        initial_node (str): The starting node.
        end_node (str): The ending node.

        Return:
        ------------
        tuple: A tuple containing the shortest path and its distance.
        """
        graph = self.graph

        # Initialize distances to all nodes as infinity except the initial node, which is 0
        distances = {node: float('inf') for node in graph}
        distances[initial_node] = 0

        # Initialize a set of visited nodes and a dictionary to keep track of the path to each node
        visited = set()
        path_to = {node: [] for node in graph}
        path_to[initial_node] = [initial_node]

        # Continue exploring the graph until the end node is visited
        while end_node not in visited:
            current_node = self.get_current_node(visited, distances)

            # Update the distances and paths to each neighbor of the current node
            for neighbor, distance in graph[current_node].items():
                if neighbor not in visited:
                    min_dist = distances[current_node] + distance

                    if min_dist < distances[neighbor]:
                        distances[neighbor] = min_dist
                        path_to[neighbor] = path_to[current_node] + [neighbor]

            # Add the current node to the set of visited nodes
            visited.add(current_node)

        # Return the shortest path and its distance
        shortest_path = path_to[end_node]
        distance_path = distances[end_node]
        return shortest_path, distance_path
