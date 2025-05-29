from time import sleep
print("BEM VINDO AO PROGRAMA DE PROGRESSAO ARITMETICA!!!")
n = int(input("Insira aqui o primeiro termo da progressao: "))
r = int(input("Agora insira a razão dessa PA: "))
contador = 1
while contador < 11:
    a = n + (contador - 1) * r
    print(a)
    contador += 1
    sleep(1)
print("PROGRAMA ENCERRADO.")