import unittest


def connection_example():
    print("fire")


class test_connection(unittest.TestCase):

    def test_connection_init(self):
        connection = Connection(connection_example)
        self.assertTrue(connection.is_connected)
        self.assertIsNotNone(connection.func)


if __name__ == '__main__':
    unittest.main()
