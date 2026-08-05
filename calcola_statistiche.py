def calcola_statistiche(dati):
    if not dati:
        return "Lista vuota"
    
    n = len(dati)
    media = sum(dati) / n
    
    dati_ordinati = sorted(dati)
    if n % 2 == 1:
        mediana = dati_ordinati[n // 2]
    else:
        mediana = (dati_ordinati[n // 2 - 1] + dati_ordinati[n // 2]) / 2
        
    varianza = sum((x - media) ** 2 for x in dati) / n
    deviazione_standard = varianza ** 0.5
    
    return {
        "Conteggio": n,
        "Media": media,
        "Mediana": mediana,
        "Minimo": dati_ordinati[0],
        "Massimo": dati_ordinati[-1],
        "Deviazione Standard": round(deviazione_standard, 4)
    }

# Esempio d'uso
numeri = [12, 45, 67, 23, 89, 34, 56, 12, 90]
print(calcola_statistiche(numeri))
