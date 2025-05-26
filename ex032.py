from time import sleep
from datetime import date
ano = int(input("Caso queira saber o ano atual digite 0 ou digite o ano que quer testar: "))
print("PROCESSANDO...")
sleep(2)
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f"O ano de {ano} é bissexto.")
else:
    print(f"O ano {ano} não é bissexto.")