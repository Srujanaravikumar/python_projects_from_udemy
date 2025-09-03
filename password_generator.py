import string
import random
print("**** WELCOME TO PASSWORD GENERATOR ****")
letters = list(string.ascii_lowercase)
numbers = list(string.digits)
special_characters = list(string.punctuation)
# print(letters)# print(numbers)# print(special_characters)
num_letter = int(input("How many letters do you want? "))
num_number = int(input("How many numbers do you want? "))
num_special_characters = int(input("How many special characters do you want? "))
#generating password
password = ""
for i in range(num_letter):
    password += random.choice(letters)
for i in range(num_number):
    password += random.choice(numbers)
for i in range(num_special_characters):
    password += random.choice(special_characters)
print(password)