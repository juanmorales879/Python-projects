
# ask the player to enter the name of the madlib file

print("Welcome to MadLibs")

#ask the user to enter new responses or use the most recent ones

fname = input("Enter the file name: ").lower()
madlibs = open(fname, 'r')
response = input("Enter new answers? y/n ").lower()
text = madlibs.readlines()

#print current or new responses
if response == "n":
    x = open('madlibs_merge.txt','r')
    for line in x:
        print(line)
else:
    count = 0
    story = ""
    newcount = 0
    secondletter = ""
    with open('madlibs_response.txt', 'w') as f:  #open madlibs response text file
        for line in text:
            if newcount == 0:
                secondletter = line[1]  #get second character of the title
            newcount+=1
            newline=""
            for word in line.split():
                if "[" in word:
                    word = word.replace("_", " ")  #replace underscore with space
                    user_input = input("Enter a " + word[1:word.index("]")] + " ")  #find the end of bracket word
                    if secondletter in user_input:
                        newline = newline + user_input[::-1] + " " #reverse string
                    else:
                        newline = newline + user_input + " "
                    f.write(user_input + '\n') #write to response file
                    count += 1 #count number of responses
                else:
                    newline = newline + word + " "
            story= story+newline+'\n' #if end of line write new line
        f.write(str(count) + " " + "responses")
        print(str(count) + " " + "responses added to madlibs_merge.txt")
        print(story)

    with open('madlibs_merge.txt', 'w') as f2:
        f2.write(story)
