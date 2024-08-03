import unittest
from ezsignal.Signal import Signal
from ezsignal.Event import Event

class test_connection(unittest.TestCase):

    def test_event_init(self):
        event = Event()
        self.assertTrue(isinstance(event.signal, Signal))


if __name__ == '__main__':
    unittest.main()
