from utils import *

ALGORITHMS = {
    "1": ("BFS",        lambda g, s, gl: bfs(g, s, gl)),
    "2": ("UCS",        lambda g, s, gl: ucs(g, s, gl)),
    "3": ("DFS",        lambda g, s, gl: dfs(g, s, gl)),
    "4": ("DLS",        None),
    "5": ("IDS",        lambda g, s, gl: ids(g, s, gl)),
    "6": ("Greedy BFS", lambda g, s, gl: greedy_bfs(g, s, gl)),
    "7": ("A*",         lambda g, s, gl: a_star(g, s, gl)),
}

def print_menu(graph, start, goal):
    print("\n" + "=" * 40)
    print("       Search Algorithms Menu")
    print("=" * 40)
    if graph:
        print(f"  Graph: {len(graph)} nodes  |  {start} -> {goal}")
    else:
        print("  Graph: none loaded")
    print("-" * 40)
    print("  g. New graph")
    for key, (name, _) in ALGORITHMS.items():
        print(f"  {key}. {name}")
    print("  0. Exit")
    print("=" * 40)

def run_algorithm(key, graph, start, goal):
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
    else:
        path, explored = fn(graph, start, goal)

    print(f"\n--- {name} ---")
    if path:
        print(f"Path found:     {' -> '.join(path)}")
        print(f"Explored nodes: {explored}")
    else:
        print("No solution found.")

def main():
    graph, start, goal = None, None, None

    while True:
        print_menu(graph, start, goal)
        choice = input("Select an option: ").strip().lower()

        if choice == "0":
            print("Goodbye!")
            break
        elif choice == "g":
            graph, start, goal = read_graph()
            print("  Graph loaded successfully.")
        elif choice in ALGORITHMS:
            if not graph:
                print("  No graph loaded. Select 'g' to create one first.")
            else:
                run_algorithm(choice, graph, start, goal)
        else:
            print("  Invalid option. Try again.")

if __name__ == "__main__":
    main()