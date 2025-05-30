i = 0
n = int(input("insira um numero para ver a tabuada: "))
while True:
    if n < 0 or i == 10:
        break
    for i in range(1, 11):
        total = n * i
        print(f"{n} x {i:2} = {total:2}")
print("=" * 18)
print("TABUADA ENCERRADA!")