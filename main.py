from utils import *

def main():
    graph, start, goal = read_graph()



    path, explored = ucs(graph, start, goal)

    if path:
        print(f"\nPath found: {' -> '.join(path)}")
        print(f"\nExplored nodes: {explored}")
    else:
        print("Didn't find a solution")


if __name__ == "__main__":
    main()
