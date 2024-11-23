class TreeNode:
    def __init__(self,v):
        self.left = None
        self.right = None
        self.data = v

def InOrderTraversal(root):  #Left, Root, Right
    if root is not None:
      if root.left is not None:
          InOrderTraversal(root.left)
      print(root.data)
      if root.right is not None:
          InOrderTraversal(root.right)

def insert(root,k):
    if root == None:
        return TreeNode(k)
    if k < root.data:
        root.left = insert(root.left, k)
    else:
        root.right =insert(root.right, k)
    return root

def search(root, ki):
    if root.data == ki:
        return root
    elif ki < root.data and root.left is not None:
        return search(root.left, ki)
    elif ki > root.data and root.right is not None:
        return search(root.right, ki)
    else:
        return -1

nom = int(input("Please tell me how many nom-noms you want in the tree. "))
root = None

for i in range(nom):
    n = int(input("What do you want the number to be in this section? "))
    root = insert(root, n)
InOrderTraversal(root)

nom2 = int(input("What nom-nom do you want to insert? "))
a = search(root, nom2)

if a == -1:
    print("The key does't exist. Sorry.")
else:
    print("The key does exist, and it is", a.data)