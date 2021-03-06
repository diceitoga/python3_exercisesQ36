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
import random
import numpy as np
def pick_rand_word():

     with open('word_dictionary.txt', 'r') as open_file:
        all_text = open_file.read()   ##open_file.readlines() runs into timeout.
        #print(type(all_text))    ##class 'str'
        split_text = all_text.split('\n')
        print(split_text)
        print(type(split_text))     # this now gives me a list type so I can do list manipulation. 
        word_count = len(split_text)
        print(f"There are {word_count} words in this text document")
        random_index = random.randint(0, word_count)
        print(random_index)
        print(split_text[random_index])
        word_selected = split_text[random_index]
        return word_selected

#word_bt_computer = pick_rand_word()

'''
This exercise is Part 2 of 3 of the Hangman exercise series. The other exercises are: Part 1 and Part 3.

Let’s continue building Hangman. In the game of Hangman, a clue word is given by the program that the player has to guess, 
letter by letter. The player guesses one letter at a time until the entire word has been guessed. 
(In the actual game, the player can only guess 6 letters incorrectly before losing).

Let’s say the word the player has to guess is “EVAPORATE”. 
For this exercise, write the logic that asks a player to guess a letter and displays letters in the clue word that were guessed correctly. 
For now, let the player guess an infinite number of times until they get the entire word. As a bonus, 
keep track of the letters the player guessed and display a different message if the player tries to guess that letter again. 
Remember to stop the game when all the letters have been guessed correctly! 
Don’t worry about choosing a word randomly or keeping track of the number of guesses the player has remaining - 
we will deal with those in a future exercise.

An example interaction can look like this:

>>> Welcome to Hangman!
_ _ _ _ _ _ _ _ _
>>> Guess your letter: S
Incorrect!
>>> Guess your letter: E
E _ _ _ _ _ _ _ E
...

'''
def guess_loop(letter_guessed, word_bt_computer, error_counter):
	'''
	The letter will be checked to see if it is contained in the word
	if element is in letter_guessed, then you return: 
		1. letter
		2. index in which the letter is contaned in: Keep the actual tracking of the game elsewhere in a sperate function 

		note: word_bt_computer returns fromt the previous exercise as to the dict of words returned in random
	'''
	word_bt_computer = word_bt_computer.lower()
	counter = 0
	word_index = []    ##new code
	correct_incorrect = 'incorrect'
	#for element in word_bt_computer:    
		#if element in letter_guessed:
			#word_index = count
			#letter_found = element
			#count+=1
	#print(f"The letter guessed within the guess loop is: {letter_guessed}")
	#print(f"the word selected randomly by the random function is: {word_bt_computer}")
	if letter_guessed in word_bt_computer:   ##Bad code is here. 
		print(f"The letter guessed within the guess loop: {letter_guessed} is now iniside the if statement as to in the word_bt_computer")
		for element in word_bt_computer:
			if letter_guessed ==element:
				word_index.append(counter)   #new code: This word_index has to be a list as it may return multiple instances of a letter
				letter_found=element   
				correct_incorrect = 'correct'      #new code
				counter+=1                   #new code
			else:
				counter+=1
	else:
		correct_incorrect = 'incorrect'   #Error code
		error_counter+=1
		letter_found = ''
		print("the letter you chose is not in the word")

	return(word_index, letter_found, correct_incorrect, error_counter)

####################################################################################################################################

def swap_underscore_w_num(word_array, current_index, letter):
	'''
	a = geek.insert(arr, 1, 9)   #syntax insert(array_name, index, value)  or use string.replace(old, new, count)
	step 1: delete() the item in the array[which_index] like so: URL: https://www.geeksforgeeks.org/numpy-delete-python/
	step 2: insert(letter_found) into the array[which_index] like so: URL: https://www.geeksforgeeks.org/numpy-insert-python/
	'''
	new_array = np.delete(word_array, current_index)
	new_array = np.insert(new_array, current_index, letter)
	return new_array
####################################################################################################################################
#######################################################  Main loop #################################################################
def main_loop(word_bt_computer,word_array, error_counter):
	while_loop_counter = 0
	letter_found = ''
	which_index = []
	correct_incorrect = ''
	while True: 
		try:
			chosen_letter = input("Guess your letter:")     #I have to break out of this...
			chosen_letter = chosen_letter.lower()
			print(f"you have chosen{chosen_letter}")
			while_loop_counter+=1
			which_index, letter_found, correct_incorrect, error_counter = guess_loop(chosen_letter, word_bt_computer, error_counter)   #this got me in infinite loop 
			#UnboundLocalError: local variable 'letter_found' referenced before assignment
		
			#print(f'Which index is it? : {which_index}')
	
			if correct_incorrect =='incorrect':
				"Incorrect!! Try again:" 
				print(f"you currently have: {word_array}")
				continue 
			else:  #This is where you have to use numpy  
				print("in last else statement where you swap underscore w letter")
				for element in which_index:
					current_index = element
					word_array = swap_underscore_w_num(word_array, current_index, chosen_letter)
				print(f"you currently have: {word_array}")
				break
		except IndexError as e:
			print(e)
	changed_word_array = word_array
	print("Changed word array to be returned is : {}".format(changed_word_array))
	return changed_word_array, error_counter




########################################################### Main  ##############################################################

complete =False   #This varialble sets the condition s.t. if all letters are found ,the game will end.
word_bt_computer = pick_rand_word()   #pics a radom word from the dictionary
word_count = len(word_bt_computer)
guessed_list = np.array([word_count])
error_counter =0


#example 

print ("Welcome to Hangman!")
word_array = np.array(['_']*word_count)
print(word_array)

while complete!=True:
	changed_word_array, error_counter = main_loop(word_bt_computer,word_array, error_counter)
	print("#####################################")
	print("letter now swapped!")
	print("below is the type for the randomly selected word")
	#print(type(word_bt_computer))
	word_array = changed_word_array
	print(f"you currently have: {word_array}")
	word_array = word_array.tolist()
	print("Here is how many times you missed: {}".format(error_counter))
	#print(type(word_array))
	print("#####################################")
	if '_' not in word_array:
		print("You WIN!!")
		complete =True
	else:
		print("Keep going...")
		complete =False
	
print("EndOfGame")










