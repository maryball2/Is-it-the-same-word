'''
Title: How many songs
Author: Riley Carpenter
Borrowed Code: Myself with the clear screen code
'''
import os
import sys

#Set variables for later
note = ""
totalwords = 0
totalnotwords = 0
total = 0

#Create clear screen code
if sys.platform == "linux" or sys.platform == "posix":
    clearorcls = "clear"
else:
    clearorcls = "cls"
os.system(clearorcls)

#Main Loop
while note != "Done":
    os.system(clearorcls) #This is where I count
    note = input("Is it the same word? ")
    if note == "Y" or note == "y":
        totalwords += 1
    elif note == "N" or note == "n":
        totalnotwords += 1
    total += 1
else: #What runs to display the final result
    os.system(clearorcls)
    print("The amount that is the same is",totalwords)
    print("The amount that is not that is",totalnotwords)
    print("Therefore the percentage amount is",str(((totalwords / total)) * 100) + "%")
