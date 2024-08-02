import threading
import unittest
from ezsignal.ThreadBundle import ThreadBundle


def target_func():
    pass


class test_thread_bundle(unittest.TestCase):

    def test_thread_bundle_init(self):
        bundle = ThreadBundle()
        self.assertEqual(len(bundle.threads), 0)
        self.assertFalse(bundle.is_dead)
        self.assertFalse(bundle.is_running)

    def test_thread_bundle_add(self):
        bundle = ThreadBundle()
        thread = threading.Thread(target=target_func)
        bundle.add(thread)
        self.assertEqual(len(bundle.threads), 1)
        self.assertEqual(bundle.threads[0], thread)


if __name__ == '__main__':
    unittest.main()
