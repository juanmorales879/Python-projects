

total = 0
discount = 0
yogurt_count = 0
ice_cream_count = 0
yogurt_total = 0
ice_cream_total = 0
sm_yogurt_cone = 3.09
med_yogurt_cone = 0.80
large_yogurt_cone = 1.60
sm_ice_cone = 3.49
med_ice_cone = 1.00
large_ice_cone = 2.00

while True:
    firstchoice = input("Frozen yogurt or ice cream? (F:frozen yogurt, I:ice cream)").upper()
    if firstchoice == "F":
        total += sm_yogurt_cone
        yogurt_count += 1
        yogurt_total+=sm_yogurt_cone
    elif firstchoice == "I":
        total += sm_ice_cone
        ice_cream_count+=1
        ice_cream_total+=sm_ice_cone
    secondchoice = input("What size? (S:small , M:medium, L:large) ").upper()
    if secondchoice == "M" and firstchoice=="F":
            total += med_yogurt_cone
            yogurt_total+= med_yogurt_cone
    elif secondchoice == "M" and firstchoice=="I":
        total += med_ice_cone
        ice_cream_total+=med_ice_cone
    elif secondchoice =="L" and firstchoice=="F":
        total += large_yogurt_cone
        yogurt_total+=large_yogurt_cone
    elif secondchoice=="L" and firstchoice == "I":
        total += large_ice_cone
        ice_cream_total+= large_ice_cone
    thirdchoice = eval(input("What kind of container (1:Cone, 2:Cup) "))
    if thirdchoice == 2 and firstchoice =="F":
        total= total + 0.10
        yogurt_total = yogurt_total+ 0.10
    elif thirdchoice == 2 and firstchoice=="I":
        total = total+0.10
        ice_cream_total = ice_cream_total+ 0.10
    fourthchoice = input("Would you like to add any toppings: ").upper()
    if fourthchoice == "Y":
        fifthchoice = input("What kind of topping G:gummies, N:nuts ").upper()
        if fifthchoice == "N":
            total = total + 1.89
        elif fifthchoice == "G":
            total = total + 1.59
    sixchoice = input("Would you like to add a cookie: ").upper()
    if sixchoice == "Y" :
        sevenchoice = input("What kind of cookie R:raisin, C:chocolate: ").upper()
        if sevenchoice == "R":
            total = total + 1.49
        elif sevenchoice == "c":
            total = total + 1.59
        eightchoice = input("What size of cookie would you like R: regular, L: large: ").upper()
        if eightchoice == "L":
            total = total + 1
    ninechoice = input("What day of the week is it, M:Monday, T:Tuesday, W:Wednesday , TH:Thursday, F:Friday, SA:Saturday, SU:Sunday) :").upper()
    if ninechoice == "F" or ninechoice == "SA" or ninechoice=="SU":
        discount = total * 0.1
        total = total - discount
    print("Your order total is ", "$%0.2f" %total)
    tenchoice = input("Enter C to continue or Q to quit ").upper()
    if tenchoice == "Q":
        break
print()

for i in range (1, 4 , +1):
    print(i * "*")

print("===========" , "Today's Sales Report", "================")

for i in range(3, 0, -1):
	print(i * "*")

print()

yogurt_average = yogurt_total/yogurt_count
ice_cream_average = ice_cream_total/ice_cream_count
total_items = yogurt_count+ice_cream_count
total_average = total/total_items

print("Item","        ","#Orders"," ","Order Total"," ","Average/Order")
print("Frozen Yogurt","  ",yogurt_count,"        ","$%0.2f" %yogurt_total,"      ", "$%0.2f" %yogurt_average)
print("Ice Cream","      ",ice_cream_count,"        ","$%0.2f" %ice_cream_total,"      ", "$%0.2f" %ice_cream_average)
print("Grand Total","    ",total_items,"        ","$%0.2f" %total,"      ", "$%0.2f" %total_average)













