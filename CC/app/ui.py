"""
Componentes de UI reutilizáveis para a aplicação CS Start.
Fornece funções para renderizar elementos visuais consistentes.
"""

from html import escape
from pathlib import Path
from typing import Literal

import streamlit as st

ICON_NAMES = frozenset(
    {
        "arrow-right",
        "brain",
        "book-open",
        "chart-no-axes-column-increasing",
        "circle-check",
        "clock-3",
        "code",
        "download",
        "house",
        "key-round",
        "lightbulb",
        "lock-keyhole",
        "log-in",
        "log-out",
        "mail",
        "map",
        "monitor",
        "moon",
        "rocket",
        "settings-2",
        "sparkles",
        "sun",
        "target",
        "user-round",
        "user-round-plus",
        "users-round",
        "wrench",
    }
)


def get_icon_svg(name: str, size: int = 24) -> str:
    """Carrega um SVG Lucide local de um nome e tamanho permitidos."""
    if name not in ICON_NAMES:
        raise ValueError(f"Unknown Lucide icon: {name}")
    if type(size) is not int or not 16 <= size <= 64:
        raise ValueError("Icon size must be an integer between 16 and 64 pixels.")

    icon_path = Path(__file__).parent.parent / "static" / "icons" / f"{name}.svg"
    svg = icon_path.read_text(encoding="utf-8")
    svg = svg.replace("<svg ", '<svg aria-hidden="true" focusable="false" ', 1)
    svg = svg.replace('width="24"', f'width="{size}"', 1)
    svg = svg.replace('height="24"', f'height="{size}"', 1)
    return svg


def render_icon_text_input(
    label: str,
    icon_name: str,
    *,
    key: str,
    placeholder: str,
    input_type: Literal["default", "password"] = "default",
) -> str:
    """Renderiza um campo com ícone Lucide e rótulo acessível."""
    icon_svg = get_icon_svg(icon_name, size=18)
    st.markdown(
        f'<div class="cs-field-label">{icon_svg}<span>{label}</span></div>',
        unsafe_allow_html=True,
    )
    return st.text_input(
        label,
        key=key,
        placeholder=placeholder,
        type=input_type,
        label_visibility="collapsed",
    )


def render_icon_button(
    label: str,
    icon_name: str,
    *,
    key: str,
    use_container_width: bool = True,
    primary: bool = False,
    disabled: bool = False,
) -> bool:
    """Renderiza um botão com rótulo textual e ícone Lucide decorativo."""
    icon_svg = get_icon_svg(icon_name, size=18)
    columns = st.columns(
        [0.12, 0.88],
        vertical_alignment="center",
        gap="small",
    )
    icon_column, button_column = columns[0], columns[1]
    with icon_column:
        st.markdown(
            f'<span class="cs-button-icon">{icon_svg}</span>',
            unsafe_allow_html=True,
        )
    with button_column:
        return st.button(
            label,
            key=key,
            use_container_width=use_container_width,
            type="primary" if primary else "secondary",
            disabled=disabled,
        )


def render_icon_link_button(label: str, icon_name: str, url: str) -> None:
    """Renderiza um link com ícone Lucide local ao lado do rótulo."""
    icon_svg = get_icon_svg(icon_name, size=18)
    columns = st.columns(
        [0.12, 0.88],
        vertical_alignment="center",
        gap="small",
    )
    icon_column, button_column = columns[0], columns[1]
    with icon_column:
        st.markdown(
            f'<span class="cs-button-icon">{icon_svg}</span>',
            unsafe_allow_html=True,
        )
    with button_column:
        st.link_button(
            label,
            url,
            use_container_width=True,
        )


def render_icon_download_button(
    label: str,
    icon_name: str,
    *,
    data: str,
    file_name: str,
    mime: str,
) -> bool:
    """Renderiza uma ação de download acompanhada de ícone Lucide local."""
    icon_svg = get_icon_svg(icon_name, size=18)
    columns = st.columns(
        [0.12, 0.88],
        vertical_alignment="center",
        gap="small",
    )
    icon_column, button_column = columns[0], columns[1]
    with icon_column:
        st.markdown(
            f'<span class="cs-button-icon">{icon_svg}</span>',
            unsafe_allow_html=True,
        )
    with button_column:
        return st.download_button(
            label,
            data=data,
            file_name=file_name,
            mime=mime,
            use_container_width=True,
        )


def render_icon_heading(text: str, icon_name: str, level: int = 3) -> None:
    """Renderiza um título semântico acompanhado de ícone Lucide."""
    if not 1 <= level <= 6:
        raise ValueError("Heading level must be between 1 and 6.")
    icon_svg = get_icon_svg(icon_name, size=22)
    safe_text = escape(text)
    st.markdown(
        f"""
        <h{level} class="cs-icon-heading">
            <span class="cs-heading-icon">{icon_svg}</span>
            <span>{safe_text}</span>
        </h{level}>
        """,
        unsafe_allow_html=True,
    )


