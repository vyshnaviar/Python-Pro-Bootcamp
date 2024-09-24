import random
print('''
       _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       ''')

stages = ['''
    _______
    |/      |
    |      (_)
    |      \\|/
    |       |
    |      / \\
    ---------
    ''', '''
    _______
    |/      |
    |      (_)
    |      \\|/
    |       |
    |      / 
    ---------
    ''', '''
    _______
    |/      |
    |      (_)
    |      \\|/
    |       |
    |      
    ---------
    ''', '''
    _______
    |/      |
    |      (_)
    |      \\|
    |       |
    |      
    ---------
    ''', '''
    _______
    |/      |
    |      (_)
    |       |
    |       |
    |      
    ---------
    ''', '''
    _______
    |/      |
    |      (_)
    |      
    |       
    |      
    ---------
    ''', '''
    _______
    |/      |
    |      
    |      
    |       
    |      
    ---------
    ''']


word_list = ["aardvark", "baboon", "camel"]
lives = 6
choosen_word = random.choice(word_list)
print(choosen_word)  
game_over = False
correct_letters = []


while not game_over:
    guess = input("Guess a letter: ").lower()
    display = ""
    for letter in choosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

   
    if guess not in choosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("You lose!")

    if "_" not in display:
        game_over = True
        print("You win!")

    
    print(stages[lives])
