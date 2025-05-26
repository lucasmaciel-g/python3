print("Bem-vindo ao MULTA 2.0")
carro = int(input("Digite aqui a velocidade que o carro estava, em km/h: "))
if carro <= 80:
    print("Dessa vez ele estava dentro do limite de velocidade da via!")
else:
    excedente = carro - 80
    multa = float(excedente * 7)
    print(f"Já que você achou que era o Dom Toretto, toma essa multa de R${multa:.2f}.")