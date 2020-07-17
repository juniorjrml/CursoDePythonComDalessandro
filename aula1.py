exercicio = [3]
############# inicio so exercicio 1 ##################
print("*"*20,"inicio do exercicio 1","*"*20)
if(1 in exercicio):
    numeros = []
    qntNumeros = 2
    for i in range(qntNumeros):
        try:
            auxiliar = float(input("digite um numero "))
            numeros.append(auxiliar)
        except:
            print("Erro na leitura do numero")
            numero = []
            break
    i = 0
    j = 1
    try:
        if numeros[i]>=numeros[j]:
            print("primeiro é maior ou igual que o segundo")
    except:
        print("Nao foi possivel comparar")
else:
    print("Exercicio nao solicitado!")

print("*"*20,"fim do exercicio 1","*"*20)
############# fim so exercicio 1 ##################



############# inicio so exercicio 2 ##################
print("*"*20,"inicio do exercicio 2","*"*20)
if(2 in exercicio):
    textos = []
    qntNumeros = 3
    for i in range(qntNumeros):
        try:
            auxiliar = input("digite uma string ")
            textos.append(auxiliar)
        except:
            print("Erro na leitura da string" )
            numero = []
            break
    texto = ''
    for i in textos:
        texto += i+" "

    print(texto)
else:
    print("Exercicio nao solicitado!")

print("*"*20,"fim do exercicio 2","*"*20)
############# fim so exercicio 2 ##################




############# inicio so exercicio 3 ##################
print("*"*20,"inicio do exercicio 3","*"*20)
if(3 in exercicio):
    numero = int(input("digite um numero: "))
    divisores = []
    for i in range(1,numero):
        if((numero%i)==0):
            divisores.append(i)

    print(divisores)



    print("-"*10,"usando while ")
    numeros = list(range(1,numero))
    print(type(numeros))
    divisores = []
    while numeros:
        auxiliarInteiro = numeros.pop()
        if((numero%auxiliarInteiro)==0):
            divisores.append(auxiliarInteiro)

    print(divisores)
else:
    print("Exercicio nao solicitado!")

print("*"*20,"fim do exercicio 3","*"*20)
############# fim so exercicio 3 ##################