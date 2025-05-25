nome = str(input("Digite seu nome completo para analise completa: "))
print(f"Seu nome completo é {nome.upper()}.")
print(f"Em minúsculo é {nome.lower()}")
print(f"Seu nome e sobrenome possui {len(nome) - nome.count(" ")} letras.")