aso a paso
Paso 1: Iniciar sesión en AWS
Ve a la consola de AWS: AWS Console.
Inicia sesión con tus credenciales.
Paso 2: Acceder al servicio EC2
En la barra de búsqueda superior, escribe EC2 y selecciona el servicio.
En el panel de EC2, haz clic en Launch Instances (Lanzar instancias).
Paso 3: Configurar la instancia
Nombre de la instancia:

Asigna un nombre como MiPrimerServidorEC2.
Imagen de la máquina (AMI):

Selecciona una Amazon Machine Image (AMI) como Amazon Linux 2 (gratis en el nivel gratuito de AWS).
Tipo de instancia:

Elige el tipo t2.micro (incluido en el nivel gratuito).
Clave de acceso (Key Pair):

Si ya tienes un par de claves, selecciónalo.
Si no tienes, crea uno nuevo:
Haz clic en Create new key pair.
Escribe un nombre para el par de claves.
Descarga el archivo .pem (muy importante, ya que no podrás descargarlo después).
Configuración de red:

Usa la opción predeterminada o crea un nuevo grupo de seguridad.
Permite las reglas de entrada:
SSH (puerto 22): Para conectarte a la instancia.
HTTP (puerto 80): Para servir páginas web.
Almacenamiento:

Acepta el valor predeterminado (8 GB es suficiente).
Paso 4: Lanzar la instancia
Revisa la configuración.
Haz clic en Launch Instance (Lanzar instancia).
Espera unos segundos hasta que se cree la instancia.
En el panel de instancias, busca tu instancia en la lista y verifica que el estado sea Running.
Paso 5: Conectar a la instancia
Selecciona la instancia en la lista.
Haz clic en Connect.
Sigue las instrucciones para conectarte vía SSH:
Abre tu terminal (Linux/Mac) o PuTTY (Windows).
Usa el comando proporcionado (se verá algo así):
bash
Copia
Modifica
ssh -i "TuClave.pem" ec2-user@<DirecciónIP>
Paso 6: Instalar un servidor web (Apache)
Una vez conectado a la instancia, instala Apache ejecutando estos comandos:
bash
Copia
Modifica
sudo yum update -y
sudo yum install httpd -y
sudo systemctl start httpd
sudo systemctl enable httpd
Verifica que el servidor esté corriendo:
bash
Copia
Modifica
sudo systemctl status httpd
Paso 7: Probar el servidor web
Entra a tu navegador.
Escribe la dirección IP pública de tu instancia (puedes encontrarla en la consola de EC2).
Deberías ver la página de bienvenida de Apache.
Paso 8: Detener o terminar la instancia
Una vez que hayas terminado, vuelve a la consola de EC2.
Selecciona la instancia y haz clic en Instance State > Stop (para detenerla) o Terminate (para eliminarla).