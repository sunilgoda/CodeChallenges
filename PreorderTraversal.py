# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        list1 = []
        if root is None:
            return list1
        list1.append(root.val)
        self.preorder(list1, root.left)
        self.preorder(list1, root.right)
        return list1

    def preorder(self, list1, root):
        if root is None:
            return list1
        list1.append(root.val)
        self.preorder(list1, root.left)
        self.preorder(list1, root.right)