class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        s = s.lower()
        while left <= right:
            while left <= right and not s[left].isalnum():
                left += 1
            while right >= left and not s[right].isalnum():
                right -= 1
            if left <= right:
                if s[left] == s[right]:
                    left += 1
                    right -= 1
                else:
                    return False
        return True
