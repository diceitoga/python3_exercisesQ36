#Reading in text 
#Exercise 30: https://www.practicepython.org/exercise/2016/09/24/30-pick-word.html
'''
This exercise is Part 1 of 3 of the Hangman exercise series. 
The other exercises are: Part 2 and Part 3.

In this exercise, the task is to write a function that picks a random word from a list of words 
from the SOWPODS dictionary. Download this file and save it 
in the same directory as your Python code. 
This file is Peter Norvig’s compilation of the dictionary of words used in professional Scrabble tournaments. 
Each line in the file contains a single word.

Hint: use the Python random library for picking a random word.

SOWPODS is a word list commonly used in word puzzles and games (like Scrabble for example). 
It is the combination of the Scrabble Player’s Dictionary and the Chamber’s Dictionary.
(The history of SOWPODS is quite interesting, I highly recommend reading the Wikipedia article if you are curious.)
'''

def pick_rand_word():
     with open('word_dictionary.txt', 'r') as open_file:
        all_text = open_file.read()   ##open_file.readlines() runs into timeout.
        print(type(all_text))    ##class 'str'
        split_text = all_text.split(' ')
        print(split_text)
        #text_count = count(all_text)
        #print(all_text)
        #text_count = len(all_text)



pick_rand_word()