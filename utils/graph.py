# build a graph
def build_graph():
    graph = {}
    return graph

# Read user data for the graph
def read_graph():
    graph = build_graph()
    n = int(input("Number of nodes: "))
    nodes = input("Name of the nodes: ").split()

    for node in nodes:
        graph[node] = []

    start = input("Inicial state: ").strip()
    goal = input("Final state: ").strip()

    t = int(input("Number of transactions: "))

    for _ in range(t):
        line = input("Transaction (origin destiny cost): ").split()
        origin, destination, cost = line[0], line[1], int(line[2])
        graph[origin].append((destination, cost))

    return graph, start, goal
