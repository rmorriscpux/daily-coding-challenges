'''
Given a clock time in hh:mm format, determine, to the nearest degree, the angle between the hour and the minute hands.

Bonus: When, during the course of a day, will the angle be zero?
'''

class TimeFormatException(Exception):
    pass

# 12-hour analog clock face. Input can be in 12-hour or 24-hour format.
def clockAngle(time: str) -> int:
    try:
        hour, minute = time.split(':')
        hour = int(hour)
        minute = int(minute)
        assert hour >= 0 and hour < 24 and minute >= 0 and minute < 60
    except:
        raise TimeFormatException("Improperly formatted time. cloclAngle('hh:mm'); 'hh' between 0 and 23; 'mm' between 00 and 59.")
    minute_angle = minute * 6
    hour_angle = (hour % 12) * 30 + minute / 2
    total_angle = abs(round(hour_angle - minute_angle))
    return min(total_angle, 360 - total_angle)

# Determines when angle first increases after decreasing, then adds the last time to the list where the angle equals 0.
def printAngleZeroTimes():
    zero_angle_times = []
    last_angle = 180
    last_t = None
    can_label = True
    for h in range(1, 13):
        for m in range(0, 60):
            t = str(h) + ':' + str(m).zfill(2)
            cur_angle = clockAngle(t)
            if cur_angle > last_angle:
                if can_label:
                    zero_angle_times.append(last_t)
                    can_label = False
            elif not can_label:
                can_label = True
            last_angle = cur_angle
            last_t = t
    print("Times Where Hand Angle Is Zero:")
    print(zero_angle_times)
    return



if __name__ == "__main__":
    print(clockAngle('3:00'))
    print(clockAngle('12:00'))
    print(clockAngle('6:45'))

    print("----------")
    printAngleZeroTimes()