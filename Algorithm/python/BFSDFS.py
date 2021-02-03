graph = {
    'A':['B', 'C'],
    'B':['A', 'C', 'D'],
    'C':['A', 'B', 'D', 'E'],
    'D':['B', 'C', 'E', 'F'],
    'E':['C', 'D'],
    'F':['D']
}

def BFS(graph, s):
    queue = []
    queue.append(s)
    seen = set()
    seen.add(s) 
    parent = {s : None}
    while len(queue) > 0 :
        vertex = queue.pop(0)
        nodes = graph[vertex]
        for node in nodes:
            if node not in seen:
                queue.append(node)
                seen.add(node)
                parent[node] = vertex
        #print(vertex)
    return parent
parent = BFS(graph=graph, s='E')
v = 'B'
while v != None:
    print(v)
    v = parent[v]

def DFS(graph, s):
    stack = []
    stack.append(s)
    seen = set()
    seen.add(s) 
    while len(stack) > 0 :
        vertex = stack.pop()
        nodes = graph[vertex]
        for node in nodes:
            if node not in seen:
                stack.append(node)
                seen.add(node)
        print(vertex)
