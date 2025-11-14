# Archivo: Motor.py
class Motor:
    """
    Clase de Composición: Representa el motor de un vehículo.
    Implementa encapsulamiento con @property y @setter.
    """
    def __init__(self, tipo: str, potencia: int):
        # Atributos privados
        # Inicialización usando los setters para aplicar la validación inmediatamente
        self.tipo = tipo
        self.potencia = potencia
        self._encendido = False  # CORRECTO: Inicialización del estado de encendido

    # --- Encapsulamiento (@property y @setter) para tipo ---
    @property
    def tipo(self):
        """Getter para el tipo de motor."""
        return self._tipo

    @tipo.setter
    def tipo(self, nuevo_tipo):
        """Setter para el tipo de motor. Asegura que el valor sea una cadena no vacía."""
        if isinstance(nuevo_tipo, str) and nuevo_tipo.strip():
            self._tipo = nuevo_tipo.strip()
        else:
            print("Error: El tipo de motor debe ser una cadena no vacía.")

    # --- Encapsulamiento (@property y @setter) para potencia ---
    @property
    def potencia(self):
        """Getter para la potencia del motor."""
        return self._potencia

    @potencia.setter
    def potencia(self, nueva_potencia):
        """Setter para la potencia del motor. Asegura que sea un número entero positivo."""
        if isinstance(nueva_potencia, int) and nueva_potencia > 0:
            self._potencia = nueva_potencia
        else:
            print("Error: La potencia debe ser un número entero positivo.")

    # --- Métodos de Comportamiento (Con lógica de estado) ---
    def encender_motor(self):
        """Simula el encendido del motor."""
        if not self._encendido:
            self._encendido = True
            return f"Motor de tipo {self.tipo} con {self.potencia} HP: ¡Encendido!"
        return f"Motor de tipo {self.tipo}: Ya estaba encendido."

    def detener_motor(self):
        """Simula la detención del motor."""
        if self._encendido:
            self._encendido = False
            return f"Motor de tipo {self.tipo} con {self.potencia} HP: Detenido."
        return f"Motor de tipo {self.tipo}: Ya estaba detenido."

    # --- Sobrescritura de str() ---
    def __str__(self):
        """Muestra la información del motor en formato legible, incluyendo el estado."""
        # Indentación corregida y usa el atributo inicializado
        estado = "Encendido" if self._encendido else "Detenido"
        return f"MOTOR: Tipo={self.tipo}, Potencia={self.potencia} HP, Estado={estado}"


# ----------------------------------------------------------------------
# PRUEBAS Y USO DEL MOTOR
# ----------------------------------------------------------------------

#print("### PRUEBA MOTOR 1 (Eléctrico) ###")
#motor1 = Motor(tipo="Eléctrico", potencia=260) # Corregida la 'e' minúscula
#print(f"Tipo y Potencia inicial: {motor1.tipo}, {motor1.potencia} HP")

# Encender
#print(motor1.encender_motor())
# Intentar encender de nuevo (prueba la lógica "Ya estaba encendido")
#print(motor1.encender_motor())

# Detener
#print(motor1.detener_motor())

#print("\n### PRUEBA MOTOR 2 (Gasolina) ###")
#motor2 = Motor(tipo="Gasolina", potencia=140)
#print(f"Tipo y Potencia inicial: {motor2.tipo}, {motor2.potencia} HP")

# Intentar detener sin encender (prueba la lógica "Ya estaba detenido")
#print(motor2.detener_motor())

# Encender
#print(motor2.encender_motor())

# Detener
#print(motor2.detener_motor())