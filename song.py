liked_songs = {
    "Bad Habits": "Ed Sheeran",
    "I'm Just Ken": "Ryan Gosling",
    "Mastermind": "Taylor Swift",
    "Uptown Funk": "Mark Ronson ft. Bruno Mars",
    "Ghost": "Justin Bieber",
}

def x(liked_songs, adudu):
    song = open('song.txt', 'w')
    song.write("Liked Songs:\n")
    for songs, artist in liked_songs.items():
        song.write(f"{songs} by {artist}\n")
    print(f"Successfully added Liked songs to {adudu} ❤️")

x(liked_songs, 'song.txt')    

class BankAccount:
  def __init__(self, initial_balance=0):
    self.balance = initial_balance

  def deposit(self, amount):
    if amount <= 0:
      raise ValueError('Deposit amount must be positive')
    self.balance += amount

  def withdraw(self, amount):
    if amount <= 0:
      raise ValueError('Withdrawal amount must be positive')
    if amount > self.balance:
      raise ValueError('Insufficient funds')
    self.balance -= amount



import unittest
from paste_only import CoffeeMenu

class TestCoffeeMenu(unittest.TestCase):

  def setUp(self):
    self.menu = CoffeeMenu()

  def test_get_price_existing_item(self):
    self.assertEqual(self.menu.get_price('latte'), 2.75)

  def test_get_price_non_existing_item(self):
    self.assertIsNone(self.menu.get_price('mocha'))

  def test_add_item(self):
    self.menu.add_item('mocha', 3.50)
    self.assertEqual(self.menu.get_price('mocha'), 3.50)

if __name__ == '__main__':
  unittest.main()