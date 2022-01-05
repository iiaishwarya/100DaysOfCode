class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(root,low=-math.inf, high=math.inf):
            if not root:
                return True
            val = root.val
            if root.val >= high or root.val <= low:
                return False
            left = validate(root.left, low, root.val)
            right = validate(root.right, root.val, high)
            
            return left and right
    
        return validate(root)
