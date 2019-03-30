import datetime
#返回一天剩余的时间
def get_day_left_in_second():
    now=datetime.datetime.now()
    tomorrow = now + datetime.timedelta(days=1)
    left=(datetime.datetime(tomorrow.year,tomorrow.month,tomorrow.day,0,0,0)-now)
    return int(left.total_seconds())