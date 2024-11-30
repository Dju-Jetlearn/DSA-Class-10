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


def Insert(root,k):
    if root == None:
        return TreeNode(k)
    if k < root.data:
        root.left = Insert(root.left, k)
    else:
        root.right = Insert(root.right, k)
    return root

def Search(root, ki):
    if root.data == ki:
        return root
    elif ki < root.data and root.left is not None:
        return Search(root.left, ki)
    elif ki > root.data and root.right is not None:
        return Search(root.right, ki)
    else:
        return -1
    
root = TreeNode(10)
root.left = TreeNode(20)
root.right = TreeNode(30)
root.left.left = TreeNode(40)
root.left.right = TreeNode(50)
root.right.left = TreeNode(60)
root.right.right = TreeNode(70)

user = input("Do you want to insert a number, or search for one? ")

if user == "Insert":
    userinput = int(input("What number do you want to insert? "))
    Insert(root, userinput)
    InOrderTraversal(root)
elif user == "Search":
    userinput = int(input("What number do you want to search for? "))
    Search(root, userinput)
    InOrderTraversal(root)
else:
    print("That is not a valid choice, either choose the options available, or remember there are no spaces and the first letter is capital.")