import shutil
desktop_path = r'C:\Users\zezr\Desktop\a.txt'

target_file = r'C:/Users/zezr/Desktop/target.txt'

shutil.copy(desktop_path, target_file)

print("文件复制完成！")

