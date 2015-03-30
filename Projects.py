## Name game Anthony and Frankie

def name_game(name):
    '''input can only be letters and preferably a name

once you put in a name it gives each letter a value and adds them together, then divides by the number of letters

the output would print the answer to the equation above'''
    name = raw_input('Write Text: ')

    name = name.lower()

    output = []

    for character in name:
        number = ord(character) - 96
        output.append(number)
    
    answer = (sum(output) / float(len(output)))

    print answer

## Vending Anthony Frankie
def vending_machine(money, choice):
    '''input would be (money, choice)
    money needs to be int or floats, choice is "Oprhan Tears" "FireBall" "Alien Piss" "Water"
    
    if money = 1 and choice is applicable return choice
    if money > 1 and choice is applicable return choice and money - 1
    if money < 1 print Insuficient funds
    if choice is not applicable print Not applicable choice'''
    if money >= 1:
        if choice == "Orphan Tears" or choice == "FireBall" or choice == "Alien Piss" or choice == "Water":
            return (choice, money - 1)
    if money < 1:
        print "Insuficient Funds"
    else:
        print "Not applicable choice"        
           
## FizzBuzz Anthony and Frankie
def FizzBuzz():
    '''Input is nothing.
    
    if numbers in range(1, 100) divided by 15 has a remainder of 0 print "FizzBuzz"
    if numbers divded by 3 has a remaider of 0 print "Fizz"
    if numbers divided by 5 has a remaider of 0 print "Buzz"
    if number have a remainder print numbers'''
    for numbers in range(1,100):
        if numbers %15==0:
            print "FizzBuzz"
        elif numbers %3==0:
            print "Fizz"
        elif numbers %5==0:
            print "Buzz"
        else:
            print numbers

## Prime Checker Anthony and Frankie
def primeCheck(number):
    '''Input int.
    
    Checks if the int you entered is Prime or not
    
    if the number is prime return True
    if the number is not prime return False'''
    for x in range(2, number):
        if number % x == 0:
            return False
    return True
 
pList=[]
for i in range(3, 1000):
     if primeCheck(i):
         pList.append(i)

            

