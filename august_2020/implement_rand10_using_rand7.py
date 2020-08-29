# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7


def rand7():
    pass


class Solution:
    """
    Given the API rand7 which generates a uniform random integer in the range 1 to 7, write a function rand10 which generates a uniform random integer in the range 1 to 10. You can only call the API rand7 and you shouldn't call any other API. Please don't use the system's Math.random().

    Notice that Each test case has one argument n, the number of times that your implemented function rand10 will be called while testing.

    Follow up:

        What is the expected value for the number of calls to rand7() function?
        Could you minimize the number of calls to rand7()?


    Example 1:

    Input: n = 1
    Output: [2]

    Example 2:

    Input: n = 2
    Output: [2,8]

    Example 3:

    Input: n = 3
    Output: [3,8,10]

    Constraints:

        1 <= n <= 105
    """

    def rand10(self):
        """
        :rtype: int
        """
        curr = 40
        while curr >= 40:
            curr = (rand7() - 1) * 7 + rand7() - 1
        return curr % 10 + 1


# general format to convert from randN() to randM()
# The randN() API is already defined for you.
# def randN():
# @return a random integer in the range 1 to M


def randN():
    pass


class Solution_general:
    def randM(self, N, M):
        """
        :rtype: int
        """
        # acceptable is the desired range which can generate required integer directly
        curr = acceptable = N * N - (N * N) % M
        # if current no is not in the acceptable range, discard it and repeat the process again
        while curr >= acceptable:
            curr = (randN() - 1) * N + randN() - 1
        return curr % M + 1
