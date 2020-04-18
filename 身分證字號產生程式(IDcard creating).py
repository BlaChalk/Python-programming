# 身分證字號產生程式
import random

area = {
    'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15, 'G':16, 'H':17, 'I':34, 'J':18, 'K':19, 'L':20, 'M':21, 
    'N':22, 'O':35, 'P':23, 'Q':24, 'R':25, 'S':26, 'T':27, 'U':28, 'V':29, 'W':32, 'X':30, 'Y':31, 'Z':33
}


# 隨機生成前九碼
def randomID():

    randID = input('請輸入想要的區域碼(A~Z): ')
    randID += input('請輸入想要的性別(男:1 / 女: 2): ')
    for x in range(7): 
        randID += str(random.randint(0,9))
    
    return randID


id = randomID()

# 檢查碼生成
area_number = area.get(id[0])
pipe_code = area_number//10 + area_number%10*9 + int(id[1])*8 + int(id[2])*7 + int(id[3])*6 + int(id[4])*5 + int(id[5])*4 + int(id[6])*3 + int(id[7])*2 + int(id[8])*1
id += str(10-pipe_code%10)


print('隨機生成身分證字號: {}'.format(id))
