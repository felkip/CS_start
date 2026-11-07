# Changelog do projeto

Este arquivo reúne os principais registros de evolução do projeto desde o MVP, mantendo a linha do tempo e destacando as mudanças relevantes em cada etapa.

---

## 2026-07 a 2026-08 | Atualizações após o MVP

### Interface visual e UX
- Adição do arquivo de estilos em [static/style.css](static/style.css) com visual moderno, gradientes e layout responsivo.
- Criação do módulo [app/ui.py](app/ui.py) com componentes reutilizáveis para cabeçalho, cards, badge do usuário, progresso, roadmap e estados vazios.
- Ajuste do [main.py](main.py) para usar uma navegação em sidebar, layout amplo e interface mais refinada.

### Quiz e roadmap
- Revisão da experiência do quiz com barra de progresso e cards de pergunta.
- Aprimoramento do módulo [app/quiz.py](app/quiz.py) com inicialização controlada, reset do estado e correção de erros de session state.
- Melhorias no [app/roadmap.py](app/roadmap.py), incluindo perfis, itens formatados, dicas e download do roadmap.

### Autenticação e fluxo do app
- Mantém a autenticação em [app/auth.py](app/auth.py) e melhora o fluxo de login/cadastro no [main.py](main.py).
- Sincronização do estado de navegação com a sidebar.
- Ações de iniciar quiz e voltar ao início passaram a ser mais consistentes e previsíveis.

### Configuração, testes e manutenção
- Criação do arquivo de configuração do Streamlit em [.streamlit/config.toml](.streamlit/config.toml).
- Atualização de dependências em [requirements.txt](requirements.txt).
- Instalação e uso do pytest para validação local.
- Criação de documentação de limpeza em [cleanup_suggestions.md](cleanup_suggestions.md) e ajustes no [.gitignore](.gitignore).
- Registro de erros e correções em [errors.md](errors.md).

### Como validar localmente
1. Ativar o ambiente virtual.
2. Executar a aplicação com Streamlit.
3. Rodar a suíte de testes com pytest.

---

## 2026-08 a 2026-10 | Aprimoramentos de conteúdo e aprendizagem

### Área de aprendizagem
- Criação de [app/learning.py](app/learning.py) com quatro categorias principais: fundamentos de computação, programação, tecnologia e sistemas, e produtividade.
- Inclusão de 13 módulos de estudo com descrição, nível, duração, idioma, link externo, atividade prática e tópicos relacionados ao roadmap.
- Filtros por categoria, nível e etapa do roadmap para facilitar a recomendação de conteúdo.
- Personalização do conteúdo com base no perfil do usuário.

### Integração com o roadmap
- O [app/roadmap.py](app/roadmap.py) passou a incluir conteúdos relevantes para cada etapa e perfil.
- O [main.py](main.py) recebeu entrada para a nova seção de aprendizagem e também uma tela de configurações.
- O fluxo agora permite avançar entre início, quiz, roadmap e aprender de forma mais clara.

### Testes
- Criação de [tests/test_learning.py](tests/test_learning.py) para validar categorias, módulos, filtros e ligações com os perfis.
- Atualização de [tests/test_roadmap.py](tests/test_roadmap.py) para validar navegação e integração do roadmap.
- Resultado verificado: 16 testes passaram, com 28 subtests aprovados.

### Arquivos principais envolvidos
- Adicionados: [app/learning.py](app/learning.py), [app/theme.py](app/theme.py), [tests/test_learning.py](tests/test_learning.py)
- Atualizados: [main.py](main.py), [app/roadmap.py](app/roadmap.py), [tests/test_roadmap.py](tests/test_roadmap.py), [README.md](README.md)

---

## 2026-11-04 | Sistema visual e refinamento da interface

### Design system e tokens
- Criação de [design_system.md](design_system.md) com paleta, tokens, contraste, espaçamento, tipografia e diretrizes de uso.
- Padronização visual da aplicação para melhorar legibilidade e consistência em tema claro e escuro.
- Ajuste de cores, superfícies e estados para manter uma hierarquia visual mais clara.

### Ícones e componentes
- Substituição de emoji por ícones Lucide em SVG em [static/icons](static/icons). 
- Atualização dos componentes compartilhados em [app/ui.py](app/ui.py) para usar ícones, botões e inputs mais consistentes.
- Melhorias de acessibilidade em rótulos, contraste e organização visual.

### Tema e paleta aplicada
- Ajuste da paleta para a harmonia ciano, azul e violeta.
- Remoção de elementos decorativos que competiam com o conteúdo.
- Melhor equilíbrio entre ações principais, cards e textos em ambos os temas.

### Validação
- Validação de consistência visual e de contraste.
- Suíte validada com 30 testes e 80 subtests aprovados.
- Verificação do app em largura estreita e larga, sem rolagem horizontal no tema claro.
- Python compilado sem erros; o fluxo de início, quiz, roadmap e aprendizagem foi validado em testes automatizados.

### Próximos passos
- Consolidar tokens e remover duplicações entre CSS e Python.
- Revisar estados de foco, hover e desabilitados.
- Aplicar a mesma checagem visual em telas restantes e em dispositivos móveis.
- Manter a padronização de ícones, espaçamento e cores em futuras evoluções.

### Correções finais da interface
- Substituição dos emojis restantes em `main.py` por ícones Lucide locais, incluindo autenticação, navegação, cards, quiz, configurações e ações.
- Navegação lateral migrada para botões reutilizáveis com ícones, preservando o destaque da página ativa. Também foi corrigido um nome de ícone inválido que impedia a renderização da tela inicial.
- Links para materiais e botões de download ajustados para usar fundo ciano, texto branco, hover mais escuro e foco visível, corrigindo texto ilegível no tema claro.
- Botões secundários da sidebar no tema escuro receberam superfície, borda e estados de hover/foco distinguíveis do fundo.
- Corrigido o ícone do controle de expandir a sidebar, que não tinha contraste suficiente no cabeçalho escuro; cor, superfície, borda e foco passaram a seguir os tokens do tema.
- A revisão de contraste registrou `5,36:1` para texto branco sobre o ciano primário e `14,6:1` para texto claro sobre a superfície escura dos botões secundários.

### Validações incrementais em 2026-11-04
- Revisão geral de telas e temas: `30 passed, 80 subtests passed`; compilação Python e AppTest aprovados.
- Links de materiais e downloads: `31 passed, 82 subtests passed`; estilos conferidos no navegador.
- Navegação e saída no tema escuro: `32 passed, 84 subtests passed`; estilos computados conferidos no navegador.
- Controle para expandir a sidebar: `33 passed, 86 subtests passed`; compilação Python aprovada e cores do ícone, superfície e borda conferidas no navegador.
- Login verificado no navegador em 1200 px e cadastro em 390 px, sem erros ou rolagem horizontal.

---

## Resumo
O projeto evoluiu de uma interface inicial para uma experiência mais completa, começando em melhorias visuais e fluxo de navegação, passando por conteúdo educativo personalizado e consolidando uma base de design mais profissional e acessível.
