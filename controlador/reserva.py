from bd import select_all, select_one, execute
from modelo.reserva import Reserva
from controlador.usuario import buscar_usuario_por_id
from controlador.paqueteturistico import buscar_paquete

def crear_reserva(monto_final, cant_adultos, cant_ninos, id_cliente, id_paquete):
    sql = """
        INSERT INTO reserva (fecha_reserva, estado, monto_final, cant_adultos, cant_ninos, id_cliente, id_paquete)
        VALUES (SYSDATE, 'Confirmada', :1, :2, :3, :4, :5)
    """
    return execute(sql, (monto_final, cant_adultos, cant_ninos, id_cliente, id_paquete))

def listar_reservas():
    sql = """
        SELECT id_reserva, TO_CHAR(fecha_reserva, 'DD-MM-YYYY'), estado, monto_final, id_cliente, id_paquete
        FROM reserva ORDER BY id_reserva
    """
    rows = select_all(sql)
    lista = []
    for r in rows:
        id_r, fecha, estado, monto, id_c, id_p = r
        cliente = buscar_usuario_por_id(id_c)
        paquete = buscar_paquete(id_p)
        lista.append(Reserva(fecha, estado, monto, cliente, paquete, id_reserva=id_r))
    return lista

def cancelar_reserva(id_reserva):
    sql = "UPDATE reserva SET estado = :1 WHERE id_reserva = :2"
    return execute(sql, ("Cancelada", id_reserva))