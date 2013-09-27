
#import repeat function to create initial blank list
from itertools import *

#get file from user
#text_file = raw_input("Type your filename: ")

#open and read the file
f = open("twain.txt")
file_text = f.read()

#create initial empty letter_result list
letter_result = list(repeat(0,26))
  #print len(letter_result)
  #print letter_result

#converting all characters to lowercase
#limit count to just lowercase alphabet
#for each letter, add 1 to count
for char in file_text:
    char = char.lower()
    ordinal = ord(char)
    if ordinal in range(97,123):
        letter_result[ordinal-97] += 1
  
#code for testing: 
#print letter_result

#return list of letter_results
for number in letter_result:
    print number 
f.close()