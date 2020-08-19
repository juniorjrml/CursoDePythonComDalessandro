from aula1 import coletar_numero

exercicio = ["2_1"]


# -------------------- inicio do exercicio 1 --------------------
def fatorial(x):
    if x < 0:
        raise Exception("Fatorial de numero negativo")
    elif x == 0:
        return 1
    else:
        return x * fatorial(x - 1)


if "2_1" in exercicio:
    print("*" * 20, "inicio do exercicio 1", "*" * 20)

    print("Exercício: implemente uma função que receba um valor x e retorne seu")
    print("fatorial.\n\n")

    a = coletar_numero()
    b = fatorial(a)
    print("O fatorial de", a, "e:", b)

    print("*" * 20, "fim do exercicio 1", "*" * 20)
# -------------------- fim do exercicio 1 --------------------

# -------------------- inicio do exercicio 2 --------------------
"""
defs fora do condicional para poder ser importado
"""


def converter_para_tipo_do_elemento(x):
    try:
        return int(x)
    except ValueError:
        try:
            return float(x)
        except ValueError:
            return x


def adicionar_elementos(lista, quantidade=None):
    try:
        numero_auxiliar = int(quantidade)
    except:
        numero_auxiliar = int(input("Digite a quantidade de elementos a ser digitado: "))
    for i in range(numero_auxiliar):
        auxiliar_elemento = input("Insira um elemento: ")
        lista.append(converter_para_tipo_do_elemento(auxiliar_elemento))


def mostrar_elementos_do_tipo(lista, tipo):
    for i in lista:
        if type(i) == tipo:
            print(i)


if "2_2" in exercicio:
    print("*" * 20, "inicio do exercicio 2", "*" * 20)

    print("Exercício: faça um programa que leia uma lista de objetos(inteiro,")
    print("floats e strings), imprima o número de elementos que são do tipo")
    print("‘float’ e imprima na tela a lista lida.\n\n")

    elementos = []
    adicionar_elementos(elementos)
    mostrar_elementos_do_tipo(elementos, float)

    print("*"*20, "fim do exercicio 2", "*"*20)

# -------------------- fim do exercicio 2 --------------------
