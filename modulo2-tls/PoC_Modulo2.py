import os
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

print("--- INICIANDO PROTOCOLO HÍBRIDO (SIMULAÇÃO TLS) ---")

# =====================================================================
# PASSO 1: O Servidor gera suas chaves Assimétricas (RSA)
# =====================================================================
private_key_server = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key_server = private_key_server.public_key()
print("[Servidor] Chaves RSA de 2048 bits geradas.")

# =====================================================================
# PASSO 2: O Cliente gera a 'Chave de Sessão' Simétrica (AES-256)
# =====================================================================
# Em um cenário real, o cliente pegaria a public_key_server na rede
chave_sessao_cliente = os.urandom(32) # 256 bits aleatórios
print(f"[Cliente] Chave Simétrica (AES) temporária gerada: {chave_sessao_cliente.hex()[:20]}...")

# =====================================================================
# PASSO 3: O Handshake - Cliente cifra a Chave AES usando o RSA do Servidor
# =====================================================================
chave_criptografada = public_key_server.encrypt(
    chave_sessao_cliente,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
print("[Handshake] Chave AES cifrada com RSA e enviada ao servidor.")

# =====================================================================
# PASSO 4: O Servidor decifra a Chave AES usando sua Chave Privada RSA
# =====================================================================
chave_sessao_servidor = private_key_server.decrypt(
    chave_criptografada,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
print(f"[Servidor] Chave AES decifrada com sucesso: {chave_sessao_servidor.hex()[:20]}...")

# Verificação de segurança do Handshake
assert chave_sessao_cliente == chave_sessao_servidor
print("[Handshake] Sucesso! Ambos possuem a mesma chave simétrica de forma segura.\n")

# =====================================================================
# PASSO 5: Transferência de Dados Cifrada com AES (Criptografia Simétrica)
# =====================================================================
mensagem_original = b"Dados Confidenciais da Requisicao HTTP: Senha=123456"
print(f"[Cliente] Mensagem original: {mensagem_original.decode()}")

# Configurando o AES-GCM (Modo simétrico autenticado moderno)
iv = os.urandom(12) # Vetor de Inicialização
encryptor = Cipher(algorithms.AES(chave_sessao_cliente), modes.GCM(iv)).encryptor()
dados_cifrados = encryptor.update(mensagem_original) + encryptor.finalize()
tag_autenticacao = encryptor.tag

print(f"[Canal] Dados trafegando na rede (Cifrados): {dados_cifrados.hex()}")

# =====================================================================
# PASSO 6: O Servidor recebe e decifra os dados com o AES
# =====================================================================
decryptor = Cipher(algorithms.AES(chave_sessao_servidor), modes.GCM(iv, tag_autenticacao)).decryptor()
mensagem_decifrada = decryptor.update(dados_cifrados) + decryptor.finalize()

print(f"[Servidor] Dados decifrados recebidos: {mensagem_decifrada.decode()}")
print("--- FIM DA SIMULAÇÃO ---")