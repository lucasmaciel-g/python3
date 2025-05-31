palavras = ("amor", "peixe", "python", 
            "sotreq", "lucas", "celular")

# Esse primeiro for analisa cada elemento dentro da tupla 'palavras' e aloca ela na variavel 'p' e roda o que esta dentro

for p in palavras:
    print(f"\nDentro da palavra {p} temos ", end="")

# O segundo for esta alocando cada letra dentro da variavel p e fazendo o que esta aninhado.

    for vogal in p:

# O grande macete aqui é usar o if com in. Aqui estamos verificando se dentro da variavel 'vogal' temos alguma palavra que esta dentro do aeiou.

        if vogal.lower() in "aeiou":
            print(f"{vogal}", end=" ")