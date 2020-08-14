import json
import csv
"""

with open("pessoas.csv", 'r') as arquivo_csv:
    leitor = csv.reader(arquivo_csv, delimiter = ';')
    leitor.__next__()
    x = 1
    for i in leitor:
        if i[2] == 'f' and int(i[1]) > x:
            print("Nome: {} | Idade: {}".format(i[0], i[1]))
"""

"""
Exercicio pra casa 1
nome_arquivo_entrada = "caso_full.csv"
nome_arquivo_saida = "RioDasOstras.csv"
with open(nome_arquivo_entrada, 'r') as arquivo_entrada:
    leitor = csv.reader(arquivo_entrada, delimiter = ',')
    leitor.__next__()
    with open(nome_arquivo_saida, 'a') as arquivo_saida:
        escritor = csv.writer(arquivo_saida, delimiter=',', lineterminator='\n')
        for linha in leitor:
            print(linha)
            if linha[0] == "Rio das Ostras":
                escritor.writerow(linha)
"""


"""
with open("teste3.json","r") as arquivo_json:
    cursos = json.load(arquivo_json)
    for curso in cursos:
        quantidade_de_alunos = len(curso['Alunos'])
        acumulador = 0
        for pessoa in curso['Alunos']:
            acumulador += pessoa['idade']
        print("A media das idades dos alunos do curso de {} é {}".format(curso["Curso"], acumulador / quantidade_de_alunos))
"""


nome_arquivo_entrada = "RioDasOstras.csv"
nome_arquivo_saida = "RioDasOstras.json"

with open(nome_arquivo_entrada, 'r') as arquivo_entrada:
    leitor = csv.reader(arquivo_entrada, delimiter=',')
    label = ["city","city_ibge_code","date","epidemiological_week","estimated_population_2019","is_last","is_repeated","last_available_confirmed","last_available_confirmed_per_100k_inhabitants","last_available_date","last_available_death_rate","last_available_deaths","order_for_place","place_type","state","new_confirmed","new_deaths"]
    contador_confirmados = 0
    contador_mortes = 0
    for linha in leitor:
        caso = {label[2]: linha[2], label[-2]: int(linha[-2]), label[-1]: int(linha[-1])}
        contador_confirmados += int(linha[-2])
        contador_mortes += int(linha[-1])
        with open(nome_arquivo_saida, 'a') as arquivo_de_saida:
            json.dump(caso, arquivo_de_saida, indent=2)
    print("Mortes confirmadas = {} | casos confirmados = {}".format(contador_mortes,contador_confirmados))