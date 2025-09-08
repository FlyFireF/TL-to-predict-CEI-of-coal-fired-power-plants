import pandas as pd
import os

directory = r'D:\FlyFireF\Work and Study\毕业设计\宿州电厂数据汇总\2024汽机5号机'
dataframes = []
for file in os.listdir(directory):
    file_path = os.path.join(directory, file)
    df=pd.read_excel(file_path,skiprows=[0,2,3])
    cols=["设备名称","再热汽温","排汽温度","给水温度"]
    df=df[cols]
    df = df.iloc[:-1]
    dataframes.append(df)
df_all=pd.concat(dataframes)
# df_all = df_all.dropna(subset=["主汽压","主汽温","排汽温度","给水温度"])
df_all.to_excel("../data/2024汽机5号机汇总数据.xlsx",index=False)