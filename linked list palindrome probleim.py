class Node:
	def __init__(self,data):
		self.data=data
		self.next=None
class linkedlist:
	def insertnode(self,temp,data_value):
		newnode=Node(data_value)
		newnode.next=temp
		temp=newnode
		return temp
	def isPalindrome(head):
    		p1=p2=head
			while(p2 and p2.next):
    			p2=p2.next.next
				p1=p1.next
head = None
n = linkedlist()
k = input("enter data:")
length=len(k)
for i in range(length):
    	head = n.insertnode(head,k[i])
result=n.palindrome(head)		
if result == True:
	print("linked list is a palindrome")
else:
	print("linked list is not a palindrome")	