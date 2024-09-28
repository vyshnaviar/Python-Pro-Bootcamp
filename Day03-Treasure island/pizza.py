print("Welcome to Python pizza Deliveries")
size=input("What size pizza they eant? S,M or L: ")
pepperoni=input("Do you want peppironi on your pizza?  y or n?")
extra_cheese=input("Do you want extra cheese?y or n?")
bill=0
#todo based on size
if size=="S":
    bill+=15
   
elif size=="M":
    bill+=20
    
elif size=="L":
    bill+=30
else:
    print("You have typed the wrong inputs")
#todo  based on pepproni
if pepperoni=="y":
    if size=="S":
        bill+=5
    else:
        bill+=7
#todo finam amt extra cheese
if extra_cheese=="y":
    bill+=3

print(f"Your final bill is: {bill}.")

