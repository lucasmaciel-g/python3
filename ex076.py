lista = ("iPhone", 3000,
         "iPad", 5000,
         "MacBook Pro", 10000,
         "AirPods Pro 2", 2000)
print("=" * 40)

# Texto com centralização precisa ser usado o f-string da forma abaixo, colocando em chave o texto, com as aspas abrindo e fechando o texto, mas após fechar as aspas do texto, colocar dois pontos pra informar como será a formatação desse texto. Nesse caso, usamos o ^ para centralização e informamos que devera ocupar 40 espaços.

print(f"{"Lista de produtos Apple":^40}")
print("=" * 40)

# Agora para exibir a lista colocamos um range usando o length para pegamos o tamanho total da lista. Depois, criando uma nova variavel com o for, que no caso foi "item", testamos par ou impar porque sabemos que par é o nome do produto e impar é seu valor

for item in range(0, len(lista)):
    if item % 2 == 0:

#Aqui estou imprimindo, para cada par, o item da tupla, usando o lista[item] porque se nao colocar assim ele imprime so a posicao, nao o item em si. A impressao acontece com 30 espaços, completando com pontos e ficando a esquerda.

        print(f"{lista[item]:.<30}", end="") 
    else:
        print(f"R$ {lista[item]:>8.2f}")