# build a graph
def build_graph():
    graph = {}
    return graph

def _read_positive_int(prompt, allow_zero=False):
    while True:
        try:
            value = int(input(prompt))
            if value < 0 or (not allow_zero and value == 0):
                print(f"  Error: enter a {'non-negative' if allow_zero else 'positive'} integer.")
            else:
                return value
        except ValueError:
            print("  Error: enter a valid integer.")

# Read user data for the graph
def read_graph():
    graph = build_graph()

    n = _read_positive_int("Number of nodes: ")

    while True:
        nodes = input("Name of the nodes (Example: A B C D): ").split()
        if len(nodes) != n:
            print(f"  Error: expected {n} node names, got {len(nodes)}.")
        elif len(nodes) != len(set(nodes)):
            print("  Error: node names must be unique.")
        else:
            break

    for node in nodes:
        graph[node] = []

    while True:
        start = input("Initial state: ").strip()
        if start not in graph:
            print(f"  Error: '{start}' is not in the node list.")
        else:
            break

    while True:
        goal = input("Final state: ").strip()
        if goal not in graph:
            print(f"  Error: '{goal}' is not in the node list.")
        else:
            break

    t = _read_positive_int("Number of transactions: ", allow_zero=True)

    for i in range(t):
        while True:
            line = input(f"Transaction {i + 1} (Format: origin destination cost): ").split()
            if len(line) != 3:
                print("  Error: enter exactly 3 values: origin destination cost.")
                continue
            origin, destination, raw_cost = line
            if origin not in graph:
                print(f"  Error: '{origin}' is not a known node.")
                continue
            if destination not in graph:
                print(f"  Error: '{destination}' is not a known node.")
                continue
            try:
                cost = float(raw_cost)
                if cost < 0:
                    print("  Error: cost must be non-negative.")
                    continue
            except ValueError:
                print("  Error: cost must be a number.")
                continue
            graph[origin].append((destination, cost))
            break

    return graph, start, goal
