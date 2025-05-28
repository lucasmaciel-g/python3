from datetime import datetime
s = 0
ano_atual = datetime.now().year
print("Insira seu ano de nascimento que te falo se é maior de idade ou não.")
for i in range(0, 7):
    nascimento = int(input("Ano de nascimento: "))
    if ano_atual - nascimento >= 18:
        s += 1
print(f"{s} pessoas são maiores de idade.")