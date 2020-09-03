class Solution:
    """
    Given an array of integers, find out whether there are two distinct indices i and j in the array such that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.

    Example 1:

    Input: nums = [1,2,3,1], k = 3, t = 0
    Output: true

    Example 2:

    Input: nums = [1,0,1,1], k = 1, t = 2
    Output: true

    Example 3:

    Input: nums = [1,5,9,1,5,9], k = 2, t = 3
    Output: false

    Hide Hint #1
    Time complexity O(n logk) - This will give an indication that sorting is involved for k elements.
    Hide Hint #2
    Use already existing state to evaluate next state - Like, a set of k sorted numbers are only needed to be tracked. When we are processing the next number in array, then we can utilize the existing sorted state and it is not necessary to sort next overlapping set of k numbers again.
    """

    def containsNearbyAlmostDuplicate(self, nums, k, t):
        # Bucket sort. Each bucket has size of t. For each number, the possible
        # candidate can only be in the same bucket or the two buckets besides.
        # Keep as many as k buckets to ensure that the difference is at most k.
        buckets = {}
        for i, v in enumerate(nums):
            # t == 0 is a special case where we only have to check the bucket
            # that v is in.
            bucketNum, offset = (int(v // t), 1) if t else (v, 0)
            for idx in range(bucketNum - offset, bucketNum + offset + 1):
                if idx in buckets and abs(buckets[idx] - nums[i]) <= t:
                    return True

            buckets[bucketNum] = nums[i]
            if len(buckets) > k:
                # Remove the bucket which is too far away. Beware of zero t.
                del buckets[int(nums[i - k] // t) if t else nums[i - k]]

        return False
