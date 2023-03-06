import unittest
from banking_system import \
    valid_password, update, transfer, signup, login, import_and_create_bank, delete_account, change_password


# test for valid password
class TestValidPassword(unittest.TestCase):
    def test_valid_password(self):
        self.assertTrue(valid_password("StrongPa55word", "user123"))
        self.assertTrue(valid_password("aBcD1234", "user456"))
        self.assertFalse(valid_password("weak", "user789"))
        self.assertFalse(valid_password("user123", "user123"))
        self.assertFalse(valid_password("password", "user123"))


# test for update
class TestBankUpdate(unittest.TestCase):

    def test_update_successful(self):
        bank = {}
        log_in = {"user1": True}
        username = "user1"
        amount = 100
        self.assertTrue(update(bank, log_in, username, amount))
        self.assertEqual(bank[username], 100)

    def test_update_not_enough_balance(self):
        bank = {"user1": 50}
        log_in = {"user1": True}
        username = "user1"
        amount = -100
        self.assertFalse(update(bank, log_in, username, amount))
        self.assertEqual(bank[username], 50)

    def test_update_not_logged_in(self):
        bank = {"user1": 50}
        log_in = {"user2": True}
        username = "user1"
        amount = 100
        self.assertFalse(update(bank, log_in, username, amount))
        self.assertEqual(bank[username], 50)

    def test_update_new_user(self):
        bank = {}
        log_in = {"user1": True}
        username = "user1"
        amount = 100
        self.assertTrue(update(bank, log_in, username, amount))
        self.assertEqual(bank[username], 100)


# test for transfer
class TestTransfer(unittest.TestCase):

    def test_transfer_successful(self):
        bank = {"userA": 100, "userB": 50}
        log_in = {"userA": True}
        userA = "userA"
        userB = "userB"
        amount = 50
        self.assertTrue(transfer(bank, log_in, userA, userB, amount))
        self.assertEqual(bank[userA], 50)
        self.assertEqual(bank[userB], 100)

    def test_transfer_not_enough_balance(self):
        bank = {"userA": 50, "userB": 0}
        log_in = {"userA": True}
        userA = "userA"
        userB = "userB"
        amount = 100
        self.assertFalse(transfer(bank, log_in, userA, userB, amount))
        self.assertEqual(bank[userA], 50)
        self.assertEqual(bank[userB], 0)

    def test_transfer_not_logged_in(self):
        bank = {"userA": 100, "userB": 50}
        log_in = {"userB": True}
        userA = "userA"
        userB = "userB"
        amount = 50
        self.assertFalse(transfer(bank, log_in, userA, userB, amount))
        self.assertEqual(bank[userA], 100)
        self.assertEqual(bank[userB], 50)

    def test_transfer_to_self(self):
        bank = {"userA": 100}
        log_in = {"userA": True}
        userA = "userA"
        userB = "userA"
        amount = 50
        self.assertFalse(transfer(bank, log_in, userA, userB, amount))
        self.assertEqual(bank[userA], 100)

    def test_transfer_invalid_amount(self):
        bank = {"userA": 100, "userB": 50}
        log_in = {"userA": True}
        userA = "userA"
        userB = "userB"
        amount = 0
        self.assertFalse(transfer(bank, log_in, userA, userB, amount))
        self.assertEqual(bank[userA], 100)
        self.assertEqual(bank[userB], 50)

    def test_transfer_unknown_users(self):
        bank = {"userA": 100}
        log_in = {"userA": True}
        userA = "userA"
        userB = "userC"
        amount = 50
        self.assertFalse(transfer(bank, log_in, userA, userB, amount))
        self.assertEqual(bank[userA], 100)


# test for signup
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


# test for login
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


# test for import_create_bank
class TestBankCreation(unittest.TestCase):

    def test_bank_creation(self):
        # create a sample file with test data
        with open('test_data.txt', 'w') as f:
            f.write('John: 100.0\n')
            f.write('Mary: 200.0\n')
            f.write('Tom: 50.0\n')
            f.write('Sue: abc\n')  # invalid value, should be skipped

        # call the function with the test file
        bank = import_and_create_bank('test_data.txt')

        # assert that the bank is created correctly
        self.assertEqual(bank['John'], 100.0)
        self.assertEqual(bank['Mary'], 200.0)
        self.assertEqual(bank['Tom'], 50.0)
        self.assertNotIn('Sue', bank)

        # delete the test file
        import os
        os.remove('test_data.txt')


# test for delete_account
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


# test for change_password
class TestChangePassword(unittest.TestCase):

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