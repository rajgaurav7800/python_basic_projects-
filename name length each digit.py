while 1:
    input_user = input("enter your name...")
    input_len = len(input_user)
    nu = t = 0
    new_str = "~"
    while input_len != 0:
        t = input_user[nu]
        if t in new_str:
            nu += 1
        else:
            print(f"{t} = {input_user.count(t)}")
        new_str += t
        input_len -= 1

