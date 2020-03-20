graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

visited = [] # List to keep track of visited nodes.
queue = []     #Initialize a queue

def bfs(graph, node):

    while node not in visited:
        visited.append(node)

        for neighbor in graph[node]:
            bfs(graph, neighbor)


# Driver Code
bfs(graph, 'A')
print(visited)
