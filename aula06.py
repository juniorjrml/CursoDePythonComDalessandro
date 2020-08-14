import json
import csv

"""
Exercicio: implemente uma funcao que leia o arquivo CSV indicado
pelo professor e imprima todas as mulheres com idade acima de um
valor x fornecido
"""


# definindo a solucao:
def mulheres_idade_superior_aX(base,x):
    with open(base, 'r') as arquivo_csv:
        leitor = csv.reader(arquivo_csv, delimiter = ';')

        # primeira linha tem os titulos de cada coluna
        # .__next__() retorna o conteudo atual apontado pelo iterator e avanca para o prox
        cabecalho = leitor.__next__()

        for i in leitor:
            if i[2] == 'f' and int(i[1]) > x:
                print("{}: {} | {}: {}".format(cabecalho[0], i[0], cabecalho[1], i[1]))


#utilizando a solucao
mulheres_idade_superior_aX("pessoas.csv",15)


"""
Exercicio: imprima a media dos alunos de cada curso descrito
no arquivo teste3.json
"""

# definindo a solucao:
def media_alunos(base):
    with open(base, "r") as arquivo_json:
        cursos = json.load(arquivo_json)
        for curso in cursos:
            quantidade_de_alunos = len(curso['Alunos'])
            acumulador = 0
            for pessoa in curso['Alunos']:
                acumulador += pessoa['idade']
            print("A media das idades dos alunos do curso de {} é {}".format(curso["Curso"], acumulador / quantidade_de_alunos))

#utilizando
media_alunos("teste3.json")

"""
Exercicio para casa:
acessar https://brasil.io/dataset/covid19/caso_full/ e baixar o dataset
ler o arquivo caso_full.csv e criar um arquivo caso_RO.csv com apenas
as informaçoes da cidade de Rio das Ostras
"""

"""
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


# o arquivo "RioDasOstras.csv" foi criado no trecho comentado acima
# caso queira executar o trecho novamente apague o conteudo ou exclua o arquivo "RioDasOstras.csv" ou ficara com dados duplicados


# Solucao alternativa:
def criar_arquivo_cidade_csv(nome_arquivo_entrada, cidade):

    with open(nome_arquivo_entrada, 'r') as arquivo_entrada:
        leitor = csv.reader(arquivo_entrada, delimiter=',')
        # primeira linha tem os titulos de cada coluna
        # .__next__() retorna o conteudo atual apontado pelo iterator e avanca para o prox
        titulos = leitor.__next__()

        nome_arquivo_saida = cidade.replace(" ", "_") + ".csv"

        # apagando o arquivo se existente e colocando o cabecalho
        with open(nome_arquivo_saida, 'w') as arquivo_saida:
            escritor = csv.writer(arquivo_saida, delimiter=',', lineterminator='\n')
            escritor.writerow(titulos)

        with open(nome_arquivo_saida, 'a') as arquivo_saida:
            escritor = csv.writer(arquivo_saida, delimiter=',', lineterminator='\n')

            for linha in leitor:
                if linha[0] == cidade:
                    escritor.writerow(linha)


# utilizando a segunda solucao:
criar_arquivo_cidade_csv("caso_full.csv","Rio das Ostras")


"""
Exercicio para casa: Leia o arquivo csv do site "Brasil IO" e escreva
em um arquivo JSON, para cada data(date),o numero de novos 
casos (new_confirmed) e de novos obitos (new_deaths) para a cidade
de Rio das Ostras.
"""

"""
nome_arquivo_entrada = "RioDasOstras.csv"
nome_arquivo_saida = "RioDasOstras.json"

with open(nome_arquivo_entrada, 'r') as arquivo_entrada:
    leitor = csv.reader(arquivo_entrada, delimiter=',')
    titulos = ["city", "city_ibge_code", "date", "epidemiological_week", "estimated_population_2019", "is_last",
               "is_repeated", "last_available_confirmed", "last_available_confirmed_per_100k_inhabitants",
               "last_available_date", "last_available_death_rate", "last_available_deaths", "order_for_place",
               "place_type", "state", "new_confirmed", "new_deaths"]
    # contador_confirmados = 0
    # contador_mortes = 0
    for linha in leitor:
        # as entradas do arquivo de origem é por data, logo e so passar para o arquivo em json
        caso = {titulos[2]: linha[2], titulos[-2]: int(linha[-2]), titulos[-1]: int(linha[-1])}
        # contador_confirmados += int(linha[-2]) #contadores nao pedido no exercicio
        # contador_mortes += int(linha[-1])

        with open(nome_arquivo_saida, 'a') as arquivo_de_saida:  # abre para adicionar no fim do arquivo
            # optei por abrir o arquivo diversas vezes(json) para evitar sobrecarregar a memoria
            json.dump(caso, arquivo_de_saida, indent=2)
    # print("Mortes confirmadas = {} | casos confirmados = {}".format(contador_mortes,contador_confirmados))
"""

# outra solucao
def converter_cidade_modelo_json_D_NC_ND(nome_arquivo_entrada,cidade):
    # cria um csv para a cidade
    criar_arquivo_cidade_csv(nome_arquivo_entrada, cidade)
    # configura o nome do arquivo da cidade criado acima
    nome_arquivo_entrada = cidade.replace(" ", "_") + ".csv"
    with open(nome_arquivo_entrada, 'r') as arquivo_entrada:
        leitor = csv.reader(arquivo_entrada, delimiter=',')
        # primeira linha tem os titulos de cada coluna
        # .__next__() retorna o conteudo atual apontado pelo iterator e avanca para o prox
        titulos = leitor.__next__()
        nome_arquivo_saida = cidade.replace(" ", "_") + ".json"

        with open(nome_arquivo_saida, 'a') as arquivo_de_saida:
            pass

        for linha in leitor:
            # as entradas do arquivo de origem é por data, logo e so passar para o arquivo em json
            caso = {titulos[2]: linha[2], titulos[-2]: int(linha[-2]), titulos[-1]: int(linha[-1])}

            # abre para adicionar no fim do arquivo
            with open(nome_arquivo_saida, 'a') as arquivo_de_saida:
                # optei por abrir o arquivo diversas vezes(json) para evitar sobrecarregar a memoria
                json.dump(caso, arquivo_de_saida, indent=2)


#utilizando a outra solucao
converter_cidade_modelo_json_D_NC_ND("RioDasOstras.csv", "Rio das Ostras")
