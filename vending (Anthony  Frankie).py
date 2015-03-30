def vending_machine(money, choice):
    if money == 1:
        if choice == "Orphan Tears" or choice == "FireBall" or choice == "Alien Piss" or choice == "Water":
            return choice
    if money > 1:
        return (choice, money - 1)
    if money < 1:
        print "Insuficient Funds"   