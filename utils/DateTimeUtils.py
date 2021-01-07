from datetime import datetime


def get_unix_time(dt: datetime):
    """ This function returns the unix time when a datetime object it passed to it """
    return (dt - datetime(1970, 1, 1)).total_seconds()

