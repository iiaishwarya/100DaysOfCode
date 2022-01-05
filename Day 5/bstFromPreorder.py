class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def bst(preorder):
            if not preorder:
                return None
            root = TreeNode(preorder[0], None, None)
            i = 1
            while i<len(preorder) and  preorder[i] < root.val:
                i+=1
            root.left = bst(preorder[1:i])
            root.right = bst(preorder[i:])
            return root

        return bst(preorder)
