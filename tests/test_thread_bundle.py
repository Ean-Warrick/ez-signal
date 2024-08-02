import unittest
from ezsignal.ThreadBundle import ThreadBundle


class test_thread_bundle(unittest.TestCase):

    def test_thread_bundle_init(self):
        bundle = ThreadBundle()
        self.assertEqual(len(bundle.threads), 0)
        self.assertFalse(bundle.is_dead)
        self.assertFalse(bundle.is_running)


if __name__ == '__main__':
    unittest.main()
