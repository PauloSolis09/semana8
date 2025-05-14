# Definición de la clase ColaClinica
class ColaClinica:
    def __init__(self):
        self.cola = []

    def registrar_paciente(self, nombre):
        """Agrega un paciente al final de la cola."""
        self.cola.append(nombre)
        print(f"Paciente '{nombre}' ha sido registrado en la cola.")

    def atender_paciente(self):
        """Atiende al primer paciente en la cola."""
        if self.cola:
            paciente = self.cola.pop(0)
            print(f"Atendiendo al paciente: {paciente}")
        else:
            print("No hay pacientes en espera.")

    def mostrar_pacientes(self):
        """Muestra la lista actual de pacientes en espera."""
        if self.cola:
            print("Pacientes en espera:")
            for idx, paciente in enumerate(self.cola, start=1):
                print(f"{idx}. {paciente}")
        else:
            print("No hay pacientes en espera.")

# Ejemplo de uso
if __name__ == "__main__":
    clinica = ColaClinica()
    clinica.registrar_paciente("Ana")
    clinica.registrar_paciente("Luis")
    clinica.registrar_paciente("María")
    clinica.mostrar_pacientes()
    clinica.atender_paciente()
    clinica.mostrar_pacientes()