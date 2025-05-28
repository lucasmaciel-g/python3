print("BEM VINDO AO PROGRAMA DE PROGRESSAO ARITMETICA!!!")
n = int(input("Insira aqui o primeiro termo da progressao: "))
r = int(input("Agora insira a razão dessa PA: "))
for i in range(1, 11):
    a = n + (i - 1) * r
    print(a)
