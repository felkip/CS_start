try:
    import streamlit as st
    from app.ui import render_roadmap_item, render_empty_state
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
            "🗺️"
        )
        return

    topics = get_roadmap_for_profile(profile)
    
    # Títulos e descrições dos perfis
    profile_info = {
        "programming": {
            "titulo": "🧑‍💻 Caminho do Programador",
            "descricao": "Focado em desenvolvimento de soluções, algoritmos e pensamento lógico. Você aprenderá a criar programas e resolver problemas através de código.",
            "cor": "linear-gradient(135deg, #667eea, #764ba2)",
        },
        "tech": {
            "titulo": "🔧 Caminho da Tecnologia",
            "descricao": "Exploração de ferramentas, sistemas e inovações tecnológicas. Você descubrirá como a tecnologia funciona e como usá-la de forma criativa.",
            "cor": "linear-gradient(135deg, #f093fb, #f5576c)",
        },
        "beginner": {
            "titulo": "🌟 Caminho do Iniciante",
            "descricao": "Abordagem suave e estruturada para aprender o básico de computação. Você evoluirá no seu próprio ritmo com fundamentos sólidos.",
            "cor": "linear-gradient(135deg, #4facfe, #00f2fe)",
        },
    }
    
    info = profile_info.get(profile, profile_info["beginner"])
    
    # Header do roadmap
    st.markdown(
        f"""
        <div style='
            background: {info["cor"]};
            color: white;
            border-radius: 12px;
            padding: 2rem;
            margin-bottom: 2rem;
        '>
            <h2 style='margin-top: 0; margin-bottom: 0.5rem;'>{info["titulo"]}</h2>
            <p style='margin: 0; opacity: 0.95;'>{info["descricao"]}</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown("### 📚 Seu Plano de Estudos")
    st.markdown(f"**Progresso:** 0 de {len(topics)} tópicos concluídos")
    
    # Itens do roadmap
    for index, topic in enumerate(topics, start=1):
        render_roadmap_item(topic, index)
    
    st.markdown("---")
    
    # Seção de dicas e recursos
    with st.expander("💡 Dicas para ter sucesso", expanded=False):
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
        if st.button("🔄 Refazer Quiz", use_container_width=True):
            from app.quiz import reset_quiz_state
            reset_quiz_state()
            st.rerun()
    
    with col2:
        st.download_button(
            label="📥 Baixar Roadmap (PDF)",
            data=f"Roadmap para {profile.title()}\n\n" + "\n".join([f"{i}. {t}" for i, t in enumerate(topics, 1)]),
            file_name="meu_roadmap.txt",
            mime="text/plain",
            use_container_width=True
        )
    
    with col3:
        if st.button("🏠 Voltar ao Início", use_container_width=True):
            st.session_state.current_page = "home"
            st.rerun()
