casa = int(input("Digite aqui o valor do imóvel: "))
salario = int(input("Digite aqui seu salario mensal: "))
tempo = int(input("Digite em quantos anos você pretende quitar a dívida: "))
mes = tempo*12
parcela = float(casa/mes)
if parcela <= salario * 0.3:
    print("Parabéns, seu financiamento foi aprovado!")
else:
    print("Infelizmente não podemos liberar o financiamento.")