n = int(input("Insira um numero: "))
if n % 2 == 0 or n % 3 == 0:
    print(f"O numero {n} NAO E PRIMO.")
else:
    print(f"O numero {n} é PRIMO.")