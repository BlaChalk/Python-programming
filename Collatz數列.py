def collatz(x):
    print(x)
    if x != 1:
        if (x%2 == 0):
            return collatz(int(x/2))
        else:
            return collatz(int(x*3+1))

num = input('輸入一個數值產生Collatz: ')
collatz(int(num))
