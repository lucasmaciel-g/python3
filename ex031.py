distancia = float(input("Digite aqui a distância que você pretende viajar, em km: "))
if distancia <= 200:
    passagem = distancia * 0.50
    print(f"Já que sua viagem será de apenas {distancia}km, então sua passagem custará R${passagem:.2f}")
else:
    passagem = distancia * 0.45
    print(f"Numa viagem de {distancia}km, vou te cobrar R${passagem:.2f}")