print("Bem vindo ao programa que transforma numeros em nossa base decimal para binario, octal e hexadeciaml!")
n = int(input("Digite aqui um número: "))
escolha =  int(input("Você quer converter para binário [1], octal [2] ou hexadecimal [3]? "))
if escolha == 1:
    alteracao = bin(n)
    print(f"Seu número {n}, em base binária é {alteracao[2:]}.")
elif escolha == 2:
    alteracao = oct(n)
    print(f"Seu número {n}, em base octal é {alteracao[2:]}.")
elif escolha == 3:
    alteracao = hex(n)
    print(f"Seu número {n}, em base hexadecimal é {alteracao[2:]}.")
else:
    print("Você inseriu uma escolha inválida!")
print("Programa encerrado. Obrigado!")