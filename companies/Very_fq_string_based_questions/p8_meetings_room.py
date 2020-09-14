# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

# Example 1:

# Input: [[0,30],[5,10],[15,20]]
# Output: false
# Example 2:

# Input: [[7,10],[2,4]]
# Output: true

# Microsoft
# 2
# Amazon
# 2


class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        # for i in range(len(intervals)):
        #     for j in range(i+1,len(intervals)):                      
        #         if (min (intervals[i][1], intervals[j][1]) > max(intervals[i][0], intervals[j][0])):
        #             return False
        # return True
        
#         out=[]
#         for interval in sorted(intervals):
#             if out and interval[0] < out[-1][1]:
#                 return False
                
#             else:
#                 out.append(interval)
                
#         return True
        if not intervals or len(intervals) < 2:
            return True

        intervals.sort(key=lambda x: x[0])
        
        start = intervals[0][0]
        end = intervals[0][1]
        
        for i in range(1, len(intervals)):
            
            intervalStart = intervals[i][0]
            intervalEnd = intervals[i][1]
            
            if intervalStart < end:
                return False
            
            start = intervalStart
            end = intervalEnd
            
        return True
            
       
