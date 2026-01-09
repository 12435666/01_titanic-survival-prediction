import pandas as pd
pd.set_option('display.max_rows', 5)
fruuu=pd.DataFrame({'App':[30],'Banama':[21]})
print(fruuu)

fru=pd.DataFrame({'App':[35,41],'Banama':[21,34]},index=['2017','2018'])
fru.to_excel(r'C:\Users\tengxy\Downloads\11121.xlsx')
print(fru)

Q3=pd.Series(['FLOU','MILK','EGGS'],['4','5','6'],name='牛牛')
print(Q3)

CSV_READD=pd.read_excel(r'C:\Users\tengxy\Downloads\89FF5389704050442F26193E0A0A6649.xlsx').dropna(axis=1,how='all')
CSV_READD.to_excel(r'C:\Users\tengxy\Downloads\11122.xlsx')
print(CSV_READD)

