
TEN_DOLLAR_BILL = 10
FIVE_DOLLAR_BILL = 5
TWO_DOLLAR_BILL = 2
ONE_DOLLAR_BILL = 1
QUARTER = 0.25
DIME = 0.10
NICKEL = 0.05
PENNY = 0.01


cost = float(input("What is the amount of the purchase $ "))
cashTendered = float(input("What is the amount of cash tendered $ "))
changeBack = float(cashTendered - cost)

amountOfTen = int(changeBack/TEN_DOLLAR_BILL)
amountLeft= float(changeBack%TEN_DOLLAR_BILL)

amountOffive= int(amountLeft/FIVE_DOLLAR_BILL)
fiveLeft = float(amountLeft%FIVE_DOLLAR_BILL)

amountOfOnes = int(fiveLeft/ONE_DOLLAR_BILL)
oneLeft = float(fiveLeft%ONE_DOLLAR_BILL)

amountOfquaters = int(oneLeft/QUARTER)
quarterLeft = float(oneLeft%QUARTER)

amountOfdime = int(quarterLeft/DIME)
dimeLeft = float(quarterLeft%DIME)

amountOfnickel = int(dimeLeft/NICKEL)
nickelLeft = float(dimeLeft%NICKEL)

amountOfpenny = int(nickelLeft/PENNY)
pennyLeft = float(nickelLeft%PENNY)

numTen = float(amountOfTen*TEN_DOLLAR_BILL)
numFive = float(amountOffive*FIVE_DOLLAR_BILL)
numOnes= float(amountOfOnes*ONE_DOLLAR_BILL)
numQuarters= float(amountOfquaters*QUARTER)
numDimes= float(amountOfdime*DIME)
numNickels = float(amountOfnickel*NICKEL)
numPennies = float(amountOfpenny*PENNY)

print("------------Receipt--------------")
print(amountOfTen, "Tens       $%0.2f" %numTen)
print(amountOffive, "Fives      $%0.2f" % numFive)
print(amountOfOnes, "Ones       $%0.2f" %numOnes)
print(amountOfquaters,"Quarters   $%0.2f" % numQuarters )
print(amountOfdime, "Dimes      $%0.2f" %numDimes)
print(amountOfnickel, "Nickels    $%0.2f" %numNickels)
print(amountOfpenny, "Pennies    $%0.2f"% numPennies)
total = numTen+numFive+numOnes+numQuarters+numDimes+numNickels+numPennies

print("Total change: $%0.2f" %total)
print("---------------------------------")

print("Total Bills: " , amountOfTen+amountOfOnes+amountOffive)
print("Total coins: ", amountOfpenny+amountOfnickel+amountOfquaters+amountOfdime)

