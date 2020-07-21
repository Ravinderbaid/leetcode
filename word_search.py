from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(i, j, word, l, r, board):
            if len(word) == 0:
                return True
            elif i < 0 or j < 0 or i >= l or j >= r or board[i][j] != word[0]:
                return False
            s = board[i][j]
            board[i][j] = "#"
            result = (
                backtrack(i, j + 1, word[1:], l, r, board)
                or backtrack(i, j - 1, word[1:], l, r, board)
                or backtrack(i + 1, j, word[1:], l, r, board)
                or backtrack(i - 1, j, word[1:], l, r, board)
            )
            board[i][j] = s
            return result

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    if backtrack(
                        i, j, word[1:], len(board), len(board[i]), board
                    ):
                        return True
        return False
