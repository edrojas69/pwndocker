#!/bin/bash

valAuth(){
    
    if [ -f pwnvpn/auth ]; then
        echo $?
    else
        echo $?
    fi

}

dockerBuild(){
    docker build -t pwntools pwntools/.
    docker build -t pwnvpn pwnvpn/.
}

function sourceVPN()
{
    echo -e "[+] Credenciales de VPN \n"
    read -p "[!] Correo: " user
    read -p "[!] Password: " pass
    touch pwnvpn/auth
    echo $user >> pwnvpn/auth
    echo $pass >> pwnvpn/auth
}

tmp=$(valAuth)

if [ $tmp -eq 0 ]; then
    
    dockerBuild

else
    sourceVPN
    dockerBuild
    
fi

echo "[+] Instalacion finalizada"