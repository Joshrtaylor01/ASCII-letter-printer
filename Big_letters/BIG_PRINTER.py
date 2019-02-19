import letters

print_again = 'y'
chars = letters.OUTPUT('', '', '', '', '', '')

in_string = str(input("put ya words in"))

for i in range(0, len(in_string)):
    chars.ASCII = ord(in_string[i])
    if chars.ASCII >= 97:
        chars.ASCII -= 32
    chars.add_letter(chars.ASCII)

print(chars.print_letters())


#while print_again: