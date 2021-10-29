# **PWNDocker**

PWNBot es una herramienta de hacking creada con python3 para hacer uso de pwndocker desde Telegram, principalmente el enfoque es poder realizar ataques basicos de fuzzing, diccionario, etc. desde el telefono.


## **Instalacion**
Para poder funcionar es necesario poder instalar las dependencias que necesita para validar y ocupar la libreria de Telegram

```bash
pipenv install validators
pipenv install python-telegram-bot
```

## **Uso**

Para poder ejecutar cualquier comando debe ser escrito entre comillas

```python3
git clone https://github.com/edrojas69/pwndocker.git
cd pwndocker/pwnbot/
pipenv run python pwnbot.py
```

## **Comandos habilitados en Telegram**
Como esta en face de desarrollo aun queda mucho por hacer, pero ya tiene algunos comandos basicos para poder funcionar. Son los siguientes:

```apache
/help       -   Show this help
/pwn        -   Do the thing EX. /pwn nmap doamin-localhost
/toolslist  -   List of avaible tools
/wordlist   -   List all the bot wordlist
/version    -   Show bot develop version
```

## **TODO**
- Poder enviar multiples parametros.
- Seguridad en los comandos ejecutados.
- Hacer el uso mas sencillo de lo que ya es.
- Hacer que funcione con pwnvpn, ahora solo funciona con pwntools
