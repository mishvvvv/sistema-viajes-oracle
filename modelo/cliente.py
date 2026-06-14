from modelo.usuario import Usuario

class Cliente(Usuario):
    def __init__(self, nombre, apellido, direccion, telefono, correo, password, 
                 id_cliente=None, id_usuario=None):
        super().__init__(nombre, correo, password, "cliente", id_usuario)
        self.id_cliente = id_cliente
        self.apellido = apellido
        self.direccion = direccion
        self.telefono = telefono

    def actualizar_datos(self, nueva_direccion=None, nuevo_telefono=None):
        if nueva_direccion:
            self.direccion = nueva_direccion
        if nuevo_telefono:
            self.telefono = nuevo_telefono

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
