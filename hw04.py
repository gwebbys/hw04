# ------------------------------------------------------
#        Name: Grace W
#       Peers: Malia L
#  References: (anything you checked to solve this)
# ------------------------------------------------------
import sys

secret_word = "food"

# Task 1
def check_text():
    """Ask for a given sentence until it contains the secret word, or the word dog or Dog"""
    while True:
    #getting a sentence from the user
        givensentence = input("Write me a sentence: ")
    #checking if secret word is in text, and telling user they used it
        if secret_word in givensentence:
            print("You used the secret word!")
            break
    
    #checking if the user used dog, and telling user they used it
        if "dog" in givensentence or "Dog" in givensentence:
            print("You used the word \"dog\" or the word \"Dog\"!")
            break
        
    #if neither condition is true, make them try again
        else:
            print("Try again")
        

# Task 2
def check_greater():
    """This function will get two integers from the user
    and then compare their values"""
    
    #this forms a loop
    while True:
        #this gets 2 inputs from user
        integer1 = int(input("Give me an integer: "))
        integer2 = int(input("Give me a second integer: "))
        
        #if the first input is larger than the second, we say so
        if integer1 > integer2:
            print("First is Greater")
            break
        #if the second input is larger than the first, we say so
        elif integer1 < integer2:
            print("Second is Greater")
            break
        #if the inputs are equal, the user tries again
        else:
            print("Try again")


# Task 3
def get_special_numbers():
    """ Print numbers that are odd, multiples of three,
and not multiples of 2 or 5 within the range of 1-40"""
    
    for num in range(1, 41):
        #ignore multiples of 2
        if num % 2 == 0:
            continue
        #a weird way of saying we want multiples of 3
        if num % 3 != 0:
            continue
        #ignore multiples of 5
        if num % 5 == 0:
            continue
        
        print(num)


# Task 4.a
def my_for_loop():
    """This function takes a string from the user and checks
if it is within the correct range [2,5]. Then, if it is in the right range,
it labels the consonants and vowels in the phrase"""
    
    string = input("Give me a string: ")
    
    #reenter string if it is not 2-5 characters long
    if len(string) < 2 or len(string) > 5:
        print("bad word")
        return
    #reenter string if it has a space in it
    if " " in string:
        print("bad word")
        return
    
    for letter in string:
       if letter.lower() in "aeiou":  #still confused why we use letter.lower? what does that even mean?
           print(f"{letter} is a vowel")
           
       else:
            print(f"{letter} is a consonant")
    
# Task 4.b
def my_while_loop():
    """ This function will ask the user for an option a, b, or c, and complete
different actions depending on the choice"""
    
    while True:
        optionchoice = input("Choose option a, b, or c: ")
        
        if optionchoice == "a":
            continue
        
        elif optionchoice == "b":
            print("Goodbye")
            return
        
        elif optionchoice == "c":
            sys.exit()
            
        else:
            print("try again")
            continue

# ---------------------------------------
# Do not modify anything below this line
# ---------------------------------------

def main():

    # Task 1 calls
    check_text()

    # Task 2 calls
    check_greater()

    # Task 3 calls
    get_special_numbers()

    # Task 4 calls
    my_for_loop()
    my_while_loop()

if __name__ == "__main__":
    main()
    print("The End")
