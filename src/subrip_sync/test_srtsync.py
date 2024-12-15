import unittest
from . import subrip
from datetime import timedelta

class TestSubRipMethods(unittest.TestCase):
    def test_parse_timecode(self):
        tc = '123:12:04,657'
        td = timedelta(hours=123, minutes=12, seconds=4, milliseconds=657)
        self.assertEqual(subrip.parse_timecode(tc), td)

    def test_strf_timecode(self):
        td = timedelta(hours=123, minutes=12, seconds=4, milliseconds=657)
        tc = '123:12:04,657'
        self.assertEqual(subrip.strf_timecode(td), tc)

    def test_process_line(self):
        line = '...01:02:04,999 --> 01:12:02,057...'
        lag = 64002
        result = '...01:03:09,001 --> 01:13:06,059...'
        self.assertEqual(subrip.process_line(line, lag), result)

    def test_process_doc(self):
        doc1 = '''
1
00:01:24,210 --> 00:01:25,503
"Apocalypse 21.

2
00:01:27,588 --> 00:01:29,840
"Je vis un nouveau Ciel
et une nouvelle Terre.

'''
        doc2 = '''
1
00:01:24,330 --> 00:01:25,623
"Apocalypse 21.

2
00:01:27,708 --> 00:01:29,960
"Je vis un nouveau Ciel
et une nouvelle Terre.

'''
        self.assertEqual(subrip.process_document(doc1.splitlines(keepends=True), 120), doc2)