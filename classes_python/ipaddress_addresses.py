# playaround with python standard library
import binascii
import ipaddress

ADDRESS = [
    '10.9.0.6',
    'fdfd:87b5:b475:5e3e:b1bc:e121:a8eb:14aa'
]

for ip in ADDRESS:
    addr = ipaddress.ip_address(ip)

    print('\n{!r}'.format(addr))
    print(f"IP Version: {addr.version}")
    print(f"Is Private: {addr.is_private}")
    print(f"Packed from: {binascii.hexlify(addr.packed)}")
    print(f"Integer: {int(addr)}")