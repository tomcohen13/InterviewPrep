# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        # output
        rightSide = []
        
        # if tree is empty
        if root is None:
            return rightSide
        
        # queue for BFS
        queue = [(root,0)] 
        
        # store last level encountered
        last_level = -1
        
        while queue:
            
            # pop first item from the queue
            node, level = queue.pop(0)
            
            # if None, continue to next node 
            if not node:
                continue
            
            # if it is the first node of the next level, add it to output 
and update current level
            elif level > last_level:
                rightSide.append(node.val)
                last_level = level
            
            # add child nodes to queue
            queue.extend([(node.right, level + 1),(node.left, level + 1)])                
        
        return rightSide
            
    
