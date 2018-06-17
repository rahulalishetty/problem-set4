import random
from ps4a import *
#
# Problem #5: Playing a game
# 


#
#
# Computer chooses a word
#
#
def compChooseWord(hand, wordList, n):
	"""
	Given a hand and a wordList, find the word that gives 
	the maximum value score, and return it.

	This word should be calculated by considering all the words
	in the wordList.

	If no words in the wordList can be made from the hand, return None.

	hand: dictionary (string -> int)
	wordList: list (string)
	n: integer (HAND_SIZE; i.e., hand size required for additional points)

	returns: string or None
	"""
	# Create a new variable to store the maximum score seen so far (initially 0)
	max=0
	max_w=''
	for word in wordList:
		if isValidWord(word, hand, wordList):
			c=getWordScore(word, HAND_SIZE)
			if c>max:
				max=c
				max_w=word
	if max==0: 
		return '.'
	else:
		return max_w

#
# Computer plays a hand
#
def compPlayHand(hand, wordList, n):
	"""
	Allows the computer to play the given hand, following the same procedure
	as playHand, except instead of the user choosing a word, the computer 
	chooses it.

	1) The hand is displayed.
	2) The computer chooses a word.
	3) After every valid word: the word and the score for that word is 
	displayed, the remaining letters in the hand are displayed, and the 
	computer chooses another word.
	4)  The sum of the word scores is displayed when the hand finishes.
	5)  The hand finishes when the computer has exhausted its possible
	choices (i.e. compChooseWord returns None).
 
	hand: dictionary (string -> int)
	wordList: list (string)
	n: integer (HAND_SIZE; i.e., hand size required for additional points)
	"""
	# Keep track of the total score
	total_score=0
	print('initial score:',total_score)
	while calculateHandlen(hand)>0: 
		# Display the hand
		displayHand(hand)
		# Ask user for input
		input1=compChooseWord(hand, wordList, HAND_SIZE)
		print("choose input:", input1)
		# If the input is a single period:
		if input1=='.':
			# End the game (break out of the loop)
			break
		# Otherwise (the input is not a single period):
		else:
			# If the word is not valid:
			if not isValidWord(input1, hand, wordList):
				# Reject invalid word (print a message followed by a blank line)
				print("not valid input")
			# Otherwise (the word is valid):
			else:
				# Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
				sc=getWordScore(input1, n)
				print(sc)
				total_score+=sc
				print("points earned:", sc, "total_score:",total_score)
				# Update the hand 
				hand=updateHand(hand, input1)
				

	# Game is over (user entered a '.' or ran out of letters), so tell user the total score
	print("your total score:", total_score)
#
# Problem #6: Playing a game
#
#
def playGame(wordList):

	"""
	Allow the user to play an arbitrary number of hands.
 
	1) Asks the user to input 'n' or 'r' or 'e'.
		* If the user inputs 'e', immediately exit the game.
		* If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

	2) Asks the user to input a 'u' or a 'c'.
		* If the user inputs anything that's not 'c' or 'u', keep asking them again.

	3) Switch functionality based on the above choices:
		* If the user inputted 'n', play a new (random) hand.
		* Else, if the user inputted 'r', play the last hand again.
	  
		* If the user inputted 'u', let the user play the game
		  with the selected hand, using playHand.
		* If the user inputted 'c', let the computer play the 
		  game with the selected hand, using compPlayHand.

	4) After the computer or user has played the hand, repeat from step 1

	wordList: list (string)
	"""
	# TO DO... <-- Remove this comment when you code this function
	#print("playGame not yet implemented.") # <-- Remove this when you code this function
	hand=dealHand(HAND_SIZE)
	c=0
	flag=True
	while flag:
		inp=input("input 'n' or 'r' or 'e'")
		if inp=='e':
			break
		choice=input("input a 'u' or a 'c'")
		if choice=='u':
			if inp=='n':
				hand=dealHand(HAND_SIZE)
				playHand(hand, wordList, HAND_SIZE)
				c+=1
			elif inp=='r':
				if c!=0:
					playHand(hand, wordList, HAND_SIZE)
				else:
					print("play a game first and then replay")
			else:
				print("enter valid input")
		elif choice=='c':
			if inp=='r':
				if c!=0:
					compPlayHand(hand, wordList, HAND_SIZE)
				else:
					print("play a game first and then replay")
			elif inp=='n':
				c+=1
				compPlayHand(dealHand(HAND_SIZE), wordList, HAND_SIZE)
			else:
				print("enter valid input")
		else:
			print("enter valid choice")

			
		
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
	wordList = loadWords()
	playGame(wordList)


