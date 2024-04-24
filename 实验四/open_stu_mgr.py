
with open('stu_mgr.py', 'r', encoding='utf-8') as file:
    for line in file:
        if not line.startswith('#'):
            print(line.strip())