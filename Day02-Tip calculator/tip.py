print("Welcome to the tip calcualtor!")
bill=float(input("What was the total bill? Rs"))
tip=int(input("What percentagetip would you like to  give?10,12 , 15 "))
people=int(input("How many people to split the bill?"))
bill_with_tip=tip/100*bill+bill
print(bill_with_tip)