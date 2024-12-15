from datetime import timedelta
from itertools import chain
import re

TIMECODE_PATTERN = re.compile(r'\d{2}:\d{2}:\d{2},\d{3}')

def parse_timecode(timecode):
    keys = ['hours', 'minutes', 'seconds', 'milliseconds']
    values = [e.split(':') for e in timecode.split(',')]
    values = [int(e) for e in chain(*values)]
    kwargs = dict(zip(keys, values))
    return timedelta(**kwargs)

def strf_timedelta(td: timedelta):
    microseconds = td.microseconds // 1000
    seconds = td.seconds % 60
    minutes = td.seconds // 60 % 60
    hours = td.days * 24 + td.seconds // 3600
    return f'{hours:02d}:{minutes:02d}:{seconds:02d},{microseconds:03d}'

def process_timecode(timecode, lag):
    td = parse_timecode(timecode)
    return strf_timedelta(td + timedelta(milliseconds=lag))

def process_line(line, lag):
    return TIMECODE_PATTERN.sub(lambda m: process_timecode(m.group(0), lag), line)

def process_document(lines, lag):
    return ''.join(process_line(line, lag) for line in lines)