import heapq

def ucs(graph, start, goal):
    heap = []
    heapq.heappush(heap, (0, start, [start]))

    visited = set()
    explored = []

    while heap:
        cost, node, path = heapq.heappop(heap)

        if node in visited:
            continue

        visited.add(node)
        explored.append(node)

        if node == goal:
            return path, explored

        for neighbor, edge_cost in graph[node]:
            if neighbor not in visited:
                heapq.heappush(heap, (cost + edge_cost, neighbor, path + [neighbor]))


    return None, explored