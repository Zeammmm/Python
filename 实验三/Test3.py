# 1.冒泡排序
nums = [9, 6, 5, 8, 4, 2, 1]
n = len(nums)
for i in range(n-1):
    for j in range(n-i-1):
        if nums[j] > nums[j+1]:
            nums[j], nums[j+1] = nums[j+1],nums[j]

print(nums)

# 2.求列表中最大的数
nums = [6, 5, 8, 4, 2, 1]
n = len(nums)
max = nums[0]
for i in range(1,n-1):
    if max < nums[i+1]:
        max = nums[i+1]
print(max)

# 3.统计列表里出现的次数最多的元素

chars = ['a', 'b', 'c', 'd', 'e', 'a', 'c', 'e']
chars_count = {}

for char in chars:
    if char in chars_count:
        chars_count[char] += 1
    else:
        chars_count[char] = 1
print(chars_count.items())
max_count = 0
most_common_chars = []
for char, count in chars_count.items():
    if count > max_count:
        max_count = count
        most_common_chars = [char]
    elif count == max_count:
        most_common_chars.append(char)

print("出现次数最多的元素:", most_common_chars)
print("出现次数:", max_count)

# 4.让用户输入姓名，如果姓名已经存在，提示用户;如果姓名不存在，继续输入年龄，并存入列表里
id = []

while True:
    name = input("请输入姓名（输入 no 退出）：")

    if name == 'no':
        break

    for names in id:
        if names[0] == name:
            print("姓名已经存在，请重新输入。")
            break
    else:
        age = input("请输入年龄：")
        id.append([name, age])

print("姓名和年龄列表：", id)

# --------------------------------------------------------------------------------
students = [
    {'name': '张三', 'age': 15, 'score': 99, 'tel': '13298788909', 'gender': 'female'},
    {'name': '李四', 'age': 19, 'score': 47, 'tel': '13298788909', 'gender': 'male'},
    {'name': '王五', 'age': 18, 'score': 96, 'tel': '13298788908', 'gender': 'unknown'},
    {'name': 'tony', 'age': 21, 'score': 52, 'tel': '13298788909', 'gender': 'female'},
    {'name': 'jack', 'age': 18, 'score': 98, 'tel': '13298786908', 'gender': 'male'},
    {'name': 'magic', 'age': 17, 'score': 99, 'tel': '13298788909', 'gender': 'unknown'}
]

# 打印不及格人数
fail = 0
for student in students:
    if student['score'] < 60:
        fail +=1
print("不及格人数：",fail)


# 打印不及格学生的名字和对应的成绩
for student in students:
    if student['score'] < 60:
        print("姓名：", student['name'], "成绩：",student['score'])

# 统计未成年学生的个数
not_age = 0
for student in students:
    if student['age'] <18:
        not_age +=1
print("未成年学生个数：",not_age)

# 打印手机尾号是8的学生的名字
for student in students:
    if student['tel'].endswith("8"):
        print("手机尾号8的学生姓名：", student['name'])

# 打印最高分和对应的学生的名字
max_score = 0
max_score_name = ""
for student in students:
    if student['score'] > max_score:
        max_score = student['score']
        max_score_name = student['name']

print("最高分：",max_score)
print("最高分学生姓名：",max_score_name)


# 删除性别不明的所有学生（这个地方有坑）
for student in students[:]:
    if student['gender'] == 'unknown':
        students.remove(student)
print("删除性别不明的学生后的学生列表:")
for student in students:
    print(student)

#将列表按学生成绩从大到小排序
students = [
    {'name': '张三', 'age': 15, 'score': 99, 'tel': '13298788909', 'gender': 'female'},
    {'name': '李四', 'age': 19, 'score': 47, 'tel': '13298788909', 'gender': 'male'},
    {'name': '王五', 'age': 18, 'score': 96, 'tel': '13298788908', 'gender': 'unknown'},
    {'name': 'tony', 'age': 21, 'score': 52, 'tel': '13298788909', 'gender': 'female'},
    {'name': 'jack', 'age': 18, 'score': 98, 'tel': '13298786908', 'gender': 'male'},
    {'name': 'magic', 'age': 17, 'score': 99, 'tel': '13298788909', 'gender': 'unknown'}
]

for i in range(len(students) - 1):
    for j in range(len(students) - i - 1):
        if students[j]['score'] < students[j + 1]['score']:  # 如果前一个学生的成绩小于后一个学生的成绩
            students[j], students[j + 1] = students[j + 1], students[j]
print("成绩降序")
for i in range(len(students)):
    print(students[i])

