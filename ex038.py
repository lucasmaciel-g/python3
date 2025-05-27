from time import sleep
n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))
print("PROCESSANDO...")
sleep(2)
if n1 > n2:
    print(f"O primeiro número, ou seja, {n1} é maior que {n2}, seu segundo número.")
elif n1 < n2:
    print(f"O segundo número inserido, que foi {n2}, é maior que o primeiro, {n1}.")
else:
    print("Não existe maior, os dois são iguais.")
print("Obrigado por usar o programa!")