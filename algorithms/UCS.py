import heapq

# Search Algorithm: Uniform cost search
def ucs(graph, start, goal):
    priority_queue = []
    heapq.heappush(priority_queue, (0, start, [start]))

    visited = set()
    explored = []

    while priority_queue:
        cost, node, path = heapq.heappop(priority_queue)

        if node in visited:
            continue

        visited.add(node)
        explored.append(node)

        if node == goal:
            return path, explored

        for neighbor, edge_cost in graph[node]:
            if neighbor not in visited:
                heapq.heappush(priority_queue, (cost + edge_cost, neighbor, path + [neighbor]))


    return None, explored