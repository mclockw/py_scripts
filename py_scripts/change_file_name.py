import os
import string

# define path 
path = '/Users/wangchenzhong/CFA2023/CFA 2023/视频/财报分析'

# list all files in path 
files = os.listdir(path)

# print all filenames 
for file in files: 
    filename, file_ext = os.path.splitext(file)
    name_parts = filename.split("｜")
    # print(name_parts)
    new_name = f"{name_parts[-1]}".strip()
    # print(f"{new_name}{file_ext}")
    os.rename(os.path.join(path, file), os.path.join(path, f"{new_name}{file_ext}"))


