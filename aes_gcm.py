from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os

# Generate a random 256-bit (32-byte) key
key = AESGCM.generate_key(bit_length=256)
aesgcm = AESGCM(key)

# Generate a random 96-bit (12-byte) IV/nonce
nonce = os.urandom(12)
data = b"Confidential financial data."
aad = b"user_id=42"

# Encrypt
ct = aesgcm.encrypt(nonce, data, aad)
print(f"Ciphertext: {ct.hex()}")

# Decrypt
pt = aesgcm.decrypt(nonce, ct, aad)
print(f"Decrypted: {pt.decode('utf-8')}")
