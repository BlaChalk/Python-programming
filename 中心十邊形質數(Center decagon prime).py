def prime(p):
    for i in range(2, p):
        if p%i == 0:
            return False
    return True
def ten(p):
    for i in range(1, p):
        if p == 5*(i*i+i)+1:
            return True
    return False


max = input('輸入一個數值顯示到它為止的中心十邊形質數: ')
for i in range(int(max)):
    if prime(i) and ten(i):
        print(i)
