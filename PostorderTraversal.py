# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        list1 = []
        self.postorder(list1, root)
        return list1

    def postorder(self, list1, root):
        if root is None:
            return list1
        self.postorder(list1, root.left)
        self.postorder(list1, root.right)
        list1.append(root.val)

        return list1           