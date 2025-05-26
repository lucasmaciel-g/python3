n1 = int(input("Digite aqui um numero: "))
n2 = int(input("Digite outro: "))
n3 = int(input("Digite mais um: "))
if n1>n2>n3 or n1>n3>n2:
    print(f"O maior número é {n1}.")
else:
    if n2>n1>n3 or n2>n3>n1:
        print(f"O maior  numero é {n2}.")
    else:
        if n3>n1>n2 or n3>n2>n1:
            print(f"O maior numero é {n3}")