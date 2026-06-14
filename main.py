"Este archivo es el menú principal del programa, desde aquí se accede a todas las funcionalidades del sistema"
"tanto para clientes como para administradores. Se recomienda ejecutar este archivo desde la terminal para una mejor experiencia de usuario."

import os
import getpass
from controlador.usuario import validar_login
from controlador.cliente import crear_cliente, buscar_cliente_por_usuario, actualizar_datos_cliente
from controlador.administrador import crear_administrador
from controlador.destino import crear_destino, listar_destinos, buscar_destino, buscar_destino_por_nombre, actualizar_destino, eliminar_destino
from controlador.paqueteturistico import crear_paquete, listar_paquetes, agregar_destino_a_paquete, crear_paquete_personalizado_cliente
from controlador.reserva import crear_reserva, listar_reservas, cancelar_reserva

def limpiar():
    os.system('cls' if os.name == 'nt' else 'clear')

def pausar():
    input("\nPresione Enter para continuar...")

def menu_principal():
    while True:
        limpiar()
        print("=== VIAJES AVENTURA ===")
        print("1. Iniciar Sesion")
        print("2. Registrarse")
        print("0. Salir")
        opcion = input("Seleccione: ")

        if opcion == "1":
            login()
        elif opcion == "2":
            registro_cliente()
        elif opcion == "0":
            break

def login():
    correo = input("Correo: ")
    clave = getpass.getpass("Contraseña: ")
    user = validar_login(correo, clave)
    
    if user:
        print(f"\nBienvenido {user.nombre} ({user.rol})")
        pausar()
        if user.rol == "admin":
            menu_admin(user)
        else:
            cliente_obj = buscar_cliente_por_usuario(user.id_usuario)
            if cliente_obj:
                menu_cliente(cliente_obj)
            else:
                print("Error cargando perfil cliente")
    else:
        print("Credenciales inválidas.")
        pausar()

def registro_cliente():
    print("\n--- CREAR CUENTA ---")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    mail = input("Correo: ")
    password = input("Contraseña: ")
    direccion = input("Direccion: ")
    telefono = input("Telefono: ")
    
    if crear_cliente(nombre, apellido, direccion, telefono, mail, password):
        print("Registro exitoso. Ahora puede iniciar sesion.")
    else:
        print("Error al registrar.")
    pausar()

def menu_admin(user):
    while True:
        limpiar()
        print(f"Gestión Administrador - {user.nombre}")
        print("1. Gestionar Destinos")
        print("2. Gestionar Paquetes")
        print("3. Ver Reservas")
        print("4. Crear Nuevo Administrador")
        print("0. Cerrar Sesion")
        opcion = input("Opcion: ")

        if opcion == "1":
            submenu_destinos_admin()
        elif opcion == "2":
            submenu_paquetes_admin()
        elif opcion == "3":
            print("\n--- LISTA DE RESERVAS ---")
            reservas = listar_reservas()
            if not reservas:
                print("No hay reservas registradas.")
            for reserva in reservas: 
                print(reserva.generar_comprobante())
            pausar()
        elif opcion == "4":
            print("\n--- CREAR NUEVO ADMINISTRADOR ---")
            nom = input("Nombre: ")
            mail = input("Correo: ")
            pw = input("Contraseña: ")
            cargo = input("Cargo: ")
            if crear_administrador(nom, mail, pw, cargo):
                print("Administrador creado exitosamente.")
            else:
                print("Error al crear administrador (correo duplicado?).")
            pausar()
        elif opcion == "0": break

