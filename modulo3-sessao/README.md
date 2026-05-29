# Módulo 3: Segurança de Sessão (HttpOnly vs XSS)

## 1. Ferramentas Usadas
* **VS Code** com a extensão **Live Server** (para rodar o servidor HTTP local).
* **Navegador Web** (Edge, Chrome ou Firefox).
* **DevTools** (Console do Navegador) para execução de scripts.

-----------------------------------------------------------------------------------------

## 2. Passo a Passo
1. Abra a pasta do projeto no VS Code e inicie o arquivo `PoC_Modulo3.html` com o **Live Server** (rodando em `http://127.0.0.1:5500`).
2. Abra o console do navegador pressionando a tecla **F12**.
3. **Cenário 1 (Vulnerável):** Selecione o "Modo Vulnerável", preencha o login e clique em "Entrar". No console, digite `document.cookie` e aperte Enter.
4. **Cenário 2 (Seguro):** Selecione o "Modo Seguro", clique em "Entrar" novamente. No console, digite `document.cookie` e aperte Enter.

-----------------------------------------------------------------------------------------

## 3. Resultado
* **No Cenário 1:** O console exibe o token em texto claro: `SessionID=XYZ123...`.
* **No Cenário 2:** O console retorna vazio (`""`), ocultando o cookie de sessão.

-----------------------------------------------------------------------------------------

## 4. Explicação Técnica do Resultado
* **Cenário 1:** Como o cookie foi gerado sem restrições, o motor de JavaScript do navegador tem acesso total à propriedade `document.cookie`. Isso simula uma falha de **XSS (Cross-Site Scripting)**, onde um atacante injeta um script malicioso para roubar o `SessionID` e sequestrar a sessão do usuário (*Session Hijacking*).
* **Cenário 2:** Ao ativar a flag **`HttpOnly`** na criação do cookie, o navegador isola esse dado em uma área protegida da memória. O JavaScript do *client-side* fica proibido de ler ou modificar o cookie, mitigando o risco de roubo por scripts maliciosos, enquanto o navegador continua enviando o token normalmente nas requisições HTTP para manter o usuário logado.
