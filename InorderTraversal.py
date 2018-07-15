# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        list1 = []
        if root is None:
            return list1
        self.inorder(list1, root.left)
        list1.append(root.val)
        self.inorder(list1, root.right)
        return list1

    def inorder(self, list1, root):
        if root is None:
            return list1

        self.inorder(list1, root.left)
        list1.append(root.val)
        self.inorder(list1, root.right)