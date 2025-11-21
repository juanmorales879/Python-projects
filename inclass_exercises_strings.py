"""
Class: CS230--Section 002 
Name: juan jose morales
Description: in class exercises on strings
I pledge that I have completed the programming assignment independently. 
I have not copied the code from a student or any source.
I have not given my code to any student. 
"""


print("Exercise 1")
str = "orange"
print(str[::-1])


print("Exercise 2")
str = input("enter a string: ")
vowels = 0
for i in str:
    if ( i =="a" or i=="e" or i=="i" or i =="o" or i=="u"):
        vowels += 1
print("amount of vowels", vowels)


print("Exercise 3")
s = "Programming in Python"
print(len(s))
print(s.find("in"))
print(s.count("n"))
print(s.count(" "))
print(s[0:-18])
print(s[17:])
print(s[:17])
print(s[5])
print(s.split(" "))
print(s.upper())
print(s.lower())
print(s.replace("in","with"))


print("Exercise 4")
str = input("Enter a string: ")
word = input("Enter word: ")
print(str.count(word))


print("Exercise 5")
str = input("enter a string: ")
lowercase = 0
for i in str:
    if i.islower():
        lowercase+=1
print("Amount of lower case letters" , lowercase)


print("Exercise 6")
str = input("Enter a string: ")
letters = 0
numbers = 0
for i in str:
    if i.isalpha():
        letters+=1
    elif i.isnumeric():
        numbers+=1
print("Number of words", letters, "Count of numbers" , numbers)


print("Exercise 7")
str = input("Enter a string: ")
replace = input("Enter character to replace: ")
newletter = input("Enter character to replace with: ")

print(str.replace(replace,newletter))

listofwords = ['noun', 'season_of_the_year', 'government_official', 'animal_(plural)', 'government_official', 'verb_meaning_create']

listreplace = []

fname = input("Enter the file name: ")

madlibs = open (fname, 'r')

text = madlibs.read()

for word in text.split():
    word = word.replace("_", " ")
    if word in listofwords:
        listreplace.append(word)

madlibs.close()

for word in range(len(listreplace)):
        userInput = input("Enter a" + listreplace[word])
        text = text.replace(listreplace[word], userInput)

result = open("madlibs.txt", 'w')
result.write(text)
result.close()
