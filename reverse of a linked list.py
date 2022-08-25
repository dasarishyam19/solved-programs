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
    def reverseList(self, head):
        prev=None
        curr=head
        while curr is not None:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        head=prev
        return prev
    def printlist(self, head):
        while head:
            print('[%d]->'% head.data,end="")
            head = head.next
        print("NULL")        
head = None
object1 = Linkedlist()
length_of_linkedlist = int(input("enter length of linked list"))
for i in range(length_of_linkedlist):
    head=object1.insertnode(head,int(input())) 
head = object1.reverseList(head)
object1.printlist(head)