print("Vamos reajustar o salário de alguns funcionários, começando por você!")
salario = float(input("Digite seu salário, em R$: "))
if salario > 1250.00:
    novosalario = salario * 1.1
    print(f"Garanti 10% de aumento. Seu novo salário passou para R${novosalario:.2f}.")
else:
    novosalario = salario * 1.15
    print(f"Parabéns, seu novo salário é de R${novosalario:.2f}.")