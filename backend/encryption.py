import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

# 🔐 Derive a Fernet key from the password using PBKDF2
def generate_key(password: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=390000,
        backend=default_backend()
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))

# 🔐 Encrypt a message with password, returns (encrypted_text, salt)
def encrypt_message(message: str, password: str) -> tuple[str, str]:
    salt = os.urandom(16)  # Unique per encryption
    key = generate_key(password, salt)
    fernet = Fernet(key)
    encrypted = fernet.encrypt(message.encode())
    # Return both encrypted text and salt (as base64 string)
    return encrypted.decode(), base64.urlsafe_b64encode(salt).decode()

# 🔓 Decrypt a message using the password and salt
def decrypt_message(encrypted_text: str, password: str, salt_str: str) -> str:
    try:
        salt = base64.urlsafe_b64decode(salt_str.encode())
        key = generate_key(password, salt)
        fernet = Fernet(key)
        decrypted = fernet.decrypt(encrypted_text.encode())
        return decrypted.decode()
    except Exception:
        return None  # Decryption failed