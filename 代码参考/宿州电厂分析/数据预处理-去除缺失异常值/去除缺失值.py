import pandas as pd

# 读取Excel文件
input_file_path = '../data/数据整合.xlsx'  # 替换为你的Excel文件路径
df = pd.read_excel(input_file_path)

# 删除包含缺失值的列
df_cleaned = df.dropna(axis=0, how='any')

# 将结果保存到新的Excel文件
output_file_path = '../data/数据整合cleaned_new.xlsx'
df_cleaned.to_excel(output_file_path, index=False)
