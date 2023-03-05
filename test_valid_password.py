import unittest
from banking_system import valid_password


class TestValidPassword(unittest.TestCase):
    def test_valid_password(self):
        self.assertTrue(valid_password("StrongPa55word", "user123"))
        self.assertTrue(valid_password("aBcD1234", "user456"))
        self.assertFalse(valid_password("weak", "user789"))
        self.assertFalse(valid_password("user123", "user123"))
        self.assertFalse(valid_password("password", "user123"))


if __name__ == '__main__':
    unittest.main()
