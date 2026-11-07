"""Categorias e módulos iniciais de aprendizagem por perfil."""

from dataclasses import dataclass

import streamlit as st

from app.ui import get_icon_svg, render_icon_heading, render_icon_link_button


@dataclass(frozen=True)
class LearningCategory:
    """Categoria de aprendizagem associada aos perfis do quiz."""

    id: str
    name: str
    description: str
    profiles: tuple[str, ...]


@dataclass(frozen=True)
class StudyModule:
    """Módulo curto com objetivo prático e material de referência."""

    id: str
    title: str
    description: str
    category_id: str
    level: str
    study_minutes: int
    language: str
    url: str
    activity: str
    roadmap_topics: tuple[str, ...]


LEARNING_CATEGORIES = (
    LearningCategory(
        id="fundamentos-computacao",
        name="Fundamentos de Computação",
        description="Conceitos essenciais de computação e tecnologia para iniciar os estudos.",
        profiles=("programming", "tech", "beginner"),
    ),
    LearningCategory(
        id="programacao",
        name="Programação",
        description="Lógica, algoritmos e primeiros passos na criação de programas.",
        profiles=("programming", "beginner"),
    ),
    LearningCategory(
        id="tecnologia-sistemas",
        name="Tecnologia e Sistemas",
        description="Internet, computadores, sistemas e segurança no uso da tecnologia.",
        profiles=("tech", "beginner"),
    ),
    LearningCategory(
        id="ferramentas-produtividade",
        name="Ferramentas e Produtividade",
        description="Ferramentas digitais e práticas para estudar e trabalhar com tecnologia.",
        profiles=("tech",),
    ),
)

CATEGORY_ICONS = {
    "fundamentos-computacao": "brain",
    "programacao": "code",
    "tecnologia-sistemas": "monitor",
    "ferramentas-produtividade": "wrench",
}

