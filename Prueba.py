import serial
import statistics

# Configurar la conexión serial con Arduino
arduino = serial.Serial('COM3', 9600, timeout=1)

# Leer 30 valores del potenciómetro desde Arduino
valores = []
while len(valores) < 30:
    lectura = arduino.readline().decode().strip()
    if lectura:
        valores = list(map(int, lectura.strip().rstrip(',').split(',')))

print("Valores recibidos:", valores)

# Calcular la moda, media, mediana, mayor y menor
moda = statistics.mode(valores)
media = statistics.mean(valores)
mediana = statistics.median(valores)
mayor = max(valores)
menor = min(valores)

# Imprimir los resultados
print("Moda: ", moda)
print("Media: ", media)
print("Mediana: ", mediana)
print("Mayor: ", mayor)
print("Menor: ", menor)

# Cerrar la conexión serial con Arduino
arduino.close()
