import os

def add_ok_format_to_tests(root_directory):
    # 定义要添加的行
    ok_format_line = "OK_FORMAT = True\n"

    # 遍历根目录下的所有文件夹和文件
    for root, dirs, files in os.walk(root_directory):
        # 如果当前目录是 tests 文件夹
        if os.path.basename(root) == "tests":
            for file in files:
                # 只处理 .py 文件
                if file.endswith(".py"):
                    file_path = os.path.join(root, file)
                    
                    # 读取文件内容
                    with open(file_path, "r", encoding="utf-8") as f:
                        lines = f.readlines()
                    
                    # 如果第一行已经包含 OK_FORMAT，不重复添加
                    if any(line.strip() == "OK_FORMAT = True" for line in lines):
                        continue
                    
                    # 添加 OK_FORMAT = True 到文件开头
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(ok_format_line)
                        f.writelines(lines)
                    print(f"Updated: {file_path}")

# 指定 sp23 目录为根目录
root_directory = os.path.dirname(os.path.abspath(__file__))

# 调用函数处理所有 tests 文件夹
add_ok_format_to_tests(root_directory)
