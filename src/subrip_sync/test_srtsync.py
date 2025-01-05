import unittest
from . import subrip

class TestSubRip(unittest.TestCase):
    def test_timecode_to_milliseconds(self):
        tc = '23:12:04,657'
        ts = 23 * 3600_000 + 12 * 60_000 + 4 * 1000 + 657
        self.assertEqual(subrip.timecode_to_milliseconds(tc), ts)

    def test_milliseconds_to_timecode(self):
        ts = 23 * 3600_000 + 12 * 60_000 + 4 * 1000 + 657
        tc = '23:12:04,657'
        self.assertEqual(subrip.milliseconds_to_timecode(ts), tc)

    def test_milliseconds_to_timecode_big(self):
        ts = 223 * 3600_000 + 2 * 60_000 + 4 * 1000 + 57
        tc = '223:02:04,057'
        self.assertEqual(subrip.milliseconds_to_timecode(ts), tc)

    def test_shift_timecode(self):
        tc1 = '01:02:14,949'
        tc2 = '01:02:19,131'
        lag = 4182
        self.assertEqual(subrip.shift_timecode(tc1, lag), tc2)

    def test_process_line(self):
        line = '...01:02:04,999 --> 01:12:02,057...'
        lag = 64002
        result = '...01:03:09,001 --> 01:13:06,059...'
        self.assertEqual(subrip.process_line(line, lag), result)

    def test_subtitles_shift_ms(self):
        doc1 = '''
1
00:01:24,210 --> 00:01:25,503
"Apocalypse 21.

2
00:01:27,588 --> 00:01:29,840
"Je vis un nouveau Ciel.

'''
        doc2 = '''
1
00:01:24,330 --> 00:01:25,623
"Apocalypse 21.

2
00:01:27,708 --> 00:01:29,960
"Je vis un nouveau Ciel.

'''
        self.assertEqual(subrip.subtitles_shift_ms(doc1.splitlines(keepends=True), 120), doc2)