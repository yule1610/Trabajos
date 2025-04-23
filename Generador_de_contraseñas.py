import string 
import random 
import secrets


longitud = 8


caracteres = string.ascii_letters + string.digits + string.punctuation

contraseña = []

contraseña.append(random.choice(string.ascii_lowercase)) 
contraseña.append(random.choice(string.ascii_uppercase)) 
contraseña.append(random.choice(string.digits)) 
contraseña.append(random.choice(string.punctuation)) 

while len(contraseña) < longitud:
  contraseña.append(secrets.choice(caracteres)) 

random.shuffle(contraseña)

contraseña = "".join(contraseña)

print("Tu contraseña es:", contraseña)

contraseña2 = []
while len(contraseña2) < longitud:
  contraseña2.append(secrets.choice(caracteres)) 

random.shuffle(contraseña2)

contraseña2 = "".join(contraseña2)

print("Tu contraseña es:", contraseña2)
