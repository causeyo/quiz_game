print("\t### computer quiz ###\n")

play = input("do you want to play a game? (yes/no) ")

if play.lower() != "yes":
    quit()
print("let's start!!!")

score =0


answer = input("what does PC stands for? ").lower()
if answer == "personal computer":
    print("you're right")
    score += 1
else:
    print("you're wrong!!!")

answer = input("what does USB stands for? ").lower()
if answer == "universal serial bus":
    print("you're right")
    score += 1
else:
    print("you're wrong!!!")

answer = input("what does UDP stands for? ").lower()
if answer == "user datagram protocol":
    print("you're right")
    score += 1
else:
    print("you're wrong!!!")

print("\nyou've collected {} points during this game".format(score))
