'''
Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
'''

def min_rooms(time_intervals):
    rooms = []
    
    for lecture_time in time_intervals:
        lecture_booked = False
        for room in rooms:
            room_booked = False
            # Check the times where the room is booked. Conditions where another room is needed:
            # 1) Start time or end time is between the booked times.
            # 2) Start time is before the booked times and end time is after the booked times.
            for booking in room:
                if ((lecture_time[0] < booking[1] and lecture_time[0] > booking[0]) or
                    (lecture_time[1] < booking[1] and lecture_time[1] > booking[0]) or
                    (lecture_time[0] < booking[0] and lecture_time[1] > booking[1])):
                    room_booked = True
                    break
            # Add booking to room if there is an available slot.
            if not room_booked:
                room.append(lecture_time)
                lecture_booked = True
        # Add new room if there is no available room.
        if not lecture_booked:
            rooms.append([lecture_time])

    # print(rooms)

    return len(rooms)

print(min_rooms([(30,75), (70, 120), (60,150), (0,50)]))