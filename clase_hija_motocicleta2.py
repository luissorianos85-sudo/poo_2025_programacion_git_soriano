# Archivo: Motocicleta.py

# Importar la superclase y la clase de composición
from super_clase_vehiculo2 import Vehiculo
from motor3 import Motor

class Motocicleta(Vehiculo):
    """
    Clase Hija 2: Hereda de Vehiculo y utiliza Composición con Motor.
    """
    def __init__(self, marca: str, modelo: str, anio: int, cilindraje: int, motor: Motor):
        # 1. Herencia: Llamada al constructor de la superclase
        super().__init__(marca, modelo, anio)

        # 2. Atributo adicional
        self._cilindraje = cilindraje # Cilindraje en cc

        # 3. Composición: La Motocicleta 'tiene un' Motor
        self._motor = motor

    # --- Encapsulamiento (@property y @setter) para cilindraje ---
    @property
    def cilindraje(self):
        """Getter para el cilindraje."""
        return self._cilindraje

    @cilindraje.setter
    def cilindraje(self, nuevo_cilindraje):
        """Setter para el cilindraje."""
        if isinstance(nuevo_cilindraje, int) and nuevo_cilindraje > 50:
            self._cilindraje = nuevo_cilindraje
        else:
            print("Error: El cilindraje debe ser un entero mayor a 50cc.")

    # --- Métodos de Comportamiento ---
    def hacer_caballito(self):
        """Simula la acción de hacer un caballito."""
        if self._encendido:
            return f"{self._modelo} ({self._cilindraje}cc): ¡vamos chica! Levantando la rueda delantera (Caballito)."
        return f"{self._modelo}: Necesita encenderse para hacer un caballito."

    def usar_patada_arranque(self):
        """Simula el uso de la patada de arranque (kick-start)."""
        if not self._encendido:
            return f"{self._modelo}: Usando patada de arranque... ¡Motor en marcha!"
        return f"{self._modelo}: El motor ya está encendido, no necesita patada."

    # --- Sobrescritura de str() ---
    def __str__(self):
        """Muestra la información completa (usando super() e información de composición)."""
        info_vehiculo = super().__str__()
        info_motor = self._motor.__str__() # Llama a str() de la clase Motor

        return (f"{info_vehiculo}\n"
                f"Tipo de Vehículo: Motocicleta\n"
                f"Cilindraje: {self._cilindraje} cc\n"
                f"{info_motor}\n"
                f"--------------------------------")


# --- PRUEBA DEL ARCHIVO Motocicleta.py ---

    # Creamos un objeto Motor
#motor_moto = Motor(tipo="Gasolina 4T", potencia=45)
#print("Motor instanciado con éxito.")

    # 2. Crear una instancia de Motocicleta
    # Motocicleta(marca, modelo, anio, cilindraje, motor)
#moto1 = Motocicleta(
    #marca="Kawasaki",
    #modelo="Ninja 400",
    #anio=2024,
    #cilindraje=399,
    #motor=motor_moto  # Pasamos el objeto Motor
    #)
#print("Motocicleta instanciada con éxito.")
#print("--------------------------------")

    # 3. Mostrar la información completa usando __str__
#print("### Información Completa de la Motocicleta 1 ###")
#print(moto1)

    # 4. Probar Métodos de Comportamiento de la Superclase (Vehiculo)
#print("### Comportamiento Heredado (Vehiculo) ###")
    # El método 'encender()' de la superclase actualiza self._encendido
#print(moto1.encender())

    # 5. Probar Métodos de Comportamiento Propios (Motocicleta)
#print("### Comportamiento Propio ###")
    # Probar un método que requiere que esté encendido
#print(moto1.hacer_caballito())
    # Probar un método que requiere que esté apagado (debe mostrar el mensaje de que ya está encendido)
#print(moto1.usar_patada_arranque())

    # 6. Detener el motor (llama al método de la Superclase)
#print("### Detener y Re-probar ###")
#print(moto1.apagar())
    # Ahora que está apagado, la patada debe funcionar
#print(moto1.usar_patada_arranque())

    # 7. Probar Setter con validación
#print("### Prueba de Setter de Cilindraje ###")
#moto1.cilindraje = 650  # Valor válido
#print(f"Cilindraje actualizado a: {moto1.cilindraje} cc")
#moto1.cilindraje = 40  # Valor inválido (debe ser > 50cc)
    # Output: Error: El cilindraje debe ser un entero mayor a 50cc.
