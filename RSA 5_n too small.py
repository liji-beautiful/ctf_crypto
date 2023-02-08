from Crypto.Util.number import bytes_to_long, getPrime
from gmpy2 import invert
import os


e = 65537
encrypted_secret=22677115537648501665625035594569314583201274078937194228422129093254475205833
n=38804990157462268860034103915629114294202425411972714689832516285735474256963
"""
由于n较小，故通过yafu分解n得到答案
"""
p= 192628028063286518008805452139728993349
q= 201450383662304716770027302695583904487
d=invert(e,(p-1)*(q-1))
print(pow(encrypted_secret,d,n))