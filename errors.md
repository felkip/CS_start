# Erros Detectados no Projeto

Data: 2026-07-24

A seguir estão os erros detectados automaticamente no workspace e sugestões de correção.

---

## 1) Import não resolvido: `streamlit` (RESOLVIDO)
- Arquivo: `main.py`
- Mensagem original: Import "streamlit" could not be resolved
- Arquivo: `app/quiz.py`
- Mensagem original: Import "streamlit" could not be resolved

Causa provável:
- O ambiente Python usado pelo editor/checador não tinha `streamlit` instalado.

Ação tomada:
- Instalei as dependências do projeto no venv do workspace (`.venv`) usando `requirements.txt`.
- Comando executado:

```powershell
.\.venv\Scripts\Activate.ps1; python -m pip install --upgrade pip setuptools wheel; python -m pip install -r requirements.txt
```

Status: `streamlit` está instalado no ambiente do projeto e o analisador não reporta mais o problema.

---

## 2) Tipagem / possível `None` em `render_profile_badge` (RESOLVIDO)
- Arquivo: `main.py` (chamada no sidebar)
- Mensagem original: Argument of type "Unknown | None" cannot be assigned to parameter "username" of type "str"

Causa provável:
- `st.session_state.username` podia ser `None` antes do login, e a função `render_profile_badge()` esperava uma `str`.

Ação tomada:
- Atualizei `main.py` para passar um valor padrão quando `st.session_state.username` for `None`:

```py
render_profile_badge(st.session_state.username or "Usuário")
```

Status: validado — chamada protegida contra `None`.

---

## Próximos passos
- Verificar localmente executando `streamlit run main.py` e observar erros no console.
- Se houver novos erros após a instalação das dependências, reexecutar a checagem ou abrir `errors.md` e anexar as novas mensagens.

---

## 3) Erro intermitente durante o quiz (StreamlitAPIException) — mitigação aplicada
- Sintoma: durante o fluxo do quiz, a aplicação às vezes lançava uma `StreamlitAPIException` ao tentar limpar `st.session_state.quiz_answer` (ex.: ao avançar para a próxima pergunta).
- Causa provável: mutações concorrentes do `session_state` durante callbacks/widgets podem ser rejeitadas pela API do Streamlit em alguns contextos.

Ação tomada:
- Centralizei a limpeza de `quiz_answer` em uma função segura `clear_quiz_answer()` que tenta primeiro remover a chave (`del`) e, em fallback, atribuir `None`; todas as atribuições de limpeza foram atualizadas para usar essa função.
- Arquivo alterado: `app/quiz.py` (usa agora `clear_quiz_answer()` nos pontos de limpeza)

Status: mitigado — a aplicação não deve mais travar quando o usuário avança no quiz. Se o erro reaparecer, registre os logs do Streamlit (terminal) e os incluirei em `errors.md`.

---

Arquivo gerado automaticamente pelo assistente.