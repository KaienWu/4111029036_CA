import os
import time

directory_name = "CS"
if not os.path.exists(directory_name):
    os.mkdir(directory_name)

file_name = os.path.join(directory_name, "homework.txt")
with open(file_name, "w") as file:
    file.write("4111029036_伍凱恩")

with open(file_name, "r") as file:
    content = file.read()
    print("檔案內容：", content)

file_size = os.path.getsize(file_name)
print(f"文件大小: {file_size} 字節")

modification_time = os.path.getmtime(file_name)
print(f"最後修改時間為: {modification_time}")

formatted_time = time.ctime(modification_time)
print(f"最後修改時間(人類可讀格式): {formatted_time}")

os.remove(file_name)
os.rmdir(directory_name)
