class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node:
                return max(dfs(node.left) + 1, dfs(node.right) + 1)
                # return count
            else:
                return 0
            
        return dfs(root)
