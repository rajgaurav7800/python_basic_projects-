x=int(input("enter your age..."))
if x<1:
    print("pleas enter your correct age")
elif x<18:
    print("you are under age to drive come back after", 18-x, "years")
elif x==18:
    print("you are at right age to drive. do you have a licence..? (yes/no)")
    y = input()
    if y == str("yes"):
        print("good have a safe drive")
    elif y == str("no"):
        print("come to us to get a licens")
    else:
        print("error... enter correct answer")
elif x>100:
    print("pleas enter your correct age")
elif x>18:
    print("do you have a licens (yes/no)")
    y = input()
    if y == str("yes"):
        print("good have a safe drive")
    elif y == str("no"):
        print("come to us to get a licens")
    else:
        print("error... enter correct answer")