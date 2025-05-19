print("PRIMEIRA SERIE: ")
series = {
    "nome": "the originais",
    "diretor": "Julie Plec",
    "ano de lançamento": 2013,
    "genero": "drama",
}
for chave, valor in series.items():
    print(f"{chave}:{valor}")

print(".")
print(".")
print(".")

print("SEGUNDA SERIE: ")
series1 = {
    "nome": "the VAMPIRES DIARES",
    "diretor": "Kevin Williamson e Julie Plec",
    "ano de lançamento": 2009,
    "genero": "drama",
}
for chave, valor in series1.items():
    print(f"{chave}:{valor}")
    
print(".")
print(".")
print(".")

print("TERCEIRA SERIE: ")
series2 = {
    "nome": "legacies",
    "diretor": "Jeffrey G. Hunt",
    "ano de lançamento": 2018,
    "genero": "drama",
}
for chave, valor in series2.items():
    print(f"{chave}:{valor}")
    
print(".")
print(".")
print(".")

#exibir dicionarios
lista_series = [series, series1, series2]

    #escolhendo os campos
for series in lista_series:
    print(f"{series['nome']}")

print(".")
print(".")
print(".")

    #exibendo todos
for series in lista_series:
    for chave, valor in series.items():
        print(f"{chave} - {valor}")
    print()