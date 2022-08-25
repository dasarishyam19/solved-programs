array = ["a","ab","aab","abc","a","abb","aac","a","aab","abc","ab"]
dictionary={}
for i in array:
    dictionary[i]=array.count(i)
sort_dictionary=sorted(dictionary.items(),key=lambda x:x[1],reverse=True)
print(sort_dictionary[0])
