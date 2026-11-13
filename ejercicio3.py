#::::: BEE FIGHT ::::::
abejas = int(input("Ingrese el no. de abejas : "))
avispas = int(input("Ingrese el no. de avispas : "))
abejas = abejas*2
avispas = avispas*3
if abejas > avispas :
    print (f"Ganan las abejas ({abejas} vs {avispas})")
elif abejas < avispas :
    print (f"Ganan las avispas ({avispas} vs {abejas})")
else : 
    print (f"[!] Empate ({avispas} vs {abejas})")