# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root is None:
            return None
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val == key:
            if root.left is None:
                root.val = self.getRightMostVal(root.left)
                root.left = self.removeRightMostAndGetLeftNode(root.left)
            else:
                root = root.right
        return root

    def getRightMostVal(self, root):
        while root.right:
            root = root.right
        return root.val

    def removeRightMostAndGetLeftNode(self, node):
        if not node.right:
            return node.left
        node.right = self.removeRightMostAndGetLeftNode(node.right)
        return node
