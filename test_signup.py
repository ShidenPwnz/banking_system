import unittest
from banking_system import signup


class TestSignup(unittest.TestCase):
    def setUp(self):
        self.user_accounts = {}
        self.log_in = {}

    def test_signup_success(self):
        username = "Brandon"
        password = "Pa$$w0rd"
        self.assertTrue(signup(self.user_accounts, self.log_in, username, password))
        self.assertEqual(self.user_accounts, {"Brandon": "Pa$$w0rd"})
        self.assertEqual(self.log_in, {"Brandon": False})

    def test_signup_user_exists(self):
        username = "Brandon"
        password = "Pa$$w0rd"
        self.user_accounts = {"Brandon": "Pa$$w0rd"}
        self.assertFalse(signup(self.user_accounts, self.log_in, username, password))
        self.assertEqual(self.user_accounts, {"Brandon": "Pa$$w0rd"})
        self.assertEqual(self.log_in, {})

    def test_signup_invalid_password(self):
        username = "Brandon"
        password = "password123"
        self.assertFalse(signup(self.user_accounts, self.log_in, username, password))
        self.assertEqual(self.user_accounts, {})
        self.assertEqual(self.log_in, {})

if __name__ == '__main__':
    unittest.main()


