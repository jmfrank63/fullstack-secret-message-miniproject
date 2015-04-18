import os
from string import ascii_lowercase

sentence = 'This is a secret message for testing.'
letter_dir = './images'
alphabet = ascii_lowercase + ' .'
letter_list = os.listdir(letter_dir)

letter_dict = {}
for letter in zip(alphabet, letter_list):
    letter_dict[letter[0]] = letter[1]

secret_message = []
for letter in sentence:
    secret_message.append(letter_dict[letter.lower()])

print(secret_message)
    
