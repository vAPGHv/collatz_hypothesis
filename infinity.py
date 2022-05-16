try:
        start = int(input("Введите любое НЕ ДРОБНОЕ число (старт отсчета) (не меньше 1): "))
        finish = int(input("Введите любое НЕ ДРОБНОЕ число (конец отсчета) (не меньше старта): "))
        if start < 1:
            start = 1
        if finish <= start:
            finish=start+1
except:
    print("Вы ввели не дробное число (или вообще не число)!")

for i in range(start, finish+1):
    x = i
    o = 0

    while x != 1:
        if x < 1:
            break
        o+=1
        if x % 2 == 0:
            x/=2
        else:
            x=x*3+1
    
    print(f"\nУ числа {i}: {o} операций!\n\n\n\n")
