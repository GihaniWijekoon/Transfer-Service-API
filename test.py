import unittest
from service import TransferService
from models import Transaction, accounts

class TestTransferService(unittest.TestCase):

    def test_valid_transfer(self):
        transaction = Transaction("123", "456", 50.0)
        response = TransferService.transfer_funds(transaction)
        self.assertEqual(response["status"], "success")

    def test_insufficient_balance(self):
        transaction = Transaction("123", "456", 1000.0)
        response = TransferService.transfer_funds(transaction)
        self.assertEqual(response["status"], "error")
        self.assertEqual(response["message"], "Insufficient balance")

    def test_invalid_account(self):
        transaction = Transaction("999", "456", 50.0)
        response = TransferService.transfer_funds(transaction)
        self.assertEqual(response["status"], "error")
        self.assertEqual(response["message"], "Invalid account number")

if __name__ == "__main__":
    unittest.main()
