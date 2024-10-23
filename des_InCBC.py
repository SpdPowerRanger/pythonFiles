from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes


def des_encrypt_cbc(key, plaintext):

    iv = get_random_bytes(DES.block_size) # initialization vector, for random first ciphertext

    cipher = DES.new(key, DES.MODE_CBC, iv) 

    padded_plaintext = pad(plaintext.encode('utf-8'), DES.block_size)

    ciphertext = iv + cipher.encrypt(padded_plaintext)

    return ciphertext


def des_decrypt_cbc(key,ciphertext):

    iv = ciphertext[:DES.block_size] # extract initialization vector

    original_padded_cipherText = ciphertext[DES.block_size:] # get the original ciphertext

    cipher = DES.new(key, DES.MODE_CBC, iv) # cipher object creation

    padded_decrypted_ciphertext = cipher.decrypt(original_padded_cipherText)  # decryption operation

    decrypted_ciphertext = unpad(padded_decrypted_ciphertext, DES.block_size) # unpadding

    return decrypted_ciphertext.decode('utf-8')


if __name__ == '__main__' :

    key = b'8bytekey'

    plaintext = 'beautiful girls are sexy and lewd.'


    encrypted_message = des_encrypt_cbc(key , plaintext)

    print(f'This is the encrypted Message : {encrypted_message.hex()}')



    decrypted_message = des_decrypt_cbc(key, encrypted_message)

    print(f'This the decrypted Message : {decrypted_message}')
