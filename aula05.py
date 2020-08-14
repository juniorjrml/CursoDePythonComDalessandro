exercicios = ["xxx"]
"""
m = [[1,2,3],[4,5,6],[7,8,9]]
print(m)
m2 = m.copy()
#m2.sort(reverse=True)
[i.sort(reverse=True) for i in m2]
print(m2)


def soma1_em_par(lista):
    return list(map(lambda x: x+1 if(x%2==0) else x,lista))
l=[1,2,3]
print(l)
l = soma1_em_par(l)
print(l)"""




"""
def matriz_transposta(matriz):
    matriz_auxiliar = []
    for coluna in range(len(matriz[0])):
        nova_linha = []
        for linha in matriz:
            nova_linha.append(linha[coluna])
        matriz_auxiliar.append(nova_linha)
    return matriz_auxiliar


m1 = [[1, 2], [3, 4]]
m2 = [[1, 2], [3, 4], [5, 6]]
m3 = [[1, 2, 7], [3, 4, 8], [5, 6, 9]]
matrizes = [m1, m2, m3]

from aula04 import mostrar_matriz


for matriz in matrizes:
    mostrar_matriz(matriz)
    print("")
    mostrar_matriz(matriz_transposta(matriz))
    print("")


from functools import reduce
import operator


def divisor_de_x(x,numero):
    return True if x%numero == 0 else False


def divisores_de_x(x):
    divisores = list(range(x))
    divisores.remove(0)
    func_auxliar = lambda y: divisor_de_x(x,y)
    return filter(func_auxliar,divisores)

def e_perfeito(x):
    return True if reduce(operator.add,divisores_de_x(x)) == x else False

print(e_perfeito(7))
#qual o recurso para reduzir a quantidade de parametros
"""

# _______________ inicio do exercicio xxx _______________


def inserir_pessoas(base,lista_pessoas,caracteristicas):
    with open(base, "a") as f:
        for pessoa in lista_pessoas:
            for caracteristica in caracteristicas:
                f.write("{} ".format(pessoa[caracteristica]))
            f.write("\n")


def imprimir_mulher_maior_que(base, x, campos):
    with open(base, "r") as f:
        pessoas = f.readlines()
    for p in pessoas:
        caracteristicas = p.split()
        if int(caracteristicas[1]) > x and caracteristicas[2] == "f":
            for campo in enumerate(campos):
                print("{}: {}".format(campo[1],caracteristicas[campo[0]]))
            print("")
def coleta_dados_pessoas(caracteristicas,numero_entradas):
    lista_pessoas = []
    for i in range(numero_entradas):
        pessoa = {}
        for caracteristica in caracteristicas:
            pessoa[caracteristica] = input("Digite o {} ".format(caracteristica))
        lista_pessoas.append(pessoa)
    return lista_pessoas


if "xxx" in exercicios:
    print("Exercicio: implemente um programa que possua duas funcoes:")
    print("(i) inserir conteudos de pessoas (nome, idade, sexo) em um arquivo texto")
    print("(ii) imprimir o nome das mulheres com idade superior a x(dado de entrada)")
    pessoas = [{"nome": "joao", "idade": 11, "sexo": 'm'},
               {"nome": "maria", "idade": 22, "sexo": 'f'}]
    campos = ["nome", "idade", "sexo"]
    #pessoas = coleta_dados_pessoas(campos,3)

    inserir_pessoas("pessoas.txt", pessoas, campos)
    imprimir_mulher_maior_que("pessoas.txt", 4, campos)

# _______________ fim do exercicio xxx _______________
