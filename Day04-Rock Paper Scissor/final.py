import random

# ASCII Art for rock, paper, scissors
rock = '''
                
| | | |/\       
|_|_|_|\ \       
|        /
|_______/           
 |______|     
      
      '''

paper = '''
               
  __..----- ._ 
              "-..__
            '"--..__";
 ___        '--...__"";
    `-..__ '"---..._;"
          """"----'    
      
      '''

scissors = '''
  
       _    (^)
      (_\   |_|
       \|_\  |_|
       |_\,/_||
      (`|(_|`||
     (`/,)  \ |
      \,)   | |  
        \__(__|
       
         '''

game_images=[rock,paper,scissors]

user_choice=int(input("What do you choose?Type 0 for rock,1 for paper,2 for scissors\n"))
print(game_images[user_choice])

computer_choice=random.randint(0,2)
print("Computer choice is: ")
print(game_images[computer_choice])
if user_choice>=3 or user_choice<0:
    print("You have entered a invalid number.You lose")
elif user_choice==0 and computer_choice==2:
    print("You win!")
elif user_choice==0 and user_choice==2:
    print("You lose")
elif computer_choice>user_choice:
    print("You lose!")
elif user_choice>computer_choice:
    print("You win!")
elif computer_choice==user_choice:
    print("It's a draw")

