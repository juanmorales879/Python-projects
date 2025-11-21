
import random

loop = 1

while loop == 1:

    def menu ():
        print("1. Load Questions")
        print("2. Add Questions")
        print("3. Show Questions")
        print("4. Delete Questions")
        print("5. Play Game")
        print("6. Show Leaders")
        print("7. Quit")
        selection = int(input("Please select an option from the menu "))
        if selection == 1:
            load()
        elif selection == 2:
            add()
        elif selection == 3:
            show()
        elif selection == 4:
            delete()
        elif selection == 5:
            play()
        elif selection == 6:
            leaders()
        elif selection == 7:
            exit()  #end game

    def load():

        print("<<< Questions loaded >>>")
        with open('quest_load.txt') as f:
            for line in f:

                id = line.index("|")
                str = line[:id] #print only the questions to the user dont show answer
                str = str.strip()

                print(str)


    def add():

        with open('quest_load.txt', 'a') as f1: #append to file
            question = input("Enter the question ")
            answer = input("Enter the answer ")
            points = input("Enter the points ")
            result = question + '|' + answer + '|' + points #concatenate to format
            f1.write(result)


    def show():
        print("Question                              |    Answer    |Points")
        with open('quest_load.txt') as f:
            for line in f:
                line = line.strip().split("|")
                print(line[0], " " * 5, line[1],line[2]) #print question,answer,points in table format


    def delete():

        with open('quest_load.txt', 'r') as f1:
            count=0
            lines=f1.readlines()
            for line in lines:
                line=line.strip()
                count += 1
                print(str(count) + "-" + line)  #enumerate each question

        with open('quest_load.txt','w') as f2:
            erase = int(input("Select question to delete: "))
            for i in range(len(lines)): #get length of lines
                if i+1 != erase:  #if input = length of line do not write back
                    f2.write(lines[i]) #else write the question


    def play():

        with open('quest_load.txt', 'r') as l:
            l = l.read(1)
            if not l:
                print("Please add questions") #check for empty questions file
            else:
                print("Are you ready to play?")

                name = input("What is your name friend? ")
                leader = {}
                with open('leaders.txt', 'r') as f1:
                    for i in f1.readlines():
                        k,v = i.strip().split("|")
                        leader[k] = v
                    for k in leader:
                        if k == name: #check if player exits in board
                            print("Welcome back", name, "your previous score was", leader[k])

                print("Choose up to 7 questions", name)

                with open('quest_load.txt', 'r') as file:

                    dict = {}
                    for line in file:
                        key, val, points = line.strip().split("|",2)
                        dict[key] = val, points

                    total = 0
                    correct = 0
                    num = int(input("Enter number of questions you want "))
                    r = random.sample(list(dict), num)
                    for key in r:
                        inp = input(key)
                        if inp == dict[key][0]: #check if input = value of answer
                            print("Nailed it!")
                            z = int(dict[key][1])
                            total = total + z #keep total of score
                            correct +=1 #count # of correct answers
                        else:
                            print("Incorrect response")
                    print("You got", correct, "out of", num, "correct")
                    print("Your score based on question dificulty is", total)


                if name in leader.keys():
                    leader[name] = int(leader[name]) + total #if name in leader add new score to old score
                else:
                    leader[name]=total #else write the name and current score

                with open('leaders.txt', 'w') as f2:
                    for k, v in leader.items():
                        f2.write(k + "|" + str(v) + '\n')


    def leaders():
        print("<<<Leader Board>>>")
        dict = {}
        with open('leaders.txt') as f:
            for line in f:
                k,v = line.strip().split("|")
                dict[k] = v
            for k,v in sorted(dict.items(), key=lambda k: k[1],reverse=True): #print key value in descending order
                print(k + "  " * (10-len(k)) + str(v)) #determine length to print as a table

    menu()
