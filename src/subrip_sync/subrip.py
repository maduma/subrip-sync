import re

def parse_timecode(timecode):
    mult = [3600_000, 60_000, 1000, 1]
    fields = [e.split(':') for e in timecode.split(',')]
    values = [int(e) for e in fields[0] + fields[1]]
    return sum([i * j for (i, j) in zip(mult, values)])

def strf_duration(duration):
    microseconds = duration % 1000
    seconds = duration // 1000 % 60
    minutes = duration // 60_000 % 60
    hours = duration // 3600_000
    return f'{hours:02d}:{minutes:02d}:{seconds:02d},{microseconds:03d}'

def process_timecode(timecode, lag):
    duration = parse_timecode(timecode)
    return strf_duration(duration + lag)

pattern = re.compile(r'\d{2}:\d{2}:\d{2},\d{3}')
def process_line(line, lag):
    return pattern.sub(lambda m: process_timecode(m.group(0), lag), line)

def process_document(lines, lag):
    return ''.join(process_line(line, lag) for line in lines)