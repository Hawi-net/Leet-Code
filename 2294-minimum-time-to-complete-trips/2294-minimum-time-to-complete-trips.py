class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        check = lambda t: sum(t // bus for bus in time) >= totalTrips

        lo, hi = 1, time[0] * totalTrips
        while lo < hi:
            mid = (lo + hi) // 2
            if check(mid):
                hi = mid
            else:
                lo = mid + 1
        
        return lo
