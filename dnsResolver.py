import socket,sys

if len(sys.argv) != 3:
    print('Modo de uso: python3 dnsforce.py <alvo.com> <wordlist>')
    sys.exit(1)

host = sys.argv[1]

with open(sys.argv[2]) as wordlist:
    for p in wordlist.readlines():
        p = p.replace('\n', '')
        host_enum = f'{p}.{host}'

        try:
            info = socket.getaddrinfo(host_enum, None, socket.AF_INET)
            print(f'{host_enum} - {info[0][4][0]}')

        except socket.gaierror: # subdominio não existe
            None