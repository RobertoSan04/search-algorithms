from algorithms.DLS import dls

# Search Algorithm: Iterative deepening search
def ids(graph, start, goal):
    explored_all = []
    limit = 0

    while True:
        path, explored = dls(graph, start, goal, limit)
        explored_all.extend(explored)

        if path is not None:
            return path, explored_all

        if len(explored) == 0:
            return None, explored_all

        limit += 1