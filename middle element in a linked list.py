class Node:
    def __init__(self, data):	
        self.data = data
        self.next = None
class  Linkedlist:
    def insertnode(self,head_ref,data_val):
        newnode = Node(data_val)
        newnode.next = head_ref
        head_ref = newnode
        return head_ref
    def getLength(self, head):
        t = 0
        temp = head
        while temp != None:
            t += 1
            temp = temp.next
        return t        
    def middle_element(self, head):
        if head != None:
            length = self.getLength(head)
            temp = head
            middle_index = length // 2
            while middle_index != 1:
                temp = temp.next
                middle_index -= 1
            print("middle element is [%d]:" % temp.data)


head = None
object1 = Linkedlist()
length_of_linkedlist = int(input("enter length of linked list"))
for i in range(length_of_linkedlist):
    head=object1.insertnode(head,int(input()))   
object1.middle_element(head)