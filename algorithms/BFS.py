from collections import deque

# Search algorithm: Breadth First Search
def bfs(graph, start, goal):
    # Queue: each element is (actual_node, current_path)
    queue = deque()
    queue.append ((start, [start]))

    # Visited: nodes visited for no repeat
    visited = set()
    visited.add(start)

    # Records for the order in which we explore
    explored = []

    while queue:
        node, path = queue.popleft()
        explored.append(node)

        if node == goal:
            return path, explored

        for neighbor, cost in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))


    return None, explored