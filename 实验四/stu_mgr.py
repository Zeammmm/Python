students = []


# 功能一：添加学生信息，list[dic{}]
def add_student():

    student_id = int(input("请输入学号："))
    name = input("请输入姓名：")
    tel = int(input("请输入联系电话："))
    for student in students:
        if student["student_id"] == student_id:
            print("该用户已经存在!")
            return
    students.append({'student_id': student_id, 'name': name, 'tel': tel})
    print(students)


# 功能二：学生信息修改#
def modify_student():

    modify_name = input("请输入要修改的姓名：")
    new_tel = int(input("请输入新电话："))
    for student in students:
        if student['name'] == modify_name:
            student['tel'] = new_tel
            print(students)
            return
    print("该学员不存在！")


# 功能三：查询某个学员
def query_student():

    query_name = input("请输入查询姓名：")
    for student in students:
        if student['name'] == query_name:
            print("学号：", student['student_id'])
            print("姓名：", student['name'])
            print("手机号：", student['tel'])
            return
    print("该学员不存在！")


# 功能四：查询所有学员信息
def query_all_students():

    print("学号 姓名 手机号")
    for student in students:
        print(student['student_id'], student['name'], student['tel'])


# 功能五：删除学员

def delete_all_students():

    delete_name = input("请输入要删除的姓名：")
    for student in students:
        if student['name'] == delete_name:
            students.remove(student)
            return
    print("该学员不存在！")


# 功能六：退出系统

def exit_system():
    while True:
        over = input("是否继续退出请输入 y/n：")
        if over == "y":
            print("退出系统，感谢使用！")
            return True
        elif over == "n":
            return False
        else:
            print("输入错误，请重新输入！")

# 主函数

def main():
    while True:
        print("1.添加")
        print("2.修改")
        print("3.删除")
        print("4.查询")
        print("5.查询全部")
        print("6.退出")
        select = int(input("请用户输入功能编号："))
        if select == 1:
            add_student()
        elif select == 2:
            modify_student()
        elif select == 3:
            delete_all_students()
        elif select == 4:
            query_student()
        elif select == 5:
            query_all_students()
        elif select == 6:
            if exit_system():
                break

        else:
            print("输入编号不存在！")

if __name__ == "__main__":
    main()
