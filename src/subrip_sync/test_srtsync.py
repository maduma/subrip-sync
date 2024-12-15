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
