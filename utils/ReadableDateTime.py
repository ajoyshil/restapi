import pytz
from django.db.models import DateTimeField


def generate_readable_date_time(date_time: DateTimeField):
    tz = pytz.timezone("Asia/Kolkata")
    return date_time.astimezone(tz=tz).strftime('%a, %d %B %Y %I:%M:%S %p')


def generate_readable_time(date_time: DateTimeField):
    tz = pytz.timezone("Asia/Kolkata")
    return date_time.astimezone(tz=tz).strftime('%I:%M %p')