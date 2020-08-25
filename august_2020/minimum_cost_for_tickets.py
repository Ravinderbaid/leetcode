from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        NOT_Traveling_Day = -1
        dp_cost = [NOT_Traveling_Day for _ in range(366)]
        dp_cost[0] = 0

        for day in days:
            dp_cost[day] = 0
        for day_i in range(1, 366):

            if dp_cost[day_i] == NOT_Traveling_Day:
                dp_cost[day_i] = dp_cost[day_i - 1]
            else:
                dp_cost[day_i] = min(
                    dp_cost[day_i - 1] + costs[0],
                    dp_cost[max(day_i - 7, 0)] + costs[1],
                    dp_cost[max(day_i - 30, 0)] + costs[2],
                )

        # Cost on last day of this year is the answer
        return dp_cost[365]
