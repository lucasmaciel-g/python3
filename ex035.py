n1 = int(input("Digite o valor de uma reta, em cm: "))
n2 = int(input("Digite outro valor: "))
n3 = int(input("Digite o último valor: "))
if n1 + n2 <= n3:
    print("De acordo com a geometria euclidiana, não podemos formar um triângulo com essas retas.")
else:
    if n2 + n3 <= n1:
        print("De acordo com a geometria euclidiana, não podemos formar um triângulo com essas retas.")
    else:
        if n1 + n3 <= n2:
            print("De acordo com a geometria euclidiana, não podemos formar um triângulo com essas retas.")
        else:
            print("As retas podem formar um triâgulo já que a soma de quaisquer duas delas não será igual ou inferior a terceira.")