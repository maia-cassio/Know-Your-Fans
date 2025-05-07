📊 Know Your Fan
Know Your Fan é uma plataforma web completa para coletar, gerenciar e analisar dados de fãs de e-sports, desenvolvida com foco em performance, integração e usabilidade. A aplicação conta com backend em Python (Flask), frontend em React (Vite) e comunicação via API RESTful.

✅ Objetivo
O projeto tem como propósito central estreitar a relação entre clubes de e-sports e sua comunidade de fãs, por meio de um sistema robusto que permite:

Cadastro e gerenciamento de fãs.

Registro de preferências e comportamentos.

Visualização e análise de dados em tempo real.

Comunicação entre frontend e backend via API.

🧱 Tecnologias Utilizadas
🖥️ Frontend
React.js (com Vite para build rápido)

HTML5 + CSS3

JavaScript (ES6+)

Fetch API para consumir a API Flask

⚙️ Backend
Python 3.11+

Flask – microframework para construção da API

Flask-CORS – para permitir comunicação com o frontend

API RESTful – estrutura de rotas

🗂️ Estrutura do Projeto
arduino
Copiar
Editar
know-your-fan/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   └── requirements.txt
│   ├── venv/
│   └── run.py
│
└── frontend/
    ├── public/
    ├── src/
    │   ├── App.jsx
    │   ├── App.css
    │   └── main.jsx
    └── index.html
🔄 Comunicação Frontend ↔ Backend
O frontend realiza requisições HTTP para o backend Flask hospedado localmente na porta 5000. Exemplo de endpoint ativo:

nginx
Copiar
Editar
GET http://127.0.0.1:5000/api/hello
🚀 Como Executar o Projeto
🔧 1. Clonar o Repositório
bash
Copiar
Editar
git clone https://github.com/seu-usuario/know-your-fan.git
cd know-your-fan
🐍 2. Rodar o Backend (Flask)
bash
Copiar
Editar
cd backend
python -m venv venv
# Ative o ambiente virtual:
# Windows
.\venv\Scripts\activate
# Linux/macOS
source venv/bin/activate

pip install -r app/requirements.txt
python run.py
O backend estará rodando em http://127.0.0.1:5000

🌐 3. Rodar o Frontend (React + Vite)
bash
Copiar
Editar
cd frontend
npm install
npm run dev
O frontend estará rodando em http://localhost:5173

📈 Funcionalidades Planejadas
 API de boas-vindas (teste de integração)

 Cadastro de fãs com formulário

 Listagem e edição de fãs

 Dashboard com estatísticas e gráficos

 Upload de imagem de perfil do fã

 Integração com redes sociais

 IA para análise de comportamento

👨‍💻 Autor
Seu Nome Aqui
https://www.linkedin.com/in/cassio-maia-n/ | [GitHub](https://github.com/maia-cassio)

📃 Licença
Este projeto está licenciado sob a MIT License – veja o arquivo LICENSE para detalhes.
