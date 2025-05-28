print("Vamos criar uma tabuada completa de 1 a 10!")
n = int(input("Insira um número: "))
for i in range(1, 11):
    r = n * i
    print(f"{n} x {i:2} = {r:2}\n")