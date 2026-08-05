def funzione_obiettivo(x):
    # Esempio: f(x) = x^3 - x - 2
    return x**3 - x - 2

def metodo_bisezione(a, b, tolleranza=1e-5, max_iter=100):
    if funzione_obiettivo(a) * funzione_obiettivo(b) >= 0:
        return "Il metodo della bisezione fallisce: f(a) e f(b) devono avere segno opposto."
    
    c = a
    for i in range(max_iter):
        c = (a + b) / 2
        if abs(funzione_obiettivo(c)) < tolleranza:
            return f"Trovata radice approssimata: {c} dopo {i+1} iterazioni"
        
        if funzione_obiettivo(c) * funzione_obiettivo(a) < 0:
            b = c
        else:
            a = c
            
    return f"Raggiunto limite iterazioni. Valore approssimato: {c}"

# Esempio d'uso
print(metodo_bisezione(1, 2))
