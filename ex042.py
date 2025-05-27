n1 = int(input("Digite o valor de uma reta, em cm: "))
n2 = int(input("Digite outro valor: "))
n3 = int(input("Digite o último valor: "))
if n1 + n2 <= n3 or n1 + n3 <= n2 or n3 + n2 <= n1:
    print("De acordo com a geometria euclidiana não podemos formar um triângulo com essas retas.")
else:
    if n1 == n2 == n3:
        print(f"Como todas as retas possuem o mesmo valor de {n1}cm, o triângulo formado é EQUILATERO.")
    elif n1 != n2 != n3:
        print(f"Nessa caso temos retas diferentes: {n1}cm, {n2}cm, {n3}cm. Dessa forma, nosso trângulo é ESCALENO.")
    else:
        print("Nesse caso, dois dos valores inseridos são iguais e somente um se difere. Portanto, temos um trângulo ISOCELES.")


#if n1 + n2 <= n3:
#    print("De acordo com a geometria euclidiana, não podemos formar um triângulo com essas retas.")
#else:
#    if n2 + n3 <= n1:
#        print("De acordo com a geometria euclidiana, não podemos formar um triângulo com essas retas.")
#    else:
#        if n1 + n3 <= n2:
#            print("De acordo com a geometria euclidiana, não podemos formar um triângulo com essas retas.")
#        else:
#            print("As retas podem formar um triâgulo já que a soma de quaisquer duas delas não será igual ou inferior a terceira.")