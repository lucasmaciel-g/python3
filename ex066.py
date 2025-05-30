c = s = 0
while True:
    n = int(input("Insira um valor ou 999 para encerrar: "))
    if n == 999:
        break
    c += 1
    s += n
print(f"Voce inseriu {c} numero e a soma deles foi {s}.")