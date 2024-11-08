import os
import glob
import sys

input_directory = "/home/runner/work/SSTap-Rule/SSTap-Rule/rules"  # 规则文件夹路径
output_file = "rules.list"  # 输出文件名
entries = os.listdir(input_directory)
# 打印所有文件和目录
for entry in entries:
    print(entry)

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
                # 假设每行是一个IP或域名，没有前缀
                # 检查是否是IP地址
                if '.' in line and line.count('.') == 3:
                    # 假设所有IP地址都需要转换为CIDR格式，这里使用/32作为示例
                    rules.append(f"IP-CIDR,{line}/32")
                else:
                    # 假设所有非IP地址都是域名，并使用域名后缀匹配
                    rules.append(f"DOMAIN-SUFFIX,{line}")

# 去重并排序规则（可选）
rules = sorted(set(rules))

# 将规则写入 .list 文件
with open(output_file, "w") as f:
    f.write("\n".join(rules))

print(f"Generated list configuration file at {output_file}")

# 读取输入文件，并将每行转换为指定格式
# with open(input_file, 'r') as f:
#     for line in f:
#         line = line.strip()  # 去除行首尾的空白字符
#         if not line:
#             continue  # 跳过空行

#         # 判断是IP还是域名，并添加到列表
#         if '.' in line and line.count('.') == 3:  # 简单的IP地址检查
#             # 假设所有IP地址都需要转换为CIDR格式，这里使用/32作为示例
#             converted_rules.append(f"IP-CIDR,{line}/32")
#         else:
#             # 假设所有非IP地址都是域名，并使用域名后缀匹配
#             converted_rules.append(f"DOMAIN-SUFFIX,{line}")

# # 将转换后的规则写入输出文件
# with open(output_file, 'w') as f:
#     for rule in converted_rules:
#         f.write(rule + '\n')

# print(f"Rules have been converted and written to {output_file}")
