try:
    import streamlit as st
    from app.learning import render_learning_categories
    from app.ui import (
        get_icon_svg,
        render_icon_download_button,
        render_empty_state,
        render_icon_button,
        render_icon_heading,
        render_roadmap_item,
    )
except ModuleNotFoundError:  # pragma: no cover - fallback para testes simples
    class _StreamlitFallback:
        def info(self, *args, **kwargs):
            return None

        def markdown(self, *args, **kwargs):
            return None

        def subheader(self, *args, **kwargs):
            return None

        def write(self, *args, **kwargs):
            return None

    st = _StreamlitFallback()
    
    def render_roadmap_item(*args, **kwargs):
        pass
    
    def render_empty_state(*args, **kwargs):
        pass

    def render_learning_categories(*args, **kwargs):
        pass

ROADMAPS = {
    "programming": [
        "Fundamentos de lógica",
        "Variáveis e estruturas básicas",
        "Funções",
        "Estruturas de decisão e repetição",
        "Introdução à programação com Python",
    ],
    "tech": [
        "Fundamentos de computadores",
        "Internet e sistemas",
        "Ferramentas básicas de produtividade",
        "Introdução a bancos de dados",
        "Noções de segurança e uso de tecnologia",
    ],
    "beginner": [
        "Introdução à computação",
        "Conceitos básicos de tecnologia",
        "Primeiros passos em lógica",
        "Pequenos exercícios práticos",
        "Estudo guiado com ritmo leve",
    ],
}


def get_roadmap_for_profile(profile):
    return ROADMAPS.get(profile, ROADMAPS["beginner"])


def render_roadmap(profile=None):
    if profile is None:
        profile = st.session_state.get("quiz_result", {}).get("profile")

    if profile is None:
        render_empty_state(
            "Roadmap não disponível",
            "Complete o quiz para ver um plano de estudos personalizado.",
            "map"
        )
        return

    dark_mode = st.session_state.get("theme") == "dark"
    topics = get_roadmap_for_profile(profile)

    # Títulos e descrições dos perfis
    profile_info = {
        "programming": {
            "titulo": "Caminho do Programador",
            "icone": "code",
            "descricao": "Focado em desenvolvimento de soluções, algoritmos e pensamento lógico. Você aprenderá a criar programas e resolver problemas através de código.",
            "cor": "linear-gradient(135deg, var(--brand-primary), var(--brand-accent))",
        },
        "tech": {
            "titulo": "Caminho da Tecnologia",
            "icone": "monitor",
            "descricao": "Exploração de ferramentas, sistemas e inovações tecnológicas. Você descobrirá como a tecnologia funciona e como usá-la de forma criativa.",
            "cor": "linear-gradient(135deg, var(--brand-accent), var(--brand-secondary))",
        },
        "beginner": {
            "titulo": "Caminho do Iniciante",
            "icone": "sparkles",
            "descricao": "Abordagem suave e estruturada para aprender o básico de computação. Você evoluirá no seu próprio ritmo com fundamentos sólidos.",
            "cor": "linear-gradient(135deg, var(--brand-primary), var(--brand-secondary))",
        },
    }

    info = profile_info.get(profile, profile_info["beginner"])
    profile_icon = get_icon_svg(info["icone"], size=28)

    # Header do roadmap
    st.markdown(
        f"""
        <div style='
            background: {info["cor"]};
            color: var(--text-on-brand);
            border-radius: 12px;
            padding: 2rem;
            margin-bottom: 2rem;
            box-shadow: inset 0 1px 0 rgba(255,255,255,0.18), 0 12px 28px rgba(15, 23, 42, 0.22);
        '>
            <h2 class="cs-roadmap-heading" style='margin-top: 0; margin-bottom: 0.5rem;'>
                {profile_icon}<span>{info["titulo"]}</span>
            </h2>
            <p style='margin: 0; opacity: 0.95;'>{info["descricao"]}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    render_icon_heading("Seu Plano de Estudos", "book-open")
    if dark_mode:
        st.markdown(f"<p style='color: var(--text-secondary); margin-top: 0;'><strong>Progresso:</strong> 0 de {len(topics)} tópicos concluídos</p>", unsafe_allow_html=True)
    else:
        st.markdown(f"**Progresso:** 0 de {len(topics)} tópicos concluídos")
    
    # Itens do roadmap
    for index, topic in enumerate(topics, start=1):
        render_roadmap_item(topic, index)
    
    st.markdown("---")
    render_learning_categories(profile)
    
    # Seção de dicas e recursos
    render_icon_heading("Dicas para ter sucesso", "lightbulb", level=4)
    with st.expander("Ver dicas e recursos", expanded=False):
        st.markdown(f"""
        #### Dicas para o perfil {profile.title()}:
        
        - **Seja consistente:** Dedique tempo regularmente ao aprendizado
        - **Pratique:** Quanto mais você praticar, mais rápido aprenderá
        - **Tire dúvidas:** Não hesite em buscar ajuda quando tiver dúvidas
        - **Celebre pequenas vitórias:** Cada passo é uma conquista!
        - **Explore além:** Procure recursos adicionais que complementem seu aprendizado
        
        ##### Recursos Recomendados:
        - Plataformas online (Coursera, Udemy, YouTube)
        - Comunidades de programadores (GitHub, Stack Overflow)
        - Documentações oficiais das linguagens
        - Grupos de estudo e mentorias
        """)
    
    # Botões de ação
    col1, col2, col3 = st.columns(3)
    with col1:
        render_icon_download_button(
            "Baixar Roadmap",
            "download",
            data=f"Roadmap para {profile.title()}\n\n" + "\n".join([f"{i}. {t}" for i, t in enumerate(topics, 1)]),
            file_name="meu_roadmap.txt",
            mime="text/plain",
        )

    with col2:
        if render_icon_button("Fazer outro quiz", "target", key="roadmap_restart_quiz"):
            from app.quiz import iniciar_quiz
            iniciar_quiz()
            st.session_state.current_page = "quiz"
            st.rerun()
    
    with col3:
        if render_icon_button("Voltar ao Início", "house", key="roadmap_home"):
            st.session_state.current_page = "home"
            st.rerun()
