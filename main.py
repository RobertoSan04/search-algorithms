from utils import *

ALGORITHMS = {
    "1": ("BFS",        lambda g, s, gl: bfs(g, s, gl)),
    "2": ("UCS",        lambda g, s, gl: ucs(g, s, gl)),
    "3": ("DFS",        lambda g, s, gl: dfs(g, s, gl)),
    "4": ("DLS",        None),
    "5": ("IDS",        lambda g, s, gl: ids(g, s, gl)),
    "6": ("Greedy BFS", None),
    "7": ("A*",         None),
}

def _ask_heuristic(graph, preloaded=None):
    if preloaded:
        print("  Preloaded heuristic values:")
        for node, h in preloaded.items():
            print(f"    h({node}) = {h}")
        answer = input("  Use preloaded heuristic? (y/n): ").strip().lower()
        if answer == "y":
            return preloaded

    print("  Enter heuristic values for each node:")
    heuristic = {}
    for node in graph:
        while True:
            try:
                h = float(input(f"    h({node}): "))
                if h < 0:
                    print("  Error: heuristic must be non-negative.")
                else:
                    heuristic[node] = h
                    break
            except ValueError:
                print("  Error: enter a valid number.")
    return heuristic

def run_algorithm(key, graph, start, goal, heuristic=None):
    name, fn = ALGORITHMS[key]
    if key == "4":
        while True:
            try:
                limit = int(input("Depth limit: "))
                if limit < 0:
                    print("  Error: depth limit must be non-negative.")
                else:
                    break
            except ValueError:
                print("  Error: enter a valid integer.")
        path, explored = dls(graph, start, goal, limit)
    elif key in ("6", "7"):
        h = _ask_heuristic(graph, heuristic)
        if key == "6":
            path, explored = greedy_bfs(graph, start, goal, h)
        else:
            path, explored = a_star(graph, start, goal, h)
    else:
        path, explored = fn(graph, start, goal)

    print(f"\n--- {name} ---")
    if path:
        print(f"Path found:     {' -> '.join(path)}")
        print(f"Explored nodes: {explored}")
    else:
        print("No solution found.")

def show_menu(graph, start, goal, ALGORITHMS, heuristic):
    clear_console()
    print_menu(graph, start, goal, ALGORITHMS, heuristic)
    return input("Select an option: ").strip().lower()

def main():
    graph, start, goal, heuristic = None, None, None, None

    while True:
        choice = show_menu(graph, start, goal, ALGORITHMS, heuristic)

        if choice == "0":
            clear_console()
            print("Goodbye!")
            break

        clear_console()
        if choice == "g":
            graph, start, goal = read_graph()
            heuristic = None
            print("  Graph loaded successfully.")
            print_graph(graph, start, goal)
        elif choice == "p":
            graph, start, goal, heuristic = preloaded_graph()
            print("  Preloaded graph loaded successfully.")
            print_graph(graph, start, goal)
        elif choice == "v":
            if not graph:
                print("  No graph loaded.")
            else:
                print_graph(graph, start, goal)
        elif choice in ALGORITHMS:
            if not graph:
                print("  No graph loaded. Select 'g' or 'p' to load a graph first.")
            else:
                run_algorithm(choice, graph, start, goal, heuristic)
        else:
            print("  Invalid option. Try again.")

        wait_any_key()

if __name__ == "__main__":
    main()