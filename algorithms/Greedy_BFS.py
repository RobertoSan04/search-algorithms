import heapq

# Search Algorithm: Greedy BFS
def greedy_bfs(graph, start, goal, heuristic):
    priority_queue = []
    heapq.heappush(priority_queue, (heuristic[start], start, [start]))

    visited = set()
    explored = []

    while priority_queue:
        h, node, path = heapq.heappop(priority_queue)

        if node in visited:
            continue

        visited.add(node)
        explored.append(node)

        if node == goal:
            return path, explored

        for neighbor, cost in graph[node]:
            if neighbor not in visited:
                heapq.heappush(priority_queue, (heuristic[neighbor], neighbor, path + [neighbor]))

    return None, explored