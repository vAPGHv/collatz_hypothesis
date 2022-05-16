while True:
    try:
        x = int(input("Введите любое НЕ ДРОБНОЕ число: "))
    except:
        print("Вы ввели не дробное число (или вообще не число)!")
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
    
    print(f"\nОпераций {o}\n\n\n\n")
