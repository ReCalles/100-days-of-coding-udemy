alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.
# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.
# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?

def encypt(original_text, shift_amount):
    encrypted_text = ""
    for letter in original_text:                                    # For loop to loop through each of the letters in the plain_text.
        shifted_position = alphabet.index(letter) + shift_amount    # Find the position of each letter in the alphabet List and add shift_amount
        # print(shifted_position)                                   # TEST
        shifted_position %= len(alphabet)                           # shift z forwards by 9 --> 25+9 = 34, 34%25 = 9, make sure we are always within 0-25
        
        # Another Solution to the Z issue.
        # if shifted_position >= len(alphabet):
        #     shifted_position -= len(alphabet)
        #     ## print(shifted_position)                            # TEST
        #     encrypted_text += alphabet[shifted_position]
        # else:
        #     encrypted_text += alphabet[shifted_position]
        
        encrypted_text += alphabet[shifted_position]
            
    print(f"The encoded text is: {encrypted_text}")




# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.
encypt(original_text=text, shift_amount=shift)