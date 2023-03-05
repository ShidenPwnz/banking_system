import unittest
from banking_system import transfer

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

if __name__ == '__main__':
    unittest.main()
