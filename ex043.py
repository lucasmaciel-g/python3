print("Bem vindo ao programa que calcula o IMC. Vou te pedir algumas informações para calcular o seu.")
peso = float(input("Digite aqui seu peso, em kg: "))
altura = float(input("Agora insira sua altura, em m: "))
imc = peso / pow(altura, 2)
if imc < 18.5:
    print(f"Você está abaixo do seu peso, seu imc={imc:.2f}kg/m2.")
elif 18.5 <= imc <= 25:
    print(f"Que ótimo, você está no peso ideal, seu imc={imc:.2f}kg/m2.")
elif 25 < imc <= 30:
    print(f"Tome cuidado! Seu peso está acima do indicado, seu imc={imc:.2f}kg/m2.")
elif 30 < imc <= 40:
    print(f"Procure se cuidar, você já esta com obesidade, seu imc={imc:.2f}kg/m2.")
elif imc > 40:
    print(f"Você precisa ir ao médico, seu quadro é de obesidade mórbida, seu imc={imc:.2f}kg/m2.")