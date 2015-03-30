import random
 
def loadWord():
     
    ''' Populate each list with at least 10 different items.  Create a variable called secretWord that is assigned a random word from one of the lists. 
     
    return a tuple in the following format:  (secretWord, list the secretWord is from)   
     
    Hint:  You will need to randomly choose one of the lists, and THEN choose a random word from that list.
    '''
    person = ['elvispresely', 'billyjoel', 'billyidol', 'beyonce', 'eminem', 'neilpatrickharris','weswelker', 'tombrady', 'einstein','tesla', 'vonbraun']
    place = ['california', 'paris', 'ocala','newyorkcity', 'baltimore', 'egypt','chicago', 'germany', 'dubai', 'brazil','mississippi','losangeles', 'florida','berlin', 'amsterdam']
    thing = ['desk','computer','tea','phone', 'jacket', 'boat','suit', 'lamp', 'washingmachine', 'toaster', 'truck', 'couch', 'pencil', 'ford','corvette','chevrolet']
    listOfLists = [person, place, thing]
    randomListChoice = random.choice(listOfLists)
     
    hint = ''
    secretWord = random.choice(randomListChoice)
     
    if randomListChoice == person:
        hint = 'person'
    elif randomListChoice == place:
        hint = 'place'
    elif randomListChoice == thing:
        hint = 'thing'
     
    return (secretWord, hint)
         
 
def isWordGuessed(secretWord, lettersGuessed):
    for letter in secretWord:
        if letter not in lettersGuessed:
            return False
    return True
             
def getGuessedword(secretWord, lettersGuessed):
     printedWord = ''
     for letter in secretWord:
         if letter in lettersGuessed:
             printedWord += letter + ' '
         else:
            printedWord += '_ '
     return printedWord
      
def getAvailableLetters(lettersGuessed):
     notGuessed = ''
     alphabet = 'abcdefghijklmnopqrstuvwxyz'
     for letter in alphabet:
         if letter not in lettersGuessed:
             notGuessed += letter + ' '
             
     return notGuessed
         
   
def hangman():
     
    #DECLARING NECESSARY VARIABLES
    temp = loadWord()
    secretWord = temp[0]
    hint = temp[1]
    wrongGuesses = 0
    lettersGuessed = []
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
     
    print "Welcome to hangman!  I'm thinking of a " + hint
              
    while wrongGuesses < 6:
              
        if isWordGuessed(secretWord, lettersGuessed) == True:
            return "You Win!"
        else:
            print getGuessedword(secretWord, lettersGuessed)
            print getAvailableLetters(lettersGuessed)
            guess = raw_input('Choose a letter:    ')
            guess = guess.lower()
          
              
            while len(guess) != 1 or guess in lettersGuessed or guess not in alphabet:
                print getAvailableLetters(lettersGuessed)
                guess = raw_input('Not valid, try again:    ')
              
            if guess not in secretWord:
                wrongGuesses += 1
                print"Sorry!  Wrong guess."
            else:
                print "Good guess!"
                  
            lettersGuessed.append(guess) 
            
             
            print "You have " + str(6 - wrongGuesses) + " misses remaining before hangman!"
        hangmanPics = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
        print hangmanPics[int(wrongGuesses)]
    return "You LOSE!..... I mean seriously. Who loses at hangman???"
