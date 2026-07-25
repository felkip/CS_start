import os
import sys

import streamlit as st

# Adicionar pasta ao path para imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.auth import login_user, register_user
from app.quiz import init_quiz_state, render_quiz, reset_quiz_state, iniciar_quiz
from app.roadmap import render_roadmap
from app.ui import load_css, header_principal, render_profile_badge, render_feature_card, render_empty_state

# Configuração da página
st.set_page_config(
    page_title="CS Start",
    page_icon="🚀",
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

init_quiz_state()

# Header principal
header_principal()

if not st.session_state.logged_in:
    # Seção de autenticação
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("<div style='padding: 2rem; background: white; border-radius: 16px; box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1);'>", unsafe_allow_html=True)
        
        tab1, tab2 = st.tabs(["🔐 Login", "📝 Cadastro"])

        with tab1:
            st.markdown("### Faça Login")
            st.markdown("<p style='color: #64748b; margin-bottom: 1.5rem;'>Acesse sua conta para começar</p>", unsafe_allow_html=True)
            
            username = st.text_input("👤 Usuário", key="login_username", placeholder="Digite seu usuário")
            password = st.text_input("🔑 Senha", type="password", key="login_password", placeholder="Digite sua senha")
            
            col_btn1, col_btn2 = st.columns(2)
            with col_btn1:
                if st.button("🚀 Entrar", use_container_width=True):
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
                        st.warning("⚠️ Preencha todos os campos")

        with tab2:
            st.markdown("### Criar Conta")
            st.markdown("<p style='color: #64748b; margin-bottom: 1.5rem;'>Junte-se à nossa comunidade</p>", unsafe_allow_html=True)
            
            new_username = st.text_input("👤 Usuário", key="register_username", placeholder="Escolha um usuário")
            new_email = st.text_input("📧 Email", key="register_email", placeholder="seu@email.com")
            new_password = st.text_input("🔑 Senha", type="password", key="register_password", placeholder="Digite uma senha")
            confirm_password = st.text_input("🔐 Confirmar Senha", type="password", key="confirm_password", placeholder="Confirme sua senha")

            if st.button("📝 Cadastrar", use_container_width=True):
                if not (new_username and new_email and new_password):
                    st.warning("⚠️ Preencha todos os campos")
                elif new_password != confirm_password:
                    st.warning("❌ As senhas não coincidem")
                else:
                    success, message = register_user(new_username, new_email, new_password)
                    if success:
                        st.success(message)
                        st.info("✅ Você pode fazer login agora!")
                    else:
                        st.error(message)
        
        st.markdown("</div>", unsafe_allow_html=True)
    
    # Seção de features
    st.markdown("<div style='margin-top: 3rem;'></div>", unsafe_allow_html=True)
    st.markdown("### 🌟 O que você encontrará aqui", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        render_feature_card(
            "Quiz de Perfil",
            "Descubra seu perfil em Ciência da Computação com perguntas simples e diretas.",
            "🎯",
            "primary"
        )
    with col2:
        render_feature_card(
            "Roadmap Personalizado",
            "Receba um plano de estudos adaptado ao seu perfil e objetivos.",
            "🗺️",
            "success"
        )
    with col3:
        render_feature_card(
            "Comunidade",
            "Conecte-se com outros iniciantes e compartilhe suas experiências.",
            "👥",
            "warning"
        )

else:
    # Sidebar com menu de navegação
    with st.sidebar:
        st.markdown("### 📋 Menu")
        
        render_profile_badge(st.session_state.username or "Usuário")

        # Sincroniza `current_page` com a opção do menu (permite navegação via botões)
        if st.session_state.get("current_page") == "quiz":
            st.session_state.menu_option = "🎯 Quiz"
        elif st.session_state.get("current_page") == "roadmap":
            st.session_state.menu_option = "🗺️ Roadmap"

        menu_option = st.radio(
            "Navegação",
            options=["🏠 Início", "🎯 Quiz", "🗺️ Roadmap", "⚙️ Configurações"],
            label_visibility="collapsed",
            key="menu_option"
        )
        
        st.markdown("---")
        
        if st.button("🚪 Sair", use_container_width=True):
            st.session_state.logged_in = False
            st.session_state.user_id = None
            st.session_state.username = None
            reset_quiz_state()
            st.rerun()
    
    # Página principal após login
    if menu_option == "🏠 Início":
        st.markdown(f"### Bem-vindo de volta, {st.session_state.username}! 🎉", unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown(
                """
                <div style='
                    background: linear-gradient(135deg, #667eea, #764ba2);
                    color: white;
                    padding: 1.5rem;
                    border-radius: 12px;
                    text-align: center;
                '>
                    <p style='font-size: 2rem; margin: 0;'>🎯</p>
                    <p style='margin: 0.5rem 0 0 0; font-size: 0.9rem; opacity: 0.9;'>Status</p>
                    <p style='margin: 0; font-size: 1.2rem; font-weight: 600;'>
                        {'✅ Quiz Completo' if st.session_state.get('quiz_completed') else '⏳ Não iniciado'}
                    </p>
                </div>
                """,
                unsafe_allow_html=True
            )
        with col2:
            st.markdown(
                f"""
                <div style='
                    background: linear-gradient(135deg, #ec4899, #f472b6);
                    color: white;
                    padding: 1.5rem;
                    border-radius: 12px;
                    text-align: center;
                '>
                    <p style='font-size: 2rem; margin: 0;'>🗺️</p>
                    <p style='margin: 0.5rem 0 0 0; font-size: 0.9rem; opacity: 0.9;'>Perfil</p>
                    <p style='margin: 0; font-size: 1.2rem; font-weight: 600;'>
                        {st.session_state.get('quiz_result', {}).get('profile', 'Desconhecido').title() if st.session_state.get('quiz_completed') else '---'}
                    </p>
                </div>
                """,
                unsafe_allow_html=True
            )
        with col3:
            st.markdown(
                """
                <div style='
                    background: linear-gradient(135deg, #10b981, #34d399);
                    color: white;
                    padding: 1.5rem;
                    border-radius: 12px;
                    text-align: center;
                '>
                    <p style='font-size: 2rem; margin: 0;'>📚</p>
                    <p style='margin: 0.5rem 0 0 0; font-size: 0.9rem; opacity: 0.9;'>Roadmap</p>
                    <p style='margin: 0; font-size: 1.2rem; font-weight: 600;'>
                        {'Disponível' if st.session_state.get('quiz_completed') else 'Bloqueado'}
                    </p>
                </div>
                """,
                unsafe_allow_html=True
            )
        
        st.markdown("---")
        
        st.markdown("### 🚀 Próximos Passos")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown(
                """
                <div style='
                    background: white;
                    border: 2px solid #e2e8f0;
                    border-radius: 12px;
                    padding: 1.5rem;
                '>
                    <h3 style='margin-top: 0; color: #1e293b;'>📋 Quiz de Perfil</h3>
                    <p style='color: #64748b;'>Responda 5 perguntas simples para descobrir qual é o seu perfil em Ciência da Computação.</p>
                </div>
                """,
                unsafe_allow_html=True
            )
            if st.button("🎯 Começar Quiz", use_container_width=True):
                iniciar_quiz()
                st.session_state.current_page = "quiz"
                st.rerun()
        
        with col2:
            st.markdown(
                """
                <div style='
                    background: white;
                    border: 2px solid #e2e8f0;
                    border-radius: 12px;
                    padding: 1.5rem;
                '>
                    <h3 style='margin-top: 0; color: #1e293b;'>🗺️ Seu Roadmap</h3>
                    <p style='color: #64748b;'>Veja o plano de estudos personalizado de acordo com seu perfil.</p>
                </div>
                """,
                unsafe_allow_html=True
            )
            if st.session_state.get("quiz_completed"):
                if st.button("📚 Ver Roadmap", use_container_width=True):
                    st.session_state.current_page = "roadmap"
                    st.rerun()
            else:
                st.button("📚 Ver Roadmap", use_container_width=True, disabled=True)
    
    elif menu_option == "🎯 Quiz":
        st.markdown("### 🎯 Quiz de Perfil")
        st.markdown("Responda algumas perguntas para descobrir seu perfil em Ciência da Computação!")
        st.markdown("---")
        render_quiz()
    
    elif menu_option == "🗺️ Roadmap":
        st.markdown("### 🗺️ Seu Roadmap de Estudos")
        
        if st.session_state.get("quiz_completed") and st.session_state.get("quiz_result"):
            profile = st.session_state.quiz_result.get("profile")
            st.markdown(f"**Perfil Detectado:** {profile.title()}")
            st.markdown("---")
            render_roadmap(profile)
        else:
            render_empty_state(
                "Quiz não realizado",
                "Complete o quiz primeiro para ver seu roadmap personalizado.",
                "📭"
            )
            if st.button("🎯 Fazer Quiz Agora"):
                iniciar_quiz()
                st.session_state.current_page = "quiz"
                st.rerun()
    
    elif menu_option == "⚙️ Configurações":
        st.markdown("### ⚙️ Configurações")
        
        with st.container(border=True):
            st.markdown("#### 👤 Perfil do Usuário")
            col1, col2 = st.columns(2)
            with col1:
                st.markdown(f"**Usuário:** {st.session_state.username}")
            with col2:
                st.markdown(f"**ID:** {st.session_state.user_id}")
        
        with st.container(border=True):
            st.markdown("#### 🎯 Quiz")
            if st.session_state.get("quiz_completed"):
                st.success("✅ Quiz Completado")
                profile = st.session_state.quiz_result.get("profile")
                st.markdown(f"**Seu Perfil:** {profile.title()}")
                
                if st.button("🔄 Refazer Quiz"):
                    reset_quiz_state()
                    st.rerun()
            else:
                st.info("⏳ Quiz não realizado ainda")
                if st.button("Começar Quiz"):
                    iniciar_quiz()
                    st.session_state.current_page = "quiz"
                    st.rerun()

