times = [
    "Palmeiras",
    "Flamengo",
    "Cruzeiro",
    "Red Bull Bragantino",
    "Fluminense",
    "Ceará",
    "Bahia",
    "Corinthians",
    "Mirassol",
    "Atlético-MG",
    "Botafogo",
    "Grêmio",
    "São Paulo",
    "Internacional",
    "Fortaleza",
    "Santos",
    "Sport",
    "Vasco da Gama",
    "Vitória",
    "Juventude"
]
print(f"Os 5 primeiros do campeonato são: {times[0:5]}.")
print(f"Os que estao na zona de rebaixamento são: {times[16:]}")
print(f"Em ordem alfabetica temos: {sorted(times)}")
print(f"O saudoso Galo está na posicao {times.index("Atlético-MG") + 1}")