STUDY_MODULES = (
    StudyModule(
        id="intro-ciencia-computacao",
        title="Introdução à Ciência da Computação (CS50x)",
        description="Panorama de pensamento computacional, algoritmos e fundamentos da área.",
        category_id="fundamentos-computacao",
        level="Iniciante",
        study_minutes=45,
        language="Inglês",
        url="https://cs50.harvard.edu/x/",
        activity="Anote três problemas cotidianos que poderiam ser divididos em passos menores.",
        roadmap_topics=("Introdução à computação", "Fundamentos de computadores"),
    ),
    StudyModule(
        id="algoritmos-pensamento-computacional",
        title="Visualize algoritmos passo a passo",
        description="Use animações para observar como algoritmos e estruturas de dados processam cada operação.",
        category_id="fundamentos-computacao",
        level="Iniciante",
        study_minutes=30,
        language="Inglês",
        url="https://visualgo.net/en",
        activity="Escolha uma visualização, acompanhe uma operação e descreva como o estado muda a cada passo.",
        roadmap_topics=("Fundamentos de lógica", "Primeiros passos em lógica"),
    ),
    StudyModule(
        id="scratch-primeiro-projeto",
        title="Crie seu primeiro projeto com Scratch",
        description="Aprenda programação visual por meio de projetos e exemplos interativos.",
        category_id="programacao",
        level="Iniciante",
        study_minutes=40,
        language="Português e outros idiomas",
        url="https://scratch.mit.edu/ideas",
        activity="Monte uma animação curta usando eventos e ao menos uma repetição.",
        roadmap_topics=("Pequenos exercícios práticos", "Primeiros passos em lógica"),
    ),
    StudyModule(
        id="rotina-estudo-leve",
        title="Pratique lógica em desafios curtos",
        description="Resolva desafios progressivos de programação visual, no seu ritmo e em sessões curtas.",
        category_id="programacao",
        level="Iniciante",
        study_minutes=15,
        language="Português",
        url="https://blockly.games/?lang=pt-br",
        activity="Resolva um desafio por sessão e anote qual instrução ou sequência ajudou a avançar.",
        roadmap_topics=("Estudo guiado com ritmo leve",),
    ),
    StudyModule(
        id="python-primeiros-passos",
        title="Primeiros passos com Python",
        description="Pratique variáveis, expressões e execução de pequenos programas.",
        category_id="programacao",
        level="Iniciante",
        study_minutes=45,
        language="Inglês",
        url="https://www.py4e.com/lessons",
        activity="Faça um programa que peça dois valores e mostre a soma deles.",
        roadmap_topics=("Introdução à programação com Python", "Variáveis e estruturas básicas"),
    ),
    StudyModule(
        id="python-controle-fluxo",
        title="Decisões e repetições em Python",
        description="Estude condicionais e laços para controlar o fluxo de um programa.",
        category_id="programacao",
        level="Intermediário",
        study_minutes=40,
        language="Inglês",
        url="https://docs.python.org/3/tutorial/controlflow.html",
        activity="Crie um programa que percorra uma lista e classifique os valores pares.",
        roadmap_topics=("Estruturas de decisão e repetição", "Funções"),
    ),
    StudyModule(
        id="primeiro-site-web",
        title="Monte seu primeiro site",
        description="Introdução prática à estrutura, ao estilo e ao conteúdo de uma página web.",
        category_id="tecnologia-sistemas",
        level="Iniciante",
        study_minutes=45,
        language="Inglês",
        url="https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Your_first_website",
        activity="Desenhe uma página simples com título, parágrafo e uma lista de interesses.",
        roadmap_topics=("Internet e sistemas", "Conceitos básicos de tecnologia"),
    ),
    StudyModule(
        id="fundamentos-redes",
        title="Noções iniciais de redes",
        description="Conheça conceitos introdutórios de redes e comunicação entre dispositivos.",
        category_id="tecnologia-sistemas",
        level="Iniciante",
        study_minutes=35,
        language="Inglês",
        url="https://www.netacad.com/networking",
        activity="Desenhe o caminho que uma mensagem percorre entre seu dispositivo e um site.",
        roadmap_topics=("Fundamentos de computadores", "Internet e sistemas"),
    ),
    StudyModule(
        id="primeiros-passos-sql",
        title="Primeiros passos com bancos de dados e SQL",
        description="Aprenda como tabelas relacionais organizam dados e pratique consultas SQL.",
        category_id="tecnologia-sistemas",
        level="Iniciante",
        study_minutes=35,
        language="Inglês",
        url="https://sqlbolt.com/",
        activity="Faça uma consulta que selecione apenas alguns registros de uma tabela.",
        roadmap_topics=("Introdução a bancos de dados",),
    ),
    StudyModule(
        id="seguranca-web-top-10",
        title="Introdução aos riscos de segurança web",
        description="Conheça categorias comuns de riscos e boas práticas para desenvolver com segurança.",
        category_id="tecnologia-sistemas",
        level="Intermediário",
        study_minutes=35,
        language="Inglês",
        url="https://owasp.org/www-project-top-ten/",
        activity="Escolha um risco apresentado e escreva uma medida preventiva em suas palavras.",
        roadmap_topics=("Noções de segurança e uso de tecnologia",),
    ),
    StudyModule(
        id="github-introducao",
        title="Primeiros passos no GitHub",
        description="Pratique repositórios, branches, commits e pull requests em um exercício guiado.",
        category_id="ferramentas-produtividade",
        level="Iniciante",
        study_minutes=45,
        language="Inglês",
        url="https://github.com/skills/introduction-to-github",
        activity="Conclua o exercício e registre o que cada commit representa no projeto.",
        roadmap_topics=("Ferramentas básicas de produtividade", "Estudo guiado com ritmo leve"),
    ),
    StudyModule(
        id="github-hello-world",
        title="Hello World com GitHub",
        description="Crie um repositório e experimente branches, alterações e pull requests.",
        category_id="ferramentas-produtividade",
        level="Iniciante",
        study_minutes=30,
        language="Inglês",
        url="https://docs.github.com/en/get-started/using-github/hello-world",
        activity="Crie um arquivo README e proponha uma alteração usando uma branch.",
        roadmap_topics=("Ferramentas básicas de produtividade",),
    ),
    StudyModule(
        id="introducao-vscode",
        title="Conheça o Visual Studio Code",
        description="Veja os recursos básicos do editor e prepare o ambiente para praticar programação.",
        category_id="ferramentas-produtividade",
        level="Iniciante",
        study_minutes=25,
        language="Inglês",
        url="https://code.visualstudio.com/docs/getstarted/introvideos",
        activity="Abra um arquivo, use a busca e personalize uma configuração do editor.",
        roadmap_topics=("Ferramentas básicas de produtividade", "Estudo guiado com ritmo leve"),
    ),
)


def get_categories_for_profile(profile: str) -> tuple[LearningCategory, ...]:
    """Retorna as categorias adequadas ao perfil; perfis desconhecidos usam o iniciante."""
    selected_profile = profile if profile in {"programming", "tech", "beginner"} else "beginner"
    return tuple(
        category
        for category in LEARNING_CATEGORIES
        if selected_profile in category.profiles
    )


