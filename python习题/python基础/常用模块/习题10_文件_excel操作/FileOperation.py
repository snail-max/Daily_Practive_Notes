# -*-coding:utf-8-*-
import json
import pandas as pd
import xlwt


with open("student.txt",encoding="utf-8") as f:
    infoDic = json.load(f)
    df= pd.DataFrame(infoDic)
    # dataframe 转置
    df2 = pd.DataFrame(df.values.T, index=df.columns, columns=df.index)  # 转置
    # dataframe写入excel
    df2.to_excel("student.xls")





