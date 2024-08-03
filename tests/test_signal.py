import time
import unittest
from ezsignal import Signal
from ezsignal import Connection
from ezsignal import ThreadBundle


def test_connection_func():
    time.sleep(.5)


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

    def test_signal_emit(self):
        signal = Signal()
        connection = signal.connect(test_connection_func)
        thread_bundle = signal.emit()
        self.assertTrue(isinstance(thread_bundle, ThreadBundle))
        self.assertEqual(len(thread_bundle.threads), 1)
        self.assertTrue(thread_bundle.is_running)
        self.assertFalse(thread_bundle.is_dead)
        thread_bundle.join()
        self.assertFalse(thread_bundle.is_running)
        self.assertTrue(thread_bundle.is_dead)


if __name__ == '__main__':
    unittest.main()
