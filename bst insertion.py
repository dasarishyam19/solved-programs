class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key
    def insertnode(self, root, e):             #insertion
        if root is None:
            return Node(e)
        else:
            if root.val == e:
                return root
            elif root.val < e:
                root.right = r.insertnode(root.right, e)
            else:
                root.left = r.insertnode(root.left,e)
        return root
    def search(self,root,key):         #search
        if root is None or root.val == key:
            return root
        if root.val < key:
            return r.search(root.right,key)
        return r.search(root.left,key)
    def minValueNode(self,node):               #find inordersuccessor(min value)
        current = node
        while current.left is not None:
            current = current.left
        return current     
    def deleteNode(self,root, val):             #deletion
      
        if root is None:
            return root

        if val < root.val:
            root.left = r.deleteNode(root.left, val)
        elif val > root.val:    
            root.right = r.deleteNode(root.right, val)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
  
            elif root.right is None:
                temp = root.left
                root = None
                return temp
  
        temp = r.minValueNode(root.right)
  
        root.val = temp.val
  
        root.right = r.deleteNode(root.right, temp.val)
  
        return root               
    def inorder(self,root):              #inorder
        if root:
            r.inorder(root.left)
            print(root.val)
            r.inorder(root.right)
    def preorder(self,root):             #preorder
        if root:
            print(root.val)
            r.preorder(root.left)
            r.preorder(root.right)
    def postorder(self,root):           #postorder
        if root:
            r.postorder(root.left)
            r.postorder(root.right)
            print(root.val)
    def height(self, root):              #height of the tree
        if root is None:
            return 0
        left = r.height(root.left)
        right = r.height(root.right)
        return max(left,right) + 1
n = int(input("enter no of nodes:"))  
r = Node(int(input()))          
for i in range(n-1):
    e = int(input())
    r = r.insertnode(r,e)
a=r.height(r)
print("height of the tree is :",str(a),end='\n') 
print("inorder :",end='\n')   
r.inorder(r)
print("preorder:",end='\n')
r.preorder(r)
print("postorder:",end='\n')
r.postorder(r)
print("search:",end='\n')
s=int(input("enter element to search:"))
temp=r.search(r,s)
if temp == None:
    print("element not found",end='\n')
else:
    print("element is found",end='\n')  
l = int(input("enter element to be deleted:"))
r.deleteNode(r,l)      
print("after deletion:",end='\n')
r.inorder(r)   

