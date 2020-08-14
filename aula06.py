"""
todas as funcoes estao do lado de fora das
condicionais para poder se exportadas
"""


import json
import csv
exercicio = ["6_1","6_2","6_3","6_4"]

############# inicio do exercicio 1 ##################

# definindo a solucao:
def mulheres_idade_superior_aX(base,x):
    with open(base, 'r') as arquivo_csv:
        leitor = csv.reader(arquivo_csv, delimiter = ';')

        # primeira linha tem os titulos de cada coluna
        # .__next__() retorna o conteudo atual apontado pelo iterator e avanca para o prox
        cabecalho = leitor.__next__()
        print("As mulheres acima de {} anos sao: ".format(x))
        for i in leitor:
            if i[2] == 'f' and int(i[1]) > x:
                print("{}: {} | {}: {}".format(cabecalho[0], i[0], cabecalho[1], i[1]))

if("6_1" in exercicio):
    print("Exercicio: implemente uma funcao que leia o arquivo CSV indicado")
    print("pelo professor e imprima todas as mulheres com idade acima de um")
    print("valor x fornecido")
    #utilizando a solucao
    mulheres_idade_superior_aX("pessoas.csv",15)
    print("")

############# fim do exercicio 1 ##################

############# inicio do exercicio 2 ##################

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

if ("6_2" in exercicio):
    print("Exercicio: imprima a media dos alunos de cada curso descrito")
    print("no arquivo teste3.json")
    #utilizando
    media_alunos("teste3.json")
    print("")

############# fim do exercicio 2 ##################


############# inicio do exercicio 3 ##################

# Solucao:
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

if ("6_3" in exercicio):
    print("Exercicio para casa:")
    print("acessar https://brasil.io/dataset/covid19/caso_full/ e baixar o dataset")
    print("ler o arquivo caso_full.csv e criar um arquivo caso_RO.csv com apenas")
    print("as informaçoes da cidade de Rio das Ostras")
    # utilizando a solucao:
    criar_arquivo_cidade_csv("caso_full.csv","Rio das Ostras")
    print("arquivo criado com sucesso!")
    print("")

############# fim do exercicio 3 ##################


############# inicio do exercicio 4 ##################

# Solucao
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

if ("6_4" in exercicio):
    print("Exercicio para casa: Leia o arquivo csv do site 'Brasil IO' e escreva")
    print("em um arquivo JSON, para cada data(date),o numero de novos ")
    print("casos (new_confirmed) e de novos obitos (new_deaths) para a cidade")
    print("de Rio das Ostras.")
    #utilizando a outra solucao
    converter_cidade_modelo_json_D_NC_ND("RioDasOstras.csv", "Rio das Ostras")
    print("")

############# fim do exercicio 4 ##################
