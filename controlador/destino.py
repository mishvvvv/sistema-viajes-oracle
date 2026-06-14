from bd import select_all, select_one, execute
from modelo.destino import Destino

def crear_destino(nombre, descripcion, actividades, costo_adulto, costo_nino):
    sql = """
        INSERT INTO destino (nombre, descripcion, actividades, costo_adulto, costo_nino)
        VALUES (:1, :2, :3, :4, :5)
    """
    return execute(sql, (nombre, descripcion, actividades, costo_adulto, costo_nino))

def listar_destinos():
    sql = "SELECT id_destino, nombre, descripcion, actividades, costo_adulto, costo_nino FROM destino ORDER BY id_destino"
    rows = select_all(sql)
    lista = []
    for r in rows:
        id_d, nom, desc, act, ca, cn = r
        lista.append(Destino(nom, desc, act, ca, cn, id_destino=id_d))
    return lista

def buscar_destino(id_destino):
    sql = "SELECT id_destino, nombre, descripcion, actividades, costo_adulto, costo_nino FROM destino WHERE id_destino = :1"
    r = select_one(sql, (id_destino,))
    if not r: return None
    id_d, nom, desc, act, ca, cn = r
    return Destino(nom, desc, act, ca, cn, id_destino=id_d)

def buscar_destino_por_nombre(nombre_busqueda):
    sql = """
        SELECT id_destino, nombre, descripcion, actividades, costo_adulto, costo_nino 
        FROM destino 
        WHERE LOWER(nombre) LIKE LOWER(:1)
    """
    param = f"%{nombre_busqueda}%"
    rows = select_all(sql, (param,))
    lista = []
    for r in rows:
        id_d, nom, desc, act, ca, cn = r
        lista.append(Destino(nom, desc, act, ca, cn, id_destino=id_d))
    return lista

def actualizar_destino(id_destino, nombre, descripcion, actividades, costo_adulto, costo_nino):
    sql = """
        UPDATE destino
        SET nombre = :1, descripcion = :2, actividades = :3, costo_adulto = :4, costo_nino = :5
        WHERE id_destino = :6
    """
    return execute(sql, (nombre, descripcion, actividades, costo_adulto, costo_nino, id_destino))

def eliminar_destino(id_destino):
    sql = "DELETE FROM destino WHERE id_destino = :1"
    return execute(sql, (id_destino,))