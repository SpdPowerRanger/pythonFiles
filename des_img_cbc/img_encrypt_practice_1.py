from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# des image encription in cbc mode

def des_img_encrypt(key, img_path, encrypt_img_path):

    with open( img_path, 'rb') as image_file:  # reading image as image_file.
        image_data = image_file.read()  # storing it in image_data variable.

    
    iv = get_random_bytes(DES.block_size) # intialization vector (a non-secret 64 bit encryption block that is needed to be XORed with the next encryption block).

    cipher = DES.new(key, DES.MODE_CBC, iv) # cipher object in cbc mode with initialization vector.

    padded_img_data = pad(image_data, DES.block_size) # image data needs to be padded in a 64 bit block size, because des and most encryption algos work in bytes. 

    cipher_img_data = iv + cipher.encrypt(padded_img_data)

    
    with open(encrypt_img_path,'wb') as encrypted_img:  # opening the encryptedImg.jpg file as encrypted_img.
        encrypted_img.write(cipher_img_data)  # writing our cipher_img_data on it.
    


def des_img_decrypt(key, encrypted_img_path, out_img_path):

    with open(encrypted_img_path,'rb') as cipher_img_file:  # reading encrypted image in binary format as cipher_image_data.
        cipher_img_data = cipher_img_file.read()  # storing it in the cipher_img_data variable.

    iv = cipher_img_data[:DES.block_size]  # separating iv

    padded_cipher_data = cipher_img_data[DES.block_size:] # separating the padded encrypted image data.

    cipher = DES.new(key, DES.MODE_CBC, iv) # cipher object creation in cbc mode.

    deciphered_img_data = cipher.decrypt(padded_cipher_data)

    decrypted_img_data = unpad(deciphered_img_data, DES.block_size) # unpadding the padded data to get the original encrypted image data.

    with open(out_img_path,'wb') as decrypted_img_file:
         decrypted_img_file.write(decrypted_img_data)



if __name__ == "__main__" :

    key = get_random_bytes(8)

    img_path = r"C:\Users\Pradyumn Yadu\Desktop\programing\PythonFiles\des_img_cbc\images\myImg3.jpg"

    encrypt_img_path = r"C:\Users\Pradyumn Yadu\Desktop\programing\PythonFiles\des_img_cbc\encryptedImages\encryptImage.jpg"

    decrypt_img_path = r"C:\Users\Pradyumn Yadu\Desktop\programing\PythonFiles\des_img_cbc\decryptedImages\decryptedImg.jpg"


    des_img_encrypt(key, img_path, encrypt_img_path)

    des_img_decrypt(key, encrypt_img_path, decrypt_img_path)
    