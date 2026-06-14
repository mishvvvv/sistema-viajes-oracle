from modelo.usuario import Usuario

class Administrador(Usuario):
    def __init__(self, nombre, correo, password, cargo, id_admin=None, id_usuario=None):
        super().__init__(nombre, correo, password, "admin", id_usuario)
        self.id_admin = id_admin
        self.cargo = cargo

    def __str__(self):
        return f"Administrador {self.nombre} - {self.cargo}"
