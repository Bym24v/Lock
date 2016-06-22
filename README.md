# Lock.py

Esto es una prueba de concepto de una de las charlas de Rooted CON 2016

https://www.youtube.com/watch?v=JeO-ABq_joc


### Probado en Ubuntu 16.04 LTS


# Configuración

Conecta tu dispositivo de USB

Navega asta esta ruta

```bash
/usr/bin
  ```
Ejecuta el comando 

```bash
udisksctl monitor
 ```
 ![alt tag](https://github.com/Bym24v/Lock/blob/master/img/monitor1.png)
 
Desconecta y vuelve a conectar el dispositivo usb

![alt tag](https://github.com/Bym24v/Lock/blob/master/img/monitor2.png)

Tendrás que buscar tu dispositivo USB para conseguir la ID

Una vez que tengas el ID, solo tienes que remplazarlo en el script

![alt tag](https://github.com/Bym24v/Lock/blob/master/img/script.png)

# Ejecutar el Script

```bash
python lock.py
  ```

## Que debería suceder ?

Si todo anda bien, debería de salirte la pantalla de iniciar sesión automáticamente una vez que desconectes el usb.

si intentas hacer login y el dispositivo esta desconectado, automáticamente 
en dos segundos saldrá la pantalla de login.

Ahora bien, si el dispositivo esta conectado y intentas hacer login de nuevo, reconocerá el dispositivo usb y tendrás acceso al sistema.


### WIP ? 