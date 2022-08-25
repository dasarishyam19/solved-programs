import collections
def dfs(visited, graph, root,p):
    if root not in visited:
        p.append(root)
        visited.add(root)
        for j in graph[root]:
            dfs(visited,graph,j,p)
    return p               
def bfs(graph,root):
    visited = set()
    queue = collections.deque([root])
    while queue:
        vertex = queue.popleft()
        visited.add(vertex)
        for i in graph[vertex]:
            if i not in visited:
                queue.append(i)
    print(visited)            
dictionary = {'a': ['b','d','e'], 'b': ['c','e'], 'c':['e','f','g'], 'd':['e'], 'e':['f'],'f':['g'],'g':[]} 
get_first_key = list(dictionary.keys())[0]
visited = set()  
print("dfs:",end='\n')
path=list()
print(dfs(visited,dictionary,get_first_key,path))
print("bfs:",end='\n')
bfs(dictionary,get_first_key)