class Reserva:
    def __init__(self, fecha_reserva, estado, monto_final, cliente_obj, paquete_obj, id_reserva=None):
        self.id_reserva = id_reserva
        self.fecha_reserva = fecha_reserva
        self.estado = estado
        self.monto_final = float(monto_final)
        self.cliente = cliente_obj
        self.paquete = paquete_obj

    def cambiar_estado(self, nuevo_estado):
        self.estado = nuevo_estado

    def generar_comprobante(self):
        return f"Reserva #{self.id_reserva} - {self.cliente.nombre} - {self.paquete.nombre}"

    def __str__(self):
        return f"Reserva #{self.id_reserva} | Estado: {self.estado}"
