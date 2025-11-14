# Archivo: Vehiculo.py

class Vehiculo:
    """
    Superclase: Define la estructura base de un vehículo.
    Implementa encapsulamiento con @property y @setter y métodos de comportamiento.
    """
    def __init__(self, marca: str, modelo: str, anio: int):
        # Atributos privados
        self._marca = marca
        self._modelo = modelo
        self._anio = anio
        self._encendido = False # Estado interno para comportamiento

    # --- Encapsulamiento (@property y @setter) para marca ---
    @property
    def marca(self):
        """Getter para la marca."""
        return self._marca

    @marca.setter
    def marca(self, nueva_marca):
        """Setter para la marca."""
        if isinstance(nueva_marca, str) and nueva_marca:
            self._marca = nueva_marca
        else:
            print("Error: La marca debe ser una cadena no vacía.")

    # --- Encapsulamiento (@property y @setter) para modelo ---
    @property
    def modelo(self):
        """Getter para el modelo."""
        return self._modelo

    @modelo.setter
    def modelo(self, nuevo_modelo):
        """Setter para el modelo."""
        if isinstance(nuevo_modelo, str) and nuevo_modelo:
            self._modelo = nuevo_modelo
        else:
            print("Error: El modelo debe ser una cadena no vacía.")

    # --- Encapsulamiento (@property y @setter) para anio ---
    @property
    def anio(self):
        """Getter para el año."""
        return self._anio

    @anio.setter
    def anio(self, nuevo_anio):
        """Setter para el año. Asegura que sea un número positivo."""
        if isinstance(nuevo_anio, int) and nuevo_anio > 1900:
            self._anio = nuevo_anio
        else:
            print("Error: El año debe ser un número entero positivo (ej: > 1900).")

    # --- Métodos de Comportamiento ---
    def encender(self):
        """Simula el encendido del vehículo."""
        if not self._encendido:
            self._encendido = True
            return f"{self._marca} {self._modelo}: ¡Vehículo encendido, listo para rodar!"
        return f"{self._marca} {self._modelo}: Ya estaba encendido."

    def apagar(self):
        """Simula el apagado del vehículo."""
        if self._encendido:
            self._encendido = False
            return f"{self._marca} {self._modelo}: Vehículo apagado."
        return f"{self._marca} {self._modelo}: Ya estaba apagado."

    # --- Sobrescritura de str() ---
    def __str__(self):
        """Muestra la información básica del vehículo."""
        estado = "Encendido" if self._encendido else "Apagado"
        return (f"--- Información del Vehículo ---\n"
                f"Marca: {self._marca}, Modelo: {self._modelo}, Año: {self._anio}\n"
                f"Estado: {estado}")

# Creación de vehiculo1
#vehiculo1 = Vehiculo(marca="mercedes", modelo="Vehiculo1", anio=1989)
#print(vehiculo1.encender())
#print(vehiculo1.marca, vehiculo1.modelo, vehiculo1.anio)

# Creación de vehiculo2
#vehiculo2 = Vehiculo(marca="mercedes", modelo="Vehiculo2", anio=1989) # Cambié el modelo para distinguirlo
#print(vehiculo2.apagar())
#print(vehiculo2.marca, vehiculo2.modelo, vehiculo2.anio)
#print(vehiculo2.encender())

