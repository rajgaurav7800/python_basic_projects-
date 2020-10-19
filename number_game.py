import random
while (1):
    t = 7
    n = random.randint(1, 99)
    print('the number is between 1~99\n')
    while (1):
        i = int(input("enter your guess..."))
        if i == n:
            print("....................you won.........................")
            break
        elif i < n:
            print("your guess is........... (small)")
        elif i > n:
            print("your guess is........... (big)")
        t = t - 1
        if t == 0:
            print(".........game over !..........""\n\n")
            print("you are a looser..  <-_->\n\n")
            break
        print("tryals left", "(", t, ")")
    p = input("do you want to play again (y/n)...")
    if p=="y":
        continue
    else:
        print("thanks for playing")
        break