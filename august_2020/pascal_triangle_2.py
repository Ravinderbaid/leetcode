from typing import List


class Solution:
    """
    Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.
    Note that the row index starts from 0.
    Example:
    Input: 3
    Output: [1,3,3,1]
    1
    1   1
    1   2   1
    1   3   3   1
    1   4   6   4   1
    """

    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        else:
            ans = [1, 1]
            while rowIndex >= 2:
                temp = []
                for i in range(len(ans)):
                    if i == 0:
                        temp.append(1)
                    else:
                        temp.append(ans[i - 1] + ans[i])
                temp.append(1)
                ans = temp
                rowIndex -= 1
        return ans
