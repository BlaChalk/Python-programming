# 身分證字號檢查器

area = {
    'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15, 'G':16, 'H':17, 'I':34, 'J':18, 'K':19, 'L':20, 'M':21, 
    'N':22, 'O':35, 'P':23, 'Q':24, 'R':25, 'S':26, 'T':27, 'U':28, 'V':29, 'W':32, 'X':30, 'Y':31, 'Z':33
}

# 檢驗的身份證字號
id = "N116454392"

# 數字加總
area_number = area.get(id[0])
pipe_code = area_number//10 + area_number%10*9 + int(id[1])*8 + int(id[2])*7 + int(id[3])*6 + int(id[4])*5 + int(id[5])*4 + int(id[6])*3 + int(id[7])*2 + int(id[8])*1

# 條件判斷
if pipe_code%10 == 10-int(id[9]) or not(pipe_code%10):
    print('此身份證字號符合規範。')
else:
    print('身份證字號錯誤。')