import threading
import time
import unittest
from ezsignal.ThreadBundle import ThreadBundle


def target_func():
    time.sleep(.5)


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

    def test_thread_bundle_start(self):
        bundle = ThreadBundle()
        thread = threading.Thread(target=target_func)
        bundle.add(thread)
        bundle.start()
        self.assertTrue(bundle.is_running)
        self.assertFalse(bundle.is_dead)
        thread.join()
        self.assertTrue(bundle.is_dead)
        self.assertFalse(bundle.is_running)



if __name__ == '__main__':
    unittest.main()
