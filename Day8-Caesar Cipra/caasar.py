print('''
                                  _                 
                                   (_)                
  ___ __ _  ___  ___  __ _ _ __ ___ _ _ __  _ __ __ _ 
 / __/ _` |/ _ \/ __|/ _` | '__/ __| | '_ \| '__/ _` |
| (_| (_| |  __/\__ \ (_| | | | (__| | |_) | | | (_| |
 \___\__,_|\___||___/\__,_|_|  \___|_| .__/|_|  \__,_|
                                     | |              
                                     |_|              

      ''')
alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def caesar(original_text,shift_amt,encode_or_decode):
    output_text=""
    if encode_or_decode== "decode":
                shift_amt *= -1
    for letter in original_text:
        if letter not in alphabets:
            output_text += letter
        else:
            
            shifted_position=alphabets.index(letter) + shift_amt
            shifted_position %= len(alphabets)
            output_text += alphabets[shifted_position]

    print(f"Here is the encoded result: {output_text}")
should_continue = True
while should_continue:

    direction=input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text=input("Type your message:\n").lower()
    shift=int(input("Type your shift number:\n"))

    caesar(text,shift,direction)
    restart=input("Type 'yes if you want to go again. Otherwise,type 'no'.\n")
    if restart=="no":
        should_continue=False
        print("Goodbye")
    

