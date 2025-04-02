import csv

# with open("exemplo.csv", "r") as arquivo_csv:
#     leitor_csv = csv.reader(arquivo_csv)
#     for linha in leitor_csv:
#         print(linha)


caminho_arquivo: str = "exemplo.csv"

arquivo_csv: list = []

with open(file=caminho_arquivo, mode="r", encoding="utf-8") as arquivo:
    leitor_csv = csv.DictReader(arquivo)

    for linha in leitor_csv:
        arquivo_csv.append(linha)

print(arquivo_csv)


