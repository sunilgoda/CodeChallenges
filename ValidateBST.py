# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.prev = None
        return self.isValidNode(root)

    def isValidNode(self, root):
        if root is None:
            return True

        valid = self.isValidNode(root.left)

        if not self.prev:
            self.prev = root
        else:
            if root.val <= self.prev.val:
                valid = False
            self.prev = root

        valid = valid and self.isValidNode(root.right)

        return valid
