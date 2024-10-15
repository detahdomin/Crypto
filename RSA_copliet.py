from Crypto.Util.number import *

p = getPrime(512)
q = getPrime(512)
n = p*q
phi = (p-1)*(q-1)

e = 65537 
assert GCD(e ,phi) == 1,"该e不满足互素条件"
d = inverse(e ,phi) #乘法逆元

message=b"hello" #不能使用python字符串 原生存储
m = bytes_to_long(message) #转换为数字

c = pow(m, e, n) #注意不要写成m**e % n，二者代表的意义相同，但是pow函数内置快速幂
msg = pow(c, d, n)
print(long_to_bytes(msg))



