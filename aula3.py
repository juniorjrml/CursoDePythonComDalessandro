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
        "1. Inserir um Elemento x na lista",
        "2. Remover um Elemento x da lista",
        "3. Imprimir a lista",
        "4. Contar o numero de ocorrencias de um elemento x",
        "5. Imprimir os elementos inteiros da lista",
        "6. Sair"
    ]

    acoes_do_menu = [
        lambda lista: adicionar_elementos(lista, quantidade=1),
        # caso queira adicionar mais de um elemento por vez basta
        # remover a função lambda e deixar apenas adicionar_elementos
        remove_elemento,
        lambda lista: [print(i) for i in lista],
        contar_elemento,
        lambda lista: mostrar_elementos_do_tipo(lista, int),
        lambda: print("Saindo...")]
    escolha_do_menu = [1, 2, 3, 4, 5, 6]

    menu = [textos_do_menu, escolha_do_menu, acoes_do_menu]
    lista = []
    while True:
        try:
            for i in menu[0]:
                print(i)
            opcao = int(coletar_numero())
            try:
                menu[2][menu[1].index(opcao)](lista)  # So 1 funcao não recebe a lista como parametro(1parametro apenas)
            except:
                try:
                    menu[2][menu[1].index(opcao)]()  # Saindo do looping(nao recebe parametroo)
                    break
                except:
                    print("Algo deu Errado :(")  # Se for passado um numero fora do alcance da lista !
                    raise
            print("\n\n")
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
