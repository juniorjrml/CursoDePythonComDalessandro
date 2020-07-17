#2 exercicio para casa
exercicio = [3]
############# inicio do exercicio 1 ##################
if(1 in exercicio):
    print("*" * 20, "inicio do exercicio 1", "*" * 20)
    valor_p_remover = 1
    l1 = [2, 1, 3, 4, 1, 5, 6, 1, 7]
    l1.reverse()
    l1.remove(valor_p_remover)
    l1.reverse()
    print(l1)
    print("*"*20,"fim do exercicio 1","*"*20)
############# fim do exercicio 1 ##################

############# inicio do exercicio 2 ##################
if(2 in exercicio):
    print("*" * 20, "inicio do exercicio 2", "*" * 20)
    def funcao_parametros_infinito(*parametros):
        return [i[1] for i in enumerate(parametros)]
    print(funcao_parametros_infinito(1,2,3,"olamundo"))
    print("*"*20,"fim do exercicio 2","*"*20)
############# fim do exercicio 2 ##################

