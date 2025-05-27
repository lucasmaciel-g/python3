from time import sleep
from statistics import fmean
print("Bem vindo ao analisador de notas!")
nota1 = float(input("Digite aqui sua primeira nota: "))
nota2 = float(input("Digite aqui sua segunda nota: "))
print("ANALISANDO...")
sleep(2)
media = fmean([nota1,nota2])
if media < 5.0:
    print(f"REPROVADO. Uma pena que sua média tenha sido apenas {media}, continue estudando.")
elif 5.0 <= media <= 6.9:
    print(f"RECUPERAÇAO. Você poderá ter uma nova chance com outra prova para aumentar sua nova que foi apenas {media}.")
elif media >= 7:
    print(f"APROVADO. Parabéns, seu esforço foi recompensado! Continue assim!")