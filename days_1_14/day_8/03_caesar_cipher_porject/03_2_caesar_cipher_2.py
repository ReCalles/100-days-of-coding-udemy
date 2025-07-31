alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# def encypt(original_text, shift_amount):
#     encrypted_text = ""
#     for letter in original_text:                                    # For loop to loop through each of the letters in the plain_text.
#         shifted_position = alphabet.index(letter) + shift_amount    # Find the position of each letter in the alphabet List and add shift_amount
#         # print(shifted_position)                                   # TEST
#         shifted_position %= len(alphabet)                           # shift z forwards by 9 --> 25+9 = 34, 34%25 = 9, make sure we are always within 0-25
        
#         # Another Solution to the Z issue.
#         # if shifted_position >= len(alphabet):
#         #     shifted_position -= len(alphabet)
#         #     ## print(shifted_position)                            # TEST
#         #     encrypted_text += alphabet[shifted_position]
#         # else:
#         #     encrypted_text += alphabet[shifted_position]
        
#         encrypted_text += alphabet[shifted_position]
            
#     print(f"Here is the encoded result: {encrypted_text}")


# # TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.
# # TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
# #  by the shift amount and print the decrypted text.


# def decrypt(original_text, shift_amount):
#     decrypted_text = ""
#     for letter in original_text:
#         shifted_position = alphabet.index(letter) - shift_amount
#         # print(shifted_position)                                     # TEST
#         shifted_position %= len(alphabet)
#         decrypted_text += alphabet[shifted_position]
#     print(f"Here is the decoded result: {decrypted_text}")


# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.


def caesar(encode_or_decode, original_text, shift_amount):
    output_text = ""
    
    for letter in original_text:
        
        if encode_or_decode == "decode":                              # this will only occur when we decode, so that is why we multiply by -1.
            shift_amount *= -1
        
        shifted_position = alphabet.index(letter) + shift_amount
        # print(shifted_position)                                     # test
        shifted_position %= len(alphabet)
        output_text += alphabet[shifted_position]
    print(f"here is the {encode_or_decode}d result: {output_text}")
    
    
   
caesar(encode_or_decode=direction, original_text=text, shift_amount=shift)
# encypt(original_text=text, shift_amount=shift)
# decrypt(original_text=text, shift_amount=shift)