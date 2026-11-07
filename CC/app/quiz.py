import streamlit as st
from app.ui import (
    get_icon_svg,
    render_empty_state,
    render_icon_button,
    render_icon_heading,
    render_quiz_progress,
)

QUESTIONS = [
    {
        "pergunta": "O que mais te atrai em tecnologia?",
        "opcoes": [
            {"texto": "Criar soluções e programas", "valor": "programming"},
            {"texto": "Explorar ferramentas e novidades", "valor": "tech"},
            {"texto": "Entender o básico com calma", "valor": "beginner"},
        ],
    },
    {
        "pergunta": "Quando encontra um problema, o que costuma fazer?",
        "opcoes": [
            {"texto": "Tentar resolver logicamente", "valor": "programming"},
            {"texto": "Buscar formas novas de lidar com ele", "valor": "tech"},
            {"texto": "Pedir ajuda e aprender passo a passo", "valor": "beginner"},
        ],
    },
    {
        "pergunta": "Você gosta mais de:",
        "opcoes": [
            {"texto": "Pensar em algoritmos e estrutura", "valor": "programming"},
            {"texto": "Testar apps e produtos digitais", "valor": "tech"},
            {"texto": "Aprender fundamentos primeiro", "valor": "beginner"},
        ],
    },
    {
        "pergunta": "Como prefere aprender algo novo?",
        "opcoes": [
            {"texto": "Com exercícios práticos", "valor": "programming"},
            {"texto": "Com exemplos modernos e tecnológicos", "valor": "tech"},
            {"texto": "Com explicações simples e repetição", "valor": "beginner"},
        ],
    },
    {
        "pergunta": "O que te inspira mais?",
        "opcoes": [
            {"texto": "Construir algo do zero", "valor": "programming"},
            {"texto": "Ver novas ideias ganhando forma", "valor": "tech"},
            {"texto": "Crescer com passos pequenos", "valor": "beginner"},
        ],
    },
]


def init_quiz_state():
    if "quiz_started" not in st.session_state:
        st.session_state.quiz_started = False
    if "quiz_completed" not in st.session_state:
        st.session_state.quiz_completed = False
    if "quiz_step" not in st.session_state:
        st.session_state.quiz_step = 0
    if "quiz_scores" not in st.session_state:
        st.session_state.quiz_scores = {"programming": 0, "tech": 0, "beginner": 0}
    if "quiz_result" not in st.session_state:
        st.session_state.quiz_result = None
    if "quiz_answer" not in st.session_state:
        st.session_state.quiz_answer = None


def clear_quiz_answer():
    """Tenta remover a chave `quiz_answer` do session_state; se falhar, atribui None com segurança."""
    try:
        if "quiz_answer" in st.session_state:
            del st.session_state["quiz_answer"]
    except Exception:
        try:
            st.session_state.quiz_answer = None
        except Exception:
            pass


def iniciar_quiz():
    init_quiz_state()
    st.session_state.quiz_started = True
    st.session_state.quiz_completed = False
    st.session_state.quiz_step = 0
    st.session_state.quiz_scores = {"programming": 0, "tech": 0, "beginner": 0}
    st.session_state.quiz_result = None
    st.session_state.quiz_answer = None


def reset_quiz_state():
    init_quiz_state()
    st.session_state.quiz_started = False
    st.session_state.quiz_completed = False
    st.session_state.quiz_step = 0
    st.session_state.quiz_scores = {"programming": 0, "tech": 0, "beginner": 0}
    st.session_state.quiz_result = None
    st.session_state.quiz_answer = None


def calcular_result(scores):
    perfil = max(scores, key=scores.get)
    resultados = {
        "programming": {
            "titulo": "Perfil de Programação",
            "descricao": "Você tende a gostar de resolver problemas, pensar logicamente e criar soluções.",
            "profile": "programming",
        },
        "tech": {
            "titulo": "Perfil de Tecnologia",
            "descricao": "Você se interessa por ferramentas, inovação e por explorar o universo tecnológico.",
            "profile": "tech",
        },
        "beginner": {
            "titulo": "Perfil de Início",
            "descricao": "Você está começando e pode evoluir com passos simples, práticos e bem guiados.",
            "profile": "beginner",
        },
    }
    return resultados[perfil]


