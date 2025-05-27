print("A Confederação Nacional de Natação precisa categorizar os atletas, inclusive você.")
idade = int(input("Insira sua idade: "))
if idade <= 9:
    print(f"De acordo com nossa categorização, por você ter {idade} anos, é considerado MIRIM")
elif 9 < idade <= 14:
    print(f"Você já é considerado INFANTIL com a idade de {idade}.")
elif 14 < idade <= 19:
    print(f"Agora que tem {idade} anos, consideramos que você é JUNIOR.")
elif 19 < idade <= 25:
    print(f"Estamos diante de um SENIOR, já que você tem {idade}.")
elif 25 < idade:
    print(f"Parabéns pela experiência na natação. Já com {idade} anos você é considerado um MASTER.")
print("FIM DO PROGRAMA.")