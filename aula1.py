exercicio = ["1_3"]


def coletar_numero():
    try:
        return float(input("digite um numero "))
    except ValueError:
        print("Erro na leitura do numero(digite apenas numeros)")


# -------------------- inicio so exercicio 1 --------------------
if "1_1" in exercicio:
    print("*" * 20, "inicio do exercicio 1", "*" * 20)
    print("1. Ler dois números reais e informa se o primeiro é maior, menor ou")
    print("igual ao segundo:\n\n")

    numeros = []
    qnt_numeros = 2
    for i in range(qnt_numeros):
        auxiliar = coletar_numero()
        numeros.append(auxiliar)

    try:
        if numeros[0] > numeros[1]:
            print("O primeiro numero digitado({}) é maior que o segundo numero digitado({})".format(numeros[0],
                                                                                                    numeros[1]))
        elif numeros[0] == numeros[1]:
            print(
                "O primeiro numero digitado({}) é igual ao segundo numero digitado({})".format(numeros[0], numeros[1]))
        else:
            print("O primeiro numero digitado({}) é menor que o segundo numero digitado({})".format(numeros[0],
                                                                                                    numeros[1]))
    except:
        print("Nao foi possivel comparar :( \n tente novamente!")

    print("*" * 20, "fim do exercicio 1", "*" * 20)
# -------------------- fim so exercicio 1 --------------------


# -------------------- inicio so exercicio 2 --------------------

if "1_2" in exercicio:
    print("*" * 20, "inicio do exercicio 2", "*" * 20)

    print("2. Leia três strings e construa uma quarta string que representa a")
    print("concatenação das três strings anteriores, separadas por espaço.")
    print("Imprima a string construída.")

    textos = []
    qnt_palavras = 3
    for i in range(qnt_palavras):
        try:
            auxiliar = input("digite uma string ")
            textos.append(auxiliar)
        except:
            print("Erro na leitura da string")
            textos = []
            break
    texto = ''
    for i in textos:
        texto += i + " "

    print(texto)
    print("*" * 20, "fim do exercicio 2", "*" * 20)
# -------------------- fim so exercicio 2 --------------------

# -------------------- inicio so exercicio 3 --------------------

if "1_3" in exercicio:
    print("*" * 20, "inicio do exercicio 3", "*" * 20)
    print("3. Leia um número inteiro x e imprima todos os seus divisores.")
    print("a. Use 'while'")
    print("b. Use 'for'\n\n")

    numero = int(coletar_numero())
    print("Usando while\n")
    divisores = []
    for i in range(1, numero):
        if (numero % i) == 0:
            divisores.append(i)

    print(divisores)

    print("Usando while\n")
    numeros = list(range(1, numero))
    divisores = []
    while numeros:
        auxiliarInteiro = numeros.pop()
        if (numero % auxiliarInteiro) == 0:
            divisores.append(auxiliarInteiro)

    print(divisores)
    print("*" * 20, "fim do exercicio 3", "*" * 20)
# -------------------- fim so exercicio 3 --------------------
