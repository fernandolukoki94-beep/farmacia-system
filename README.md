# 💊 Sistema de Gestão de Stock Farmacêutico (Fullstack)

Este é um sistema robusto de controlo de inventário, vendas e autenticação de utilizadores, desenvolvido com foco em arquitetura RESTful, persistência de dados e segurança de rotas.

🚀 **Link do Projeto:** [Acede aqui ao Sistema Live](https://fernandolukoki94-beep.github.io/farmacia-system/)

---

## 🛠️ O Grande Diferencial Técnico (Mobile Development)
Todo o ecossistema deste projeto — desde a escrita do código, gestão da base de dados relacional (SQLite), controlo de versões com Git, até a preparação dos ficheiros para deploy — foi realizado de forma nativa dentro de um **ambiente mobile Linux utilizando o Termux (Android)**. Isto demonstra uma forte capacidade de adaptação técnica, resolução de problemas e domínio de ferramentas de terminal sob limitações de hardware.

---

## 🧰 Tecnologias Utilizadas
- **Backend:** Python 3, Flask (API REST)
- **Frontend:** HTML5, CSS3 (Modern Dark Mode), JavaScript (ES6 / Fetch API)
- **Base de Dados:** SQLite3
- **DevOps/Ambiente:** Git, GitHub, GitHub Pages, Render, Termux (Linux Mobile)

---

## 🎯 Funcionalidades Implementadas
- [x] **🔐 Tela de Autenticação (Login/Logout):** Sistema de validação de credenciais com proteção de rotas no Frontend (impede o acesso ao painel sem login ativo).
- [x] **📦 CRUD de Inventário:** API configurada para receber, ler e listar medicamentos diretamente de uma base de dados relacional.
- [x] **🔴 Baixa Automática de Stock:** Lógica de negócio que processa vendas e atualiza a quantidade disponível instantaneamente.
- [x] **⚡ Mecanismo de Contingência (Fallback):** O frontend possui uma lógica inteligente que deteta se o servidor em nuvem está em repouso e ativa uma simulação local, garantindo que o utilizador/recrutador consiga testar o fluxo completo sem interrupções.

