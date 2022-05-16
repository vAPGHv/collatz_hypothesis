try:
        start = int(input("Enter any natural number (start): "))
        finish = int(input("Enter any natural number (end): "))
        if start < 1:
            start = 1
        if finish <= start:
            finish=start+1
except:
    print("You enter is dont natural number!")

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
    
    print(f"\nNumber {i} has {o} operations!\n\n\n\n")
