
class Node:

    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
    
    def preorder(self, start, traversal):
        """root, left, right"""
        if start:
            traversal += str(start.value) + "-"
            traversal = self.preorder(start.left, traversal)
            traversal = self.preorder(start.right, traversal)
        return traversal
      
         
    def __str__(self):
        """display node"""
        self.inorder()

node1 = Node(1)
node1.left = Node(2)
node1.right = Node(3)
node1.left.left = Node(4)
node1.right.right = Node(5)

order = node1.preorder(node1, "")
print(order)

"""
notes, When you traverse a tree, you call the traversal method on the
both right and left subtree don't just call it from the node only and 
expect it to traverse on its own. 
"""