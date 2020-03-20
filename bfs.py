

# Using a Python dictionary to act as an adjacency list
graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

visited = [] # Array to keep track of visited nodes.
queue = []

def dfs(graph, node):
    if node not in visited:
        visited.append(node)
        queue.append(node)

        while queue:
            current = queue.pop(0)
            for neighbor in graph[current]:
                if neighbor not in visited:
                    visited.append(neighbor)
                    queue.append(neighbor)

# Driver Code
dfs(graph, 'A')
print(visited)
