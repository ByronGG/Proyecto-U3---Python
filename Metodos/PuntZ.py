import statistics

def puntuacion_z(valores):
    # Calcular la media y la desviación estándar
    media = statistics.mean(valores)
    desv_est = statistics.stdev(valores)

    # Calcular las puntuaciones Z de cada valor
    puntuaciones_z = [(x - media) / desv_est for x in valores]
    return [round(p, 2) for p in puntuaciones_z]
