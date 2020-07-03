import re

txt = "The rain and rain in Spain"

x = re.split(r'\s',txt, 2)
print(x)
mystr = input("Enter a word to replace: ")
mynewstr = input("Enter new word: ")
x = re.sub(' '+mystr+' ',' '+mynewstr+' ',txt, 1)
print(x)