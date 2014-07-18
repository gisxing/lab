import string
def to_digit(addr) :
    lst = map(string.atoi, addr.strip().split('.'))
    return reduce(lambda x, y: x*256+y, lst)
 
netmask = lambda n : 2**32 - 2**(32-n)
 
def belongs(addr, network) :
    if '/' in network:
        naddr, nm = network.split('/')
        mask = netmask(string.atoi(nm))
        return to_digit(addr) & mask == to_digit(naddr)
    elif '-' in network:
        naddr_b, naddr_e= network.split('-')
        ip_seg = network.strip().split('.')
        ip_seg.pop()
        ip_seg.append(naddr_e)
        ne = string.join(ip_seg, '.')
        return (to_digit(addr)>=to_digit(naddr_b)) and (to_digit(addr)<=to_digit(ne))
    else :
        return addr == network

def main():
    print belongs('127.0.0.1', '127.0.0.2')
    print belongs('127.0.0.1', '127.0.0.1-2')
    print belongs('127.0.0.1', '127.0.0.0/25')

if __name__ == '__main__':
    main()
