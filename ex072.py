tupla = ["zero", "um", "dois","tres","quatro","cinco","seis","sete","oito","nove","dez","onze","doze","treze","quartorze","quinze","dezesseis","dezessete","dezoito","dezenove","vinte"]
n = int(input("Digite um valor de 0 a 20: "))
while n < 0 or n > 20:
    n = int(input("Insira um valor dentro do limite de 0 a 20: "))
print(tupla[n])