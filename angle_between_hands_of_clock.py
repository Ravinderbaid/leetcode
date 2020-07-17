class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        if hour == 12:
            hour = 0
        hour_angle = 0.5 * (hour * 60 + minutes)
        minute_angle = 6 * minutes

        angle = abs(hour_angle - minute_angle)

        # Return the smaller angle of two possible angles
        angle = min(360 - angle, angle)

        return angle
