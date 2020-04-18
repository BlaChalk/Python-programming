#1.加總分(total), 排名(rank)
#2.使用subject為主
students = {
    'Chang':
        {
            'Math': 90, 
            'Chinese': 85, 
            'English': 60
        },
    'Thang':
        {
            'Math': 85, 
            'Chinese': 70, 
            'English': 92
        },
    'Chen':
        {
            'Math': 90, 
            'Chinese': 93, 
            'English': 95
        } 
    }
subjects = {}

# 加總分
for key, values in students.items():
    students[key]['total'] = 0
    for sub, score in values.items():
        if sub != 'total':
            students[key]['total'] += score

# 設定排名
for key in students.keys():
    students[key]['rank'] = 1
    for compareKey in students.keys():
        if students[key]['total'] < students[compareKey]['total']:
            students[key]['rank'] += 1

# 以科目為主
for key, values in students.items():
    for sub, score in values.items():
        subjects.setdefault(sub, {})
        subjects[sub][key] = score



print(students)
print(subjects)