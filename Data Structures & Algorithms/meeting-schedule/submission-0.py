class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # brute for ce method
        n = len(intervals)
        for i in range(n):
            A = intervals[i] # (0,30)
            for j in range(i + 1, n):
                B = intervals[j] # (5,10)
                if min(A.end, B.end) > max(A.start, B.start):
                    return False
        return True