def render_quiz():
    init_quiz_state()

    if not st.session_state.quiz_started:
        render_empty_state(
            "Quiz não iniciado",
            "Clique em 'Começar Quiz' no menu lateral para descobrir seu perfil em Ciência da Computação.",
            "target",
        )
        return

    st.markdown("---")

    if not st.session_state.quiz_completed:
        total_perguntas = len(QUESTIONS)
        pergunta_atual = QUESTIONS[st.session_state.quiz_step]
        progresso = (st.session_state.quiz_step + 1) / total_perguntas
        # Barra de progresso customizada
        render_quiz_progress(st.session_state.quiz_step + 1, total_perguntas)

        # Pergunta
        st.markdown(
            f"""
            <div style='
                background: var(--bg-surface);
                border: 1px solid var(--border);
                border-left: 4px solid var(--brand-primary);
                border-radius: 8px;
                padding: 1.5rem;
                margin-bottom: 2rem;
            '>
                <p style='color: var(--text-secondary); margin: 0; font-size: 0.9rem;'>Pergunta {st.session_state.quiz_step + 1} de {total_perguntas}</p>
                <h3 style='color: var(--text-primary); margin: 0.5rem 0 0 0;'>{pergunta_atual["pergunta"]}</h3>
            </div>
            """,
            unsafe_allow_html=True
        )

        # Opções com melhor design
        st.markdown("<p style='color: var(--text-secondary); font-weight: 600; margin-bottom: 1rem;'>Escolha uma opção:</p>", unsafe_allow_html=True)
        
        resposta = st.radio(
            "Escolha uma opção:",
            [opcao["texto"] for opcao in pergunta_atual["opcoes"]],
            key="quiz_answer",
            label_visibility="collapsed"
        )

        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            is_last_question = st.session_state.quiz_step == total_perguntas - 1
            button_text = "Ver Resultado" if is_last_question else "Próxima"
            button_icon = "circle-check" if is_last_question else "arrow-right"
            
            if render_icon_button(
                button_text,
                button_icon,
                key="quiz_continue",
            ):
                if resposta:
                    opcao_escolhida = next(
                        opcao for opcao in pergunta_atual["opcoes"] if opcao["texto"] == resposta
                    )
                    st.session_state.quiz_scores[opcao_escolhida["valor"]] += 1

                    if st.session_state.quiz_step < total_perguntas - 1:
                        st.session_state.quiz_step += 1
                        clear_quiz_answer()
                        st.rerun()
                    else:
                        st.session_state.quiz_completed = True
                        st.session_state.quiz_result = calcular_result(st.session_state.quiz_scores)
                        clear_quiz_answer()
                        st.rerun()
                else:
                    st.warning("Selecione uma opção para continuar.")
    else:
        # Resultado do quiz
        result = st.session_state.quiz_result
        profile = result["profile"]
        
        # Cards de resultado com gradientes
        profile_colors = {
            "programming": {
                "accent": "var(--brand-primary-text)",
                "icon": "code",
            },
            "tech": {
                "accent": "var(--brand-accent-text)",
                "icon": "monitor",
            },
            "beginner": {
                "accent": "var(--brand-secondary-text)",
                "icon": "sparkles",
            },
        }

        color_info = profile_colors.get(profile, profile_colors["beginner"])
        profile_icon = get_icon_svg(color_info["icon"], size=44)

        st.markdown(
            f"""
            <div style='
                background: var(--bg-surface);
                border: 1px solid var(--border);
                border-top: 4px solid {color_info["accent"]};
                color: var(--text-primary);
                border-radius: 12px;
                padding: 2rem;
                text-align: center;
                margin-bottom: 2rem;
                box-shadow: 0 8px 20px var(--shadow);
            '>
                <p class="cs-profile-result-icon" style='color: {color_info["accent"]} !important;'>{profile_icon}</p>
                <h2 style='color: var(--text-primary) !important; margin: 1rem 0 0.5rem 0;'>{result["titulo"]}</h2>
                <p style='color: var(--text-secondary) !important; margin: 0; font-size: 1.1rem;'>{result["descricao"]}</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        # Pontuações
        render_icon_heading("Seus Resultados", "chart-no-axes-column-increasing")
        col1, col2, col3 = st.columns(3)
        
        scores = st.session_state.quiz_scores
        
        with col1:
            st.markdown(
                f"""
                <div style='
                    background: var(--bg-surface);
                    border-radius: 8px;
                    padding: 1.5rem;
                    text-align: center;
                    border: 1px solid var(--border);
                    border-top: 3px solid var(--brand-primary-text);
                '>
                    <p style='color: var(--brand-primary-text); margin: 0; font-size: 0.9rem;'>{get_icon_svg("code", size=18)} Programação</p>
                    <p style='color: var(--text-primary); margin: 0.5rem 0 0 0; font-size: 1.8rem; font-weight: 700;'>{scores["programming"]}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

        with col2:
            st.markdown(
                f"""
                <div style='
                    background: var(--bg-surface);
                    border-radius: 8px;
                    padding: 1.5rem;
                    text-align: center;
                    border: 1px solid var(--border);
                    border-top: 3px solid var(--brand-accent-text);
                '>
                    <p style='color: var(--brand-accent-text); margin: 0; font-size: 0.9rem;'>{get_icon_svg("monitor", size=18)} Tecnologia</p>
                    <p style='color: var(--text-primary); margin: 0.5rem 0 0 0; font-size: 1.8rem; font-weight: 700;'>{scores["tech"]}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

        with col3:
            st.markdown(
                f"""
                <div style='
                    background: var(--bg-surface);
                    border-radius: 8px;
                    padding: 1.5rem;
                    text-align: center;
                    border: 1px solid var(--border);
                    border-top: 3px solid var(--brand-secondary-text);
                '>
                    <p style='color: var(--brand-secondary-text); margin: 0; font-size: 0.9rem;'>{get_icon_svg("sparkles", size=18)} Iniciante</p>
                    <p style='color: var(--text-primary); margin: 0.5rem 0 0 0; font-size: 1.8rem; font-weight: 700;'>{scores["beginner"]}</p>
                </div>
                """,
                unsafe_allow_html=True
            )
        
        st.markdown("---")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            if render_icon_button("Ver Roadmap", "map", key="quiz_open_roadmap"):
                st.session_state.current_page = "roadmap"
                st.rerun()

        with col2:
            if render_icon_button("Fazer outro quiz", "target", key="quiz_restart"):
                iniciar_quiz()
                st.session_state.current_page = "quiz"
                st.rerun()

        with col3:
            if render_icon_button("Voltar ao Início", "house", key="quiz_home"):
                st.session_state.current_page = "home"
                st.rerun()

        st.markdown(
            "<p style='color: var(--text-secondary); margin-top: 1rem;'>"
            "Seu resultado é uma primeira indicação de perfil. Pode ser ajustado "
            "conforme você avança nos estudos."
            "</p>",
            unsafe_allow_html=True,
        )
