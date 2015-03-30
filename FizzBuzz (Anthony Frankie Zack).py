def FizzBuzz():
    for numbers in range(1,100):
        if numbers %15==0:
            print "FizzBuzz"
        elif numbers %3==0:
            print "Fizz"
        elif numbers %5==0:
            print "Buzz"
        else:
            print numbers