def load_css():
    """Carrega o arquivo CSS customizado."""
    css_path = Path(__file__).parent.parent / "static" / "style.css"
    if css_path.exists():
        with open(css_path, "r", encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def header_principal():
    """Renderiza o header principal da aplicação."""
    brand_icon = get_icon_svg("rocket", size=36)
    st.markdown(
        f"""
        <div style="text-align: center; padding: 1.5rem 0 1rem 0;">
            <h1 class="cs-brand-heading">
                <span class="cs-brand-icon">{brand_icon}</span>
                <span>CS Start</span>
            </h1>
            <p class="subtitle">Sua jornada em Ciência da Computação começa aqui</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_feature_card(title: str, description: str, icon: str, color: str = "primary"):
    """Renderiza um card de feature com ícone e descrição."""
    icon_svg = get_icon_svg(icon, size=28)
    color_map = {
        "primary": "var(--brand-primary-text)",
        "secondary": "var(--brand-secondary-text)",
        "accent": "var(--brand-accent-text)",
        "success": "var(--color-success)",
        "warning": "var(--color-warning)",
    }
    border_color = color_map.get(color, "var(--brand-primary)")

    st.markdown(
        f"""
        <div style="
            background: var(--bg-surface);
            border: 1px solid var(--border);
            border-left: 5px solid {border_color};
            border-radius: 16px;
            padding: 1.4rem;
            box-shadow: 0 8px 22px var(--shadow);
            min-height: 180px;
        ">
            <h3 style="margin-top: 0; color: var(--text-primary) !important; display: flex; align-items: center; gap: 0.6rem;">
                <span class="cs-feature-icon" style="color: {border_color};">{icon_svg}</span>{title}
            </h3>
            <p style="color: var(--text-secondary) !important; margin-bottom: 0; line-height: 1.6;">{description}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_profile_badge(username: str):
    """Renderiza um badge com informações do usuário logado."""
    profile_icon = get_icon_svg("user-round", size=30)
    st.markdown(
        f"""
        <div style="
            display: flex;
            align-items: center;
            background: var(--brand-primary);
            color: var(--text-on-brand);
            padding: 1rem 1.1rem;
            border-radius: 12px;
            margin-bottom: 1.25rem;
            box-shadow: 0 8px 20px var(--shadow-strong);
        ">
            <span class="cs-profile-icon">{profile_icon}</span>
            <div>
                <p style="margin: 0; color: var(--text-on-brand) !important; font-size: 0.8rem; opacity: 0.9;">Conectado como</p>
                <p style="margin: 0; color: var(--text-on-brand) !important; font-size: 1.05rem; font-weight: 700;">{username}</p>
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
            <p style="color: var(--text-secondary) !important; font-weight: 600; margin-bottom: 0.5rem;">
                Pergunta {current} de {total}
            </p>
            <div style="
                width: 100%;
                height: 8px;
                background: var(--bg-subtle);
                border-radius: 4px;
                overflow: hidden;
            ">
                <div style="
                    width: {percentage}%;
                    height: 100%;
                    background: var(--color-progress-start);
                    transition: width 0.3s ease;
                "></div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_roadmap_item(
    title: str,
    number: int,
    is_completed: bool = False,
):
    """Renderiza um item da roadmap."""
    status_icon = (
        get_icon_svg("circle-check", size=22)
        if is_completed
        else f"0{number}"
    )
    status_color = (
        "var(--color-success)"
        if is_completed
        else "var(--brand-primary-text)"
    )
    status_bg = (
        "color-mix(in srgb, var(--color-success) 12%, transparent)"
        if is_completed
        else "color-mix(in srgb, var(--brand-primary) 12%, transparent)"
    )
    border_color = "var(--color-success)" if is_completed else "var(--border)"

    st.markdown(
        f"""
        <div style="
            display: flex;
            align-items: flex-start;
            background: var(--bg-surface);
            border: 1px solid {border_color};
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
                <span class="cs-roadmap-status">{status_icon}</span>
            </div>
            <p style="
                margin: 0;
                color: var(--text-primary) !important;
                font-weight: 500;
                {'text-decoration: line-through; color: var(--text-muted) !important;' if is_completed else ''}
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
            st.button(
                button["label"],
                key=button["key"],
                type="primary" if is_primary else "secondary",
            )


def render_empty_state(
    title: str,
    description: str,
    icon: str = "book-open",
):
    """Renderiza um estado vazio."""
    icon_svg = get_icon_svg(icon, size=40)

    st.markdown(
        f"""
        <div style="
            text-align: center;
            padding: 3rem 1rem;
            background: var(--bg-subtle);
            border-radius: 12px;
            border: 2px dashed var(--border);
        ">
            <p class="cs-empty-icon">{icon_svg}</p>
            <h3 style="color: var(--text-primary) !important; margin-bottom: 0.5rem;">{title}</h3>
            <p style="color: var(--text-secondary) !important; margin: 0;">{description}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_stat_card(label: str, value: str, icon: str = "chart-no-axes-column-increasing"):
    """Renderiza um card com estatísticas."""
    icon_svg = get_icon_svg(icon, size=28)

    st.markdown(
        f"""
        <div style="
            background: var(--bg-surface);
            border-radius: 12px;
            padding: 1.5rem;
            text-align: center;
            box-shadow: 0 4px 12px var(--shadow);
        ">
            <p class="cs-stat-icon">{icon_svg}</p>
            <p style="color: var(--text-secondary) !important; margin: 0 0 0.5rem 0; font-size: 0.9rem;">{label}</p>
            <p style="color: var(--text-primary) !important; margin: 0; font-size: 1.8rem; font-weight: 700;">{value}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
