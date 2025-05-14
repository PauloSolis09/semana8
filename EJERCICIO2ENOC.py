# Simulación de pila de panes en una panadería

# Lista para representar la pila de panes
pila_panes = []

def agregar_pan(tipo_pan):
    pila_panes.append(tipo_pan)

def vender_pan():
    if pila_panes:
        return pila_panes.pop()
    else:
        return "No hay panes para vender."

def ver_pan_listo():
    if pila_panes:
        return pila_panes[-1]
    else:
        return "No hay panes en la bandeja."

# Ejemplo de uso
agregar_pan("Baguette")
agregar_pan("Bolillo")
agregar_pan("Concha")

print("Pan listo para vender:", ver_pan_listo())

print("Se vendió un pan:", vender_pan())
print("Pan listo para vender:", ver_pan_listo())
