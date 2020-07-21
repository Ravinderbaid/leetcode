from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(i, j, word, l, r):
            if len(word) == 0:
                return True
            elif i < 0 or j < 0 or i >= l or j >= r or board[i][j] != word[0]:
                return False
            s = board[i][j]
            board[i][j] = "#"
            result = (
                backtrack(i, j + 1, word[1:], l, r)
                or backtrack(i, j - 1, word[1:], l, r)
                or backtrack(i + 1, j, word[1:], l, r)
                or backtrack(i - 1, j, word[1:], l, r)
            )
            board[i][j] = s
            return result

        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i, j, word, len(board), len(board[0])):
                    return True
        return False
