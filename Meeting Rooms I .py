def canAttendMeetings(intervals):
    # Step 1: Sort the intervals based on their start times
    intervals.sort(key=lambda x: x[0])
    
    # Step 2: Check for overlapping intervals
    for i in range(len(intervals) - 1):
        if intervals[i][1] > intervals[i + 1][0]:
            return False
    
    return True
