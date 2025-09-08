import pandas as pd
import os

directory = r'D:\FlyFireF\Work and Study\毕业设计\宿州电厂数据汇总\2024锅炉6号机'
dataframes = []
for file in os.listdir(directory):
    file_path = os.path.join(directory, file)
    df=pd.read_excel(file_path,skiprows=[0,2,3])
    cols=["设备名称","负荷","再热汽温度","氧量","排烟温度","送风机入口温度"]
    df=df[cols]
    df = df.iloc[:-1]
    dataframes.append(df)
df_all=pd.concat(dataframes)
# df_all = df_all.dropna(subset=["负荷","再热汽温度","氧量","排烟温度","送风机入口温度"])
df_all.to_excel("data/2024锅炉6号机汇总数据.xlsx",index=False)