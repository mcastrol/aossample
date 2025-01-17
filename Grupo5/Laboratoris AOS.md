LABORATORI AOS 8/11/
- ENTRAR A LAUNCH TEMPLATE

    Nombre: grupoA_template
    Descripcion sgtemplate
    Template tags con name y grupoA
    Imagen ubuntu
    Instancia t2nano
    Par de claves: no vamos a incluir
    Confguracion de red, crear grupo de seguridad sg.grupoA
    VPC por defecto
    Agregar regla de seguridad:tipo ssh puerto 22, origen 000000
    Agregamos otro tipo http origen 000000 puerto 80
    Almacencamiento volumenes por defecto
    Etiquetas de recursos agregar nueva etiqueta
    Clave: name valor grupoA,
    Detalles avanzados --> copiar scipt
    Cambiar algo para identificar
    Queremos crear un grupo de escalamiento automatico
    Nombre del grupo de autoescaling: grupoA_autoescaling
    Plantilla de lanzamiento tiene que aparecer la nuestra
    Version default
    Siguiente
    Elegir las opciones de lanzamiento de instanicas
    Red: zona de disponibilidad, seleccionar todas las default
    Avaiability zone distruibutioin , balanced best effort
    Siguiente
    Balance de carga: asociar a un nuevo balanceador de carga
    Tipo de balanceador de carga: esquema del balanceador de carga, internet-
    facing
    Agentes de escuha i direccionamiento crear un grupo de destino nombre del
    grupo de destino nuevo gurpoAgrupodestino
    Key : name value: grupoA
    Comprovaciones de estado dejar por defecto
    Tamaño del grupo – capacidad deseada 2
    Escalado, capacidad deseada mínima 2, capacidad deseada máxima 4
    Escalamiento automatico, politica de escalado de seguimiento de destino,
    utilizacion promedio de la CPU
    Elige un comportamineot de reeeplazo: sin política.

LAB 22/11 RDS

Anar a amazon RDS

Base de datos

Crear base de datos

Creación estándar
Opciones de motor → mysql

Versión del motor → la última

Plantillas → capa gratuita

Configuración → identidificador grupo

Configuración de credenciales → admin

Administración de credenciales → autoadministrado

Contraseña maestra → admingrupo

Configuración de la instancia → db.t3.micro

Escalado automático de almacenamiento → habilitar escalado automático de
almacenamiento

Conectividad → grupo de seguridad → crear nuevo → nombre: sg.grupo5.rds
Configuración adicional → configuración adicional → opciones de la base de datos →
nombre: aosbd → Periodo de retención de copia de seguridad 1 día.

Creamos base de datos

Ir a cloud

Crear entorno → nombre: cloud9.grupo5 → todo por defecto!
Crear la instancia e iniciarla

RDS base de datos → grupos de seguridad → seleccionamos el nuestro → reglas de
entrada → editar reglas de entrada → agregar regla → la nostra ip, mysqlaurora origen:
posem el grupo de seguridad.

Vamos al cloud9 y entramos a la instancia

Vamos a rds y copiamos el endpoint (punto de acceso)
