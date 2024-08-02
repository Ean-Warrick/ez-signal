import unittest
from ezsignal import Signal
from ezsignal import Connection


def test_connection_func():
    pass


class test_signal(unittest.TestCase):

    def test_signal_init(self):
        signal = Signal()
        self.assertEqual(len(signal.connections), 0)


if __name__ == '__main__':
    unittest.main()
