# Módulo 2: Criptografia e Handshake (A base do TLS)

## 1. Ferramentas Usadas
* **VS Code:** Ambiente de desenvolvimento integrado para edição e execução do script.
* **Python 3:** Ambiente de execução do código e gerenciamento de scripts.
* **Biblioteca `cryptography`:** Biblioteca padrão de mercado para operações de criptografia de alto nível (RSA e AES-GCM).

-----------------------------------------------------------------------------------------

## 2. Passo a Passo
1. Certifique-se de ter o Python instalado e instale a biblioteca de criptografia executando o comando no terminal:
   ```bash
   pip install cryptography

2. Abra o terminal na pasta do módulo e execute o arquivo script da PoC:
   python PoC_Modulo2.py

3. Acompanhe a saída do terminal dividida em duas etapas principais: o Aperto de Mão (Handshake) e a Transferência de Dados.

-----------------------------------------------------------------------------------------

## 3. Resultado

No Handshake: O terminal exibe o Servidor gerando chaves assimétricas RSA de 2048 bits. O Cliente gera uma chave AES aleatória e a envia criptografada. O Servidor decifra o pacote com sucesso, resultando na mesma chave simétrica idêntica em ambos os lados (15f6a578f1...).

Na Transferência de Dados: A mensagem confidencial clara contendo dados sensíveis (Senha=123456) é convertida em blocos de bytes hexadecimais ilegíveis (4c321c3af0...) ao trafegar simuladamente pelo canal de rede. Ao chegar no destino, o servidor decifra a carga e recupera o texto original intacto.

-----------------------------------------------------------------------------------------

## 4. Explicação Técnica do Resultado

Fase Assimétrica (Handshake): A PoC demonstra a troca de chaves utilizando o algoritmo RSA. Como chaves assimétricas demandam alto processamento computacional para cifrar grandes volumes de texto, o protocolo TLS utiliza essa etapa única e exclusivamente para autenticar o servidor e transportar com segurança uma chave simétrica temporária (Chave de Sessão), protegendo-a contra interceptações na camada de rede (sniffing).

Fase Simétrica (Transferência de Dados): Com o segredo compartilhado, o script chaveia para o algoritmo AES (modo GCM). Algoritmos simétricos operam através de manipulações matemáticas diretas de bits, sendo extremamente velozes e leves para o hardware. O modo GCM (Galois/Counter Mode) garante não apenas a confidencialidade do tráfego (impedindo a leitura de dados sensíveis em trânsito), mas também a integridade e autenticidade da mensagem através do uso de tags de autenticação criptográfica.