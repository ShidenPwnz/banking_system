import unittest
from banking_system import update


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

if __name__ == '__main__':
    unittest.main()
