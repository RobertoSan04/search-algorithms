from utils.graph import read_graph
from algorithms.BFS import bfs

def main():
    graph, start, goal = read_graph()

    path, explored = bfs(graph, start, goal)

    if path:
        print(f"\nPath find: {' -> '.join(path)}")
        print(f"\nExplored nodes: {explored}")
    else:
        print("Didn't find a solution")


if __name__ == "__main__":
    main()
