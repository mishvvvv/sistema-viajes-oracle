from datetime import datetime

class PaqueteTuristico:
    def __init__(self, nombre, fecha_inicio, fecha_fin, precio_total, id_paquete=None):
        self.id_paquete = id_paquete
        self.nombre = nombre
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.precio_total = float(precio_total)
        self.destinos = []

    def agregar_destino(self, destino):
        self.destinos.append(destino)

    def obtener_duracion(self):
        try:
            ini = datetime.strptime(self.fecha_inicio, "%d-%m-%Y")
            fin = datetime.strptime(self.fecha_fin, "%d-%m-%Y")
            return (fin - ini).days
        except:
            return 0

    def ver_paquetes(self):
        return f"{self.nombre} ({self.fecha_inicio} - {self.fecha_fin})"

    def __str__(self):
        return f"{self.nombre} ({self.fecha_inicio} - {self.fecha_fin})"