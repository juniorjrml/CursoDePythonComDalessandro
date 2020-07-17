exercicio = []

############# inicio do exercicio 1 ##################
if(1 in exercicio):
    print("*" * 20, "inicio do exercicio 1", "*" * 20)
    def fat(x):
        if(x<0):
            raise Exception("Fatorial de numero negativo")
        elif(x==0):
            return 1
        else:
            return x*fat(x-1)

    a = int(input("digite um numero "))
    b = fat(a)
    print("O fatorial de",a,"e:",b)
    print("*" * 20, "fim do exercicio 1", "*" * 20)
############# fim do exercicio 1 ##################

############# inicio do exercicio 2 ##################
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
        numeroAuxiliar = int(quantidade)
    except:
        numeroAuxiliar = int(input("Digite a quantidade de elementos a ser digitado: "))
    for i in range(numeroAuxiliar):
        auxiliarElemento = input("Insira um elemento: ")
        lista.append(converter_para_tipo_do_elemento(auxiliarElemento))

def mostrar_elementos_do_tipo(lista, tipo):
    for i in lista:
        if type(i) == tipo:
            print(i)

if(2 in exercicio):
    """

    """
    print("*" * 20, "inicio do exercicio 2", "*" * 20)
    elementos = []
    adicionar_elementos(elementos)
    mostrar_elementos_do_tipo(elementos,float)

    print("*"*20,"fim do exercicio 2","*"*20)
############# fim do exercicio 2 ##################