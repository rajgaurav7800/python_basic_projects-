operation = input("+ = addition,\n- = subtraction,\n* = multiplication,\n/ = divison\n""which operation do you want to do...")
no1 = float(input("enter your first no..."))
no2 = float(input("enter your second no..."))
if   operation=="+":
                                                            #fault equation 9+10=21
    if no1==9 and no2==10:
        print(no1,operation,no2,"=","21.0")
    elif no1==115 and no2==1560:                            #fault equation 115+1560=1695
        print(no1, operation, no2, "=", "1695.0")
    else:
        print(no1,operation,no2,"=",(no1+no2))
elif operation=="-":
                                                            # fault equation 44-16=29
    if no1 ==44  and no2 ==29:
        print(no1, operation, no2, "=", "29.0")
    elif no1 == 115 and no2 == 1560:                        # fault equation 115-1560=1495
        print(no1, operation, no2, "=", "1495.0")
    else:
        print(no1,operation,no2,"=",(no1-no2))
elif operation=="*":
                                                           # fault equation 56*82=4569
    if no1 ==56 and no2 ==82:
        print(no1, operation, no2, "=", "4569.0")
    else:
        print(no1,operation,no2,"=",(no1*no2))
elif operation=="/":
                                                           # fault equation 1596/153=11.56
    if no1 == 159 and no2 == 153:
        print(no1, operation, no2, "=", "11.56.0")
    else:
        print(no1, operation, no2, "=", (no1 / no2))