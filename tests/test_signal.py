import unittest
from ezsignal import Signal
from ezsignal import Connection


def test_connection_func():
    pass


class test_signal(unittest.TestCase):

    def test_signal_init(self):
        signal = Signal()
        self.assertEqual(len(signal.connections), 0)

    def test_signal_connect(self):
        signal = Signal()
        connection = signal.connect(test_connection_func)
        self.assertTrue(isinstance(connection, Connection))
        self.assertEqual(len(signal.connections), 1)
        self.assertEqual(signal.connections[0], connection)


if __name__ == '__main__':
    unittest.main()
