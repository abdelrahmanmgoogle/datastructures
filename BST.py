class Node:
  def __init__(self,val,right=None,left=None):
    self.val=val
    self.right=right
    self.left=left
  
class BST:
  def __init__(self,root=None):
    self.root=root
  
  def insert (self,val):
    current = self.root
    parent = current

    while current is not None:
      parent = current
      if current.val < val:
        current = current.right
      else:
        current = current.left
    
    if parent.val < val:
        parent.right = Node(val)
    else:
        parent.left = Node(val)

#Test
mybst = BST(Node(5))
mybst.insert(6)

print(mybst.root.right.val)