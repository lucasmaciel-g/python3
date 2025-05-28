from random import randint
print("="*33)
print("BEM VINDO AO PROGRAMA DE JOKENPO!")
print("="*33)
usuario = int(input("[1] PEDRA\n" \
"[2] PAPEL\n" \
"[3] TESOURA\n" \
"Digite sua escolha: "))
computador = randint(1, 3)
if usuario == 1 or usuario == 2 or usuario == 3:
    if usuario == computador:
        print(f"Ambos escolheram {usuario}. EMPATE!")
    else:
        if usuario == 1 and 2<= computador <= 3:
            print(f"VOCE PERDEU. O computador escolheu {computador} e você escolheu {usuario}.")
        elif usuario == 2 and computador == 1:
            print(f"VOCE GANHOU. O computador escolheu {computador} e você escolheu {usuario}.")
        elif usuario == 2 and computador == 3:
            print(f"VOCE PERDEU. O computador escolheu {computador} e você escolheu {usuario}.")
        elif usuario == 3:
            print(f"VOCE GANHOU. O computador escolheu {computador} e você escolheu {usuario}.")
else:
    print("Você inseriu uma opção inválida.")
print("PROGRAMA ENCERRADO.")
