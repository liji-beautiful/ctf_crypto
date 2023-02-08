from Crypto.Cipher import AES
key = b"ThisismyAESkey:)"
aes = AES.new(key, AES.MODE_ECB)

output="fef29ccb541199b860a134e0e87c59d73bd312f7671107e184ee2382b475922a5ff7e713e0a30fe030ef15c4fd4fde52"
output_=bytes.fromhex(output)
"""
本题不难，都是现成的函数，hex是一种编码格式，注意解码时候用fromhex()方法即可
"""
output__=aes.decrypt(output_)
print(output__)