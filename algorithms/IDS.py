from algorithms.DLS import _dls

# Search Algorithm: Iterative deepening search
def ids(graph, start, goal):
    explored_all = []
    limit = 0

    while True:
        path, status, explored = _dls(graph, start, goal, limit)
        explored_all.extend(explored)

        if status == "found":
            return path, explored_all

        if status == "failure":   # no cutoff occurred -> search exhausted
            return None, explored_all

        limit += 1