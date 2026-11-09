import bcrypt

password = b"SuperSecretP@ssw0rd!"

# Hash (includes generating salt with default work factor 12)
salt = bcrypt.gensalt(rounds=12)
hashed = bcrypt.hashpw(password, salt)
print(f"Hashed password: {hashed.decode('utf-8')}")

# Verify
if bcrypt.checkpw(password, hashed):
    print("Password matches!")
else:
    print("Password does not match!")
