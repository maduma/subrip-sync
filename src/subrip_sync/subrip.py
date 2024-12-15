from datetime import timedelta
from itertools import chain
import re


TIMECODE_PATTERN = re.compile(r'\d+:\d{2}:\d{2},\d{3}')


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

def process_line(line, lag):
    def fn(match):
        tc = match.group(0)
        td = parse_timecode(tc)
        td = td + timedelta(milliseconds=lag)
        return strf_timecode(td)
    return TIMECODE_PATTERN.sub(fn, line)

def process_document(lines, lag):
    return ''.join([process_line(line, lag) for line in lines])