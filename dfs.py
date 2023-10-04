graph = {
  '2' : ['9','6'],
  '9' : ['1', '7'],
  '6' : ['4'],
  '1' : [],
  '7' : ['4'],
  '4' : []
}
visited = set() 
def depth(visited, graph, node):
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            depth(visited, graph, neighbour)
print("Following is the Depth-First Search")
depth(visited, graph, '2')
