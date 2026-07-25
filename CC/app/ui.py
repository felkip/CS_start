"""
Componentes de UI reutilizáveis para a aplicação CS Start.
Fornece funções para renderizar elementos visuais consistentes.
"""

import streamlit as st
from pathlib import Path


def load_css():
    """Carrega o arquivo CSS customizado."""
    css_path = Path(__file__).parent.parent / "static" / "style.css"
    if css_path.exists():
        with open(css_path, "r", encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def header_principal():
    """Renderiza o header principal da aplicação."""
    st.markdown(
        """
        <div style="text-align: center; padding: 2rem 0 1rem 0;">
            <h1>🚀 CS Start</h1>
            <p class="subtitle">Sua jornada em Ciência da Computação começa aqui</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_feature_card(title: str, description: str, icon: str, color: str = "primary"):
    """
    Renderiza um card de feature com ícone e descrição.
    
    Args:
        title: Título da feature
        description: Descrição da feature
        icon: Emoji ou ícone
        color: Cor do card (primary, success, warning)
    """
    colors = {
        "primary": "bg-gradient-to-r from-indigo-400 to-purple-500",
        "success": "bg-gradient-to-r from-green-400 to-emerald-500",
        "warning": "bg-gradient-to-r from-yellow-400 to-orange-500",
    }
    color_class = colors.get(color, colors["primary"])
    
    st.markdown(
        f"""
        <div style="
            background: white;
            border-radius: 12px;
            padding: 1.5rem;
            border-left: 4px solid;
            border-left-color: {'#10b981' if color == 'success' else '#667eea'};
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
            transition: all 0.3s ease;
        ">
            <h3 style="margin-top: 0; color: #1e293b;">
                <span style="font-size: 1.5em; margin-right: 0.5rem;">{icon}</span>{title}
            </h3>
            <p style="color: #64748b; margin-bottom: 0;">{description}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_profile_badge(username: str):
    """Renderiza um badge com informações do usuário logado."""
    st.markdown(
        f"""
        <div style="
            display: flex;
            align-items: center;
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            padding: 1rem;
            border-radius: 8px;
            margin-bottom: 1.5rem;
        ">
            <span style="font-size: 2rem; margin-right: 1rem;">👤</span>
            <div>
                <p style="margin: 0; font-size: 0.9rem; opacity: 0.9;">Conectado como</p>
                <p style="margin: 0; font-size: 1.1rem; font-weight: 600;">{username}</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_quiz_progress(current: int, total: int):
    """Renderiza a barra de progresso do quiz."""
    percentage = (current / total) * 100
    st.markdown(
        f"""
        <div style="margin-bottom: 1.5rem;">
            <p style="color: #64748b; font-weight: 600; margin-bottom: 0.5rem;">
                Pergunta {current} de {total}
            </p>
            <div style="
                width: 100%;
                height: 8px;
                background: #e2e8f0;
                border-radius: 4px;
                overflow: hidden;
            ">
                <div style="
                    width: {percentage}%;
                    height: 100%;
                    background: linear-gradient(90deg, #667eea, #764ba2);
                    transition: width 0.3s ease;
                "></div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_roadmap_item(title: str, number: int, is_completed: bool = False):
    """Renderiza um item da roadmap."""
    status_icon = "✅" if is_completed else f"0{number}"
    status_color = "#10b981" if is_completed else "#667eea"
    status_bg = "#ecfdf5" if is_completed else "#f0f4ff"
    
    st.markdown(
        f"""
        <div style="
            display: flex;
            align-items: flex-start;
            background: white;
            border: 2px solid {status_bg};
            border-radius: 8px;
            padding: 1.25rem;
            margin-bottom: 1rem;
            transition: all 0.2s ease;
        ">
            <div style="
                display: flex;
                align-items: center;
                justify-content: center;
                width: 40px;
                height: 40px;
                background: {status_bg};
                border-radius: 50%;
                color: {status_color};
                font-weight: 700;
                margin-right: 1rem;
                flex-shrink: 0;
            ">
                {status_icon}
            </div>
            <p style="
                margin: 0;
                color: #1e293b;
                font-weight: 500;
                {'text-decoration: line-through; color: #94a3b8;' if is_completed else ''}
            ">
                {title}
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_button_group(buttons: list):
    """
    Renderiza um grupo de botões em linha.
    
    Args:
        buttons: Lista de dicts com keys {'label', 'key', 'primary': bool}
    """
    cols = st.columns(len(buttons))
    for col, button in zip(cols, buttons):
        with col:
            is_primary = button.get("primary", False)
            style = "color: white;" if is_primary else ""
            st.button(button["label"], key=button["key"])


def render_empty_state(title: str, description: str, icon: str = "📭"):
    """Renderiza um estado vazio."""
    st.markdown(
        f"""
        <div style="
            text-align: center;
            padding: 3rem 1rem;
            background: linear-gradient(135deg, rgba(102, 126, 234, 0.05), rgba(118, 75, 162, 0.05));
            border-radius: 12px;
            border: 2px dashed #e2e8f0;
        ">
            <p style="font-size: 3rem; margin: 0 0 1rem 0;">{icon}</p>
            <h3 style="color: #1e293b; margin-bottom: 0.5rem;">{title}</h3>
            <p style="color: #64748b; margin: 0;">{description}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_stat_card(label: str, value: str, icon: str = "📊"):
    """Renderiza um card com estatísticas."""
    st.markdown(
        f"""
        <div style="
            background: white;
            border-radius: 12px;
            padding: 1.5rem;
            text-align: center;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
        ">
            <p style="font-size: 2rem; margin: 0 0 0.5rem 0;">{icon}</p>
            <p style="color: #64748b; margin: 0 0 0.5rem 0; font-size: 0.9rem;">{label}</p>
            <p style="color: #1e293b; margin: 0; font-size: 1.8rem; font-weight: 700;">{value}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
