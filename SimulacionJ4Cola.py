from collections import deque

class Proceso:
    def __init__(self, pid, nombre, duracion):
        self.pid = pid
        self.nombre = nombre
        self.duracion = duracion

    def __str__(self):
        return f"ID: {self.pid} | {self.nombre} ({self.duracion} ms)"

class SimuladorMicroprocesador:
    def __init__(self):
        self.cola = deque()
        self.proceso_actual = None

    def agregar_proceso(self, proceso):
        self.cola.append(proceso)
        self._programar_siguiente()

    def _programar_siguiente(self):
        if self.proceso_actual is None and self.cola:
            self.proceso_actual = self.cola.popleft()

    def obtener_actual(self):
        return self.proceso_actual

    def obtener_pendientes(self):
        return list(self.cola)

    def completar_actual(self):
        self.proceso_actual = None
        self._programar_siguiente()

def main():
    simulador = SimuladorMicroprocesador()
    contador_pid = 1

    while True:
        print("\n--- Sistema de Gestión de Procesos ---")
        print("1. Agregar nuevo proceso")
        print("2. Mostrar proceso en ejecución")
        print("3. Mostrar procesos pendientes")
        print("4. Finalizar proceso actual")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre del proceso: ")
            duracion = int(input("Duración estimada (ms): "))
            proceso = Proceso(contador_pid, nombre, duracion)
            contador_pid += 1
            simulador.agregar_proceso(proceso)
            print(f"Proceso '{nombre}' agregado a la cola.")
            pausa()

        elif opcion == "2":
            actual = simulador.obtener_actual()
            if actual:
                print(f"\nProceso en ejecución: {actual}")
            else:
                print("\nNo hay procesos en ejecución")
            pausa()

        elif opcion == "3":
            pendientes = simulador.obtener_pendientes()
            if pendientes:
                print("\nProcesos pendientes:")
                for proceso in pendientes:
                    print(f" - {proceso}")
            else:
                print("\nNo hay procesos pendientes")
            pausa()

        elif opcion == "4":
            if simulador.obtener_actual():
                simulador.completar_actual()
                print("\nProceso actual finalizado")
                nuevo = simulador.obtener_actual()
                if nuevo:
                    print(f"Nuevo proceso en ejecución: {nuevo}")
            else:
                print("\nNo hay proceso en ejecución")
            pausa()

        elif opcion == "0":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")
            pausa()
            
def pausa():
    input("\nPresione Enter para continuar\n")
    

if __name__ == "__main__":
    main()