def submenu_destinos_admin():
    while True:
        limpiar()
        print("--- GESTION DE DESTINOS ---")
        print("1. Agregar Destino")
        print("2. Mostrar Todos los Destinos")
        print("3. Modificar Destino")
        print("4. Eliminar Destino")
        print("0. Volver")
        sub = input("Opcion: ")
        
        if sub == "1":
            nombre = input("Nombre Destino: ")
            descripcion = input("Descripcion: ")
            actividades = input("Actividades disponibles: ")
            costoa = input("Costo Adulto: ")
            coston = input("Costo Niño: ")
            if crear_destino(nombre, descripcion, actividades, costoa, coston): print("Destino Creado")
            pausar()
        elif sub == "2":
            for d in listar_destinos(): 
                print(f"ID: {d.id_destino} | {d.ver_info()}")
            pausar()
        elif sub == "3":
            id_x = input("ID Destino a modificar: ")
            d_obj = buscar_destino(id_x)
            if d_obj:
                print(f"Editando: {d_obj.nombre}")
                nombre = input(f"Nuevo Nombre ({d_obj.nombre}): ") or d_obj.nombre
                descripcion = input("Nueva Descripción: ") or d_obj.descripcion
                actividades = input("Actividades disponibles: ") or d_obj.actividades
                costoa = input("Nuevo Costo Adulto: ") or d_obj.costo_adulto
                coston = input("Nuevo Costo Niño: ") or d_obj.costo_nino
                if actualizar_destino(id_x, nombre, descripcion, actividades, costoa, coston): print("Actualizado.")
            else:
                print("ID no encontrado")
            pausar()
        elif sub == "4":
            id_x = input("ID Destino a eliminar: ")
            if eliminar_destino(id_x): print("Eliminado correctamente")
            pausar()
        elif sub == "0": break

def submenu_paquetes_admin():
    while True:
        limpiar()
        print("--- GESTION DE PAQUETES ---")
        print("1. Crear Paquete")
        print("2. Asociar Destino a Paquete")
        print("3. Listar Paquetes")
        print("0. Volver")
        sub = input("Opción: ")
        
        if sub == "1":
            nombre = input("Nombre del Paquete: ")
            fechai = input("Fecha de Inicio (DD-MM-YYYY): ")
            fechaf = input("Fecha Final (DD-MM-YYYY): ")
            precio = input("Precio Total: ")
            if crear_paquete(nombre, fechai, fechaf, precio): print("Paquete Creado")
            pausar()
        elif sub == "2":
            for paquete in listar_paquetes(): print(f"{paquete.id_paquete}: {paquete.nombre}")
            id_p = input("ID Paquete: ")
            for destino in listar_destinos(): print(f"{destino.id_destino}: {destino.nombre}")
            id_d = input("ID Destino: ")
            agregar_destino_a_paquete(id_p, id_d)
            print("Asociado correctamente.")
            pausar()
        elif sub == "3":
            for paquete in listar_paquetes():
                print(f"{paquete.ver_paquetes()} - ${paquete.precio_total}")
            pausar()
        elif sub == "0": break

