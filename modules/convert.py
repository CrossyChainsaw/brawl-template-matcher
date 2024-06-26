def seconds_to_hms(seconds):
    hours, remainder = divmod(seconds, 3600)
    minutes, remaining_seconds = divmod(remainder, 60)
    
    hours=str(int(hours))
    minutes=str(int(minutes))
    remaining_seconds=str(int(remaining_seconds))

    if len(hours) == 1:
        hours = '0' + hours
    if len(minutes) == 1:
        minutes = '0' + minutes
    if len(remaining_seconds) == 1:
        remaining_seconds = '0' + remaining_seconds

    return hours, minutes, remaining_seconds