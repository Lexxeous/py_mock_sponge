#!/usr/bin/env python
#coding: utf-8

#-------------------------------------------------- IMPORTING MODULES ------------------------------------------------#

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import random
import os
import signal


#---------------------------------------------- DEFINE HELPER FUNCTIONS ----------------------------------------------#

def rand_upper(arr, i, perc):
	mod_word = ""

	for char in arr[i]:
		if(cap_perc(perc)): mod_word += char.upper()
		else: mod_word += char

	arr[i] = mod_word
	# add original or upper character to working mod_word


def cap_perc(p):
	upper_bound = 1000000
	rand_num = random.randint(1, upper_bound)
	if(rand_num <= upper_bound*p): return True
	else: return False


def fifty_perc():
	rand_num = random.randint(1, 1000000)
	if(rand_num <= 500000): return True
	else: return False

def cap_second_letter(arr, idx):
	first_letter = arr[idx][0]
	second_letter = arr[idx][1]
	arr[idx] = first_letter + second_letter.upper()

def cap_one_letter(arr, idx):
	first_letter = arr[idx][0]
	second_letter = arr[idx][1]
	third_letter = arr[idx][2]
	rand_num = random.randint(0, 2)
	if(rand_num == 0):
		arr[idx] = first_letter.upper() + second_letter + third_letter
	elif(rand_num == 1):
		arr[idx] = first_letter + second_letter.upper() + third_letter
	elif(rand_num == 2):
		arr[idx] = first_letter + second_letter + third_letter.upper()

def cap_two_letters(arr, idx):
	first_letter = arr[idx][0]
	second_letter = arr[idx][1]
	third_letter = arr[idx][2]

	# generate 2 random numbers between 0 and 2 inclusive
	rand_num_1 = random.randint(0, 2)
	rand_num_2 = random.randint(0, 2)

	# make sure that the 2 values are unique
	if((rand_num_1 == rand_num_2) and rand_num_1 == 0):
		rand_num_2 += 1
	elif((rand_num_1 == rand_num_2) and rand_num_1 == 1):
		if(fifty_perc()): rand_num_2 += 1
		else: rand_num_2 -= 1
	elif((rand_num_1 == rand_num_2) and rand_num_1 == 2):
		rand_num_2 -= 1

	if(rand_num_1 == 0 or rand_num_2 == 0):
		first_letter = first_letter.upper()
	if(rand_num_1 == 1 or rand_num_2 == 1):
		second_letter = second_letter.upper()
	if(rand_num_1 == 2 or rand_num_2 == 2):
		third_letter = third_letter.upper()

	arr[idx] = first_letter + second_letter + third_letter

#-------------------------------------------------- GLOBAL VARIABLES -------------------------------------------------#

W, H = (502, 353) # tuple for exact size of the input image
white = (255,255,255)
black = (0,0,0)
spacing = 8
percentile = .45

#-------------------------------------------------------- MAIN -------------------------------------------------------#

msg = raw_input("Enter a phrase to mockify:\n").lower() # custom message to display
words = msg.split()

for i in range(len(words)):
	if(len(words[i]) == 1):
		if(fifty_perc()): words[i] = words[i].upper() # capitalize with 50% probability
	elif(len(words[i]) == 2):
		if(cap_perc(.70)): cap_second_letter(words, i) # capitalize second letter of <word>
		else: words[i] = words[i].capitalize() # capitalize first letter of <word>
	elif(len(words[i]) == 3):
		if(fifty_perc()): cap_one_letter(words, i) # only capitilize one letter
		else: cap_two_letters(words, i) # capitalize 2 letters
	elif(len(words[i]) >= 4):
		rand_upper(words, i, percentile) # capitalize based on <cap_perc>

mocked_msg = ' '.join(words)
file_path = os.path.dirname(os.path.abspath(__file__))
print file_path

# Image setup
img = Image.open(file_path + "/mock_sponge.jpg") # open the original image
draw = ImageDraw.Draw(img) # draw the original image
font = ImageFont.truetype("Forgottb.ttf", 40) # define the font object
w, h = draw.textsize(mocked_msg, font=font) # get the width and height of <msg>

# Define pre-formatted anchors
center_x = (W-w)/2
top_y = 8
bottom_y = (H-h)*.95

# Print final text on image
draw.text((center_x, bottom_y), mocked_msg, white, font=font, spacing=spacing)
img.save(file_path + "/../sponge_out.jpg")


