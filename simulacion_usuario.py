import random 
import uuid
from faker import Faker

#1. Sembrar semillas para los datos a simular
random.seed(42)
Faker.seed(42)

#2. IdentiFicar los datos a simular con su tipo de dato
#id (texto (UUID)), 
#nombre (texto), 
#nit (texto), 
#sector (texto) *******************, 
#contacto (texto), 
#correo (texto), 
#telefono (texto), 
#activa (booleano).

#3. ESTABLECER UNA CONSTANTE PARA EL NUEMROD E SIMULACIONS
FILAS=400

#4. Funcion generadora
def generar_datos(numero_filas):
    pass