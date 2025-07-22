import art

print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
game_over = False

def caesar(encode_decode_or_exit, original_text, shift_amount):
    if encode_decode_or_exit not in ["encode", "decode"]:
        print("You enter the wrong command. Please try again.")
    else:
        output_text = ""
        if encode_decode_or_exit == "decode":                                # This will only occur when we decode, so that is why we multiply by -1.
            shift_amount *= -1
        
        for letter in original_text:
                
            if letter not in alphabet:
                output_text += letter
            else: 
                shifted_position = alphabet.index(letter) + shift_amount
                # print(shifted_position)                                     # test
                shifted_position %= len(alphabet)
                output_text += alphabet[shifted_position]
                
        print(f"here is the {encode_decode_or_exit}d result: {output_text}")
    

while not game_over:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt or type 'exit' to exit:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    caesar(encode_decode_or_exit=direction, original_text=text, shift_amount=shift)
    play_again = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if play_again == "no":
        game_over = True
        print("Goodbye")



