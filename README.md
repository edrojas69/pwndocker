# **PWNDocker**

PWNDocker es una herramienta de hacking creada con contenedores docker, esta utiliza dos instancias de docker.

**pwntools:** La cual contiene distintas herramientas como **nmap**, **dirsearch**, **searchploit**, **wfuzz** y **wpscan**. para hacer ataques de enumaracion, fuzzing, etc.

**pwnvpn:** Es una instancia de docker la cual contiene un cliente VPN para hacer nuestros ataques de forma "anonima". **pwnvpn** esta especialmente creado para ocupar archivos .ovpn los cuales se deben dejar en **pwnvpn/torguard**.

Estos archivos son evaluados desde el codigo para usarlos de forma aleatoria y realizar las conexiones por cada comando ejecutado.


## **Instalación**

En el proceso de instalacion, es necesario entregar las credenciales que seran utilizadas por la vpn, estas son solicitadas en el archivo **install.sh**, que las consultara y dejara guardadas en el archivo **pwnvpn/auth**

```bash
git clone https://github.com/edrojas69/pwndocker.git
cd pwndocker
bash install.sh
```

## **Uso**

Para poder ejecutar cualquier comando debe ser escrito entre comillas

```python3
 python3 pwn-docker.py "curl ifconfig.co"
```


