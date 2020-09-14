# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

# Example 1:

# Input: [[0, 30],[5, 10],[15, 20]]
# Output: 2
# Example 2:

# Input: [[7,10],[2,4]]
# Output: 1
# NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

# Accepted
# 315,133
# Submissions
# 687,497

# Amazon 25 
# bloomberg 16
# Facebook 11
# Google 10
# Apple
# 5
# eBay
# 5
# Microsoft
# 3

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
      
        if not intervals:
            return 0
        
        list_rooms = []
        intervals = sorted(intervals)
        list_rooms.append(intervals[0][1])
        
        for interval in intervals[1:]:
            if interval[0] >= list_rooms[0]:
                heapq.heappop(list_rooms)
            heapq.heappush(list_rooms, interval[1] )
            print(list_rooms)
        
        return len(list_rooms)
