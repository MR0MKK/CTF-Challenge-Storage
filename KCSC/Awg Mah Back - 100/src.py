from pwn import *

with open('flag.txt', 'rb') as (f):
    flag = f.read()
a = flag[0:len(flag) // 3]
b = flag[len(flag) // 3:2 * len(flag) // 3]
c = flag[2 * len(flag) // 3:]
a = xor(a, int(str(len(flag))[0]) + int(str(len(flag))[1]))   # a1=a0 ^3 
b = xor(a, b)   # b1=a1^b0 
c = xor(b, c)   # c1=b1^c0 = a1^b0^c0
a = xor(c, a)   # a2=c1^a1 = a1^b0^c0^a1 = b0^c0
b = xor(a, b)   # b2=a2^b1 = b0^c0^a1^b0 =  c0^a1 = c0^a0^3
c = xor(b, c)   # c2=b2^c1 = c0^a1^a1^b0^c0 = b0
c = xor(c, int(str(len(flag))[0]) * int(str(len(flag))[1]))   # c3=b0^2 
enc = a + b + c
with open('int.txt', 'wb') as (f):
    f.write(enc)


