class Solution:
    def climbStairs(self, n: int) -> int:
        def solve(n, dp):
            if n == 1:
                return 1
            if n == 2:
                return 2
            if dp[n]:
                return dp[n]
            else:
                dp[n] = solve(n - 1, dp) + solve(n - 2, dp)
            return dp[n]

        dp = [0] * (n + 1)
        return solve(n, dp)
