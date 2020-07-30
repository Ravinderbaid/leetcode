# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def rec(arr):
            if len(postorder):
                value = postorder[-1]
                node = TreeNode(value)
                if value in arr:
                    pos = arr.index(value)
                    postorder.pop()
                    node.right = rec(arr[pos + 1 :])
                    node.left = rec(arr[:pos])
                    return node
                return None

        return rec(inorder)
