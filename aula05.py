
"""m = [[1,2,3],[4,5,6],[7,8,9]]
print(m)
m2 = m.copy()
#m2.sort(reverse=True)
[i.sort(reverse=True) for i in m2]
print(m2)"""

"""
def soma1_em_par(lista):
    return list(map(lambda x: x+1 if(x%2==0) else x,lista))
l=[1,2,3]
print(l)
l = soma1_em_par(l)
print(l)"""
"""pessoas = [{"nome": "j1","idade": 11,"sexo": 'm'},{"nome": "j2","idade": 22,"sexo": 'f'}]

campos = ["nome","idade","sexo"]

def inserir_pessoas(base,lista,campos):
    with open(base,"a") as f:
        for pessoa in lista:
            for campo in campos:
                f.write("{} ".format(pessoa[campo]))
            f.write("\n")

def imprimir_mulher_maior_que(base,x,campos):
    with open(base,"r") as f:
        pessoas = f.readlines()
    for p in pessoas:
        aux = p.split()
        if(int(aux[1])>x and aux[2]=="m"):
            for campo in enumerate(campos):
                print("{}: {}".format(campo[1],aux[campo[0]]))

inserir_pessoas("ola.txt",pessoas,campos)
imprimir_mulher_maior_que("ola.txt",1,campos)"""


"""def matriz_transposta(matriz):
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
    print("")"""


"""
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