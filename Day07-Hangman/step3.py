import random
word_list=["aardvark","baboon","camel"]
choosen_word=random.choice(word_list)
print(choosen_word)
game_over=False
correct_letters=[]
while not game_over:
    guess=input("Guess a letter:").lower()
    display=""
    for letter in choosen_word:
        if letter==guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(display)
    if "_" not in display:
        game_over=True
        print("You win!")
