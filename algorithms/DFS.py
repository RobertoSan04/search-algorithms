def dfs(graph, start ,goal):
    stack = [(start, [start])]
    visited = set()
    explored = []

    while stack:
        node, path = stack.pop()

        if node in visited:
            continue

        visited.add(node)
        explored.append(node)

        if node == goal:
            return path, explored

        for neighbor, cost in graph[node]:
            if neighbor not in visited:
                stack.append((neighbor, path + neighbor))

    return None, explored