from streamrandom import stream_from_seed

from unittest import TestCase

class Tests(TestCase):
    """
    Some tests.
    """

    def test_read_vector1(self):
        stream = stream_from_seed("this is a test")
        stream.read(100)
        self.assertEqual(stream.read(10), b'\xdcK:R\x93)\x0b(I\x15')


    def test_seek_vector1(self):
        stream = stream_from_seed("this is a test")
        stream.seek(100)
        self.assertEqual(stream.read(10), b'\xdcK:R\x93)\x0b(I\x15')
