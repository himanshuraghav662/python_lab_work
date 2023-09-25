graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['E', 'F'],
    'D': ['G', 'B'],
    'E': ['B', 'C'],
    'F': ['C', 'H'],
    'G': ['H'],
    'H': ['K'],
    'K': ['L'],
    'L': ['M'],
    'M': ['N']
}

visited = []
queue = []
res = ['I', 'N']


def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)
    while queue:
        s = queue.pop(0)
        if s in res:
            print(s, 'Reached')
            break
        print(s, end=' ')
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


bfs(visited, graph, 'A')
           
