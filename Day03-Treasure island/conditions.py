print("Welcome to the rollcoaster")
height=int(input("What is your height in cm: "))
bill=0
if height>=120:
    print("You can take a ride")
    age=int(input("What is your age?"))
    if age<=12:
        bill=5
        print("Child pay Rs.10")
    elif age<=18:
        bill=7
        print("Youth pay Rs.20")
    else:
        bill=10
        print("Adult pay Rs.30")
    wants_photo=input("Do you want a photo?Type y or n")
    if wants_photo=="y":
        bill+=3
        print(f"Yor final bill is:{bill}")   
else:
    print("Sorry you cannot take a ride")