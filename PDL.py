import pandas as pd
from openpyxl import load_workbook
import matplotlib.pyplot as plt

# pede ao usuário para inserir os parâmetross
campeao = input("Digite o campeão: ")
rota = input("Digite a rota: ")
pdl = int(input("Digite o pdl: "))
ranked = int(input("Digite o ranked: "))
total_pdl = int(input("Digite o total de pdl: "))
elo = input("Digite o elo: ")

# cria um DataFrame com os parâmetros inseridos
df = pd.DataFrame({
    "Campeão": [campeao],
    "Rota": [rota],
    "PDL": [pdl],
    "Ranked": [ranked],
    "Total de PDL": [total_pdl],
    "Elo": [elo]
})

# carrega o arquivo Excel (se já existir) e adiciona o DataFrame na última linha
try:
    book = load_workbook("desempenho.xlsx")
    writer = pd.ExcelWriter("desempenho.xlsx", engine='openpyxl') 
    writer.book = book
    writer.sheets = dict((ws.title, ws) for ws in book.worksheets)
    reader = pd.read_excel(r'desempenho.xlsx')
    df.to_excel(writer, index=False, header=False, startrow=len(reader)+1)
    writer.save()
except:
    # se o arquivo não existir, cria um novo com o DataFrame
    df.to_excel("desempenho.xlsx", index=False)

# cria gráficos dinâmicos
df_grafico_rota = df.groupby(['Rota', 'Campeão'])['PDL'].mean().unstack()
df_grafico_rota.plot(kind='bar')
plt.xlabel("Rota")
plt.ylabel("PDL")
plt.title("Desempenho em cada rota com cada campeão")
plt.show()

df_grafico_pdl = pd.DataFrame({
    "PDL": [pdl],
    "Ranked": [ranked],
    "Total de PDL": [total_pdl]
}, index=["Desempenho"])
df_grafico_pdl.plot(kind='bar')
plt.ylabel("PDL")
plt.title("Desempenho em PDL")
plt.show()
