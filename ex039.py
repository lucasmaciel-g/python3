sexo = str(input("Digite M para mulher e H para homem: ")).strip().upper()
if sexo == "M" or sexo == "H":
    if sexo == "M":
        print("Você é mulher, portanto está desobrigada do alistamento obrigatório.")
    else:
        idade = int(input("Insira sua idade: "))
        controle = int(18)
        if idade < 17:
            print(f"Você não precisa se alistar ainda. Faltam {controle - idade} anos para você se alistar.")
        elif 17 <= idade <= 18:
            print(f"Por você ter {idade} anos, precisa se alistar ainda esse ano!")
        else:
            print(f"Você está com {idade} anos, isso significa que já passou do prazo para se alistar. Passaram-se {idade - controle} anos da idade que você deveria ter se alistado.")
else: 
    print("Você não inseriu uma letra válida para identificar seu sexo.")
print("Programa encerrado!")