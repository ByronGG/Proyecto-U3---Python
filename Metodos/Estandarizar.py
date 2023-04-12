import statistics

def estandarizar(valores):
    # Calcular la media y la desviación estándar
    media = statistics.mean(valores)
    desv_est = statistics.stdev(valores)
    
    # Estandarizar los datos
    valores_est = [(x - media) / desv_est for x in valores]
    return valores_est
