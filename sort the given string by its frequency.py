def frequencySort(string):
    dictionary = {}
    for i in string:
        if i not in dictionary:
            dictionary[i] = 1
        else:
            dictionary[i] += 1
    d = dict(sorted(dictionary.items()))        
    sorted_dictionary=dict(sorted(dictionary.items(), key=lambda x: x[1], reverse=True))            
    result=""
    for i in sorted_dictionary:
        for j in range(sorted_dictionary[i]):
            result += i 
    return result
input_string = input()
print(frequencySort(input_string))    
            