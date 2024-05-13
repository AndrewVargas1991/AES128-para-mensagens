'''
Para executar o programa, instale as bibliotecas Cryptography e Fernet
   com os seguintes comandos no CMD:

pip install cryptography
pip install fernet
'''

from cryptography.fernet import Fernet

senha = b'I_Ny8ObjRjKI44G63y151P-zMnmJg62NhBrnz3J1UVU='
#Descomente a linha abaixo se quiser gerar uma nova senha
#senha = Fernet.generate_key()
print('Guarde a seguinte senha:')
print(senha)

original = input('\nDigite o que deseja encriptar: ')     
encriptado = Fernet(senha).encrypt(original.encode())      
decriptado = Fernet(senha).decrypt(encriptado).decode()   

print("\nOriginal:", original)
print("Encriptado:", encriptado)
print("Decriptado:", decriptado)

input("\nENTER para sair...")