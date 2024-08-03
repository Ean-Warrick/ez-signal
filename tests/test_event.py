import unittest
from ezsignal.Signal import Signal
from ezsignal.Event import Event
from ezsignal.ThreadBundle import ThreadBundle

class test_connection(unittest.TestCase):

    def test_event_init(self):
        event = Event()
        self.assertTrue(isinstance(event.signal, Signal))

    def test_event_emit(self):
        value = 0

        def test(new_value):
            global value
            value = new_value

        event = Event()
        event.signal.connect(test)
        test_value = 3
        thread_bundle = event.emit(test_value)
        self.assertTrue(isinstance(thread_bundle, ThreadBundle))
        thread_bundle.join()
        self.assertEqual(value, test_value)


if __name__ == '__main__':
    unittest.main()
