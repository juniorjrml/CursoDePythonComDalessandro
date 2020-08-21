exercicio = []
# ------------------- inicio exercicio para casa 1 -------------------
from aula2 import adicionar_elementos, mostrar_elementos_do_tipo,converter_para_tipo_do_elemento

def coletar_elemento():
    return converter_para_tipo_do_elemento(input("Digite um elemento: "))

def contar_elemento(lista):
    try:
        elemento = coletar_elemento()
        return lista.count(elemento)
    except:
        print("Nao foi possivel contar!")

def remove_elemento(lista):
    try:
        elemento = coletar_elemento()
        print(type(elemento))
        lista.remove(elemento)
    except:
        print("elemento invalido!")

if(10 in exercicio):
    print("*" * 20, "inicio do exercicio para casa 1", "*" * 20)
    textos_do_menu = [
        "1. Inserir um Elemento x na lista",
        "2. Remover um Elemento x da lista",
        "3. Imprimir a lista",
        "4. Contar o numero de ocorrencias de um elemento x",
        "5. Imprimir os elementos inteiros da lista",
        "6. Sair"
        ]
    acoes_do_menu = [
        lambda lista: adicionar_elementos(lista,quantidade=1),
        remove_elemento,
        lambda lista: [print(i) for i in lista],
        contar_elemento,
        lambda lista: mostrar_elementos_do_tipo(lista,int),
        lambda : print("Saindo...")]
    escolha_do_menu = [1, 2, 3, 4, 5, 6]
    menu = [textos_do_menu, escolha_do_menu, acoes_do_menu]
    lista = []
    while True:
        try:
            for i in menu[0]:
                print(i)
            opcao = int(input("Digite a opção desejada: "))
            try:
                menu[2][menu[1].index(opcao)](lista)  # So 1 funcao não recebe a lista como parametro(1parametro apenas)
            except:
                try:
                    menu[2][menu[1].index(opcao)]()  # Saindo do looping(nao recebe parametroo)
                    break
                except:
                    print("Algo deu Errado :(")  # Se for passado um numero fora do alcance da lista !
                    raise
        except:
            print("opção inexistente")
    print("*" * 20, 'fim do exercicio para casa 1', "*" * 20)
# ------------------- fim exercicio para casa 1 -------------------


############# inicio exercicio 3 ##################
if (3 in exercicio):
    print("*" * 20, "inicio do exercicio 3", "*" * 20)
    def coleta_dados_dicionario(campos):
        dic = {}
        for atributo in campos:
            try:
                dic[atributo] = converter_para_tipo_do_elemento(input("insira o {} ".format(atributo)))
            except:
                break
        else:
            return dic
        return {}
    atributos = ["nome","idade","cidade","altura"]
    d = coleta_dados_dicionario(atributos)
    for chave,valor in zip(d.keys(), d.values()) :
        print(chave,valor)
    print("*" * 20, 'fim do exercicio 3', "*" * 20)
############# fim exercicio 3 ##################
def leitura_de_matriz(num_linhas,num_colunas):
    matriz = []
    for linha in range(num_linhas):
        matriz.append([coletar_elemento() for _ in range(num_colunas)])
    return matriz

def mostrar_matriz(matriz):
    for linha in matriz:
        for coluna in linha:
            print(coluna,end='\t')
        print("")

if(4 in exercicio):

    def soma_de_matrizes(matriz1,matriz2):
        matriz_resultante = []
        for linha in enumerate(matriz1):
            linha_temp = []
            for coluna in enumerate(linha[1]):
                soma = coluna[1]+matriz2[linha[0]][coluna[0]]
                linha_temp.append(soma)
            matriz_resultante.append(linha_temp)
        return matriz_resultante

    m1 = leitura_de_matriz(2,2)
    m2 = leitura_de_matriz(2,2)
    # mostrar_matriz(m1)
    m3 = soma_de_matrizes(m1,m2)
    mostrar_matriz(m3)


""""
implementar funcao que retorne a 
matriz transposta de uma matriz m 
recebida como parametro


Atividade: Implementar um programa que
apresente na tela um menu de opções que,
além das opções Inserir, Remover e Imprimir,
tenha 5 funcionalidades para manipular uma 
lista de itens (dicionários) do tema escolhido.
Escolham funcionalidades que sejam uteis e que
busquem exercitar python

"""
