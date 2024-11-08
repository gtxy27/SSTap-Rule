import os
import glob
import sys

input_directory = "./rules"  # 规则文件夹路径
output_file = "rules.list"  # 输出文件名
rule_files = glob.glob("sstap-rules/**/*.rule", recursive=True)
current_directory = os.getcwd()
print(f"The current working directory is: {current_directory}")
script_directory = os.path.dirname(os.path.abspath(__file__))
print(f"The script is located in: {script_directory}")
def print_directory_tree(start_path='.'):
    for root, dirs, files in os.walk(start_path):
        # 打印当前目录路径
        level = root.replace(start_path, '').count(os.sep)
        indent = ' ' * 4 * level
        print(f"{indent}[{os.path.basename(root)}/]")
        
        # 打印该目录下的文件
        sub_indent = ' ' * 4 * (level + 1)
        for file in files:
            print(f"{sub_indent}{file}")

# 显示当前执行目录的目录树
print_directory_tree()
if not rule_files:
    print("Error: No .rule files found.")

    sys.exit(1)
# 初始化列表用于存储规则
rules = []

# 遍历 rules 文件夹中的所有 .rule 文件并转换规则
for filename in os.listdir(input_directory):
    if filename.endswith(".rule"):
        with open(os.path.join(input_directory, filename), "r") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue  # 跳过空行和注释
                # 处理规则类型并添加到列表
                if line.startswith("IPCIDR"):
                    rules.append(f"IP-CIDR,{line.split('=')[1]}")
                elif line.startswith("DOMAIN"):
                    rules.append(f"DOMAIN,{line.split('=')[1]}")
                elif line.startswith("DOMAIN-SUFFIX"):
                    rules.append(f"DOMAIN-SUFFIX,{line.split('=')[1]}")
                # 添加其他规则类型的解析...

# 去重并排序规则（可选）
rules = sorted(set(rules))

# 将规则写入 .list 文件
with open(output_file, "w") as f:
    f.write("\n".join(rules))

print(f"Generated list configuration file at {output_file}")
