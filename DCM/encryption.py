import json
from cryptography.fernet import Fernet
from cryptography.fernet import InvalidToken

# Generate an encryption key
def generate_encryption_key():
    return Fernet.generate_key()

# Encrypt a dictionary
def encrypt_data(data, key):
    cipher_suite = Fernet(key)
    encrypted_data = {}
    for key, value in data.items():
        if isinstance(value, list):
            value = json.dumps(value)
        encrypted_data[key] = cipher_suite.encrypt(value.encode())
    return encrypted_data

# Decrypt a dictionary
def decrypt_data(encrypted_data, key):
    cipher_suite = Fernet(key)
    decrypted_data = {}
    for key, value in encrypted_data.items():
        try:
            decrypted_value = cipher_suite.decrypt(value).decode()
            if key == "roles":
                decrypted_value = json.loads(decrypted_value)
            decrypted_data[key] = decrypted_value
        except InvalidToken:
            print("Invalid token. Data may be tampered.")
    return decrypted_data

# Save encrypted data to a file
def save_encrypted_data_to_file(encrypted_data, filename):
    with open(filename, 'wb') as file:
        for key, value in encrypted_data.items():
            file.write(f"{key}: {value}\n".encode())

# Read encrypted data from a file
def read_encrypted_data_from_file(filename):
    with open(filename, 'rb') as file:
        lines = file.readlines()
    encrypted_data = {}
    for line in lines:
        key, value = line.decode().strip().split(': ')
        encrypted_data[key] = value.encode()
    return encrypted_data

# # Test code:
# if __name__ == "__main__":
#     key = generate_encryption_key()
#     data_to_encrypt = {
#         "username": "my_username",
#         "password": "my_password",
#         "roles": ["admin", "user"],
#     }
    
#     encrypted_data = encrypt_data(data_to_encrypt, key)
#     save_encrypted_data_to_file(encrypted_data, 'encrypted_data.txt')
    
#     loaded_data = read_encrypted_data_from_file('encrypted_data.txt')
#     decrypted_data = decrypt_data(loaded_data, key)
    
#     if decrypted_data:
#         print("Decrypted Data:", decrypted_data)
#     else:
#         print("Data could not be decrypted due to an invalid token.")
