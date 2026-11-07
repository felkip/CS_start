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

## Estrutura do Projeto

```
CS Start/
├── app/                 # Módulos da aplicação
│   ├── auth.py         # Sistema de autenticação
│   ├── quiz.py         # Lógica do quiz de perfil
│   ├── learning.py     # Categorias de aprendizagem por perfil
│   ├── roadmap.py      # Roadmap sugerido por perfil
│   └── ui.py           # Componentes visuais reutilizáveis
├── config/             # Configurações
│   └── db_config.py    # Configuração do banco de dados
├── database/           # Scripts SQL
│   └── schema.sql      # Schema do banco
├── static/             # Arquivos estáticos (CSS, imagens e ícones)
│   ├── style.css       # Estilos personalizados
│   └── icons/          # Ícones Lucide em SVG e licenças
├── .streamlit/         # Configurações do Streamlit
│   └── config.toml
├── main.py             # Aplicação principal (Streamlit)
├── requirements.txt    # Dependências Python
├── tests/              # Testes do projeto
├── .env.example        # Exemplo de variáveis de ambiente
├── CHANGELOG.md        # Histórico de mudanças do projeto
├── design_system.md    # Tokens, paleta e diretrizes visuais
├── errors.md           # Registro de erros e correções
├── cleanup_suggestions.md # Sugestões de limpeza do repositório
└── README.md           # Documentação principal do projeto
```

## Funcionalidades

### ✅ Implementadas
- **Login e Cadastro** - Sistema de autenticação com senhas criptografadas
- **Quiz de Perfil** - Perguntas guiadas para identificar afinidade com computação
- **Roadmap de Estudos** - Sugestão de estudo com base no perfil
- **Materiais e módulos de aprendizagem** - 13 módulos iniciais com recursos externos, atividades práticas e filtros por categoria, nível e etapa do roadmap, personalizados pelo perfil do quiz
- **UI Aprimorada** - Layout renovado com sidebar, cards e componentes visuais
- **Tema claro/escuro** - Alternância do tema e ajuste de contraste para melhorar a experiência visual
- **Ícones Lucide** - SVGs locais com licenças incluídas, adotados gradualmente na interface
- **Design System** - Paleta, tokens e diretrizes visuais documentados em `design_system.md`
- **Documentação de mudanças** - changelog e arquivos de suporte para histórico e limpeza

### 🔄 Em Desenvolvimento
- **Recomendações personalizadas** - sugestões mais completas no roadmap
- **Aprimoramentos visuais adicionais** - refinamento de layout e UX

## Instalação

### 1. Clonar o projeto
```bash
cd "C:\Users\lfcar\OneDrive\Desktop\CC"
```

### 2. Criar ambiente virtual
Use Python 3.13 ou 3.14 para evitar problemas de compatibilidade.
```bash
py -3.13 -m venv .venv
.\.venv\Scripts\activate
```
Se não tiver o launcher do Windows, use:
```bash
python -m venv .venv
.\.venv\Scripts\activate
```

### 3. Atualizar instaladores e instalar dependências
```bash
python -m pip install --upgrade pip setuptools wheel
python -m pip install -r requirements.txt
```

> `requirements.txt` inclui agora `pytest` para facilitar testes locais.

### 4. Configurar banco de dados

#### Opção A: PostgreSQL Local
1. Instale PostgreSQL (https://www.postgresql.org/download/)
2. Abra o pgAdmin ou psql
3. Execute o arquivo `database/schema.sql`
4. Copie `.env.example` para `.env` e configure as credenciais

#### Opção B: Supabase (PostgreSQL em Nuvem)
1. Crie uma conta em https://supabase.com
2. Execute o arquivo `database/schema.sql` no editor SQL
3. Copie a connection string para `.env`

### 5. Executar a aplicação
```bash
streamlit run main.py
```

A aplicação abrirá em `http://localhost:8501`

### 6. Executar testes
```bash
python -m pytest -q
```

## Observações importantes

- Não commite o arquivo `.env`.
- Não commite pastas de ambiente virtual como `.venv/`.
- Arquivos de cache como `__pycache__/` e `.pytest_cache/` devem ser ignorados.

## Regras do Projeto

- ✅ Código simples
- ✅ Priorizar funcionamento
- ✅ Uma funcionalidade por vez
- ✅ Manter arquivos organizados

## Próximas Tarefas

- [x] Implementar Quiz de Perfil
- [x] Implementar Roadmap de estudos
- [x] Adicionar interface visual melhorada
- [x] Adicionar materiais de aprendizagem por perfil
- [x] Revisar paleta e design system inicial
- [ ] Implementar sistema de recomendações mais avançado
- [ ] Melhorar a experiência visual em telas e estados pendentes


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
