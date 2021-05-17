import random
input("Choose any number in your mind and press enter")
print("Now take the same number from your friend and add it")
input("Press enter to continue....")
print("If you are done then enter Y")
yes=str(input())
n=random.randint(0,100)
if yes=="Y":
    print("Add "+str(n)+" to your sum")
    input("Press Enter to continue...")
    print("now half the number and return the number which you have taken from your friend")
    input("Press Enter to continue...")
    print("you are left with the number "+str(n/2))
else:
    print("Please enter Y after following the rule")    