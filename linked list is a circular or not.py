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
    def circular(self,head):
        node=head.next
        while node is not None and node is not head:
            node=node.next
        if node == head:
            return True
        else:
            return False    
head = None
object1 = Linkedlist()
length_of_linkedlist = int(input("enter length of linked list"))
for i in range(length_of_linkedlist):
    head=object1.insertnode(head,int(input()))   
object1.middle(head)
print(object1.circular(head))
