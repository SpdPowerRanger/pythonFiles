from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes


def des_encrypt_cbc(plaintext, key):

    iv = get_random_bytes(DES.block_size)
    
    cipher = DES.new(key, DES.MODE_CBC, iv)

    paddedPlainText = pad(plaintext.encode('utf-8'), DES.block_size)

    cipherText = iv + cipher.encrypt(paddedPlainText)

    return cipherText

def des_decrypt_cbc(cipherText, key):

    iv = cipherText[:DES.block_size]

    actual_cipher_text = cipherText[DES.block_size:]

    cipher = DES.new(key , DES.MODE_CBC, iv)

    decrypted_padded_text =  cipher.decrypt(actual_cipher_text)

    decrypted_text = unpad(decrypted_padded_text, DES.block_size)

    return decrypted_text.decode('utf-8')


if __name__ == "__main__":

    key = b'8bytekey'

    plainText = "hello World!"

    encrypted_message = des_encrypt_cbc(plainText,  key)
    
    print(f'This is the encrypted Message : {encrypted_message.hex()}')

    decrypted_message = des_decrypt_cbc(encrypted_message, key)

    print(f'This is the decrypted Message : {decrypted_message}')
