import os
import glob
import sys

input_directory = "sstap-rules/rules"  # 规则文件夹路径
output_file = "rules.list"  # 输出文件名
rule_files = glob.glob("sstap-rules/**/*.rule", recursive=True)
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
