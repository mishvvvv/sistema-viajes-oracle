from bd import select_all, select_one, execute
from modelo.paqueteturistico import PaqueteTuristico
from controlador.destino import buscar_destino

def crear_paquete(nombre, fecha_inicio, fecha_fin, precio_total):
    sql = """
        INSERT INTO paquete_turistico (nombre, fecha_inicio, fecha_fin, precio_total) 
        VALUES (:1, TO_DATE(:2,'DD-MM-YYYY'), TO_DATE(:3,'DD-MM-YYYY'), :4)
    """
    return execute(sql, (nombre, fecha_inicio, fecha_fin, precio_total))

def crear_paquete_personalizado_cliente(destinos_objs, adultos, ninos):
    total = 0
    nombres_destinos = []
    
    for d in destinos_objs:
        total += (d.costo_adulto * adultos) + (d.costo_nino * ninos)
        nombres_destinos.append(d.nombre)
    
    nombre_paquete = f"Personalizado: {' + '.join(nombres_destinos)}"
    
    sql_insert = """
        INSERT INTO paquete_turistico (nombre, fecha_inicio, fecha_fin, precio_total)
        VALUES (:1, SYSDATE, SYSDATE + 7, :2)
    """
    if execute(sql_insert, (nombre_paquete, total)):
        sql_get_id = "SELECT MAX(id_paquete) FROM paquete_turistico WHERE nombre = :1"
        res = select_one(sql_get_id, (nombre_paquete,))
        if res:
            id_nuevo = res[0]
            for d in destinos_objs:
                agregar_destino_a_paquete(id_nuevo, d.id_destino)
            return id_nuevo, total
    return None, 0

def listar_paquetes():
    sql = """
        SELECT id_paquete, nombre, 
               TO_CHAR(fecha_inicio,'DD-MM-YYYY'), 
               TO_CHAR(fecha_fin,'DD-MM-YYYY'), 
               precio_total
        FROM paquete_turistico ORDER BY id_paquete
    """
    rows = select_all(sql)
    lista = []
    for r in rows:
        id_p, nombre, f_ini, f_fin, precio = r
        paquete = PaqueteTuristico(nombre, f_ini, f_fin, precio, id_paquete=id_p)
        
        sql2 = "SELECT id_destino FROM paquete_destino WHERE id_paquete = :1"
        dest_rows = select_all(sql2, (id_p,))
        for d_id, in dest_rows:
            destino = buscar_destino(d_id)
            if destino: paquete.agregar_destino(destino)
            
        lista.append(paquete)
    return lista

def agregar_destino_a_paquete(id_paquete, id_destino):
    sql = "INSERT INTO paquete_destino (id_paquete, id_destino) VALUES (:1, :2)"
    return execute(sql, (id_paquete, id_destino))

def buscar_paquete(id_paquete):
    sql = """
        SELECT id_paquete, nombre, 
               TO_CHAR(fecha_inicio,'DD-MM-YYYY'), 
               TO_CHAR(fecha_fin,'DD-MM-YYYY'), 
               precio_total
        FROM paquete_turistico WHERE id_paquete = :1
    """
    r = select_one(sql, (id_paquete,))
    if not r: return None
    id_p, nombre, f_ini, f_fin, precio = r
    paquete = PaqueteTuristico(nombre, f_ini, f_fin, precio, id_paquete=id_p)

    sql2 = "SELECT id_destino FROM paquete_destino WHERE id_paquete = :1"
    dest_rows = select_all(sql2, (id_paquete,))
    for d_id, in dest_rows:
        destino = buscar_destino(d_id)
        if destino: paquete.agregar_destino(destino)

    return paquete