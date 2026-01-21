"""
---------------------------------
Codigo Programación Estructurada
---------------------------------
"""
nombre = input("¿Cual es su nombre?")
direccion = input("¿Cual es su direccion?")
dni = input("¿Cual es su DNI?")
telefono = input("¿Cual es su telefono?")

with open("1-Ejercicio-programacion-Estructurada.txt" , "w") as archivo:
    archivo.write(f"Nombre: {nombre}\n")
    archivo.write(f"Direccion: {direccion}\n")
    archivo.write(f"DNI: {dni}\n")
    archivo.write(f"Telefono: {telefono}\n")

print("Datos guardados Programación Estructurada!!")







"""
---------------------------------
Codigo Programación Procedimental
---------------------------------
"""
def pedir_datos():
    nombre = input("¿Cual es su nombre?")
    direccion = input("¿Cual es su direccion?")
    dni = input("¿Cual es su DNI?")
    telefono = input("¿Cual es su telefono?")
    return nombre, direccion, dni, telefono

def guardar_archivo(nombre, direccion, dni, telefono):
    with open("1-Ejercicio-programacion-Procedimental.txt" , "w") as archivo:
        archivo.write(f"Nombre: {nombre}\n")
        archivo.write(f"Direccion: {direccion}\n")
        archivo.write(f"DNI: {dni}\n")
        archivo.write(f"Telefono: {telefono}\n")

def main():
    nombre, direccion, dni, telefono = pedir_datos()
    guardar_archivo(nombre, direccion, dni, telefono)
    print("Datos guardados Programación Procedimental!!")

main()