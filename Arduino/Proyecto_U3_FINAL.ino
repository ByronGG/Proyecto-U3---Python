int potPin = A0; // pin analógico del potenciómetro
int val; // variable para almacenar el valor leído del potenciómetro
int valores[30]; // arreglo para almacenar los 30 valores
int ultimaLectura = 29; // índice de la última lectura

void setup() {
  Serial.begin(9600); // iniciar la comunicación serial
}

void loop() {
  for (int i = 0; i < 30; i++) { // leer 30 valores del potenciómetro
    val = analogRead(potPin); // leer el valor del potenciómetro
    valores[i] = map(val, 0, 1023, 0, 100); // mapear el valor leído a un rango de 0 a 255
    Serial.print(valores[i]); // enviar el valor al puerto serial
    if (i != ultimaLectura) { // si no es la última lectura, enviar una coma
      Serial.print(",");
    }
    delay(100); // esperar 100ms antes de leer el siguiente valor
  }
  Serial.println(); // terminar la línea de valores
  delay(1000); // esperar 1 segundo antes de empezar de nuevo
}
