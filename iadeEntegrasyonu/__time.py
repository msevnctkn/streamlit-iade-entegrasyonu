import datetime

def ms_to_datetime(ms):
    return datetime.datetime.fromtimestamp(ms/1000.0)


def now():
    return datetime.datetime.now()