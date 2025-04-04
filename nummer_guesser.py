import random 

def show_count(count):
    print(f'You have needed {count} tries')
def show_winning_message(number,count):
    print(f'concratulation you have found the searched number {number} and needed this {count} amount of tries')

def guess_number(number):
    is_guessing = True
    count = 0
    while is_guessing == True:
        
        count += 1
        Guessed_number = int(input("guess number: "))

        
        if number == Guessed_number or Guessed_number == 0: 
            show_count(count)
            if Guessed_number == 0:
                print(f'thank you to try to guess the number {number} You have needed {count} tries')
                Q = is_guessing = False
                return
            show_winning_message(number,count)
            is_guessing = False
            return 
          
        if  Guessed_number >  number:
            print("the searched number is smaller")
        
        else :
            print("the searched number is bigger")

        if Guessed_number == 0:
            is_guessing = False
            return
to_guess_number = random.randint(1, 10)

