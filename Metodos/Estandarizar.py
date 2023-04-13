import statistics

def estandarizar(valores):
    # Calcular la media y la desviación estándar
    media = statistics.mean(valores)
    desv_est = statistics.stdev(valores)

    # Estandarizar los datos y redondear a dos decimales
    valores_est = [round((x - media) / desv_est, 2) for x in valores]
    return valores_est
