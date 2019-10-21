# read-large-files
Read large files with Python

# resolvi com Pandas


import pandas as pd

df1 = pd.read_csv(r'/home/ricardo/desafios/read-large-files/convertcsv1.csv')
df2 = pd.read_csv(r'/home/ricardo/desafios/read-large-files/convertcsv2.csv')

df = pd.concat([df1,df2], axis=1, join='inner').sort_index()


print(df.head())
df.to_csv('df.csv')

