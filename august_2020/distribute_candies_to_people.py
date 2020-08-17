from typing import List


class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        arr = [0] * num_people
        c = 1
        pointer = 0
        while candies != 0:
            if candies - c < 0:
                arr[pointer] += candies
                candies = 0
            else:
                candies = candies - c
                arr[pointer] += c
                c += 1
            pointer += 1
            if pointer == num_people:
                pointer = 0
        return arr
