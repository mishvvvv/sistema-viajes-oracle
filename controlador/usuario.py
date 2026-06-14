from bd import select_all, select_one, execute, hash_password
from modelo.usuario import Usuario

def crear_usuario(nombre, correo, clave_plana, rol):
    pass_hash = hash_password(clave_plana)
    sql = "INSERT INTO usuario (nombre, correo, password, rol) VALUES (:1, :2, :3, :4)"
    return execute(sql, (nombre, correo, pass_hash, rol))

def listar_usuarios():
    sql = "SELECT id_usuario, nombre, correo, rol FROM usuario ORDER BY id_usuario"
    rows = select_all(sql)
    lista = []
    for r in rows:
        id_u, nombre, correo, rol = r
        lista.append(Usuario(nombre, correo, None, rol=rol, id_usuario=id_u))
    return lista

def buscar_usuario_por_correo(correo):
    sql = "SELECT id_usuario, nombre, correo, rol FROM usuario WHERE correo = :1"
    r = select_one(sql, (correo,))
    if not r: return None
    id_u, nombre, correo, rol = r
    return Usuario(nombre, correo, None, rol=rol, id_usuario=id_u)

def buscar_usuario_por_id(id_usuario):
    sql = "SELECT id_usuario, nombre, correo, rol FROM usuario WHERE id_usuario = :1"
    r = select_one(sql, (id_usuario,))
    if not r: return None
    id_u, nombre, correo, rol = r
    return Usuario(nombre, correo, None, rol=rol, id_usuario=id_u)

def validar_login(correo, clave_plana):
    pass_hash = hash_password(clave_plana)
    sql = "SELECT id_usuario, nombre, correo, rol FROM usuario WHERE correo = :1 AND password = :2"
    r = select_one(sql, (correo, pass_hash))
    if not r: return None
    id_u, nombre, correo, rol = r
    return Usuario(nombre, correo, None, rol, id_usuario=id_u)