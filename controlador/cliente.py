from bd import select_all, select_one, execute
from modelo.cliente import Cliente
import controlador.usuario as usuario_ctrl

def crear_cliente(nombre, apellido, direccion, telefono, correo, password):
    if not usuario_ctrl.crear_usuario(nombre, correo, password, "cliente"):
        return False

    usuario = usuario_ctrl.buscar_usuario_por_correo(correo)
    if not usuario: return False

    sql = "INSERT INTO cliente (id_usuario, apellido, direccion, telefono) VALUES (:1, :2, :3, :4)"
    return execute(sql, (usuario.id_usuario, apellido, direccion, telefono))

def buscar_cliente_por_usuario(id_usuario):
    sql = """
        SELECT c.id_cliente, u.nombre, c.apellido, c.direccion, c.telefono, u.correo
        FROM cliente c
        JOIN usuario u ON c.id_usuario = u.id_usuario
        WHERE u.id_usuario = :1
    """
    r = select_one(sql, (id_usuario,))
    if not r: return None
    
    id_c, nombre, apellido, dire, tel, mail = r
    return Cliente(nombre, apellido, dire, tel, mail, None, id_cliente=id_c, id_usuario=id_usuario)

def actualizar_datos_cliente(id_usuario, nueva_direccion, nuevo_telefono):
    sql = "UPDATE cliente SET direccion = :1, telefono = :2 WHERE id_usuario = :3"
    return execute(sql, (nueva_direccion, nuevo_telefono, id_usuario))