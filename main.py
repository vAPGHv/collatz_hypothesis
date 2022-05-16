while True:
    try:
        x = int(input("Enter any natural number: "))
    except:
        print("You enter is dont natural number!")
    o = 0

    while x != 1:
        if x < 1:
            break
        o+=1
        if x % 2 == 0:
            x/=2
        else:
            x=x*3+1
        print(int(x))
    
    print(f"\n{o} operations!\n\n\n\n")
