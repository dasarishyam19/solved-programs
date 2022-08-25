from functools import cmp_to_key
class student:
    def __init__(self, name, age,total):
        self.name=name
        self.age=age   
        self.total = total     
    def __repr__(self):
        return {'name':self.name,'age':self.age,'total':self.total}
        
    def comparator(object1, object2):
        if object1.total>object2.total:
            return -1
        if object1.total<object2.total:
            return 1
        if object1.age>object2.age:
            return -1
        if object1.age<object2.age:
            return 1           
        return 0
n = int(input())
data = []
for i in range(n):
    name, age,= input().split()
    age = int(age)
    total = list()
    for j in range(2):
        total.append(int(input()))
    total = sum(total)
    stobj = student(name, age, total)
    data.append(stobj)
    
data = sorted(data, key=cmp_to_key(student.comparator))
for i in data:
    print(i.name,i.total,i.age)