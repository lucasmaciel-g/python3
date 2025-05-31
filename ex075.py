# Aqui estou criando uma lista já com as entradas do usuario.

lista = (int(input("Digite um valor: ")),
        int(input("Digite outro valor: ")),
        int(input("Digite mais um valor: ")),
        int(input("Digite o ultimo valor: ")))
print(f"Você digitou os valores: {lista}")

# A contagem do valor 0 é usando o método .count() onde dentro do parentese inserimos o que vai ser contado.

print(f"O valor 9 apareceu {lista.count(9)} vezes.")

# Agora para informar atraves do .index() precisamos testar se o valor existe, atraves da condicional 'if':

if 3 in lista:
    print(f"O valor 3 foi digita na posição {lista.index(3) + 1}.")
else:
    print("O número 3 não aparece na sua lista")

# No caso de imprimir os valores pares colocamos uma mensagem primeiro, usamos o end="" para que nao haja a quebra de linha que acontece com \n por padrao ao final do print. Depois colocamos um laço de repetição com uma condicional aninhada que vai verificar quais valores sao pares e vai imprimir. Mais uma vez usamos o end=" " so que com espaço para que um numero nao fique colado no outro.

print("Você digitou os valores pares ", end="")
for n in lista:
    if n % 2 == 0:
        print(n, end=" ")
