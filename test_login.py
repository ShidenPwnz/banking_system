import unittest
from banking_system import login

class TestLogin(unittest.TestCase):

    def test_login(self):


        #the function logs in a user with correct credentials
        user_accounts = {"user1": "password1", "user2": "password2", "user3": "password3"}
        log_in = {"user1": False, "user2": False, "user3": False}
        username = "user1"
        password = "password1"
        expected_log_in = {"user1": True, "user2": False, "user3": False}
        actual_log_in = log_in.copy()
        login(user_accounts, actual_log_in, username, password)
        self.assertEqual(actual_log_in, expected_log_in)

        #the function rejects invalid credentials
        user_accounts = {"user1": "password1", "user2": "password2", "user3": "password3"}
        log_in = {"user1": False, "user2": False, "user3": False}
        username = "user1"
        password = "wrong_password"
        expected_log_in = {"user1": False, "user2": False, "user3": False}
        actual_log_in = log_in.copy()
        login(user_accounts, actual_log_in, username, password)
        self.assertEqual(actual_log_in, expected_log_in)

        #the function handles non-existent usernames
        user_accounts = {"user1": "password1", "user2": "password2", "user3": "password3"}
        log_in = {"user1": False, "user2": False, "user3": False}
        username = "non_existent_user"
        password = "password1"
        expected_log_in = {"user1": False, "user2": False, "user3": False}
        actual_log_in = log_in.copy()
        login(user_accounts, actual_log_in, username, password)
        self.assertEqual(actual_log_in, expected_log_in)

if __name__ == '__main__':
    unittest.main()
