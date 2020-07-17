# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Code to check if two binary trees are equal
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p and q:
            if p.val == q.val:
                return self.isSameTree(p.right, q.right) and self.isSameTree(
                    p.left, q.left
                )
            else:
                return False
        elif (p and (not q)) or ((not p) and q):
            return False
        else:
            return True
