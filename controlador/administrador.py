from bd import select_all, select_one, execute
from modelo.administrador import Administrador
import controlador.destino as destino_ctrl
import controlador.paqueteturistico as paquete_ctrl
import controlador.reserva as reserva_ctrl
import controlador.usuario as usuario_ctrl

def crear_administrador(nombre, correo, password, cargo):
    if not usuario_ctrl.crear_usuario(nombre, correo, password, "admin"):
        return False
        
    usuario = usuario_ctrl.buscar_usuario_por_correo(correo)
    if not usuario: return False
    
    sql = "INSERT INTO administrador (id_usuario, cargo) VALUES (:1, :2)"
    return execute(sql, (usuario.id_usuario, cargo))

def listar_administradores():
    sql = """
        SELECT u.id_usuario, u.nombre, u.correo, a.id_admin, a.cargo
        FROM usuario u
        JOIN administrador a ON a.id_usuario = u.id_usuario
        ORDER BY a.id_admin
    """
    rows = select_all(sql)
    lista = []
    for r in rows:
        id_u, nombre, correo, id_admin, cargo = r
        lista.append(Administrador(nombre, correo, None, cargo, id_admin=id_admin, id_usuario=id_u))
    return lista

def buscar_administrador_por_id(id_admin):
    sql = """
        SELECT u.id_usuario, u.nombre, u.correo, a.id_admin, a.cargo
        FROM usuario u
        JOIN administrador a ON a.id_usuario = u.id_usuario
        WHERE a.id_admin = :1
    """
    r = select_one(sql, (id_admin,))
    if not r:
        return None
    id_u, nombre, correo, id_admin, cargo = r
    return Administrador(nombre, correo, None, cargo, id_admin=id_admin, id_usuario=id_u)

def eliminar_administrador(id_admin):
    sql_get = "SELECT id_usuario FROM administrador WHERE id_admin = :1"
    r = select_one(sql_get, (id_admin,))
    if not r:
        return False
    (id_usuario,) = r
    sql = "DELETE FROM administrador WHERE id_admin = :1"
    return execute(sql, (id_admin,))

def crear_paquete_admin(nombre, fecha_inicio, fecha_fin, precio_total):
    return paquete_ctrl.crear_paquete(nombre, fecha_inicio, fecha_fin, precio_total)

def actualizar_paquete_admin(id_paquete, nombre=None, fecha_inicio=None, fecha_fin=None, precio_total=None):
    sets = []
    params = []
    if nombre is not None:
        sets.append("nombre = :{}".format(len(params)+1))
        params.append(nombre)
    if fecha_inicio is not None:
        sets.append("fecha_inicio = TO_DATE(:{},'DD-MM-YYYY')".format(len(params)+1))
        params.append(fecha_inicio)
    if fecha_fin is not None:
        sets.append("fecha_fin = TO_DATE(:{},'DD-MM-YYYY')".format(len(params)+1))
        params.append(fecha_fin)
    if precio_total is not None:
        sets.append("precio_total = :{}".format(len(params)+1))
        params.append(precio_total)
    
    if not sets:
        return False
        
    sql = f"UPDATE paquete_turistico SET {', '.join(sets)} WHERE id_paquete = :{len(params)+1}"
    params.append(id_paquete)
    return execute(sql, tuple(params))

def eliminar_paquete_admin(id_paquete):
    sql_rel = "DELETE FROM paquete_destino WHERE id_paquete = :1"
    execute(sql_rel, (id_paquete,))
    sql = "DELETE FROM paquete_turistico WHERE id_paquete = :1"
    return execute(sql, (id_paquete,))

def crear_destino_admin(nombre, descripcion, actividades, costo_adulto, costo_nino):
    return destino_ctrl.crear_destino(nombre, descripcion, actividades, costo_adulto, costo_nino)

def actualizar_destino_admin(id_destino, nombre, descripcion, actividades, costo_adulto, costo_nino):
    return destino_ctrl.actualizar_destino(id_destino, nombre, descripcion, actividades, costo_adulto, costo_nino)

def eliminar_destino_admin(id_destino):
    return destino_ctrl.eliminar_destino(id_destino)

def calcular_ingresos_confirmados():
    sql = "SELECT NVL(SUM(monto_final),0) FROM reserva WHERE estado = :1"
    r = select_one(sql, ("Confirmada",))
    if not r:
        return 0
    (total,) = r
    return float(total)

def listar_reservas_por_estado(estado):
    todas = reserva_ctrl.listar_reservas()
    return [r for r in todas if r.estado == estado]

def listar_reservas_por_paquete(id_paquete):
    sql = """
        SELECT id_reserva,
               TO_CHAR(fecha_reserva,'DD-MM-YYYY'),
               estado, monto_final,
               id_cliente, id_paquete
        FROM reserva
        WHERE id_paquete = :1
        ORDER BY id_reserva
    """
    rows = select_all(sql, (id_paquete,))
    lista = []
    for r in rows:
        id_r, fecha, estado, monto, id_c, id_p = r
        obj = reserva_ctrl.buscar_reserva(id_r)
        if obj:
            lista.append(obj)
    return lista