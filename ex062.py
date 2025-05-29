print("BEM VINDO AO PROGRAMA DE PROGRESSAO ARITMETICA!!!")
n = int(input("Insira aqui o primeiro termo da progressao: "))
r = int(input("Agora insira a razão dessa PA: "))
contador = 1
termo_mostrado = 10

while contador <= 10:
    a = n + (contador - 1) * r
    print(a)
    contador += 1
print("Esses são os primeiros 10 termos dessa PA.")
decisao = int(input("Mais quantos termos você quer ver? Digite 0 para encerrar o programa"))
while decisao > 0:
    while contador <= termo_mostrado + decisao:
        a = n + (contador - 1) * r
        print(a)
        contador += 1
    termo_mostrado += decisao
    decisao = int(input("Mais quantos termos você quer ver? Digite 0 para encerrar o programa"))

print("PROGRAMA ENCERRADO!")