import re

def timecode_to_milliseconds(timecode):
    factors = [3600_000, 60_000, 1000, 1]
    l = (s.split(':') for s in timecode.split(','))
    values = [int(e) for sublist in l for e in sublist]
    return sum([i * j for (i, j) in zip(factors, values)])

def milliseconds_to_timecode(milliseconds):
    ms = milliseconds % 1000
    seconds = milliseconds // 1000 % 60
    minutes = milliseconds // 60_000 % 60
    hours = milliseconds // 3600_000
    return f'{hours:02d}:{minutes:02d}:{seconds:02d},{ms:03d}'

def shift_timecode(timecode, lag_ms):
    ts = timecode_to_milliseconds(timecode)
    return milliseconds_to_timecode(ts + lag_ms)

pattern = re.compile(r'\d+:\d{2}:\d{2},\d{3}')
def process_line(line, lag_ms):
    return pattern.sub(lambda m: shift_timecode(m.group(0), lag_ms), line)

def process_document(lines, lag_ms):
    return ''.join(process_line(line, lag_ms) for line in lines)