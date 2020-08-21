from aula2 import adicionar_elementos, mostrar_elementos_do_tipo, converter_para_tipo_do_elemento
from aula1 import coletar_numero
exercicio = ["3_menu"]


# -------------------- inicio do exercicio do menu --------------------
def coletar_elemento():
    return converter_para_tipo_do_elemento(input("Digite um elemento: "))


def contar_elemento(estrutura):
    try:
        elemento = coletar_elemento()
        print(estrutura.count(elemento))
    except:
        print("Nao foi possivel contar!")


def remove_elemento(estrutura):
    try:
        elemento = coletar_elemento()
        estrutura.remove(elemento)
    except:
        print("elemento invalido!")

"""

o objetivo em fazer um menu mais complexo e 
para poder reutilizar com qualquer tipo de 
dado e poder acrescentar qualquer opção (as 
opções de coletas e todo o resto deve ser 
implementada dentro da função que sera 
acionada na opçãço selecionada(dentro da 
variavel acoes_do_menu))

as funcoes devem conter apenas 1 parametro(a 
estrutura) com exceção da função de saida do 
looping

para utilizar basta colocar o texto a ser 
impresso como descrição da opção na 
variavel(lista) textos_do_menu
respectivamente(no mesmo indice) a função 
com as ações desejadas na variavel(lista) 
acoes_do_menu e respectivamente o numero que sera selecionado 
na variavel(lista) escolha_do_menu
ex.:

textos_do_menu[0] = "para adicionar 1 elemento"
acoes_do_menu[0] =  99
escolha_do_menu[0] =  add # função que recebe a estrutura 
                          # e coleta o elemento a ser inserido

"""


if "3_menu" in exercicio:
    print("*" * 20, "inicio do exercicio 1", "*" * 20)
    print("• Exercício para CASA: faça um programa que apresente na tela o")
    print("seguinte menu de opções:")
    print("Inserir um elemento x na lista")
    print("Remover um elemento x da lista")
    print("Imprimir a lista")
    print("Contar o número de ocorrências de um elemento x")
    print("Imprimir os elementos inteiros da lista")
    print("Sair")
    print("Obs.: O menu deve ser apresentado repetidamente até que a opção ‘6’")
    print("seja selecionada.\n\n")

    textos_do_menu = [
        " Inserir um Elemento x na lista",
        " Remover um Elemento x da lista",
        " Imprimir a lista",
        " Contar o numero de ocorrencias de um elemento x",
        " Imprimir os elementos inteiros da lista",
        " Sair"
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
                print("{}.".format(escolha_do_menu[textos_do_menu.index(i)]) + i)
            print("\n\n\n\n")
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

# -------------------- fim do exercicio do menu --------------------


# -------------------- inicio do exercicio 1 --------------------
if "3_extra_1" in exercicio:
    print("*" * 20, "inicio do exercicio 1", "*" * 20)
    print("Remova a ultima ocorrencia de um elemento:\n\n")

    valor_p_remover = 1
    l1 = [2, 1, 3, 4, 1, 5, 6, 1, 7]
    l1.reverse()
    l1.remove(valor_p_remover)
    l1.reverse()
    print(l1)

    print("*"*20, "fim do exercicio 1", "*"*20)
# -------------------- fim do exercicio 1 --------------------


# -------------------- inicio do exercicio 2 --------------------
def funcao_parametros_infinito(*parametros):
    return [i[1] for i in enumerate(parametros)]


if "3_2" in exercicio:
    print("*" * 20, "inicio do exercicio 2", "*" * 20)

    print("Exercício: implemente uma função que receba um número indefinido")
    print("de parâmetros e retorne uma lista com os valores recebidos por")
    print("parâmetro\n\n")

    print(funcao_parametros_infinito(1, 2, 3, "olamundo"))

    print("*"*20, "fim do exercicio 2", "*"*20)
# -------------------- fim do exercicio 2 --------------------
