#pip install PyDictionary
from PyDictionary import PyDictionary
dict = PyDictionary()

#To take input from user 
word = input("Enter the word:")

#To store the meaning 
meaning = dict.meaning(word)

#printing the meaning
print(meaning)