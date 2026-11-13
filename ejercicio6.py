#:::: Propina :::::
cuenta = float(input())
porcentajeP = int(input())
propina = cuenta * (porcentajeP / 100)

print(f"Propina: ${propina:.3f}")
print(f"Total a pagar: ${propina + cuenta:.3f}")