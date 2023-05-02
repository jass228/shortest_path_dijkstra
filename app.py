# from graph import Graph
from dijkstra import Dijkstra

# Define graph
graph_a = {
    'A': {'B': 3, 'C': 1},
    'B': {'A': 3, 'C': 7, 'D': 5, 'E': 1},
    'C': {'A': 1, 'B': 7, 'D': 2},
    'D': {'B': 5, 'C': 2, 'E': 7},
    'E': {'B': 1, 'D': 7}
}

graph_b = {'Reykjavik': {'Oslo': 5, 'London': 4},
           'Oslo': {'Berlin': 1, 'Moscow': 3, 'Reykjavik': 5},
           'Moscow': {'Belgrade': 5, 'Athens': 4, 'Oslo': 3},
           'London': {'Reykjavik': 4},
           'Rome': {'Berlin': 2, 'Athens': 2},
           'Berlin': {'Oslo': 1, 'Rome': 2},
           'Belgrade': {'Moscow': 5, 'Athens': 1},
           'Athens': {'Belgrade': 1, 'Moscow': 4, 'Rome': 2}}


def get_shortest_path(graph):
    print(f'\n--Graph--\n{graph}\n')

    start = input("Enter the start node: ")
    end = input("Enter the end node: ")

    D = Dijkstra(graph)
    shortest_path, distance = D.shortest_path(start, end)
    print(
        f"\nThe shortest path from {start} to {end} is {shortest_path} with a distance of {distance}\n")


def menu():
    print("\n-----------------------------------------")
    print("|                 Welcome               |")
    print("-----------------------------------------\n")
    while True:
        print("-- Menu --")
        print("1. Default graph A")
        print("2. Default graph B")
        print("3. Your own graph")
        print("4. Quit\n")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            get_shortest_path(graph_a)
        elif choice == 2:
            get_shortest_path(graph_b)
        elif choice == 3:
            graph = input("Enter a graph as a dictionary")
            get_shortest_path(graph)
        elif choice == 4:
            print("Goodbye 👋")
            break
        else:
            print("\n-----------------------------------------")
            print("|🚨 Error: Invalid choice. Try again! 🚨|")
            print("-----------------------------------------\n")


if __name__ == '__main__':
    menu()
