import unittest
from banking_system import import_and_create_bank


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

if __name__ == '__main__':
    unittest.main()
