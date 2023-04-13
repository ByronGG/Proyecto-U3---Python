import statistics

def complemento_normativo(valores):
    # Calcular la media y la desviación estándar
    media = statistics.mean(valores)
    desv_est = statistics.stdev(valores)
    
    # Calcular los valores complementarios normativos
    valores_normativos = [2 * media - x for x in valores]
    valores_comp_norm = [(x - media) / desv_est for x in valores_normativos]
    
    # Redondear los valores a dos decimales
    valores_comp_norm = [round(x, 2) for x in valores_comp_norm]
    return valores_comp_norm