def menu_cliente(cliente):
    while True:
        limpiar()
        print(f"Bienvenido Viajero {cliente.nombre} {cliente.apellido} !!")
        print("1. Buscar Destinos")
        print("2. Ver Todos los Destinos")
        print("3. Ver Paquetes Disponibles")
        print("4. Crear Paquete Personalizado (Máximo 2 Destinos por paquete)")
        print("5. Mis Reservas")
        print("6. Anular Reserva")
        print("7. Modificar Perfil")
        print("0. Salir")
        opcion = input("Opcion: ")

        if opcion == "1":
            nombre = input("Ingrese nombre del destino: ")
            resultados = buscar_destino_por_nombre(nombre)
            if resultados:
                print("\nResultados encontrados:")
                for d in resultados:
                    print(d.ver_info())
            else:
                print("\nups! el destino buscado aún no lo tenemos disponible")
            pausar()
        
        elif opcion == "2":
            print("\n--- DESTINOS DISPONIBLES ---")
            for d in listar_destinos():
                print(d.ver_info())
            pausar()
            
        elif opcion == "3":
            print("\n--- PAQUETES ---")
            paquetes = listar_paquetes()
            for pack in paquetes:
                destinos_str = ", ".join([d.nombre for d in pack.destinos])
                print(f"ID: {pack.id_paquete} | {pack.nombre} | Destinos: {destinos_str} | Precio: ${pack.precio_total}")
            
            res = input("\n¿Desea reservar algún paquete? (S/N): ")
            if res.upper() == "S":
                id_p = input("ID Paquete: ")
                monto = 0
                for pack in paquetes: 
                    if str(pack.id_paquete) == id_p: monto = pack.precio_total
                
                if monto > 0:
                    print("El paquete seleccionado estará disponible por 15 minutos solamente")
                    confirmar = input(f"Confirmar reserva por ${monto}? (S/N): ")
                    if confirmar.upper() == "S":
                        if crear_reserva(monto, 0, 0, cliente.id_usuario, id_p):
                            print("tu reserva se ha hecho con éxito")
                else:
                    print("ID de paquete no válido.")
            pausar()
            
        elif opcion == "4":
            print("\n--- CREAR PAQUETE PERSONALIZADO ---")
            print("Seleccione hasta 2 destinos de la lista:")
            todos = listar_destinos()
            for d in todos: print(f"ID: {d.id_destino} - {d.nombre}")
            
            lista_select = []
            while len(lista_select) < 2:
                id_x = input("Ingrese ID Destino (o Enter para terminar): ")
                if not id_x: break
                lista_select.append(id_x)
            
            if not lista_select: continue
            
            objs_destinos = []
            for i in lista_select:
                for d in todos:
                    if str(d.id_destino) == i: objs_destinos.append(d)
            
            adultos = int(input("Cantidad Adultos: "))
            ninos = int(input("Cantidad Niños: "))
            
            id_nuevo_pack, total = crear_paquete_personalizado_cliente(objs_destinos, adultos, ninos)
            
            if id_nuevo_pack:
                print(f"\nTotal calculado para su viaje: ${total}")
                print("La seleccion estara disponible por 15 minutos")
                confirmar = input("¿Confirmar reserva? (S/N): ")
                if confirmar.upper() == "S":
                    if crear_reserva(total, adultos, ninos, cliente.id_usuario, id_nuevo_pack):
                        print("tu reserva se ha hecho con éxito")
                else:
                    print("Operacion cancelada.")
            else:
                print("Error calculando el paquete, intente nuevamente más tarde")
            pausar()
            
        elif opcion == "5":
            listar = listar_reservas()
            mis_reservas = [reserva for reserva in listar if reserva.cliente.id_usuario == cliente.id_usuario]
            if not mis_reservas: print("No tiene reservas pendientes.")
            for reserva in mis_reservas:
                print(reserva.generar_comprobante())
            pausar()

        elif opcion == "6":
            print("\n--- ANULAR RESERVA ---")
            listar = listar_reservas()
            reservas_activas = [reserva for reserva in listar if reserva.cliente.id_usuario == cliente.id_usuario and reserva.estado != "Cancelada"]
            
            if not reservas_activas:
                print("No tienes reservas activas para anular.")
            else:
                for reserva in reservas_activas:
                    print(reserva.generar_comprobante())
                
                id_anular = input("\nIngrese ID de la reserva a anular: ")
                
                activa = False
                for reserva in reservas_activas:
                    if str(reserva.id_reserva) == id_anular: activa = True
                
                if activa:
                    conf = input("¿Seguro que desea anular? (S/N): ")
                    if conf.upper() == "S":
                        if cancelar_reserva(id_anular): print("Reserva Anulada.")
                        else: print("Error al anular.")
                else:
                    print("ID inválido.")
            pausar()

        elif opcion == "7":
            print("\n--- MODIFICAR PERFIL ---")
            print(f"Dirección actual: {cliente.direccion}")
            print(f"Teléfono actual: {cliente.telefono}")
            
            nueva_dir = input("Nueva dirección (Enter para mantener): ") or cliente.direccion
            nuevo_tel = input("Nuevo teléfono (Enter para mantener): ") or cliente.telefono
            
            if actualizar_datos_cliente(cliente.id_usuario, nueva_dir, nuevo_tel):
                print("Datos actualizados correctamente. Inicia sesión nuevamente para ver cambios.")
                cliente.direccion = nueva_dir
                cliente.telefono = nuevo_tel
            else:
                print("Error al actualizar.")
            pausar()
            
        elif opcion == "0": break

if __name__ == "__main__":
    menu_principal()