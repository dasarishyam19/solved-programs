def findMinDistance(word1, word2, Dict, result, string_index):
    temp2 = word1
    s=0
    print("word 1 :",word1)
    if word1 != word2:
        for i in Dict:
            if word1 == i:
                print("key is:",i)
                Temporary_list = list()
                Temporary_list = Dict[i]
                print("list of strings:",Temporary_list)
                for j in range(len(Temporary_list)):
                    temp = Temporary_list[j]
                    print("a string of",i,"is:",temp)
                    for k in range(len(temp)):
                        if word2[k] == temp[k] and k not in string_index:
                            s += 1
                            string_index.append(k)
                            word1 = Temporary_list[j]
                            result.append(Temporary_list[j])
                            print("strings in result  is:",result)
                            return findMinDistance(word1,word2,Dict,result,string_index)
                    if s < 1:
                            findMinDistance(temp,word2,Dict,result,string_index)    
    else:
        print(result)            
 
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
result = list() 
string_index = list()  
for i in range(len(word1)):
    if word1[i] == word2[i]:
        string_index.append(i)
print(string_index)        
findMinDistance(word1,word2,Dict,result,string_index)          