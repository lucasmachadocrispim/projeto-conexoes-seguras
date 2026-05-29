# Evidências - Módulo 3: Segurança de Sessão

Este diretório contém as capturas de tela que comprovam a execução dos testes da Prova de Conceito (PoC).

## 📊 Arquivos de Evidência

* **`Teste_ModoVulnerável.png`**
  * **O que demonstra:** O console do navegador exibindo o token `SessionID` em texto claro após o comando `document.cookie`, comprovando a vulnerabilidade a ataques XSS.

* **`Teste_ModoSeguro`**
  * **O que demonstra:** O console do navegador retornando vazio (`""`) após o mesmo comando, comprovando a eficácia e a proteção da flag `HttpOnly`.