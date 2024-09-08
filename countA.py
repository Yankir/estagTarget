def countA(s):
    return s.count('a') + s.count('A')

# entrada
string = "Banana, Abacaxi, Acerola"
result = countA(string)

print(f"Quantidade de As em \"{string}\": {result}")
