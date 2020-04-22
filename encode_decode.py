################################################################
import random
import string

def add_letters(s, n):
    string_out = ''

    for i in s:
        rand_chars =  ''
        for x in range(n):
            rand_chars += random.choice(string.ascii_letters)
        string_out += i
        string_out += rand_chars

    return string_out

def remove_letters(s, n):
    string_out = ''
    length = len(s)
    for i in range(0, length, n+1):
        string_out += s[i]
    return string_out

def shift_down(char, n):
    minimum = 0
    maximum = 0
    curr_ascii = ord(char) # Convert char to ascii digit
    curr_ascii -= 1
    return chr(curr_ascii)

def shift_up(char, n):
    minimum = 0
    maximum = 0
    curr_ascii = ord(char) # Convert char to ascii digit
    curr_ascii += 1  
    return chr(curr_ascii)

def shift_characters(s, n):
    string_out = ''
    
    if n > 0:
        for i in s:
            string_out += shift_up(i, n)
    elif n < 0:
        n = abs(n) # Shift down doesnt work with negatives
        for x in s:
            string_out += shift_down(x, n)

    return string_out

def main():
    user_in = ''
    while user_in != 'q':
        user_in = input('(e)ncode, (d)ecode or (q)uit: ')
        if user_in == 'e':
            #ENCODE
            num = int(input('Enter a number between 1 and 5: '))
            while num < 1 or num > 5:
                print('Invalid input! Try agian.')
                num = input('Enter a number between 1 and 5: ')
            phrase = input('Enter phrase to encode: ')
            rand_added = add_letters(phrase, num)
            shifted = shift_characters(rand_added, num)
            print('Your encoded word is: {}\n'.format(shifted))
        elif user_in == 'd':
            #DECODE
            num = int(input('Enter a number between 1 and 5: '))
            while num < 1 or num > 5:
                print('Invalid input! Try agian.')
                num = input('Enter a number between 1 and 5: ')
            phrase = input('Enter phrase to decode: ')
            removed = remove_letters(phrase, num)
            num = num - (num * 2) # Make num negative
            shifted = shift_characters(removed, num)
            print('Your decoded word is: {}\n'.format(shifted))
        elif user_in == 'q':
            break
        else: # Wrong letter entered
            print('Invalid input! Try again.')

main()
###############################################################################