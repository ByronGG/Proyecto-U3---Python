def normalizar(valores):
    # Normalizar los datos
    min_val = min(valores)
    max_val = max(valores)
    valores_norm = [(x - min_val) / (max_val - min_val) for x in valores]
    valores_norm = [round(x, 3) for x in valores_norm]  # Redondear a tres decimales
    return valores_norm
