from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes


def des_image_encrypt(key, imgPath, outPath):

    with open(imgPath,'rb') as image_file:
        image_data = image_file.read()

    iv = get_random_bytes(DES.block_size)

    cipher = DES.new(key,DES.MODE_CBC, iv)

    padded_img_data = pad(image_data,DES.block_size)

    cipher_img_data = iv + cipher.encrypt(padded_img_data)


    with open(outPath,'wb') as encrypted_file:
        encrypted_file.write( cipher_img_data)



def des_img_decrypt(key, encrypt_file_path, outPath):

    with open(encrypt_file_path,'rb') as encrypted_image:
        iv_encrypted_img_data = encrypted_image.read()

    
    iv = iv_encrypted_img_data[:DES.block_size]

    encrypted_img_data = iv_encrypted_img_data[DES.block_size:]

    cipher = DES.new(key, DES.MODE_CBC, iv)

    decrypted_padded_img_data = cipher.decrypt(encrypted_img_data)

    decrypted_img_Data = unpad(decrypted_padded_img_data,DES.block_size)

    with open(outPath,'wb') as decrypted_file:
        decrypted_file.write(decrypted_img_Data)




# Example usage
if __name__ == "__main__":
    # DES key must be 8 bytes long
    key = b'8bytekey'
    
    imagePath = r"C:\Users\Pradyumn Yadu\Desktop\programing\PythonFiles\des_img_cbc\images\myImg2.png"
    encryptedImage_des = r"C:\Users\Pradyumn Yadu\Desktop\programing\PythonFiles\des_img_cbc\encryptedImages\encryptedImg.png"
    decryptedImage_des = r"C:\Users\Pradyumn Yadu\Desktop\programing\PythonFiles\des_img_cbc\decryptedImages\decryptedImg.png"
   
    # Encrypt the image
    des_image_encrypt(key,imagePath, encryptedImage_des)

    # Decrypt the image
    des_img_decrypt(key,encryptedImage_des, decryptedImage_des)