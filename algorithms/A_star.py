import heapq

# Search Algorithm: A*
def a_star(graph, start, goal, heuristic):
    priority_queue = []
    heapq.heappush(priority_queue, (heuristic[start], 0, start, [start]))

    visited = set()
    explored = []

    while priority_queue:
        f, g, node, path = heapq.heappop(priority_queue)

        if node in visited:
            continue

        visited.add(node)
        explored.append(node)

        if node == goal:
            return path, explored

        for neighbor, edge_cost in graph[node]:
            if neighbor not in visited:
                g_new = g + edge_cost
                f_new = g_new + heuristic[neighbor]
                heapq.heappush(priority_queue, (f_new, g_new, neighbor, path + [neighbor]))

    return None, explored
