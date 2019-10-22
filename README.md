# read-large-files
Read large files with Python

# resolução com cvs.DictReader
1. Ler arquivo um com csv.DictReader processando linha por linha
2. Para cada linha, crio um hash
3. Para cada hash crio um arquivo (arquivo vazio, nome do arquivo é o hash)
4. Fecho o arquivo 1
5. Abro o arquivo dois linha a linha e repituo o passo 2 para ele
6. Uso o os ou `pathlib.Path`para saber se o hash existe (se existir, a linha é duplicada)
7. Escrevo as linhas duplicadas como modo a para não ter a saída (escrirta) em memória


# resolução com com Pandas
import pandas as pd

df1 = pd.read_csv(r'/home/ricardo/desafios/read-large-files/convertcsv1.csv')
df2 = pd.read_csv(r'/home/ricardo/desafios/read-large-files/convertcsv2.csv')

df = pd.concat([df1,df2], axis=1, join='inner').sort_index()

print(df.head())
