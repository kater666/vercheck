from time import localtime


def get_current_time():
    """Get the local time and return string: '[y/m/d h/m/s]'."""

    year = localtime().tm_year

    if localtime().tm_mon < 10:
        mon = '0' + str(localtime().tm_mon)
    else:
        mon = str(localtime().tm_mon)

    if localtime().tm_mday < 10:
        day = '0' + str(localtime().tm_mday)
    else:
        day = str(localtime().tm_mday)

    if localtime().tm_hour < 10:
        hour = '0' + str(localtime().tm_hour)
    else:
        hour = localtime().tm_hour

    if localtime().tm_min < 10:
        minute = '0' + str(localtime().tm_min)
    else:
        minute = localtime().tm_min

    if localtime().tm_sec < 10:
        sec = '0' + str(localtime().tm_sec)
    else:
        sec = localtime().tm_sec

    current_time = '[%d/%s/%s %s:%s:%s]' % (year, mon, day, hour, minute, sec)
    return current_time
