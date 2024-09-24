import random
word_list=["aardvark","baboon","camel"]
choosen_word=random.choice(word_list)
print(choosen_word)
guess=input("Guess a letter:").lower()
print(guess)
for letter in choosen_word:
    if letter==guess:
        print("Right")
    else:
        print("Wrong")