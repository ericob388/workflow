import unittest
from handlers.hello_handler import handle_event


class TestHelloHandler(unittest.TestCase):

    def test_string(self):
        self.assertEqual(handle_event({'name': 'Eric'}), 'Hello Eric')

    def test_non_dict(self):
        with self.assertRaises(TypeError):
            handle_event(1)

    def test_no_name_key(self):
        with self.assertRaises(KeyError):
            handle_event(dict())
            
    def test_failure(self):
        self.assertTrue(false)


if __name__ == '__main__':
    import xmlrunner
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))
