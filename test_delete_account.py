import unittest
from banking_system import delete_account

class TestDeleteAccount(unittest.TestCase):

    def test_delete_existing_account(self):
        user_accounts = {'user1': 'pass1', 'user2': 'pass2'}
        log_in = {'user1': True}
        bank = {'user1': 1000, 'user2': 500}
        username = 'user1'
        password = 'pass1'
        expected_output = True

        result = delete_account(user_accounts, log_in, bank, username, password)
        self.assertEqual(result, expected_output)
        self.assertNotIn(username, user_accounts)
        self.assertNotIn(username, log_in)
        self.assertNotIn(username, bank)

    def test_delete_nonexisting_account(self):
        user_accounts = {'user1': 'pass1', 'user2': 'pass2'}
        log_in = {'user1': True}
        bank = {'user1': 1000, 'user2': 500}
        username = 'user3'
        password = 'pass3'
        expected_output = False

        result = delete_account(user_accounts, log_in, bank, username, password)
        self.assertEqual(result, expected_output)
        self.assertNotIn(username, user_accounts)
        self.assertNotIn(username, log_in)
        self.assertNotIn(username, bank)

    def test_delete_account_with_incorrect_password(self):
        user_accounts = {'user1': 'pass1', 'user2': 'pass2'}
        log_in = {'user1': True}
        bank = {'user1': 1000, 'user2': 500}
        username = 'user1'
        password = 'wrongpass'
        expected_output = False

        result = delete_account(user_accounts, log_in, bank, username, password)
        self.assertEqual(result, expected_output)
        self.assertIn(username, user_accounts)
        self.assertIn(username, log_in)
        self.assertIn(username, bank)

    def test_delete_account_not_logged_in(self):
        user_accounts = {'user1': 'pass1', 'user2': 'pass2'}
        log_in = {'user2': True}
        bank = {'user1': 1000, 'user2': 500}
        username = 'user1'
        password = 'pass1'
        expected_output = False

        result = delete_account(user_accounts, log_in, bank, username, password)
        self.assertEqual(result, expected_output)
        self.assertIn(username, user_accounts)
        self.assertNotIn(username, log_in)
        self.assertIn(username, bank)


if __name__ == '__main__':
    unittest.main()
