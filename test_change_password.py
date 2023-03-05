import unittest
from banking_system import change_password
class TestTransfer(unittest.TestCase):

    def test_change_password(self):
        user_accounts = {"alice": "password1", "bob": "password2"}
        log_in = {"alice": True, "bob": False}

        # Case 1: User not found
        self.assertFalse(change_password(user_accounts, log_in, "eve", "password1", "password3"))
        self.assertEqual(user_accounts, {"alice": "password1", "bob": "password2"})
        self.assertEqual(log_in, {"alice": True, "bob": False})

        # Case 2: Not logged in
        self.assertFalse(change_password(user_accounts, log_in, "bob", "password2", "password3"))
        self.assertEqual(user_accounts, {"alice": "password1", "bob": "password2"})
        self.assertEqual(log_in, {"alice": True, "bob": False})

        # Case 3: Old password incorrect
        self.assertFalse(change_password(user_accounts, log_in, "alice", "wrong_password", "password3"))
        self.assertEqual(user_accounts, {"alice": "password1", "bob": "password2"})
        self.assertEqual(log_in, {"alice": True, "bob": False})

        # Case 4: Invalid new password
        self.assertFalse(change_password(user_accounts, log_in, "alice", "password1", "123"))
        self.assertEqual(user_accounts, {"alice": "password1", "bob": "password2"})
        self.assertEqual(log_in, {"alice": True, "bob": False})

        # Case 5: Successful password change
        self.assertTrue(change_password(user_accounts, log_in, "alice", "password1", "new_password"))
        self.assertEqual(user_accounts, {"alice": "new_password", "bob": "password2"})
        self.assertEqual(log_in, {"alice": True, "bob": False})


if __name__ == '__main__':
    unittest.main()