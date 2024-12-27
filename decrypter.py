import os
import pyaes

# chave para descriptografia (deve ser igual à usada na criptografia)
key = b"victorreis123456"
aes = pyaes.AESModeOfOperationCTR(key)

# descriptografar todos os arquivos .troll na pasta
for file_name in os.listdir():
    if file_name.endswith(".troll"):
        # abrir o arquivo criptografado
        with open(file_name, "rb") as file:
            file_data = file.read()

        # descriptografar o arquivo
        decrypt_data = aes.decrypt(file_data)

        # remover o arquivo criptografado
        os.remove(file_name)

        # restaurar o arquivo original
        original_file_name = file_name.replace(".troll", "")
        with open(original_file_name, "wb") as new_file:
            new_file.write(decrypt_data)

print("Arquivos descriptografados com sucesso!")
