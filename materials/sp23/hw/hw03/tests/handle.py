OK_FORMAT = True
import os

def add_ok_format(directory):
    # 定义要添加的行
    ok_format_line = "OK_FORMAT = True\n"
    script_name = os.path.basename(__file__)  # 当前脚本名（handle.py）

    # 遍历指定目录下的所有文件
    for root, _, files in os.walk(directory):
        for file in files:
            # 只处理 .py 文件，且排除当前脚本文件
            if file.endswith(".py") and file != script_name:
                file_path = os.path.join(root, file)
                
                # 读取文件内容
                with open(file_path, "r", encoding="utf-8") as f:
                    lines = f.readlines()
                
                # 如果第一行已经包含 OK_FORMAT，不需要重复添加
                if any(line.strip() == "OK_FORMAT = True" for line in lines):
                    continue
                
                # 添加 OK_FORMAT = True 到文件开头
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(ok_format_line)
                    f.writelines(lines)

# 获取脚本所在目录（即 tests 文件夹）
current_directory = os.path.dirname(os.path.abspath(__file__))

# 调用函数，处理同目录下的 .py 文件
add_ok_format(current_directory)
