import pandas as pd

# 读取Excel文件
file_path = r"D:\FlyFireF\Work and Study\毕业设计\煤质\2024年6号煤质.xlsx"  # 替换为你的Excel文件路径
df = pd.read_excel(file_path)

# 假设数据中有两列：一列是日期（datetime类型或可转换为datetime的字符串），另一列是指标数据
# 例如：日期列名为'Date'，指标数据列名为'Value'
date_column = '入炉日期'

# 确保日期列是datetime类型
df[date_column] = pd.to_datetime(df[date_column])

# 按日期分组并计算均值
daily_mean = df.groupby(df[date_column])[["全水","Aar(%)收到基灰分","Var(%)收到基挥发分","Fcad(%)空干基固定碳","QnetarMJ(MJ/kg)收到基低位发热量"]].mean().reset_index()

# 将结果保存到新的Excel文件
output_file_path = '../data/2024年6号煤质日均值.xlsx'
daily_mean.to_excel(output_file_path, index=False)