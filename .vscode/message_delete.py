sent_message = "tok nak berak tok, nak berak!, meh sini berak atas pala tok meh"

with open("sent_message.txt", "w") as doc:
  doc.write(sent_message)

with open("sent_message.txt", "r+") as doc:
  original_message = doc.read() 

  doc.seek(0)

  unsent_message = "This message has been delete."

  doc.truncate(len(unsent_message))
  doc.write(unsent_message)

print("Original message: ", original_message)
print("Unsent message: ", unsent_message)

#1
import csv

best_selling_book = None
max_sales = 0

csv1 = "Bestseller - Sheet1.csv"
with open(csv1, "r", encoding="utf-8") as csv_file:
  csv_reader = csv.reader(csv_file)

  csv_file.readline()

  for row in csv_reader:
    current_sales = float(row[4])

    if current_sales > max_sales:
      max_sales = current_sales
      best_selling_book = row


output = "bestseller_info.csv"      
with open(output, "w", newline = "") as output_file:
  csv_writer = csv.writer(output_file)

  csv_writer.writerow(["Book", "Outhor", "Sales in Million"])

  csv_writer.writerow([best_selling_book[0], best_selling_book[1], best_selling_book[4]])

print(f"Bestselling info written to {output}")  

#2
import csv

data = [
  ['Item', 'Quantity'],
  ['Blender', 2],
  ['Posters', 30],
  ['Shoes', 2]
]

try:
  pack = "packing_list.csv"
  with open(pack, "r", encoding="utf-8") as file:
    csv_reader = csv.reader(file)

    for row in csv_reader:
      print(row)

except FileNotFoundError:
  print("Packing list file not found. Creating a new one.")
  with open(pack, "w", newline = "") as file:
    csv_writer = csv.writer(file)

    csv_writer.writerows(data)

#3
def jubo(x,y):
  x = input("What's your name:")
  y = input("Where are you from:")
  return f"Hello {x} from {y}!"

print(jubo("name", "place"))  

def hex(name):
  print(f"Hello {name}!")

print(hex("Messi"))  

#4
def translator(language):

  translations = {
   'spanish': {'hello': 'hola', 'goodbye': 'adiós', 'thank you': 'gracias'},
   'french': {'hello': 'bonjour', 'goodbye': 'au revoir', 'thank you': 'merci'},
   'italian': {'hello': 'ciao', 'goodbye': 'arrivederci', 'thank you': 'grazie'}
  }

  def translate_word(word):
   if word.lower() in translations[language]:
     return translations[language][word.lower()]
   else:
     return "Translation not avaible"  
  
  return translate_word

spain = translator('spanish')
print(spain('hello'))

#5
from functools import reduce
playlist = [('What Was I Made For?', 3.42), ('Just Like That', 5.05), ('Song 3', 6.55), ('Leave The Door Open', 4.02), ('I Can\'t Breath', 4.47), ('Bad Guy', 3.14)]

def longer_than_five_min(song):
  return song[1] > 5.00

def minutes_to_sec(song):
  duration = song[1]
  minutes = int(duration)
  second = (duration - minutes) * 100

  return minutes * 60 + round(second)

def total_duration(total, song):
  duration = song[1]
  return total + duration

filtered_songs = list(filter(longer_than_five_min, playlist))
converted_songs = list(map(minutes_to_sec, playlist))
total_duration = reduce(total_duration, playlist, 0)

print(filtered_songs)
print(converted_songs)
print(total_duration)

#6
numbers = [57, 10, 82, 36, 89, 46, 13, 23, 92, 48]

even_number = [num for num in numbers if num % 2 == 0]
odd_number = [num for num in numbers if num % 2 != 0]

print("Original Numbers: ", numbers)
print("Even Numbers: ", even_number)
print("Odd Numbers: ", odd_number)

#7
import random
from functools import reduce

prefixes = ['Mystic', 'Golden', 'Dark', 'Shadow', 'Silver']
suffixes = ['storm', 'song', 'fire', 'blade', 'whisper']

def capitalize_suffix(name):
  return name.capitalize()

c_suffixes = list(map(capitalize_suffix, suffixes))  

def create_username(list_1, list_2):
  return random.choice(list_1) + " " + random.choice(list_2)

random_list = [
  create_username(prefixes, c_suffixes)
  for name in range(10)
]

def fire(name):
  return "Fire" in name

filtered_name = list(filter(fire, random_list))  

def con(acc, name):
  return acc + ", " + name

reduced_name = reduce(con, filtered_name)

def display():
  for name in random_list:
    print("Fantasy name: ", name)

  print("Name with Fire: ", filtered_name)  
  print('Concatenated names:', reduced_name) 

display()

#8
import unittest

def add(a, b):
  return a + b

class TestAddition(unittest.TestCase):
  # Define the first unit test
  def test_add(self):
    result = add(3, 4)

    # Define the expected result
    expected_result = 7
    self.assertEqual(result, expected_result)

if __name__ == '__main__':
  unittest.main()

#9
def reverse_string(s):
 return s[::-1]

def capitalize_string(s):
 return s.capitalize()

def is_capitalized(s):
 return s[0].isupper()