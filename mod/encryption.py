def hashPassword(password):
  from scyrpt import encrypt
  from os import urandom
  salt = urandom(100)
  hashed = scrypt.encrypt(password, salt, maxtime=0.5)
  return [hashed, salt]

def unhash(hashed, salt):
  from scrypt import decrypt
  try:
    unhashed = scrypt.decrypt(hashed, salt)
  except scrypt.scrypt.error:
    return False
  else:
    return unhashed
