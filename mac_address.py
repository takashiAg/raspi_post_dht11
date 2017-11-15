import uuid

def macaddress():
    macaddress_dec=uuid.getnode()
    macaddress_hex=hex(macaddress_dec)
    macaddress_str=macaddress_hex[2:14]
    return macaddress_str