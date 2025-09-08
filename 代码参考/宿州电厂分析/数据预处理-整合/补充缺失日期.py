import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# 读取Excel文件
file_path = '../data/宿州六号清洗.xlsx'  # 替换为你的Excel文件路径
df = pd.read_excel(file_path)

# 确保第一列是日期列，并将其转换为datetime类型
date_column = df.columns[0]
df[date_column] = pd.to_datetime(df[date_column])

# 生成完整的日期范围
start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 12, 29)
all_dates = pd.date_range(start=start_date, end=end_date, freq='D')

# 创建一个空的DataFrame来存储完整的数据集
complete_df = pd.DataFrame(columns=df.columns)

# 使用字典来收集行数据，键是日期，值是该日期的行数据（列表）
rows_dict = {}

# 遍历完整的日期范围
for date in all_dates:
    if date in df[date_column].values:
        # 如果存在，则从原始DataFrame中获取该行数据
        row = df[df[date_column] == date].iloc[0].tolist()
    else:
        # 如果不存在，则创建一个空行数据
        row = [date if i == 0 else np.nan for i in range(len(df.columns))]

    # 将行数据添加到字典中（覆盖相同日期的任何先前条目，假设每个日期最多一行）
    rows_dict[date] = row

# 将字典转换为DataFrame
complete_df = pd.DataFrame.from_dict(rows_dict, orient='index', columns=df.columns)

# 如果日期不是索引，并且你希望它保持为普通列，请取消以下两行的注释
# complete_df.reset_index(inplace=True)
# complete_df.rename(columns={'index': date_column}, inplace=True)

# 将结果保存到新的Excel文件
output_file_path = '../data/宿州六号清洗补充.xlsx'
complete_df.to_excel(output_file_path)