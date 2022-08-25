from collections import Counter
string1 = input()
string2 = input()
if Counter(string1) == Counter(string2):
    print("Both strings are anagrams")
else:
    print("They are not anagrams")    