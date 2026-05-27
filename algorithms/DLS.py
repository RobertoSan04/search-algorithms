# Search Algorithm: Depth Limited Search
def dls(graph, start, goal, limit):
    explored = []
    result = recursive_dls(graph, start, goal, [start], limit, explored)

    if result == "cutoff" or result is None:
        return None, explored
    return result, explored


def recursive_dls(graph, node, goal, path, limit, explored):
    explored.append(node)

    if node == goal:
        return path

    if limit == 0:
        return "cutoff"

    cutoff_occurred = False

    for neighbor, cost in graph[node]:
        if neighbor not in path:
            result = recursive_dls(graph, neighbor, goal, path + [neighbor], limit -1, explored)

            if result == "cutoff":
                cutoff_occurred = True
            elif result is not None:
                return result

    return "cutoff" if cutoff_occurred else None