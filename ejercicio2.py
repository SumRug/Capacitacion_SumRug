#:::::: PALINDROMO :::::::::

def palindromo(txt):
    txtLimpio = txt.lower().replace(" ", "")
    if not txtLimpio:
        return False
    return txtLimpio == txtLimpio[::-1]


txt = input()

if palindromo(txt):
    print("es un palindromo")
else:
    print("NO es un palindromo")
