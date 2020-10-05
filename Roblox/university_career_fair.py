import heapq

def minMeetingRooms(intervals) -> int:
    if not intervals:
        return 0

    free_rooms = []

    intervals.sort(key=lambda x: x[0])

    heapq.heappush(free_rooms, intervals[0][1])

    # For all the remaining meeting rooms
    for i in intervals[1:]:

        # If the room due to free up the earliest is free, assign that room to this meeting.
        if free_rooms[0] <= i[0]:
            heapq.heappop(free_rooms)

        # If a new room is to be assigned, then also we add to the heap,
        # If an old room is allocated, then also we have to add to the heap with updated end time.
        heapq.heappush(free_rooms, i[1])

    # The size of the heap tells us the minimum rooms required for all the meetings.
    return len(free_rooms)

"""
1. 将list按照（arrival， duration）来排序 2. 遍历 如果d[arrival]已经在d里头 那么d[arrival + duration] = max(d[arrival] + 1, d[arrival + duration]) 3.找到最大值return
"""

# def minMeetingRooms2(intervals) -> int:
