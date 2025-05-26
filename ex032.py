ano = int(input("Digite aqui um ano para saber se é bissexto ou não: "))
if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print(f"O ano de {ano} é bissexto.")
        else:
            print("O ano não é bissexto.")
    else:
        print("o ano é bissexto.")
else:
        print("o ano não é bissexto.")