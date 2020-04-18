def twinPrimeString(max):

    def prime(p):
        for i in range(2, p):
            if p%i == 0:
                return False
        return True

    def twinCheck(p):
        twinPrime = []
        count = 0
        for k in range(0, len(p)+1):
            if k<len(p)-1:
                if p[k]+2 == p[k+1]:
                    twinPrime.append((p[k], p[k+1]))
                    count += 1
        return print('孿生質數： {}\n總計: {}個'.format(twinPrime, count))
    
    pList = []
    for i in range(2, max+1):
        if prime(i):
           pList.append(i)

    return twinCheck(pList)



max = input('輸入一個數值顯示到它為止的孿生質數: ')
twinPrimeString(int(max))