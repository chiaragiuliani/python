import math

def risolvi_equazione_secondo_grado(a, b, c):
    """Calcola le radici reali o complesse di ax^2 + bx + c = 0"""
    if a == 0:
        return "Non è un'equazione di secondo grado."
    
    delta = b**2 - 4*a*c
    print(f"Delta calculated: {delta}")
    
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return f"Due soluzioni reali distinte: x1 = {x1}, x2 = {x2}"
    elif delta == 0:
        x = -b / (2*a)
        return f"Una soluzione reale doppia: x = {x}"
    else:
        parte_reale = -b / (2*a)
        parte_immaginaria = math.sqrt(-delta) / (2*a)
        return f"Soluzioni complesse: {parte_reale} ± {parte_immaginaria}i"

