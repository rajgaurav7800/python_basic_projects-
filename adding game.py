import random
per = 0
a = 0
f = None
level = int(input("choose difficulty...by level(max 5)..."))
if level==1:
    b=10
    total = 100
elif level==2:
    b=100
    total = 15
elif level==3:
    b=1000
    total = 20
elif level==4:
    b=10000
    total = 25
elif level==5:
    b=100000
    total = 10
else:
    print('saale sahi level choose krr..')

# b = 10000

questions = 0
while f !=100.0:

    n1 = random.randint(a, b)
    n2 = random.randint(a, b)
    inp = int(input(f"{n1} + {n2} = "))

    if inp == n1+n2:
        print(f'\n\nright\n')
        per += 1
        f = (per/total)*100
        questions += 1
        print(f"{(per/total)*100}%")
        print(questions)

    else:
        print(f'\nwrong\n---->{n1+n2}')
        break
if f ==100.0:
    print('<--------------WINNER WINNER CHICKEN DINNER-------------->')
else:
    print('\nsaala add krna nahe aata h jake LKG me bharti ho..')