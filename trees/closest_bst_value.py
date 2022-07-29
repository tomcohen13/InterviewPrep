def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        
        
        def binary_search(root, target):
            
            if root is None:
                return float('inf')
            
            if root.val == target:
                return root.val
            
            difference = root.val - target
            
            if difference < 0 and root.right:
                closestChild = binary_search(root.right, target)
                
            else:
                closestChild = binary_search(root.left, target)
                
            return root.val if abs(difference) < abs(closestChild - 
target) else closestChild    
        
        closest = binary_search(root, target)
        
        return closest
