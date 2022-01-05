class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.arr = []
        
        def dfs(root):
            if not root:
                return None
            dfs(root.left)
            self.arr.append(root.val)
            dfs(root.right)
        dfs(root)
        return self.arr
