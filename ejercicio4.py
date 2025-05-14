class PilaTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, tarea):
        """Agrega una nueva tarea a la pila."""
        self.tareas.append(tarea)
        print(f"Tarea agregada: {tarea}")

    def revisar_tarea(self):
        """Revisa (elimina y muestra) la última tarea agregada."""
        if self.esta_vacia():
            print("No hay tareas para revisar.")
            return None
        tarea = self.tareas.pop()
        print(f"Tarea revisada: {tarea}")
        return tarea

    def siguiente_tarea(self):
        """Muestra la próxima tarea a revisar sin eliminarla."""
        if self.esta_vacia():
            print("No hay tareas pendientes.")
            return None
        print(f"Próxima tarea a revisar: {self.tareas[-1]}")
        return self.tareas[-1]

    def esta_vacia(self):
        """Verifica si la pila de tareas está vacía."""
        return len(self.tareas) == 0

    def mostrar_tareas(self):
        """Muestra todas las tareas en la pila."""
        if self.esta_vacia():
            print("No hay tareas en la pila.")
        else:
            print("Tareas en la pila (de la primera entregada a la última):")
            for tarea in self.tareas:
                print(f"- {tarea}")

# Ejemplo de uso
if __name__ == "__main__":
    pila = PilaTareas()
    pila.agregar_tarea("Tarea de Juan")
    pila.agregar_tarea("Tarea de María")
    pila.agregar_tarea("Tarea de Luis")

    pila.siguiente_tarea()  # Muestra la tarea de Luis
    pila.revisar_tarea()    # Revisa la tarea de Luis
    pila.siguiente_tarea()  # Muestra la tarea de María
    pila.mostrar_tareas()   # Muestra las tareas restantes


    #Este sistema refleja la metodología de revisión de tareas en la que la docente siempre atiende primero la última tarea entregada, utilizando la lógica de una pila para gestionar las tareas de manera eficiente.