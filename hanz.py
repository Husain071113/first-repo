import unittest
import math

def get_sqrt(n):
  return math.sqrt(n)

def divide(a, b):
  return a / b

class TestUnexpected(unittest.TestCase):

  def test_get_sqrt(self):
    self.assertEqual(get_sqrt(144), 12)

  def test_neg_sqrt(self):
    with self.assertRaises(ValueError):
      get_sqrt(-3)

  def test_divide(self):
    self.assertEqual(divide(64,8), 8)

  def test_zero_divide(self):
    with self.assertRaises(ZeroDivisionError):
      divide(10, 0)

if __name__ == "__main__":
  unittest.main()

import unittest

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

class TestCalculator(unittest.TestCase):

  # Setup method: New Calculator instance before each test
  def setUp(self):
    self.calculator = Calculator()

  # Teardown method: Clean up resources after each test
  def tearDown(self):
    self.calculator = None

  def test_addition(self):
    self.assertEqual(self.calculator.add(3, 5), 8)

  def test_subtraction(self):
    self.assertEqual(self.calculator.subtract(10, 4), 6)

if __name__ == '__main__':
  unittest.main()  

from song import BankAccount
import unittest

class TestBankAccount(unittest.TestCase):
  def setUp(self):
    self.account = BankAccount(100)

  def tearDown(self):
    self.account = None

  def test_initial_balance(self):
    self.assertEqual(self.account.balance, 100)

  def test_deposit_positive_amount(self):
    self.account.deposit(50)
    self.assertEqual(self.account.balance, 150)

  def test_deposit_zero_amount(self):
    with self.assertRaises(ValueError):
      self.account.deposit(0)

  def test_deposit_negative_amount(self):
    with self.assertRaises(ValueError):
      self.account.deposit(-40)

  def test_withdraw_sufficient_funds(self):
    self.account.withdraw(30)
    self.assertEqual(self.account.balance, 70)

  def test_withdraw_insufficient_funds(self):
    with self.assertRaises(ValueError):
      self.account.withdraw(200)

  def test_withdraw_zero_amount(self):
    with self.assertRaises(ValueError):
      self.account.withdraw(0)

  def test_withdraw_negative_amount(self):
    with self.assertRaises(ValueError):
      self.account.withdraw(-50)

if __name__ == '__main__':
    unittest.main()