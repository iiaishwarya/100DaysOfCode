# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        
        def addAtDepth(root, depth):
            
            if not root:
                return
            
            if depth == 2:
                temp = root.left
                root.left = TreeNode(val)
                root.left.left = temp
                temp = root.right
                root.right = TreeNode(val)
                root.right.right = temp
            else:
                addAtDepth(root.left, depth - 1)
                addAtDepth(root.right, depth - 1)
        
        if depth == 1:
            node = TreeNode(val)
            node.left = root
            return node
        else:
            addAtDepth(root, depth)
            return root
            
            
