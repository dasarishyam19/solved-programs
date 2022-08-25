l =[{"model":"model3","code":"ERR-20"},
{"model":"model1","code":"ERR-03"},
{"model":"model1","code":"ERR-06"},
{"model":"model1","code":"ERR-06"},
{"model":"model3","code":"ERR-100"},
{"model":"model2","code":"ERR-11"},
{"model":"model3","code":"ERR-02"},
{"model":"model3","code":"ERR-02"},
{"model":"model2","code":"ERR-12"},
{"model":"model2","code":"ERR-12"},
{"model":"model2","code":"ERR-11"},
{"model":"model3","code":"ERR-16"},
{"model":"model1","code":"ERR-02"},
{"model":"model1","code":"ERR-01"},
{"model":"model1","code":"ERR-02"},
{"model":"model1","code":"ERR-02"},
{"model":"model1","code":"ERR-03"},
{"model":"model2","code":"ERR-11"},
{"model":"model1","code":"ERR-03"},
{"model":"model2","code":"ERR-11"},
{"model":"model2","code":"ERR-11"},
{"model":"model2","code":"ERR-11"},
{"model":"model2","code":"ERR-40"},
{"model":"model2","code":"ERR-40"},
{"model":"model2","code":"ERR-12"},
{"model":"model2","code":"ERR-40"},
{"model":"model2","code":"ERR-12"},
{"model":"model2","code":"ERR-10"},
{"model":"model2","code":"ERR-10"},
{"model":"model3","code":"ERR-100"},
{"model":"model3","code":"ERR-100"},
{"model":"model3","code":"ERR-100"},
{"model":"model3","code":"ERR-20"},
{"model":"model3","code":"ERR-20"},
{"model":"model3","code":"ERR-20"},
{"model":"model3","code":"ERR-20"}]
dictionary = dict() 
for i in l:
    key = i
    value = list()
    for j in key:
        value.append(key[j])
    if value[0] not in dictionary:
        dictionary[value[0]] = dict()
    else:        
        for k in dictionary:
            if k == value[0]:
                keyvaluedictionary = dict()
                keyvaluedictionary = dictionary[k]
                if value[1] not in keyvaluedictionary:
                    keyvaluedictionary[value[1]] = 1
                else:
                    keyvaluedictionary[value[1]] += 1
                dictionary[k] = keyvaluedictionary     
max_code_dictionary = dict()                                               
for i in dictionary:
    valuedictionary = dict()
    valuedictionary = dictionary[i]
    sorted_valuedictionary = dict(sorted(valuedictionary.items(), key=lambda x: x[1], reverse=True))
    first_value_key = list(sorted_valuedictionary.keys())[0]
    max_code_dictionary[i] = first_value_key
    sorted_valuedictionary = dict(list(sorted_valuedictionary.items())[0:3])
    dictionary[i] = sorted_valuedictionary  
sorted_max_code_dictionary = sorted(max_code_dictionary.items(), key=lambda x: x[1], reverse=True)
z = list(sorted_max_code_dictionary[0])
for i in dictionary:
    if z[0] == i:
        p = dict()
        p = dictionary[i]
        for j in p:
            if j == z[1]:
                z.append(p[j])
                break
        break        
print("z is:",z) 
print("dictionary which contains max err code in each model:",z) 
print("first 3 error codes of each model:",dictionary)   