def find_shortest_path(graph, start, end, path =[]):
        path = path + [start]
        if start == end:
            return path
        shortest = None
        for node in graph[start]:
            if node not in path:
                newpath = find_shortest_path(graph, node, end, path)
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath
        return shortest        
word1 = input()
word2 = input()
Dict = { "dog" : ["log","dot"],
      "log" : ["fog","lot"],
      "fog": ["fig"],
      "lot": ["pot"],
      "fig": ["pig"],
      "dot": ["pot","cot"],
      "cot": ["cat"],
      "pot": ["pet","pit"],
      "cab": [],
      "pet": [],
      "pit":[],
      "pig":[],
      "cat": ["cab","cap"],
      "cap": ["tap","map"],
      "tap": [],
      "map":[]}
print(find_shortest_path(Dict,word1,word2,path=[]))	  		