numero = str(input("Digite um valor de 0 a 9999 para analisar: "))
numerocerto = numero.zfill(4) 
#essa funcao zfill(n) garante que teremos n casas. Nesse caso, teremos 4 casas, caso nao tenha, serao adicionados 0 a esquerda para que seja respeitada a funcao
print(f"Seu numero possui no algoritmo da unidade {numerocerto[-1]}, na dezena {numerocerto[-2]}, na centena {numerocerto[-3]} e no milhar {numerocerto[-4]}.")