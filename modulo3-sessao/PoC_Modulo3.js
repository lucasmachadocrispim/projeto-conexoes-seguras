 function efetuarLogin(event) {
            event.preventDefault();
            
            const modo = document.querySelector('input[name="seguranca"]:checked').value;
            const usuario = document.getElementById('username').value;

            if (modo === 'vulneravel') {
                // Cenário 1: Criando cookie normal gerado na sessão
                document.cookie = "SessionID_Corporativo=SESSION_TOKEN_VULNERABLE_HTTP_849302; path=/; SameSite=Lax";
                alert(`Login efetuado como ${usuario}!\n\n[TESTE VULNERÁVEL]: Abra o console (F12) e digite 'document.cookie' para capturar o token.`);
            } else {
                // Cenário 2: Simulação do comportamento HttpOnly
                // Limpamos o escopo do JS para provar como o navegador protege a string de sessão
                document.cookie = "SessionID_Corporativo=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
                
                alert(`Login efetuado como ${usuario}!\n\n[TESTE SEGURO]: O Cookie foi protegido. Digite 'document.cookie' no console para verificar a proteção.`);
            }
        }