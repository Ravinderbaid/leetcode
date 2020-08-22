from typing import List


class Solution:
    """
    Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

    You may return any answer array that satisfies this condition.

    Example 1:

    Input: [3,1,2,4]
    Output: [2,4,3,1]
    The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

    Note:

        1 <= A.length <= 5000
        0 <= A[i] <= 5000
    """

    def sortArrayByParity(self, A: List[int]) -> List[int]:
        i = 0
        count = 0
        while i < len(A) - count:
            if bin(A[i])[-1] == "1":
                val = A.pop(i)
                A.append(val)
                count += 1
            else:
                i += 1
        return A
