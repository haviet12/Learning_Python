alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
             'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']*2

# create function caesar (text, shift, direction)
def caesar(text, shift, direction):
    messange=''
    list_letter=list(text)
    for i in range(0,len(list_letter)):

        if list_letter[i]==' ':
            messange += ' '
        
        else:
            if direction=='encode':
                new_position = alphabet.index(list_letter[i]) + shift       
                list_letter[i] = alphabet[new_position]
            elif direction=='decode':
                new_position = alphabet.index(list_letter[i]) - shift       
                list_letter[i] = alphabet[new_position]
    for letter in list_letter:
        messange += letter
    print(f'the decode text is:{messange}')


import art_caesar_cipher
while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    