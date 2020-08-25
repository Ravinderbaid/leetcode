# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Find the sum of all left leaves in a given binary tree.

    Example:

          3
         / \
        9  20
          /  \
         15   7

    There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.

    """

    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        left_leaves = []

        def preorder(root, left):
            if root:
                if root.left:
                    preorder(root.left, True)
                if root.right:
                    preorder(root.right, False)
                else:
                    if left and not root.right and not root.left:
                        left_leaves.append(root.val)

        preorder(root, False)
        return sum(left_leaves)
