# Archivo: clase_principal_prueba.py (o main.py)

# ESTOS IMPORTS DEBEN COINCIDIR CON TUS NOMBRES DE ARCHIVOS:
# Si usas 'clase_hija_automovil.py', el import debe ser 'from clase_hija_automovil import Automovil'
from motor3 import Motor
from clase_hija_automovil2 import Automovil
from clase_hija_motocicleta2 import Motocicleta

def ejecutar_programa():
    """
    Función principal para crear objetos, asignar motores, ejecutar métodos y mostrar información.
    """
    print("=============================================")
    print("  ACTIVIDAD ASINCRÓNICA: POO con Vehículos")
    print("=============================================")

    # --- 1. Crear Objetos de Composición (Motores) ---
    motor1 = Motor(tipo="Gasolina", potencia=150)
    motor2 = Motor(tipo="Eléctrico", potencia=100)
    motor3 = Motor(tipo="Gasolina 2T", potencia=45)
    motor4 = Motor(tipo="Gasolina 4T", potencia=60)

    print("\n--- Motores Creados ---")
    print(motor1)
    print(motor3)
    print("-----------------------")

    # --- 2. Crear Automóviles (Herencia + Composición) ---
    auto1 = Automovil(marca="Toyota", modelo="Corolla", anio=2022, puertas=4, motor=motor1)
    auto2 = Automovil(marca="Tesla", modelo="Model 3", anio=2024, puertas=4, motor=motor2)

    # --- 3. Crear Motocicletas (Herencia + Composición) ---
    moto1 = Motocicleta(marca="Yamaha", modelo="YZF-R3", anio=2023, cilindraje=321, motor=motor3)
    moto2 = Motocicleta(marca="Harley", modelo="Iron 883", anio=2021, cilindraje=883, motor=motor4)

    print("\n--- 4. Mostrar Objetos con print() (Llama a __str__()) ---")
    print("\n*** Automóvil 1 (Toyota Corolla) ***")
    print(auto1)

    print("\n*** Motocicleta 2 (Harley Davidson) ***")
    print(moto2)

    # --- 5. Ejecutar Métodos de Comportamiento ---

    print("\n--- 5.1 Pruebas de Comportamiento (Automóvil) ---")
    print(auto1.encender()) # Método heredado de Vehiculo
    print(auto1._motor.encender_motor()) # Método del objeto Motor (Composición)
    print(auto1.tocar_claxon()) # Método propio de Automovil
    print(auto1.abrir_maletero()) # Método propio de Automovil


    print("\n--- 5.2 Pruebas de Comportamiento (Motocicleta) ---")
    print(moto1.usar_patada_arranque()) # Método propio de Motocicleta
    print(moto1.encender()) # Ya estaba encendido por la patada (Motor)
    print(moto1.hacer_caballito()) # Método propio de Motocicleta
    print(moto1.apagar()) # Método heredado de Vehiculo

    print("\n--- 6. Demostración de Encapsulamiento (@setter) ---")
    print(f"Modelo original de auto2: {auto2.modelo}")
    auto2.modelo = "Model Y" # Usando el setter
    print(f"Modelo actualizado de auto2: {auto2.modelo}")

    print("\n--- Fin de la Demostración ---")

# Verificar si el archivo se ejecuta directamente
if __name__ == "__main__":
    ejecutar_programa()
