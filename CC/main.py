import os
import sys
from pathlib import Path

import streamlit as st

# Adicionar pasta ao path para imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.auth import login_user, register_user
from app.quiz import init_quiz_state, render_quiz, reset_quiz_state, iniciar_quiz
from app.roadmap import render_roadmap
from app.theme import configure_theme
from app.ui import (
    get_icon_svg,
    header_principal,
    load_css,
    render_empty_state,
    render_feature_card,
    render_icon_button,
    render_icon_heading,
    render_icon_text_input,
    render_profile_badge,
)

# Configuração da página
st.set_page_config(
    page_title="CS Start",
    page_icon=Path(__file__).parent / "static" / "icons" / "rocket.svg",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Carregar CSS customizado
load_css()

# Inicializar session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.user_id = None
    st.session_state.username = None
if "current_page" not in st.session_state:
    st.session_state.current_page = "home"
if "theme" not in st.session_state:
    st.session_state.theme = "light"

init_quiz_state()

configure_theme()

# Header principal
header_principal()

if not st.session_state.logged_in:
    # Seção de autenticação
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("<div class='cs-auth-panel'>", unsafe_allow_html=True)
        
        tab1, tab2 = st.tabs(["Login", "Cadastro"])

        with tab1:
            render_icon_heading("Faça Login", "log-in")
            st.markdown("<p style='color: #64748b; margin-bottom: 1.5rem;'>Acesse sua conta para começar</p>", unsafe_allow_html=True)
            
            username = render_icon_text_input(
                "Usuário",
                "user-round",
                key="login_username",
                placeholder="Digite seu usuário",
            )
            password = render_icon_text_input(
                "Senha",
                "key-round",
                key="login_password",
                placeholder="Digite sua senha",
                input_type="password",
            )
            
            col_btn1, col_btn2 = st.columns(2)
            with col_btn1:
                if render_icon_button(
                    "Entrar",
                    "log-in",
                    key="login_submit",
                    primary=True,
                ):
                    if username and password:
                        success, user_id, message = login_user(username, password)
                        if success:
                            st.session_state.logged_in = True
                            st.session_state.user_id = user_id
                            st.session_state.username = username
                            st.success(message)
                            st.rerun()
                        else:
                            st.error(message)
                    else:
                        st.warning("Preencha todos os campos")

        with tab2:
            render_icon_heading("Criar Conta", "user-round-plus")
            st.markdown("<p style='color: #64748b; margin-bottom: 1.5rem;'>Junte-se à nossa comunidade</p>", unsafe_allow_html=True)
            
            new_username = render_icon_text_input(
                "Usuário",
                "user-round",
                key="register_username",
                placeholder="Escolha um usuário",
            )
            new_email = render_icon_text_input(
                "Email",
                "mail",
                key="register_email",
                placeholder="seu@email.com",
            )
            new_password = render_icon_text_input(
                "Senha",
                "key-round",
                key="register_password",
                placeholder="Digite uma senha",
                input_type="password",
            )
            confirm_password = render_icon_text_input(
                "Confirmar Senha",
                "lock-keyhole",
                key="confirm_password",
                placeholder="Confirme sua senha",
                input_type="password",
            )

            if render_icon_button(
                "Cadastrar",
                "user-round-plus",
                key="register_submit",
                primary=True,
            ):
                if not (new_username and new_email and new_password):
                    st.warning("Preencha todos os campos")
                elif new_password != confirm_password:
                    st.warning("As senhas não coincidem")
                else:
                    success, message = register_user(new_username, new_email, new_password)
                    if success:
                        st.success(message)
                        st.info("Você pode fazer login agora!")
                    else:
                        st.error(message)
        
        st.markdown("</div>", unsafe_allow_html=True)
    
    # Seção de features
    st.markdown("<div class='cs-section-spacer'></div>", unsafe_allow_html=True)
    render_icon_heading("O que você encontrará aqui", "sparkles")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        render_feature_card(
            "Quiz de Perfil",
            "Descubra seu perfil em Ciência da Computação com perguntas simples e diretas.",
            "target",
            "primary"
        )
    with col2:
        render_feature_card(
            "Roadmap Personalizado",
            "Receba um plano de estudos adaptado ao seu perfil e objetivos.",
            "map",
            "success"
        )
    with col3:
        render_feature_card(
            "Comunidade",
            "Conecte-se com outros iniciantes e compartilhe suas experiências.",
            "users-round",
            "warning"
        )

else:
    # Sidebar com menu de navegação
    with st.sidebar:
        render_icon_heading("Menu", "settings-2")
        
        render_profile_badge(st.session_state.username or "Usuário")

        nav_items = (
            ("Início", "house", "home"),
            ("Quiz", "target", "quiz"),
            ("Roadmap", "map", "roadmap"),
            ("Configurações", "settings-2", "settings"),
        )
        for label, icon_name, page in nav_items:
            if render_icon_button(
                label,
                icon_name,
                key=f"sidebar-nav-{page}",
                primary=st.session_state.current_page == page,
            ):
                st.session_state.current_page = page
                st.rerun()
        
        st.markdown("---")
        
        if render_icon_button("Sair", "log-out", key="sidebar-logout"):
            st.session_state.logged_in = False
            st.session_state.user_id = None
            st.session_state.username = None
            reset_quiz_state()
            st.rerun()
    
    # Página principal após login
    if st.session_state.current_page == "home":
        render_icon_heading(
            f"Bem-vindo de volta, {st.session_state.username}!",
            "house",
        )

        quiz_completed = st.session_state.get("quiz_completed")
        status_text = "Quiz completo" if quiz_completed else "Não iniciado"
        status_icon = "circle-check" if quiz_completed else "clock-3"
        profile_text = (
            st.session_state.get("quiz_result", {}).get("profile", "Desconhecido").title()
            if quiz_completed
            else "---"
        )
        roadmap_text = "Disponível" if quiz_completed else "Bloqueado"

        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown(
                f"""
                <div class="dashboard-card" style='
                    background: linear-gradient(135deg, #4f46e5 0%, #7c6ae8 100%);
                    color: white;
                    padding: 1.5rem;
                    border-radius: 14px;
                    text-align: center;
                    min-height: 170px;
                    display: flex;
                    flex-direction: column;
                    justify-content: center;
                    box-shadow: inset 0 1px 0 rgba(255,255,255,0.18), 0 12px 28px rgba(79, 70, 229, 0.25);
                '>
                    <div style='margin-bottom: 0.4rem;'>{get_icon_svg(status_icon, size=32)}</div>
                    <div style='font-size: 0.9rem; opacity: 0.9; margin-bottom: 0.4rem;'>Status</div>
                    <div style='font-size: 1.1rem; font-weight: 700;'>{status_text}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        with col2:
            st.markdown(
                f"""
                <div class="dashboard-card" style='
                    background: linear-gradient(135deg, #d946ef 0%, #ec4899 100%);
                    color: white;
                    padding: 1.5rem;
                    border-radius: 14px;
                    text-align: center;
                    min-height: 170px;
                    display: flex;
                    flex-direction: column;
                    justify-content: center;
                    box-shadow: inset 0 1px 0 rgba(255,255,255,0.18), 0 12px 28px rgba(236, 72, 153, 0.24);
                '>
                    <div style='margin-bottom: 0.4rem;'>{get_icon_svg("user-round", size=32)}</div>
                    <div style='font-size: 0.9rem; opacity: 0.9; margin-bottom: 0.4rem;'>Perfil</div>
                    <div style='font-size: 1.1rem; font-weight: 700;'>{profile_text}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        with col3:
            st.markdown(
                f"""
                <div class="dashboard-card" style='
                    background: linear-gradient(135deg, #0f766e 0%, #2dd4bf 100%);
                    color: white;
                    padding: 1.5rem;
                    border-radius: 14px;
                    text-align: center;
                    min-height: 170px;
                    display: flex;
                    flex-direction: column;
                    justify-content: center;
                    box-shadow: inset 0 1px 0 rgba(255,255,255,0.18), 0 12px 28px rgba(16, 185, 129, 0.24);
                '>
                    <div style='margin-bottom: 0.4rem;'>{get_icon_svg("map", size=32)}</div>
                    <div style='font-size: 0.9rem; opacity: 0.9; margin-bottom: 0.4rem;'>Roadmap</div>
                    <div style='font-size: 1.1rem; font-weight: 700;'>{roadmap_text}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        st.markdown("---")
        render_icon_heading("Próximos Passos", "arrow-right")

        col1, col2 = st.columns(2)
        dark_cards = st.session_state.theme == "dark"
        card_bg = "rgba(15, 23, 42, 0.9)" if dark_cards else "rgba(255,255,255,0.96)"
        card_border = "1px solid rgba(148, 163, 184, 0.25)" if dark_cards else "1px solid #e2e8f0"
        card_title = "#f8fafc" if dark_cards else "#0f172a"
        card_text = "#cbd5e1" if dark_cards else "#475569"

        with col1:
            st.markdown(
                f"""
                <div class="dashboard-card" style='
                    background: {card_bg};
                    border: {card_border};
                    border-radius: 14px;
                    padding: 1.5rem;
                    min-height: 210px;
                '>
                    <h3 style='margin-top: 0; color: {card_title};'><span class="cs-heading-icon">{get_icon_svg("target", size=20)}</span> Quiz de Perfil</h3>
                    <p style='color: {card_text}; margin: 0; line-height: 1.6;'>Responda 5 perguntas simples para descobrir qual é o seu perfil em Ciência da Computação.</p>
                </div>
                """,
                unsafe_allow_html=True,
            )
            if render_icon_button("Começar Quiz", "target", key="home-start-quiz"):
                iniciar_quiz()
                st.session_state.current_page = "quiz"
                st.rerun()

        with col2:
            st.markdown(
                f"""
                <div class="dashboard-card" style='
                    background: {card_bg};
                    border: {card_border};
                    border-radius: 14px;
                    padding: 1.5rem;
                    min-height: 210px;
                '>
                    <h3 style='margin-top: 0; color: {card_title};'><span class="cs-heading-icon">{get_icon_svg("map", size=20)}</span> Seu Roadmap</h3>
                    <p style='color: {card_text}; margin: 0; line-height: 1.6;'>Veja o plano de estudos personalizado de acordo com seu perfil.</p>
                </div>
                """,
                unsafe_allow_html=True,
            )
            if render_icon_button(
                "Ver Roadmap",
                "map",
                key="home-open-roadmap",
                disabled=not quiz_completed,
            ):
                st.session_state.current_page = "roadmap"
                st.rerun()
    
    elif st.session_state.current_page == "quiz":
        render_icon_heading("Quiz de Perfil", "target")
        st.markdown("Responda algumas perguntas para descobrir seu perfil em Ciência da Computação!")
        st.markdown("---")
        render_quiz()
    
    elif st.session_state.current_page == "roadmap":
        render_icon_heading("Seu Roadmap de Estudos", "map")
        
        if st.session_state.get("quiz_completed") and st.session_state.get("quiz_result"):
            profile = st.session_state.quiz_result.get("profile")
            st.markdown(f"**Perfil Detectado:** {profile.title()}")
            st.markdown("---")
            render_roadmap(profile)
        else:
            render_empty_state(
                "Quiz não realizado",
                "Complete o quiz primeiro para ver seu roadmap personalizado.",
                "book-open",
            )
            if render_icon_button("Fazer Quiz Agora", "target", key="roadmap-start-quiz"):
                iniciar_quiz()
                st.session_state.current_page = "quiz"
                st.rerun()
    
    elif st.session_state.current_page == "settings":
        render_icon_heading("Configurações", "settings-2")
        
        with st.container(border=True):
            render_icon_heading("Perfil do Usuário", "user-round", level=4)
            col1, col2 = st.columns(2)
            with col1:
                st.markdown(f"**Usuário:** {st.session_state.username}")
            with col2:
                st.markdown(f"**ID:** {st.session_state.user_id}")
        
        with st.container(border=True):
            render_icon_heading("Quiz", "target", level=4)
            if st.session_state.get("quiz_completed"):
                st.success("Quiz Completado")
                profile = st.session_state.quiz_result.get("profile")
                st.markdown(f"**Seu Perfil:** {profile.title()}")
                
                if render_icon_button("Fazer outro quiz", "target", key="settings-restart-quiz"):
                    iniciar_quiz()
                    st.session_state.current_page = "quiz"
                    st.rerun()
            else:
                st.info("Quiz não realizado ainda")
                if render_icon_button("Começar Quiz", "target", key="settings-start-quiz"):
                    iniciar_quiz()
                    st.session_state.current_page = "quiz"
                    st.rerun()
