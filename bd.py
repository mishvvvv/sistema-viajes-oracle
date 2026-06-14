import oracledb
import hashlib

# CAMBIAR ESTA SECCIÓN POR DATOS PROPIOS DE CONEXIÓN A LA BASE DE DATOS

USER = ""        
PASSWORD = ""
DSN = ""   

# FUNCIONES DE CONEXIÓN Y EJECUCIÓN DE CONSULTAS A LA BASE DE DATOS

def obtener_conexion():
    try:
        return oracledb.connect(user=USER, password=PASSWORD, dsn=DSN)
    except Exception as e:
        print(f"\nERROR DE CONEXIÓN] {e}")
        return None

def hash_password(clave: str):
    return hashlib.sha256(clave.encode('utf-8')).hexdigest()

def execute(sql, parametros=()):
    conexion = obtener_conexion()
    if not conexion: return False
    cursor = None
    try:
        cursor = conexion.cursor()
        cursor.execute(sql, parametros)
        conexion.commit()
        return True
    except Exception as e:
        print(f"\nERROR DE SQL {e}")
        return False
    finally:
        if cursor: cursor.close()
        conexion.close()

def select_all(sql, parametros=()):
    conexion = obtener_conexion()
    if not conexion: return []
    cursor = None
    try:
        cursor = conexion.cursor()
        cursor.execute(sql, parametros)
        return cursor.fetchall()
    except Exception as e:
        print(f"\nERROR DE SELECT {e}")
        return []
    finally:
        if cursor: cursor.close()
        conexion.close()

def select_one(sql, parametros=()):
    conexion = obtener_conexion()
    if not conexion: return None
    cursor = None
    try:
        cursor = conexion.cursor()
        cursor.execute(sql, parametros)
        return cursor.fetchone()
    except Exception as e:
        print(f"\nERROR DE SELECT ONE {e}")
        return None
    finally:
        if cursor: cursor.close()
        conexion.close()


