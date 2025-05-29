menu = 0
n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))
while menu != 5:
    print("""OPÇOES
                 [1] Soma
                 [2] Multiplicação
                 [3] Maior
                 [4] Digitar novos números
                 [5] Sair do programa :""")
    menu = int(input("Insira sua escolha: "))
    if menu == 1:
        operador = n1 + n2
        print(f"{n1} + {n2} = {operador}")
    elif menu == 2:
        operador = n1 * n2
        print(f"{n1} x {n2} = {operador}")
    elif menu == 3:
        if n1 > n2:
            print(f"O maior número é {n1}.")
        elif n1 < n2:
            print(f"O maior número é {n2}.")
        else:
            print("Os dois números são iguais.")
    elif menu == 4:
        n1 = int(input("Digite o primeiro valor: "))
        n2 = int(input("Digite o segundo valor: "))
    elif menu == 5:
        print("PROGRAMA ENCERRADO.")
    else:
        print("Opção inválida!")