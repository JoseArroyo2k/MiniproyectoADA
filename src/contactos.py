# src/contactos.py

import csv

class Contacto:
    def __init__(self, nombre, apellido, telefono, email, direccion):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.email = email
        self.direccion = direccion

    def __str__(self):
        return f"{self.nombre} {self.apellido} - Teléfono: {self.telefono}, Email: {self.email}, Dirección: {self.direccion}"

class GestorContactos:
    def __init__(self):
        self.lista_contactos = []

    def agregar_contacto(self, contacto):
        self.lista_contactos.append(contacto)

    def editar_contacto(self, id_contacto, nuevo_contacto):
        if id_contacto < len(self.lista_contactos):
            self.lista_contactos[id_contacto] = nuevo_contacto
        else:
            print("El ID de contacto proporcionado no es válido.")

    def eliminar_contacto(self, id_contacto):
        if id_contacto < len(self.lista_contactos):
            del self.lista_contactos[id_contacto]
        else:
            print("El ID de contacto proporcionado no es válido.")

    def obtener_contactos(self):
        return self.lista_contactos

    def exportar_csv(self, nombre_archivo):
        with open(nombre_archivo, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(["Nombre", "Apellido", "Teléfono", "Email", "Dirección"])
            for contacto in self.lista_contactos:
                csv_writer.writerow([contacto.nombre, contacto.apellido, contacto.telefono, contacto.email, contacto.direccion])

    def exportar_vcard(self, nombre_archivo):
        with open(nombre_archivo, 'w') as f:
            for contacto in self.lista_contactos:
                f.write("BEGIN:VCARD\n")
                f.write(f"N:{contacto.apellido};{contacto.nombre}\n")
                f.write(f"TEL;TYPE=CELL:{contacto.telefono}\n")
                f.write(f"EMAIL:{contacto.email}\n")
                f.write(f"ADR;TYPE=HOME:{contacto.direccion}\n")
                f.write("END:VCARD\n")

# Ejemplo de uso
if __name__ == "__main__":
    gestor = GestorContactos()
    nuevo_contacto = Contacto("Juan", "Pérez", "123456789", "juan@example.com", "Calle Principal 123")
    gestor.agregar_contacto(nuevo_contacto)
    for contacto in gestor.obtener_contactos():
        print(contacto)
