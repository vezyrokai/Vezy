import unittest
from utils.validate import clean_domain, clean_ip

class ValidationTests(unittest.TestCase):
    def test_domain_normalization(self):
        self.assertEqual(clean_domain("HTTPS://Example.COM/path"), "example.com")

    def test_invalid_domain(self):
        with self.assertRaises(ValueError):
            clean_domain("not a domain")

    def test_ip(self):
        self.assertEqual(str(clean_ip("8.8.8.8")), "8.8.8.8")

if __name__ == "__main__":
    unittest.main()
