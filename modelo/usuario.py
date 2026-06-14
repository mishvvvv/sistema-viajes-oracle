class Usuario:
    def __init__(self, nombre, correo, password, rol, id_usuario=None):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.correo = correo
        self.password = password
        self.rol = rol

    def __str__(self):
        return f"{self.nombre} ({self.rol})"
