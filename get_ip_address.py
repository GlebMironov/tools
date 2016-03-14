import sys
import netifaces

if __name__ == '__main__':
    if len(sys.argv) == 1:
        iface = 'tun0'
    else:
        iface = sys.argv[1]

    try:
        ip_address = netifaces.ifaddresses(iface)[netifaces.AF_INET][0]['addr']
    except:
        ip_address = ''

    print ip_address

