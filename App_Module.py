import datetime as dt

def format_delta_time(delta_time: dt.timedelta):
    hours, remainder = divmod(int(delta_time.seconds), 3600)
    minutes, seconds = divmod(remainder, 60)
    hours += delta_time.days * 24
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

def get_readable_date(date: str) -> str:
    raw_month = date[5:7]
    match raw_month:
        case "01":
            month = "January"
        case "02":
            month = "February"
        case "03":
            month = "March"
        case "04":
            month = "April"
        case "05":
            month = "May"
        case "06":
            month = "June"
        case "07":
            month = "July"
        case "08":
            month = "August"
        case "09":
            month = "September"
        case "10":
            month = "October"
        case "11":
            month = "November"
        case "12":
            month = "December"
        case _:
            month = "Error"
    day = date[8:10]
    if day[0] == "0":
        day = day[1]
    year = date[0:4]
    hour = date[11:13]
    if int(hour) < 12:
        hour_modifier = "AM"
        if int(hour) < 10:
            hour = hour[0]
    elif int(hour) < 13:
        hour_modifier = "PM"
    else:
        hour = int(hour) - 12
        hour_modifier = "PM"
    minutes = date[14:16]
    return f"{month} {day}, {year} at {hour}:{minutes} {hour_modifier}"