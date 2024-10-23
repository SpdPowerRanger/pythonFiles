from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad


def des_encrypt(plaintext, key):

    cipher = DES.new(key, DES.MODE_ECB)

    paddedPlainText = pad(plaintext.encode('utf-8'), DES.block_size)

    cipherText = cipher.encrypt(paddedPlainText)

    return cipherText

def des_decrypt(cipherText, key):

    cipher = DES.new(key, DES.MODE_ECB)

    decipherText = cipher.decrypt(cipherText)

    unpaddedDecipherText = unpad(decipherText, DES.block_size)

    return unpaddedDecipherText.decode('utf-8')

if __name__ == "__main__":
    # 8-byte key for DES (must be 8 bytes long)
    key = b'8bytekey'
    
    # The plaintext message to be encrypted
    plaintext = "Hello, World!"
    
    # Encrypt the plaintext
    encrypted_message = des_encrypt(plaintext, key)
    print(f"Encrypted Message: {encrypted_message.hex()}")  # Convert to hex for readability
    
    # Decrypt the ciphertext
    decrypted_message = des_decrypt(encrypted_message, key)
    print(f"Decrypted Message: {decrypted_message}")