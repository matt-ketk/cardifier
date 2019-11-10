# Cardifier - Main Method
import requests
import json

import OxfordAPI
import VocabularyCard

# Variables
wordList = []
wordSet = set()
incorrectWordList = []

inputWord = ""
# Functions

# Main
"""
print('Welcome to Cardifier! Please type in your login:')
user = input("User: ")
pass = input("Pass: ")

print("Login Successful.")
"""

print("Enter vocabulary words that you would like to make cards for.")
print("(Type in \'q0\' to stop):")
while (len(wordList) <= 60 and (inputWord != 'q0')):
    inputWord = input()
    if (inputWord != 'q0' or (inputWord.strip() != '')):
        wordList.append(inputWord)
    if (len(wordList) >= 60):
        print("Word limit of 60 has been reached.")
    if (len(wordList) <= 0 and (inputWord == 'q0')):
wordSet = set(wordList)
wordList = []
while (len(wordSet) > 0):
    wordList.append(wordSet.pop())

print()
print("Applying Lemmatron check...")
# print(OxfordAPI.lemmatronCheck(wordList[0]).text)
