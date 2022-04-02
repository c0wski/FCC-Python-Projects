# function named that takes in two required parameters and one optional parameter:
def add_time(start, duration, day = None):

    # separate to hours and minutes and am/pm
    base = start[:-2].split(':')
    base_hour = int(base[0])
    base_minute = int(base[1])
    base_ampm = start[-2:]

    length = duration.split(':')
    length_hour = int(length[0])
    length_minute = int(length[1])

    # convert to 24 hr time
    if base_ampm == 'PM':
        base_hour += 12

    # add hours and minutes
    new_hour = base_hour + length_hour
    new_minute = base_minute + length_minute
    final_hour = new_hour

    # Adjust minutes
    if new_minute > 60:
        y = new_minute % 60
        final_hour += int((new_minute - y) / 60)
        final_minute = y
    else:
        final_minute = new_minute

    # calculate day
    time_change = (final_hour // 24)

    # if next day show (next day)
    # if more than 1 day later show (n days later)
    if time_change < 1:
        message = ''
    elif time_change == 1:
        message = ' (next day)'
    else:
        message = ' (' + str(time_change) + ' days later)'

    # Days of the week
    if day is not None:
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        low_day = day.lower()
        i = -1
        new_day = None
        while i < len(days):
            if days[i].lower() == low_day:
                # set new day
                index = int(i + time_change)
                # keeps index in range
                if index > len(days):
                    index = index % 7
                new_day = ', ' + days[int(index)]
                break
            else:
                  i = i + 1
                  continue

    #if more than 24 hrs have passed then
    if final_hour / 24 > 1:
        final_hour = final_hour % 12
        # adjust 00:00 to 12:00
        if final_hour < 1:
            final_hour = 12

    # check for AM/PM and set time back to 12 hr
    if final_hour > 12:
        base_ampm = 'PM'
        final_hour -= 12

    # flip am/pm at 12:00 for small time change
    elif final_hour == 12:
        if (final_hour - base_hour) < (12 - base_hour):
           base_ampm = base_ampm

        elif (final_hour - base_hour) >= (12 - base_hour):
            if base_ampm == 'AM':
                base_ampm = 'PM'
            else:
               base_ampm = 'AM'
    else:
        base_ampm = 'AM'

    # Confirm variables are string form
    final_minute = str(final_minute)
    final_hour = str(final_hour)

    # give minute double digit display
    if len(final_minute) < 2:
        final_minute = '0' + final_minute

       # if 3rd parameter received, include day of week result
    if day is None:
        new_time = str(final_hour + ':' + final_minute + ' ' + base_ampm + message)
    else:
        new_time = str(final_hour + ':' + final_minute + ' ' + base_ampm + new_day + message)

    return new_time



 