def get_modules_for_profile(
    profile: str,
    category_id: str | None = None,
    level: str | None = None,
    roadmap_topic: str | None = None,
) -> tuple[StudyModule, ...]:
    """Filtra módulos por perfil, categoria, nível e etapa do roadmap."""
    category_ids = {category.id for category in get_categories_for_profile(profile)}
    return tuple(
        module
        for module in STUDY_MODULES
        if module.category_id in category_ids
        and (category_id is None or module.category_id == category_id)
        and (level is None or module.level == level)
        and (roadmap_topic is None or roadmap_topic in module.roadmap_topics)
    )


def render_learning_page(profile: str | None = None) -> None:
    """Exibe as categorias de estudo, personalizadas quando há um perfil conhecido."""
    render_icon_heading("Aprender", "book-open")

    render_learning_categories(profile)


def render_learning_categories(profile: str | None = None) -> None:
    """Exibe módulos filtrados por categoria e nível, dentro da página ou roadmap."""
    from app.roadmap import ROADMAPS

    render_icon_heading("Materiais e módulos de estudo", "book-open")

    if profile is None:
        categories = LEARNING_CATEGORIES
        selected_profile = None
        st.markdown("Explore os módulos disponíveis. Complete o quiz para receber recomendações por perfil.")
        roadmap_topics = sorted(
            {topic for topics in ROADMAPS.values() for topic in topics}
        )
    else:
        categories = get_categories_for_profile(profile)
        selected_profile = profile if profile in {"programming", "tech", "beginner"} else "beginner"
        profile_names = {
            "programming": "Programação",
            "tech": "Tecnologia",
            "beginner": "Iniciante",
        }
        st.markdown(
            f"Categorias recomendadas para o perfil "
            f"**{profile_names[selected_profile]}**."
        )
        roadmap_topics = ROADMAPS[selected_profile]

    category_options = {"Todas as categorias": None}
    category_options.update({category.name: category.id for category in categories})
    level_options = ("Todos os níveis", "Iniciante", "Intermediário", "Avançado")
    topic_options = ("Todas as etapas", *roadmap_topics)

    if selected_profile is None:
        st.info("Mostrando materiais de todos os perfis. Faça o quiz para personalizar esta seleção.")

    filter_columns = st.columns(3)
    with filter_columns[0]:
        selected_category = st.selectbox(
            "Categoria",
            tuple(category_options),
            key=f"learning_category_filter_{selected_profile or 'all'}",
            index=0,
        )
    with filter_columns[1]:
        selected_level = st.selectbox(
            "Nível",
            level_options,
            key=f"learning_level_filter_{selected_profile or 'all'}",
            index=0,
        )
    with filter_columns[2]:
        selected_topic = st.selectbox(
            "Etapa do roadmap",
            topic_options,
            key=f"learning_topic_filter_{selected_profile or 'all'}",
            index=0,
        )

    allowed_category_ids = {category.id for category in categories}
    category_id = category_options[selected_category]
    roadmap_topic = None if selected_topic == "Todas as etapas" else selected_topic
    modules = tuple(
        module
        for module in STUDY_MODULES
        if module.category_id in allowed_category_ids
        and (category_id is None or module.category_id == category_id)
        and (selected_level == "Todos os níveis" or module.level == selected_level)
        and (roadmap_topic is None or roadmap_topic in module.roadmap_topics)
    )

    if not modules:
        st.info("Não há módulos para esses filtros. Tente outra categoria ou nível.")
        return

    modules_by_category = {
        category.id: tuple(module for module in modules if module.category_id == category.id)
        for category in categories
    }
    for category in categories:
        category_modules = modules_by_category[category.id]
        if not category_modules:
            continue

        category_icon = get_icon_svg(CATEGORY_ICONS[category.id], size=20)
        st.markdown(
            f"""
            <h4 class="cs-icon-heading">
                <span class="cs-heading-icon">{category_icon}</span>
                <span>{category.name}</span>
            </h4>
            """,
            unsafe_allow_html=True,
        )
        st.caption(category.description)
        columns = st.columns(2)
        for index, module in enumerate(category_modules):
            with columns[index % len(columns)]:
                with st.container(border=True):
                    st.markdown(f"##### {module.title}")
                    st.write(module.description)
                    st.caption(
                        f"{module.level} · sessão sugerida de {module.study_minutes} min "
                        f"· recurso em {module.language}"
                    )
                    st.markdown(f"**Prática:** {module.activity}")
                    if selected_profile is not None:
                        st.caption(
                            "Etapas relacionadas: " + ", ".join(module.roadmap_topics)
                        )
                    render_icon_link_button(
                        "Abrir material",
                        "arrow-right",
                        module.url,
                    )