def breadth(graph, start):
    visited = set()
    queue = [start]

    while queue:
        node = queue.pop(0)
        if node not in visited:
            print(node)
            visited.add(node)
            queue.extend(neighbour for neighbour in graph[node] if neighbour not in visited)

graph = {
    '2': ['9', '6'],
    '9': ['1', '7'],
    '6': ['4'],
    '1': [],
    '7': ['4'],
    '4': []
}

print("Following is the Breadth-First Search")
breadth(graph, '2')
