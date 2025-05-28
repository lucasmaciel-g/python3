print("Esse é a calculadora de pagamentos.")
valor = float(input("Digite aqui o valor da compra: "))
pagamento = int(input("Digite \n[1] para pagamento a vista,\n" \
"[2] se for pagar com cartão de crédito a vista,\n" \
"[3] se for parcelar em 2x no cartão de crédito,\n" \
"[4] se for dividir de 3 ou mais vezes no cartão de crédito: "))
if pagamento == 1 or pagamento == 2 or pagamento == 3 or pagamento == 4:
    if pagamento == 1:
        parcela = float(valor * 0.9)
        print(f"Você escolheu pagamento a vista, o valor será R${parcela:.2f}.")
    elif pagamento == 2:
        parcela = float(valor * 0.95)
        print(f"Você vai pagar a vista com cartão de crédito. Sua compra será no valor de R${parcela:.2f}.")
    elif pagamento == 3:
        parcela = float(valor / 2)
        print(f"Já que você vai pagar de 2 vezes no cartão, conseguimos fazer duas parcelas de R${parcela:.2f} sem juros.")
    elif pagamento == 4:
        n = int(input("Em quantas parcelas você quer pagar? "))
        parcela = float((valor * 1.2) / n)
        print(f"Você escolher pagar em {n} parcelas. Como temos juros nessa operação, cada parcela ficará em R${parcela:.2f}.")
else:
    print("Você não inseriu uma opção válida!")
print("Programa encerrado!")
