from datetime import timedelta
from itertools import chain

def parse_timecode(timecode):
    l = [e.split(':') for e in timecode.split(',')]
    l = [int(e) for e in chain(*l)]
    d = dict(zip(['hours', 'minutes', 'seconds', 'milliseconds'], l))
    return timedelta(**d)

def strf_timecode(td: timedelta):
    microseconds = td.microseconds // 1000
    seconds = td.seconds % 60
    minutes = td.seconds // 60 % 60
    hours = td.days * 24 + td.seconds // 3600
    return f'{hours:02d}:{minutes:02d}:{seconds:02d},{microseconds:03d}'