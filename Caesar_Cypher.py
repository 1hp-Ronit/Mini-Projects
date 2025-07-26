ascii_art = '''
   ██████╗ █████╗ ███████╗███████╗ █████╗ ██████╗ 
  ██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗██╔══██╗
  ██║     ███████║█████╗  ███████╗███████║██████╔╝
  ██║     ██╔══██║██╔══╝  ╚════██║██╔══██║██╔══██╗
  ╚██████╗██║  ██║███████╗███████║██║  ██║██║  ██║
   ╚═════╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝

   ██████╗██╗██████╗ ██╗  ██╗███████╗██████╗      
  ██╔════╝██║██╔══██╗██║  ██║██╔════╝██╔══██╗     
  ██║     ██║██████╔╝███████║█████╗  ██████╔╝     
  ██║     ██║██╔═══╝ ██╔══██║██╔══╝  ██╔══██╗     
  ╚██████╗██║██║     ██║  ██║███████╗██║  ██║     
   ╚═════╝╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝

'''
print(ascii_art)

letters = [chr(i) for i in range(97, 123)]  # ascii values of small alphabets to chr


def caesar(text_input, shift_input, encode_or_decode):
    if encode_or_decode == 'decode':
        shift_input *= -1
    output_text = ''
    for elem in text_input:
        if elem.isalpha():
            output_text += letters[(letters.index(elem) + shift_input) % 26]
        else:
            output_text += elem
    print(f"Here is the {encode_or_decode} result: {output_text}")


choice = True
while choice:
    text = input("Enter the text you'd like to encrypt or decrypt:\n").lower()
    shift = int(input("Enter the shift number:\n"))
    direction = input("Type \'encode\' to encrypt or \'decode\' to decrypt\n").lower()
    caesar(text_input=text, shift_input=shift, encode_or_decode=direction)
    temp_choice = input("Would you like to go again \"yes\" or \"no\"")
    if temp_choice.lower() == 'yes':
        choice = True
    elif temp_choice.lower() == 'no':
        choice = False
