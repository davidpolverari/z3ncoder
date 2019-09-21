import struct
from numpy import uint32

s = 'abcdefgh'

lista=[]

for i in range(0, len(s)-1, 4):
    lista.append(hex(struct.unpack('<L', s[i:i+4])[0]))

lista.reverse()
print lista
