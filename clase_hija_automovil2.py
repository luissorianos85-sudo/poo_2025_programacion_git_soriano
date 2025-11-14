# Archivo: Automovil.py
# Importar la superclase y la clase de composición

from super_clase_vehiculo2 import Vehiculo
from motor3 import Motor

class Automovil(Vehiculo):
    """
    Clase Hija 1: Hereda de Vehiculo y utiliza Composición con Motor.
    """
    def __init__(self, marca: str, modelo: str, anio: int, puertas: int, motor: Motor):
        # 1. Herencia: Llamada al constructor de la superclase
        super().__init__(marca, modelo, anio)

        # 2. Atributo adicional
        self._numero_puertas = puertas

        # 3. Composición: El Automovil 'tiene un' Motor
        self._motor = motor

        # Atributo de estado para un método de comportamiento
        self._maletero_abierto = False

    # --- Encapsulamiento (@property y @setter) para puertas ---
    @property
    def puertas(self):
        """Getter para el número de puertas."""
        return self._numero_puertas

    @puertas.setter
    def puertas(self, nuevo_numero):
        """Setter para el número de puertas."""
        if isinstance(nuevo_numero, int) and nuevo_numero >= 2:
            self._numero_puertas = nuevo_numero
        else:
            print("Error: El número de puertas debe ser un entero >= 2.")

    # --- Métodos de Comportamiento ---
    def abrir_maletero(self):
        """Simula abrir el maletero."""
        if not self._maletero_abierto:
            self._maletero_abierto = True
            return f"{self._modelo}: ¡Maletero abierto!"
        return f"{self._modelo}: El maletero ya estaba abierto."

    def tocar_claxon(self):
        """Simula tocar el claxon (comportamiento adicional)."""
        return f"{self._modelo}: ¡PIII PIII PIIIII! (Claxon sonando)"

    # --- Sobrescritura de str() ---
    def __str__(self):
        """Muestra la información completa (usando super() e información de composición)."""
        info_vehiculo = super().__str__()
        info_motor = self._motor.__str__() # Llama a str() de la clase Motor

        return (f"{info_vehiculo}\n"
                f"Tipo de Vehículo: Automóvil\n"
                f"Puertas: {self._numero_puertas}\n"
                f"{info_motor}\n"
                f"--------------------------------")


# --- PRUEBA DEL ARCHIVO Automovil.py ---

# 1. Necesitas instanciar la clase Motor primero, ya que Automovil depende de ella.
motor_deportivo = Motor(tipo="Gasolina Turbo", potencia=350)
print("Motor instanciado con éxito.")

    # 2. Crear una instancia de Automovil
    # Automovil(marca: str, modelo: str, anio: int, puertas: int, motor: Motor)
automovil1 = Automovil(
        marca="Toyota",
        modelo="Corolla GR",
        anio=2024,
        puertas=4,
        motor=motor_deportivo )
print("Automóvil instanciado con éxito.")
print("--------------------------------")

    # 3. Mostrar la información completa usando __str__
print("### Información Completa del Automóvil 1 ###")
print(automovil1)

    # 4. Probar Métodos de Comportamiento de la Superclase (Vehiculo)
print("###  Comportamiento de Vehiculo ###")
print(automovil1.encender())
print(automovil1.encender())  # Intentar encenderlo de nuevo

    # 5. Probar Métodos de Comportamiento de la Clase Propia (Automovil)
print("### Comportamiento de Automovil ###")
print(automovil1.tocar_claxon())
print(automovil1.abrir_maletero())
print(automovil1.abrir_maletero())  # Intentar abrirlo de nuevo

    # 6. Probar Setter con validación
print("### Prueba de Setter de Puertas ###")
automovil1.puertas = 5  # Valor válido
print(f"Número de puertas actualizado a: {automovil1.puertas}")
automovil1.puertas = 1  # Valor inválido (debe ser >= 2)
    # Output: Error: El número de puertas debe ser un entero >= 2