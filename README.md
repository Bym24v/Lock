# Lock.py

Esto es una prueba de concepto de una de las charlas de Rooted CON 2016

https://www.youtube.com/watch?v=JeO-ABq_joc


### Probado en Ubuntu 16.04 LTS


# Configuración

Conectar tu dispositivo de USB

Navega asta esta ruta

```bash
/usr/bin
  ```
  
Ejecuta el comando 

```bash
udisksctl monitor
 ```
 ![alt tag](#)
 
Desconecta y vuelve a conectar el dispositivo 

![alt tag](#)

Tendrás que buscar el dispositivo USB para conseguir su id

Una vez que tengas el id, solo tienes que remplazarlo en el script

![alt tag](#)

# Ejecutar el Script

```bash
python lock.py
  ```

## Que debería suceder ?

Si todo anda bien, debería de salirte la pantalla de iniciar sesión automáticamente una vez que desconectes el usb.

si intentas hacer login y el dispositivo esta desconectado, automáticamente 
en dos segundos saldrá la pantalla de login.

Ahora bien, si el dispositivo es de vuelta otra vez conectado y intenta hacer login de nuevo, reconocerá el dispositivo usb y tendrás acceso al sistema.