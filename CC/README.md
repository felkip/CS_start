# 🎓 CS Start

![Python](https://img.shields.io/badge/Python-3.13+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![Supabase](https://img.shields.io/badge/Supabase-3ECF8E?style=for-the-badge&logo=supabase&logoColor=white)
![GitHub last commit](https://img.shields.io/github/last-commit/felkip/CC_start?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-success?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-orange?style=for-the-badge)

Aplicação desenvolvida em **Python** e **Streamlit** para ajudar pessoas que estão pensando em ingressar ou que estão iniciando o curso de **Ciência da Computação**.

O **CS Start** surgiu como um projeto de estudo e portfólio com foco em desenvolvimento de aplicações web utilizando Python, PostgreSQL e Streamlit. O objetivo é orientar estudantes em seus primeiros passos na graduação por meio de uma experiência simples, interativa e intuitiva.

> 🚧 **Projeto em desenvolvimento.**

---

# 📸 Demonstração

Adicione aqui capturas de tela ou GIFs da aplicação.

| Tela | Descrição |
|------|-----------|
| 🏠 Home | Página inicial |
| 🔐 Login | Autenticação de usuários |
| 📝 Cadastro | Criação de conta |
| 📋 Quiz | Identificação do perfil |
| 🗺️ Roadmap | Plano inicial de estudos |

---

# ✨ Funcionalidades

- ✅ Cadastro de usuários
- ✅ Login seguro
- ✅ Criptografia de senhas com bcrypt
- ✅ Integração com PostgreSQL
- ✅ Banco hospedado no Supabase
- ✅ Quiz para identificar o perfil do estudante
- ✅ Roadmap inicial de estudos
- ✅ Interface desenvolvida com Streamlit
- ✅ Arquitetura modular
- ✅ Testes automatizados

---

# 🛠️ Tecnologias

- Python
- Streamlit
- PostgreSQL
- Supabase
- psycopg2-binary
- bcrypt
- python-dotenv
- pytest
- CSS
- Git
- GitHub

---

# 📦 Dependências

As principais dependências utilizadas são:

| Biblioteca | Finalidade |
|------------|------------|
| Streamlit | Interface da aplicação |
| psycopg2-binary | Integração com PostgreSQL |
| bcrypt | Criptografia de senhas |
| python-dotenv | Variáveis de ambiente |
| pytest | Testes automatizados |

Todas as dependências podem ser instaladas com:

```bash
pip install -r requirements.txt
```

---

# 📂 Estrutura do Projeto

```text
CS Start
│
├── .devcontainer/
│
├── app/
│   ├── auth.py
│   ├── quiz.py
│   ├── roadmap.py
│   └── ui.py
│
├── config/
│   ├── __init__.py
│   └── db_config.py
│
├── database/
│   └── schema.sql
│
├── static/
│   └── style.css
│
├── tests/
│
├── .env.example
├── cleanup_suggestions.md
├── config.toml
├── errors.md
├── updates_from_mvp.md
├── LICENSE
├── main.py
├── plano_quiz.md
├── plano_roadmap.md
├── README.md
└── requirements.txt
```

---

# 🚀 Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/felkip/CC_start.git
cd CC_start
```

---

### 2. Criar ambiente virtual

Recomenda-se utilizar **Python 3.13 ou superior**.

**Windows (com Python Launcher):**

```bash
py -3.13 -m venv venv
.\venv\Scripts\activate
```

Caso não tenha o Python Launcher instalado:

```bash
python -m venv venv
.\venv\Scripts\activate
```

**Linux/macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Atualizar instaladores e instalar dependências

```bash
python -m pip install --upgrade pip setuptools wheel
python -m pip install -r requirements.txt
```

---

### 4. Configurar variáveis de ambiente

Copie:

```text
.env.example
```

para

```text
.env
```

Configure:

```env
DB_HOST=
DB_PORT=
DB_NAME=
DB_USER=
DB_PASSWORD=
```

O projeto suporta:

- PostgreSQL local
- PostgreSQL hospedado no Supabase

---

### 5. Executar a aplicação

```bash
streamlit run main.py
```

---

# 🧪 Testes

Execute os testes com:

```bash
pytest
```

---

# 📖 Documentação

O projeto inclui documentos auxiliares durante o desenvolvimento:

| Arquivo | Descrição |
|----------|-----------|
| updates_from_mvp.md | Histórico das melhorias |
| cleanup_suggestions.md | Sugestões de refatoração |
| errors.md | Registro dos problemas encontrados |
| plano_quiz.md | Planejamento do Quiz |
| plano_roadmap.md | Planejamento do Roadmap |

---

# 🎯 Objetivos

Este projeto busca praticar:

- Desenvolvimento de aplicações Python
- Arquitetura de software
- PostgreSQL
- Integração com Supabase
- Desenvolvimento Web com Streamlit
- UI/UX
- Organização de código
- Git e GitHub
- Construção de projetos para portfólio

---

# 🚧 Status do Projeto

### ✅ Implementado

- Login
- Cadastro
- PostgreSQL
- Supabase
- Quiz
- Roadmap
- Testes básicos
- Melhorias de UI/UX

### 🔄 Em desenvolvimento

- Dashboard do estudante
- Histórico de progresso
- Recomendações mais inteligentes
- Novos conteúdos
- Melhor cobertura de testes
- Melhor responsividade

---

# 💡 Aprendizados

Durante o desenvolvimento deste projeto foram praticados conceitos como:

- Autenticação de usuários
- Criptografia de senhas
- PostgreSQL
- Integração com Supabase
- Organização modular
- Testes automatizados
- Desenvolvimento com Streamlit
- Variáveis de ambiente
- Deploy com Streamlit Community Cloud

---

# 🤝 Contribuições

Sugestões, feedbacks e melhorias são sempre bem-vindos.

Caso encontre algum problema ou tenha alguma ideia de melhoria, fique à vontade para abrir uma **Issue** ou enviar um **Pull Request**.

---

# 📄 Licença

Este projeto está licenciado sob a licença **MIT**.

Consulte o arquivo `LICENSE` para mais informações.

---

# 👨‍💻 Autor

**Luís Felipe Carmelo da Silva**

- GitHub: https://github.com/felkip
- LinkedIn: https://www.linkedin.com/in/luis-felipe-carmelo-83656929b
