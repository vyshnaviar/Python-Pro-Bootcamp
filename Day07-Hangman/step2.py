import random
word_list=["aardvark","baboon","camel"]
choosen_word=random.choice(word_list)
print(choosen_word)
placeholder=""
for position in range(1,6):
    placeholder += "_"
print(placeholder)
guess=input("Guess a letter:").lower()
display=""
for letter in choosen_word:
    if letter==guess:
        display += letter
    else:
        display += "_"
print(display)
