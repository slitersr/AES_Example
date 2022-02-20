from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from base64 import b64encode, b64decode
from hashlib import md5

class CipherFunctions:
    def __init__(self, key):
        self.key = md5(key.encode('utf8')).digest()
        #write key to key.txt and to terminal
        #print("Secret key in Hex: " + self.key.hex())
        with open('C:/Users/seans/Desktop/SeniorSem1/DataSecurityPrivacy/Project2/data/' + 'key.txt', 'w') as f:
            f.write(str(self.key.hex()))
            f.close

    def encrypt(self, data):
        self.cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return b64encode(iv + self.cipher.encrypt(pad(data.encode('utf-8'), AES.block_size)))

    def decrypt(self, data):
        raw = b64decode(data)
        self.cipher = AES.new(self.key, AES.MODE_CBC, raw[:AES.block_size])
        return unpad(self.cipher.decrypt(raw[AES.block_size:]), AES.block_size)

if __name__ == '__main__':
    #calculate iv
    iv = get_random_bytes(AES.block_size)
    #write iv to iv.txt
    with open('C:/Users/seans/Desktop/SeniorSem1/DataSecurityPrivacy/Project2/data/' + 'iv.txt', 'w') as f:
        f.write(str(iv.hex()))
        f.close

    msg = input('input message: ')
    #write plaintext to plaintext.txt
    with open('C:/Users/seans/Desktop/SeniorSem1/DataSecurityPrivacy/Project2/data/' + 'plaintext.txt', 'w') as f:
            f.write(str(msg))
            f.close

    pwd = input('input password: ')

    #write ciphertext to ciphertext.txt
    with open('C:/Users/seans/Desktop/SeniorSem1/DataSecurityPrivacy/Project2/data/' + 'ciphertext.txt', 'w') as f:
            tempCiphertext = CipherFunctions(pwd).encrypt(msg).decode('utf-8').encode().hex()
            f.write(tempCiphertext)
            f.close

    print('ciphertext:', CipherFunctions(pwd).encrypt(msg).decode('utf-8'))
    cte = CipherFunctions(pwd).encrypt(msg).decode('utf-8')

    #write result decryption to result.txt
    with open('C:/Users/seans/Desktop/SeniorSem1/DataSecurityPrivacy/Project2/data/' + 'result.txt', 'w') as f:
            tempResult = CipherFunctions(pwd).decrypt(cte).decode('utf-8')
            f.write(str(tempResult))
            f.close

    pwd = input('enter password to view decrypted message: ')
    print('decrypted message: ', CipherFunctions(pwd).decrypt(cte).decode('utf-8'))