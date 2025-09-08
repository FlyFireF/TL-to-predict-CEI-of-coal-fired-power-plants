import pandas as pd

# 读取Excel文件
file_path = '../data/2024锅炉5号机汇总数据.xlsx'  # 替换为你的Excel文件路径
df = pd.read_excel(file_path)

# 假设第一列是我们想要保留的列，其余列是需要求均值的指标数据
identifier_column = df.columns[0]

# 计算除了第一列以外的列的均值，同时保留第一列的值（每4行中的第一个）
# 使用groupby和cumcount来创建分组索引，然后用这个索引来保留第一列的值
group_index = (df.reset_index().groupby(df.index // 4).cumcount() == 0).astype(float)

# 创建一个新的DataFrame，其中第一列是原始第一列的分组首值，其余列是均值
result_df = pd.DataFrame({
    identifier_column: df.loc[group_index.astype(bool), identifier_column].reset_index(drop=True),
    **{col: df.groupby(df.index // 4)[col].mean() for col in df.columns[1:]}
})

# 将结果保存到新的Excel文件
output_file_path = '../data/2024锅炉5号机汇总数据日均值.xlsx'
result_df.to_excel(output_file_path, index=False)