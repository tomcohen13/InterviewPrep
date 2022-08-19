def buildTree(self, preorder: List[int], inorder: List[int]) -> 
Optional[TreeNode]:
        # ok nice, i think i got this
        
        if not inorder: 
            return None
        
        root = TreeNode(val=preorder.pop(0))
        
        # divide into elements to the left and the right of the root
        i = inorder.index(root.val)
        left = inorder[:i]
        right = inorder[i+1:]
                        
        root.left = self.buildTree(preorder, left)
        root.right = self.buildTree(preorder, right)
        
        return root
