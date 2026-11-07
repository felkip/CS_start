"""Controle do tema claro/escuro e estilos globais da aplicação."""

import streamlit as st
from app.ui import get_icon_svg


def configure_theme():
    """Renderiza o seletor de tema e aplica os estilos correspondentes."""
    is_dark_mode = st.session_state.theme == "dark"
    theme_icon = get_icon_svg("moon" if is_dark_mode else "sun", size=18)
    st.sidebar.markdown(
        f'<div class="cs-theme-toggle-label">{theme_icon}<span>Aparência</span></div>',
        unsafe_allow_html=True,
    )
    is_dark_mode = st.sidebar.toggle(
        "Modo escuro",
        key="dark_mode_toggle",
        value=is_dark_mode,
    )
    st.session_state.theme = "dark" if is_dark_mode else "light"

    if st.session_state.theme == "dark":
        st.markdown(
            """
            <style>
                :root {
                    --brand-primary: #0e7490;
                    --brand-primary-hover: #155e75;
                    --brand-secondary: #6d28d9;
                    --brand-accent: #2563eb;
                    --brand-primary-text: #67e8f9;
                    --brand-secondary-text: #c4b5fd;
                    --brand-accent-text: #60a5fa;
                    --brand-heading-start: #67e8f9;
                    --brand-heading-end: #c4b5fd;
                    --focus-ring: #67e8f9;
                    --color-progress-start: #67e8f9;
                    --color-progress-end: #c4b5fd;
                    --color-success: #34d399;
                    --color-warning: #fbbf24;
                    --color-danger: #f87171;
                    --color-info: #60a5fa;
                    --color-success-soft: rgba(52, 211, 153, 0.12);
                    --color-warning-soft: rgba(251, 191, 36, 0.12);
                    --color-danger-soft: rgba(248, 113, 113, 0.12);
                    --color-info-soft: rgba(96, 165, 250, 0.12);
                    --color-success-text: #d1fae5;
                    --color-warning-text: #fef3c7;
                    --color-danger-text: #fee2e2;
                    --color-info-text: #dbeafe;
                    --bg-page: #0b1220;
                    --bg-page-tint: #071b24;
                    --bg-panel: rgba(17, 24, 39, 0.88);
                    --bg-surface: #111827;
                    --bg-subtle: #1e293b;
                    --bg-sidebar: #111827;
                    --bg-soft: #12313f;
                    --text-primary: #f8fafc;
                    --text-secondary: #cbd5e1;
                    --text-muted: #94a3b8;
                    --text-on-brand: #ffffff;
                    --border: #334155;
                    --shadow: rgba(2, 6, 23, 0.35);
                    --shadow-strong: rgba(14, 116, 144, 0.35);
                    --primary: var(--brand-primary);
                    --secondary: var(--brand-accent);
                    --success: var(--color-success);
                    --warning: var(--color-warning);
                    --danger: var(--color-danger);
                    --bg-panel-strong: var(--bg-surface);
                    --bg-elevated: var(--bg-subtle);
                    --text: var(--text-primary);
                    --text-soft: var(--text-secondary);
                }
                .stApp {
                    background: linear-gradient(135deg, var(--bg-page-tint) 0%, var(--bg-page) 100%);
                    color: var(--text-primary) !important;
                }
                [data-testid="stSidebar"] {
                    background: var(--bg-surface) !important;
                    border-right: 1px solid var(--border);
                }
                [data-testid="stSidebar"] * {
                    color: var(--text-secondary) !important;
                    opacity: 1 !important;
                }
                [data-testid="stSidebar"] [class*="st-key-sidebar-nav-"] [data-testid="stButton"] > button[kind="secondary"],
                [data-testid="stSidebar"] [class*="st-key-sidebar-logout"] [data-testid="stButton"] > button {
                    background: var(--bg-subtle) !important;
                    color: var(--text-primary) !important;
                    border: 1px solid var(--border) !important;
                }
                [data-testid="stSidebar"] [class*="st-key-sidebar-nav-"] [data-testid="stButton"] > button[kind="secondary"] *,
                [data-testid="stSidebar"] [class*="st-key-sidebar-logout"] [data-testid="stButton"] > button * {
                    color: var(--text-primary) !important;
                }
                [data-testid="stSidebar"] [class*="st-key-sidebar-nav-"] .cs-button-icon,
                [data-testid="stSidebar"] [class*="st-key-sidebar-logout"] .cs-button-icon {
                    color: var(--brand-primary-text) !important;
                }
                [data-testid="stSidebar"] [class*="st-key-sidebar-nav-"] [data-testid="stButton"] > button[kind="secondary"]:hover,
                [data-testid="stSidebar"] [class*="st-key-sidebar-logout"] [data-testid="stButton"] > button:hover {
                    background: color-mix(in srgb, var(--brand-primary) 16%, var(--bg-subtle)) !important;
                    border-color: var(--brand-primary-text) !important;
                }
                [data-testid="stSidebar"] [class*="st-key-sidebar-nav-"] [data-testid="stButton"] > button[kind="secondary"]:focus-visible,
                [data-testid="stSidebar"] [class*="st-key-sidebar-logout"] [data-testid="stButton"] > button:focus-visible {
                    outline: 3px solid var(--focus-ring) !important;
                    outline-offset: 2px !important;
                }
                [data-testid="stHeader"] {
                    background: color-mix(in srgb, var(--bg-page) 92%, transparent) !important;
                    box-shadow: none !important;
                    border-bottom: 1px solid rgba(148, 163, 184, 0.18) !important;
                }
                [data-testid="stMain"] > div:first-child {
                    background: linear-gradient(135deg, var(--bg-page-tint) 0%, var(--bg-page) 100%) !important;
                }
                .block-container {
                    padding-top: 1rem !important;
                    padding-bottom: 2rem !important;
                }
                [data-testid="stSidebar"] .stRadio > label,
                [data-testid="stSidebar"] .stMarkdown p,
                [data-testid="stSidebar"] .stButton button,
                [data-testid="stSidebar"] .stRadio > label > div > div {
                    color: var(--text-secondary) !important;
                }
                .cs-section-spacer { height: 2rem; }
                .stContainer,
                [data-testid="stVerticalBlock"] > div,
                [data-testid="stHorizontalBlock"] > div {
                    background: transparent !important;
                    border: none !important;
                    box-shadow: none !important;
                    border-radius: 0 !important;
                }
                h1 {
                    background: none;
                    color: var(--brand-heading-start) !important;
                    -webkit-text-fill-color: var(--brand-heading-start) !important;
                }
                h2, h3, h4, h5, h6,
                .stMarkdown h1, .stMarkdown h2, .stMarkdown h3, .stMarkdown h4, .stMarkdown h5, .stMarkdown h6,
                .stMarkdown p, .stMarkdown li, .stMarkdown span, .stMarkdown strong, .stMarkdown em,
                .subtitle, p, li, label, .stMarkdown, .stMarkdownContainer, .stDataFrame, .stSelectbox, .stTextInput, .stNumberInput, .stRadio {
                    color: var(--text-primary) !important;
                    opacity: 1 !important;
                }
                hr, .stDivider, [data-testid="stHorizontalRule"] {
                    border-top: 1px solid rgba(148, 163, 184, 0.36) !important;
                    color: rgba(148, 163, 184, 0.36) !important;
                }
                .stButton > button {
                    background: var(--brand-primary) !important;
                    color: var(--text-on-brand) !important;
                    border: none !important;
                    border-radius: 10px !important;
                    box-shadow: 0 8px 20px var(--shadow-strong);
                }
                .stButton > button p,
                .stButton > button span {
                    color: var(--text-on-brand) !important;
                }
                [data-testid="stLinkButton"] a {
                    background: var(--brand-primary) !important;
                    border: none !important;
                    border-radius: 10px !important;
                    box-shadow: 0 8px 20px var(--shadow-strong);
                }
                [data-testid="stLinkButton"] a,
                [data-testid="stLinkButton"] a * {
                    color: var(--text-on-brand) !important;
                }
                .stTabs [data-baseweb="tab-list"] button,
                .stTabs [data-baseweb="tab-list"] button * {
                    color: var(--text-secondary) !important;
                }
                .stTabs [data-baseweb="tab-list"] button[aria-selected="true"],
                .stTabs [data-baseweb="tab-list"] button[aria-selected="true"] * {
                    color: var(--color-info) !important;
                    border-bottom-color: var(--focus-ring) !important;
                }
                .stExpander {
                    border: 1px solid var(--border) !important;
                    border-radius: 12px !important;
                    background: var(--bg-surface) !important;
                }
                .stExpander > div > div {
                    color: var(--text-primary) !important;
                }
                .stExpander .stMarkdown p,
                .stExpander .stMarkdown li,
                .stExpander .stMarkdown strong,
                .stExpander .stMarkdown span {
                    color: var(--text-secondary) !important;
                }
                .stDownloadButton > button {
                    background: var(--brand-primary) !important;
                    color: var(--text-on-brand) !important;
                    border: none !important;
                    border-radius: 10px !important;
                    box-shadow: 0 8px 20px var(--shadow-strong) !important;
                    font-weight: 600 !important;
                }
                .stDownloadButton > button span,
                .stDownloadButton > button p,
                .stDownloadButton > button div {
                    color: var(--text-on-brand) !important;
                }
                .stTextInput > div > div > input,
                .stNumberInput > div > div > input,
                .stSelectbox > div > div > select,
                textarea {
                    background: var(--bg-subtle) !important;
                    color: var(--text-primary) !important;
                    border: 1px solid var(--border) !important;
                }
                [data-testid="stTextInput"] [data-baseweb="base-input"] {
                    background: var(--bg-subtle) !important;
                }
                [data-testid="stTextInput"] [data-testid="stTextInputRootElement"] {
                    background: var(--bg-subtle) !important;
                    border-color: var(--border) !important;
                }
                [data-testid="stTextInput"] button[aria-label*="password text"] {
                    background: var(--bg-subtle) !important;
                    color: var(--text-primary) !important;
                    border: 1px solid var(--border) !important;
                }
                [data-testid="stSelectbox"] [data-baseweb="select"] > div {
                    background: var(--bg-subtle) !important;
                    color: var(--text-primary) !important;
                    border-color: var(--border) !important;
                }
                [data-testid="stSelectbox"] [data-baseweb="select"] * {
                    color: var(--text-primary) !important;
                }
                [data-baseweb="popover"]:has([data-testid="stSelectboxVirtualDropdown"]),
                [data-testid="stSelectboxVirtualDropdown"] {
                    background: var(--bg-surface) !important;
                }
                [data-testid="stSelectboxVirtualDropdown"] [role="option"] {
                    background: var(--bg-surface) !important;
                    color: var(--text-secondary) !important;
                }
                [data-testid="stSelectboxVirtualDropdown"] [role="option"]:hover,
                [data-testid="stSelectboxVirtualDropdown"] [role="option"][aria-selected="true"] {
                    background: var(--bg-subtle) !important;
                    color: var(--text-primary) !important;
                }
                .stTextInput > div > div > input:focus,
                .stNumberInput > div > div > input:focus,
                .stSelectbox > div > div > select:focus {
                    border-color: var(--focus-ring) !important;
                    box-shadow: 0 0 0 3px color-mix(in srgb, var(--focus-ring) 20%, transparent) !important;
                }
                .stSuccess {
                    background-color: var(--color-success-soft) !important;
                    border-left: 4px solid var(--color-success) !important;
                    color: var(--color-success-text) !important;
                }
                .stError {
                    background-color: var(--color-danger-soft) !important;
                    border-left: 4px solid var(--color-danger) !important;
                    color: var(--color-danger-text) !important;
                }
                .stWarning {
                    background-color: var(--color-warning-soft) !important;
                    border-left: 4px solid var(--color-warning) !important;
                    color: var(--color-warning-text) !important;
                }
                .stInfo {
                    background-color: var(--color-info-soft) !important;
                    border-left: 4px solid var(--color-info) !important;
                    color: var(--color-info-text) !important;
                }
                .divider { background: var(--border); }
                .dashboard-card {
                    color: var(--text-primary) !important;
                    background: var(--bg-surface) !important;
                    border: 1px solid var(--border) !important;
                }
                .dashboard-card .metric-label,
                .dashboard-card .metric-value,
                .dashboard-card .metric-title,
                .dashboard-card p,
                .dashboard-card h3,
                .dashboard-card h4 {
                    color: var(--text-primary) !important;
                }
                [data-testid="stMarkdownContainer"] h3,
                [data-testid="stMarkdownContainer"] h2,
                [data-testid="stMarkdownContainer"] p,
                [data-testid="stMarkdownContainer"] li,
                [data-testid="stMarkdownContainer"] span {
                    color: var(--text-primary) !important;
                }
                .dashboard-card h3,
                .dashboard-card p,
                .dashboard-card div,
                .dashboard-card span {
                    color: var(--text-primary) !important;
                }
                .dashboard-card .stMarkdown p,
                .dashboard-card .stMarkdown span {
                    color: var(--text-secondary) !important;
                }
            </style>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            """
            <style>
                .stApp {
                    background: linear-gradient(135deg, var(--bg-page-tint) 0%, var(--bg-page) 100%);
                    color: var(--text-primary) !important;
                }
                [data-testid="stSidebar"] {
                    background: var(--bg-sidebar) !important;
                    border-right: 1px solid var(--border);
                }
                [data-testid="stSidebar"] * {
                    color: var(--text-primary) !important;
                    opacity: 1 !important;
                }
                .cs-section-spacer { height: 2rem; }
                .stContainer,
                [data-testid="stVerticalBlock"] > div,
                [data-testid="stHorizontalBlock"] > div {
                    background: transparent !important;
                    border: none !important;
                    box-shadow: none !important;
                    border-radius: 0 !important;
                }
                h1 {
                    background: none;
                    color: var(--brand-heading-start) !important;
                    -webkit-text-fill-color: var(--brand-heading-start) !important;
                }
                .subtitle, p, li, label, .stMarkdown, .stMarkdownContainer, .stDataFrame, .stSelectbox, .stTextInput, .stNumberInput, .stRadio {
                    color: var(--text-primary) !important;
                    opacity: 1 !important;
                }
                .stButton > button {
                    background: var(--brand-primary) !important;
                    color: var(--text-on-brand) !important;
                    border: none !important;
                    border-radius: 10px !important;
                    box-shadow: 0 8px 20px color-mix(in srgb, var(--brand-primary) 24%, transparent);
                }
                .stButton > button p,
                .stButton > button span {
                    color: var(--text-on-brand) !important;
                }
                .stTabs [data-baseweb="tab-list"] button {
                    color: var(--text-secondary) !important;
                }
                .stTabs [data-baseweb="tab-list"] button[aria-selected="true"] {
                    color: var(--brand-primary-hover) !important;
                    border-bottom-color: var(--focus-ring) !important;
                }
                .stTextInput > div > div > input,
                .stNumberInput > div > div > input,
                .stSelectbox > div > div > select,
                textarea {
                    background: var(--bg-surface) !important;
                    color: var(--text-primary) !important;
                    border: 1px solid var(--border) !important;
                }
                .stTextInput > div > div > input:focus,
                .stNumberInput > div > div > input:focus,
                .stSelectbox > div > div > select:focus {
                    border-color: var(--focus-ring) !important;
                    box-shadow: 0 0 0 3px color-mix(in srgb, var(--focus-ring) 12%, transparent) !important;
                }
                .stSuccess {
                    background-color: var(--color-success-soft) !important;
                    border-left: 4px solid var(--color-success) !important;
                    color: var(--color-success-text) !important;
                }
                .stError {
                    background-color: var(--color-danger-soft) !important;
                    border-left: 4px solid var(--color-danger) !important;
                    color: var(--color-danger-text) !important;
                }
                .stWarning {
                    background-color: var(--color-warning-soft) !important;
                    border-left: 4px solid var(--color-warning) !important;
                    color: var(--color-warning-text) !important;
                }
                .stInfo {
                    background-color: var(--color-info-soft) !important;
                    border-left: 4px solid var(--color-info) !important;
                    color: var(--color-info-text) !important;
                }
                .divider { background: var(--border); }
                .dashboard-card {
                    color: var(--text-primary) !important;
                    background: var(--bg-surface) !important;
                    border: 1px solid var(--border) !important;
                }
                .dashboard-card .metric-label,
                .dashboard-card .metric-value,
                .dashboard-card .metric-title,
                .dashboard-card p,
                .dashboard-card h3,
                .dashboard-card h4 {
                    color: var(--text-primary) !important;
                }
            </style>
            """,
            unsafe_allow_html=True,
        )
