import pandas as pd
import os

pd.set_option('display.float_format', '{:.3f}'.format)
dataframes = []
# Specify the directory containing the Excel files
directory = r'C:\Users\RY\Desktop\火电碳排放影响因素识别与降碳措施研究\电厂调研数据\重要-五电厂碳排放数据汇总\宿州六号机组'
#D:\FlyFireF\Work and Study\毕业设计\宿州\六号机组
# Loop through all files in the directory
for file in os.listdir(directory):
    file_path = os.path.join(directory, file)
    df = pd.read_excel(file_path,skiprows=1).iloc[::,2:]
    #选择非停机数据
    df_without0 = df[df["负荷率平均值(%)"] != 0]
    #计算5mins 间隔的 碳排放强度
    df_without0["碳排放强度"] = ( (df_without0["C02浓度平均值(%)"]*44/22.4*10000)/1000*df_without0["烟气流量平均值(dNm3/h)"] ) / (1000 * df_without0["有功功率平均值(MW)"])
    #convert to datetime datatype
    df_without0['时间'] = pd.to_datetime(df_without0['时间'])
    # set date to index
    df_without0.set_index('时间', inplace=True)
    # resample to daily data
    daily = df_without0.resample('d').agg({
        '有功功率平均值(MW)': 'mean',
        '负荷率平均值(%)': 'mean',
        'C02浓度平均值(%)': 'sum',
        '氧含量平均值(%)': 'mean',
        '烟气流量平均值(dNm3/h)': 'mean',
        '碳排放量五分钟累计值(t)': 'sum' ,
        '排放量绩效平均值(g/kwh)': 'mean',
        '碳排放强度': 'mean'
    })
    dataframes.append(daily)
year_df = pd.concat(dataframes)
year_df = year_df.sort_index()
# year_df = year_df[(year_df["碳排放强度"] != 0) & (year_df["碳排放强度"].notnull()) ]
year_df.to_excel("data/宿州六号清洗2.xlsx")