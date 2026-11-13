#::::: Contador de Vocales ::::::
txt = input()
contador = 0
for letra in txt:
    letra = letra.lower()
    if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
        contador += 1

print(contador)