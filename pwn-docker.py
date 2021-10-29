#!/bin/evn python3

from random import choice
import os,sys,time

retries = 10

def isVPNReady():
    global retries
    if retries > 0:
        retries -= 1
        r = os.popen(' docker logs pwnvpn').read()
        try:
            r = r.split("\n")
            if r.__len__() > 3:
                if "Initialization Sequence Completed" in r[-2]:
                    print("[+] VPN Connected")
                    return True

            print("[!] VPN not ready yet, retrying...")
            time.sleep(4)
            return isVPNReady()

        except Exception as e:
            print("[-] Error ", e)

    else:
        print("[-] VPN not initalized")
        return False


def vpnRandom():
    vpnfiles = os.listdir("./pwnvpn/torguard")
    return (choice(vpnfiles))

def dockerComand():
    os.system(' docker run --cap-add=NET_ADMIN --device /dev/net/tun --name=pwnvpn --rm -i -d pwnvpn openvpn --config /root/vpn/torguard/' + vpnRandom() + ' --auth-user-pass /root/vpn/auth >/dev/null')
    rw = isVPNReady()
    if rw:
        print("[+] Executing commands\n")
        os.system(' docker run --rm --network=container:pwnvpn -it pwntools sh -c "' + sys.argv[1]+'"')
        print("\n")
        os.system(' docker rm $( docker ps -a -q) --force > /dev/null ')
    else:
        global retries
        retries = 10
        os.system(' docker rm $( docker ps -a -q) --force > /dev/null')
        print("[-] Restarting process")
        return dockerComand()

if len(sys.argv) != 2:
    print('\n Usage: python3 ' + sys.argv[0] + ' "comando a ejecutar"\n')
    sys.exit(1)

if __name__ == '__main__':
    try:
        dockerComand()

    except Exception as e:
        print(e)