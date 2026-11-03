from cryptography.fernet import Fernet

#Put this somewhere safe!
key = Fernet.generate_key()
f=Fernet(key)
print(key)
token = f.encrypt(b"Welcome to my GitHub repo.")
print(token)
token= f.decrypt(token)
print(token)

#this is the first program of this series