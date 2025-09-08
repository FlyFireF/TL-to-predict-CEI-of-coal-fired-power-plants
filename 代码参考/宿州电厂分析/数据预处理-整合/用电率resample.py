import pandas as pd
import os
file_path=r"D:\FlyFireF\Work and Study\毕业设计\宿州电厂数据汇总\5-6厂用电率\用电率.xlsx"
df = pd.read_excel(file_path)
df['时间'] = pd.to_datetime(df['时间'])
df.set_index('时间', inplace=True)
daily = df.resample('d').mean()
daily.to_excel("data/宿州电厂日平均用电率.xlsx")