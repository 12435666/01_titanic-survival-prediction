import pandas as pd
pd.set_option('display.max_rows', 5)
# 第一阶段-读取和输出
# fruuu=pd.DataFrame({'App':[30],'Banama':[21]})
# print(fruuu)
#
# fru=pd.DataFrame({'App':[35,41],'Banama':[21,34]},index=['2017','2018'])
# fru.to_excel(r'C:\Users\tengxy\Downloads\11121.xlsx')
# print(fru)
#
# Q3=pd.Series(['FLOU','MILK','EGGS'],['4','5','6'],name='牛牛')
# print(Q3)
#
# CSV_READD=pd.read_excel(r'C:\Users\tengxy\Downloads\89FF5389704050442F26193E0A0A6649.xlsx').dropna(axis=1,how='all')
# CSV_READD.to_excel(r'C:\Users\tengxy\Downloads\11122.xlsx')
# print(CSV_READD)
#
# Q2=111
# print(Q2)



# 第二阶段-索引
# CSV_READD=pd.read_excel(r'C:\Users\tengxy\Downloads\11122.xlsx')
#
# AAA=CSV_READD.loc[0:9,'指标名称']
# print(AAA)
#
# BBB=CSV_READD.loc[[1,2,3,5,8],['指标代码','指标名称']]
# print(BBB)
#
# CCC=CSV_READD.loc[CSV_READD.指标代码 ==1480010003,'指标代码']
# print(CCC)
#
# DDD=CSV_READD.loc[(CSV_READD.指标代码 ==1480010003) | ((CSV_READD.指标代码 ==1480010004) & (CSV_READD.指标名称 =='电影票房(广州:日)') )]
# print(DDD)

#第三阶段-摘要
# CSV_READD=pd.read_excel(r'C:\Users\tengxy\Downloads\11122.xlsx')
# median_points = CSV_READD.指标代码.median()
# print(median_points)
#
# countries = CSV_READD.关键词.unique()
# print(countries)
#
# reviews_per_country = CSV_READD.关键词.value_counts()
# print(reviews_per_country)
#
# CSV_MAXZBDM=CSV_READD.loc[(CSV_READD.指标代码-1).idxmax(),'指标代码']
# print(CSV_MAXZBDM)
#
# CSV_MAXJZRQ=CSV_READD.loc[(CSV_READD.截止日期).idxmax(),'截止日期']
# print(CSV_MAXJZRQ)
#
# A1=CSV_READD.关键词.map(lambda a: "北" in a).sum()
# A2=CSV_READD.关键词.map(lambda a: "上" in a).sum()
# A12=pd.Series([A1,A2],['北','上'])
# print(A12)
#
# B1=CSV_READD.apply(lambda b1:3 if b1['关键词']=='北' else 1,axis=1)
# print(B1)
#
# B2=CSV_READD.apply(lambda a:3 if a['指标代码']=='144' else 1,axis=1)
# print(B2)

