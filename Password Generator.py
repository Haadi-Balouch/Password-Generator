from string import ascii_lowercase,ascii_letters,digits
from random import choice

alpha_num = ascii_letters+digits

def lower_alpha_gen(n):    #Generate lower case word
    mylist = [choice(ascii_lowercase) for _ in range(n)]
    my_str = ''.join(mylist)
    print(my_str)


def alpha_gen(n):   #Generate a random string of alphabets only.
    mylist = [choice(ascii_letters) for _ in range(n)]
    my_str = ''.join(mylist)
    print(my_str)

def alpha_num_gen(n):   #Generate a random string of alphabets and numbers.
    mylist = [choice(alpha_num) for _ in range(n)] 
    my_str = ''.join(mylist) 
    print(my_str)

def main():
# Main code
    while True:
        try:
            level = int(input('''Welcome to Password Generator. Please select difficulty level
 1) Easy
 2) Hard
 3) Hackproof
Please choose among 1, 2, and 3: '''))
            
            if level not in (1, 2, 3):
                print('Incorrect Value! Please choose among 1, 2, and 3.')
                continue
            
            length = int(input('Please enter the length of your desired password (greater than 4):'))
            
            if length < 4:
                print('Incorrect Value! Length should be greater than 4.')
                continue
            if level == 1:
                lower_alpha_gen(length)
            elif level == 2:
                alpha_gen(length)
            elif level == 3:
                alpha_num_gen(length)

            repeat = input('Would you like to try again [y/n]: ').strip().lower()
            if repeat not in ('y', 'n'):
                print('Please choose between y (Yes) and n (No)')
                continue
            elif repeat == 'n':
                break

        except ValueError:
            print('Invalid input. Please enter a valid number.')

    print('Thank you for using Password Generator')

if __name__ == "__main__":
    main()
