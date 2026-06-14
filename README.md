# Sistema de Gestión de Viajes y Reservas Turísticas

## Descripción

Proyecto desarrollado en Python utilizando Oracle Database bajo una arquitectura Modelo-Vista-Controlador (MVC).

La aplicación permite gestionar usuarios, destinos turísticos, paquetes de viaje y reservas mediante una interfaz de consola. El sistema incorpora autenticación de usuarios, administración de perfiles, gestión de paquetes turísticos y control de reservas, diferenciando funcionalidades para clientes y administradores.

Este proyecto fue desarrollado con el objetivo de aplicar conceptos de programación orientada a objetos, acceso a bases de datos relacionales, diseño de software por capas y consultas SQL parametrizadas.

---

## Tecnologías Utilizadas

* Python
* Oracle Database
* SQL
* Arquitectura MVC (Modelo - Vista - Controlador)
* Git
* GitHub

---

## Funcionalidades Principales

### Clientes

* Registro de nuevos usuarios.
* Inicio de sesión con autenticación.
* Consulta de destinos turísticos disponibles.
* Búsqueda de destinos por nombre.
* Visualización de paquetes turísticos.
* Creación de paquetes personalizados.
* Generación de reservas.
* Cancelación de reservas.
* Actualización de datos personales.

### Administradores

* Gestión de destinos turísticos.
* Creación, modificación y eliminación de destinos.
* Creación de paquetes turísticos.
* Asociación de destinos a paquetes.
* Visualización de reservas registradas.
* Creación de nuevos administradores.

---

## Arquitectura del Proyecto

El sistema fue desarrollado utilizando el patrón MVC:

```text
Usuario
   │
   ▼
Vista (Menús)
   │
   ▼
Controlador
   │
   ▼
Modelo
   │
   ▼
Oracle Database
```

### Estructura del Proyecto

```text
CODIGO_VIAJES
│
├── capturas/
├── controlador/
├── modelo/
├── sql/
│
├── bd.py
├── menu.py
└── README.md
```

---

## Características Técnicas

* Arquitectura MVC.
* Conexión a Oracle Database mediante Python.
* Consultas SQL parametrizadas.
* Gestión centralizada de conexiones.
* Manejo de excepciones y errores de base de datos.
* Uso de hashing SHA-256 para almacenamiento seguro de contraseñas.
* Implementación de relaciones entre entidades mediante claves foráneas.

---

## Base de Datos

La base de datos contempla las siguientes entidades:

* Usuario
* Cliente
* Administrador
* Destino
* Paquete Turístico
* Reserva

Incluye scripts de creación de tablas, relaciones e inserción de datos de prueba.

---

## Aprendizajes Obtenidos

Durante el desarrollo de este proyecto se aplicaron conocimientos relacionados con:

* Programación orientada a objetos.
* Arquitectura MVC.
* Diseño de bases de datos relacionales.
* Oracle SQL.
* Integración entre Python y Oracle Database.
* Gestión de usuarios y autenticación.
* Control de acceso basado en roles.
* Uso de Git y GitHub para control de versiones.
