# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Given two binary search trees root1 and root2.

    Return a list containing all the integers from both trees sorted in ascending order.

    Example 1:

    Input: root1 = [2,1,4], root2 = [1,0,3]
    Output: [0,1,1,2,3,4]

    Example 2:

    Input: root1 = [0,-10,10], root2 = [5,1,7,0,2]
    Output: [-10,0,0,1,2,5,7,10]

    Example 3:

    Input: root1 = [], root2 = [5,1,7,0,2]
    Output: [0,1,2,5,7]

    Example 4:

    Input: root1 = [0,-10,10], root2 = []
    Output: [-10,0,10]

    Example 5:

    Input: root1 = [1,null,8], root2 = [8,1]
    Output: [1,1,8,8]


    Constraints:

        Each tree has at most 5000 nodes.
        Each node's value is between [-10^5, 10^5].

    Hide Hint #1
    Traverse the first tree in list1 and the second tree in list2.
    Hide Hint #2
    Merge the two trees in one list and sort it.
    """

    def traverse(self, root, l):
        if not (root):
            return []
        else:
            self.traverse(root.left, l)
            l.append(root.val)
            self.traverse(root.right, l)
        return l

    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        list1 = self.traverse(root1, [])
        list2 = self.traverse(root2, [])
        i = j = 0
        ans = []
        while i < len(list1) and j < len(list2):
            if list1[i] < list2[j]:
                ans.append(list1[i])
                i += 1
            elif list1[i] > list2[j]:
                ans.append(list2[j])
                j += 1
            else:
                ans.append(list1[i])
                ans.append(list2[j])
                i += 1
                j += 1
        while i < len(list1):
            ans.append(list1[i])
            i += 1
        while j < len(list2):
            ans.append(list2[j])
            j += 1
        return ans
