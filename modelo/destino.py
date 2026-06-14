class Destino:
    def __init__(self, nombre, descripcion, actividades, costo_adulto, costo_nino, id_destino=None):
        self.id_destino = id_destino
        self.nombre = nombre
        self.descripcion = descripcion
        self.actividades = actividades
        self.costo_adulto = float(costo_adulto)
        self.costo_nino = float(costo_nino)

    def ver_info(self):
        return f"{self.nombre} | Adulto: ${self.costo_adulto} | Niño: ${self.costo_nino}"