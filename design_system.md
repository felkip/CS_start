# Design System — CS Start

## 1. Objetivo

Este documento orienta a evolução visual do CS Start para que cores, tipografia, ícones e componentes formem uma experiência coesa nos temas claro e escuro.

O sistema deve ajudar quem está começando a estudar computação a entender onde está, o que pode fazer e qual é o próximo passo. Clareza e acessibilidade têm prioridade sobre decoração.

## 2. Identidade visual

- **Personalidade:** acolhedora, clara, confiável e ligada à tecnologia.
- **Cores de identidade:** ciano como primário, com azul e violeta como acentos análogos frios.
- **Estilo:** superfícies simples, hierarquia tipográfica evidente e destaques usados com intenção.
- **Princípio geral:** elementos visualmente próximos ou semelhantes devem também ter relação ou comportamento semelhante.

Gradientes podem destacar áreas de identidade, como o cabeçalho, mas não devem ser usados em todos os fundos. Evitar competir com o conteúdo ou prejudicar a leitura.

## 3. Princípios de percepção aplicados à interface

Os princípios de Gestalt devem orientar a organização visual, sem substituir rótulos, instruções e estrutura semântica.

### Proximidade

Elementos próximos são percebidos como relacionados.

- Agrupar título, descrição, duração e ação dentro do mesmo card de material.
- Manter filtros próximos aos resultados que controlam.
- Separar etapas diferentes do roadmap com espaço consistente.
- Não usar proximidade como único indicador de associação; manter títulos e rótulos claros.

### Similaridade

Elementos com aparência semelhante são percebidos como pertencentes à mesma categoria.

- Usar o mesmo padrão de card para materiais do mesmo tipo.
- Manter ações equivalentes com aparência, rótulo e posição consistentes.
- Reservar cores semânticas para sucesso, aviso, erro e informação, sem reutilizá-las como decoração.
- Usar a mesma família e estilo de ícones em toda a aplicação.

### Figura e fundo

O conteúdo importante deve se destacar do plano de fundo sem perder legibilidade.

- Diferenciar página, painel e conteúdo elevado com tons e bordas adequados ao tema.
- Garantir contraste entre texto, fundo, controles e estados.
- Usar sombra com moderação; não depender dela para delimitar conteúdo.
- Evitar que fundos coloridos ou gradientes prejudiquem texto e foco.

### Continuidade

O olhar deve conseguir acompanhar uma sequência ou direção.

- Apresentar as etapas do roadmap em ordem clara e com numeração ou marcadores.
- Alinhar títulos, indicadores de etapa e ações de forma previsível.
- Mostrar visualmente a relação entre etapa atual, concluída e próxima.
- Em telas estreitas, preservar a ordem da jornada ao reorganizar o layout.

### Fechamento e boa forma

Conjuntos relacionados devem parecer completos e fáceis de reconhecer.

- Usar limites, espaçamento e cabeçalhos para organizar seções sem excesso de caixas.
- Manter os cards visualmente simples e com conteúdo agrupado por finalidade.
- Evitar ornamentos que pareçam controles ou estados interativos.

### Região comum

Elementos dentro de uma mesma área delimitada tendem a ser percebidos como um grupo.

- Usar cards ou painéis para agrupar conteúdo realmente relacionado.
- Não aninhar muitos cards nem colocar cada linha de texto em uma caixa.
- Aplicar a mesma estrutura visual a áreas equivalentes, como perfil, roadmap e aprendizagem.

## 4. Tokens de design

Os valores abaixo consolidam a identidade já presente na aplicação e propõem uma base para futuras revisões. Os tokens devem ser a referência; componentes não devem introduzir novas cores sem uma necessidade definida.

### 4.1 Marca e ações

| Token | Valor aplicado | Uso |
|---|---|---|
| `brand-primary` | `#0E7490` | Ação principal, seleção e links |
| `brand-primary-hover` | `#155E75` | Hover e ênfase da ação principal |
| `brand-secondary` | `#6D28D9` | Acento violeta |
| `brand-accent` | `#2563EB` | Acento azul pontual |

### 4.2 Tema claro

| Token | Valor inicial | Uso |
|---|---|---|
| `bg-page` | `#F8FAFC` | Fundo principal |
| `bg-surface` | `#FFFFFF` | Cards e painéis |
| `bg-subtle` | `#F1F5F9` | Campos e áreas secundárias |
| `text-primary` | `#0F172A` | Títulos e conteúdo principal |
| `text-secondary` | `#475569` | Descrições |
| `text-muted` | `#64748B` | Metadados e texto auxiliar |
| `text-on-brand` | `#FFFFFF` | Texto sobre superfícies de marca |
| `border` | `#E2E8F0` | Bordas e divisores |

### 4.3 Tema escuro

| Token | Valor inicial | Uso |
|---|---|---|
| `bg-page` | `#0B1220` | Fundo principal |
| `bg-surface` | `#111827` | Cards e painéis |
| `bg-subtle` | `#1E293B` | Campos e áreas secundárias |
| `text-primary` | `#F8FAFC` | Títulos e conteúdo principal |
| `text-secondary` | `#CBD5E1` | Descrições |
| `text-muted` | `#94A3B8` | Metadados e texto auxiliar |
| `text-on-brand` | `#FFFFFF` | Texto sobre superfícies de marca |
| `border` | `#334155` | Bordas e divisores |

### 4.4 Cores semânticas

| Estado | Valor inicial | Uso |
|---|---|---|
| Sucesso | `#059669` | Confirmação e conclusão |
| Atenção | `#D97706` | Aviso e informação que requer atenção |
| Erro | `#DC2626` | Falha e ação destrutiva |
| Informação | `#2563EB` | Mensagens informativas |

As cores semânticas devem ser verificadas contra a superfície do tema. A cor não deve ser o único meio de comunicar um estado: incluir texto, ícone ou outro indicador.

### 4.5 Estratégia de evolução da paleta

A paleta atual contém gradientes, tons de destaque e valores específicos de componentes que surgiram em momentos diferentes. A atualização deve ser gradual: primeiro consolidar os tokens por função, depois migrar os componentes e só então remover os valores antigos.

- **Hierarquia:** usar superfícies neutras para a maior parte da interface; reservar a cor primária para ações principais, seleção e orientação.
- **Similaridade:** aplicar os mesmos tokens a componentes com a mesma função, em vez de dar uma cor exclusiva a cada página ou card.
- **Figura e fundo:** separar conteúdo e superfície por luminosidade, borda e espaçamento; não depender de gradientes ou sombras para criar contraste.
- **Proximidade:** manter cores de grupo e estados consistentes dentro de áreas relacionadas; evitar fundos coloridos diferentes em itens equivalentes.
- **Uso contido da paleta:** cada superfície deve ter uma cor dominante; ciano, azul e violeta podem aparecer em componentes diferentes, mas não devem ser misturados no mesmo gradiente ou bloco.
- **Significado:** usar sucesso, atenção, erro e informação apenas para esses estados e acompanhá-los de texto ou outro indicador.
- **Tema:** definir equivalentes funcionais nos modos claro e escuro, sem inverter mecanicamente todas as cores.
- **Acessibilidade:** medir o contraste das combinações reais, inclusive estados de foco e interação, antes de adotar novos valores.

#### Ordem recomendada para a migração

1. Centralizar as cores de marca, superfície, texto, borda e estado em tokens.
2. Atualizar os componentes compartilhados e testar os dois temas.
3. Migrar telas por grupos relacionados, como autenticação, navegação e aprendizagem.
4. Reduzir gradientes e cores decorativas conforme a hierarquia ficar clara.
5. Remover tokens antigos apenas depois de confirmar que nenhum componente ainda os utiliza.

Cada etapa deve ser revisada visualmente em desktop e celular; não alterar simultaneamente paleta, estrutura e conteúdo de uma mesma tela, para que regressões sejam fáceis de localizar.

#### Estado da implementação (2026-11-04)

- Os componentes compartilhados em `app/ui.py` usam tokens de tema para superfícies, texto, bordas, sombras, progresso e estados do roadmap. O token `text-on-brand` representa texto sobre fundos de marca.
- A paleta ciano–azul–violeta definida abaixo foi aplicada em `static/style.css`, `app/theme.py`, `.streamlit/config.toml`, `main.py`, `app/quiz.py` e `app/roadmap.py`.
- Os fundos rosa e verdes usados como decoração nos cards de perfil foram removidos; os acentos seguem os tokens azul/ciano/violeta e os cards usam superfícies neutras.
- Testes automatizados verificam consistência do token primário entre CSS, tema e configuração Streamlit e contraste de texto branco sobre cores da paleta.
- Uma primeira revisão corrigiu o contraste do cartão de resultado do quiz; depois, conforme a preferência do usuário, o cartão foi simplificado para superfície neutra e um acento por perfil, sem gradiente.
- Os gradientes da marca foram removidos dos botões, título, badge de perfil e progresso. Azul e violeta aparecem separadamente nos cards de pontuação, mantendo a paleta mas evitando misturar seus três acentos no mesmo componente.
- Validação da revisão: `30 passed, 80 subtests passed`; os arquivos Python alterados passaram por `py_compile`. AppTest executou início, quiz/resultados, roadmap e aprendizagem nos dois temas sem exceções.
- No navegador, o resultado foi conferido em 390px e 1200px no tema claro: superfície do card sem gradiente e nenhuma rolagem horizontal. A renderização do fluxo de resultado em tema escuro foi coberta pelo AppTest.
- A medição anterior do índigo (`#6366F1`, `4.47:1`; ajustado para `#6164EF`, `4.59:1`) antecedeu a escolha do ciano e não representa mais a cor primária ativa.
- **Ainda pendente:** consolidar definições duplicadas entre CSS e Python, revisar todas as telas e estados de foco/hover/desabilitado, e ampliar a validação responsiva a tablet e às demais telas. O checklist permanece não verificado até concluir essas revisões.

#### Próximas etapas do design

As etapas abaixo mantêm cada mudança visual pequena, verificável e fácil de reverter:

1. **Paleta — concluída:** aplicar a harmonia ciano–azul–violeta aprovada e medir os pares principais.
2. **Consolidar tokens:** manter os valores de cada tema em uma única fonte de estilos e remover definições duplicadas entre CSS e Python. Manter a regra aprovada de uma cor dominante por superfície, sem gradientes que misturem os três acentos.
3. **Migrar/revisar telas:** tokens aplicados ao início, autenticação, quiz e roadmap; continuar a revisão visual da área Aprender/configurações e dos estados auxiliares sem alterar conteúdo junto com as cores.
4. **Revisar estados e acessibilidade:** medir contraste real em texto, botões, links, seleção, foco, hover, desabilitado e mensagens; verificar teclado e rótulos acessíveis.
5. **Revisar responsividade:** a tela de resultado foi verificada em 390px e 1200px no navegador em tema claro, sem rolagem horizontal; validar os demais grupos e o tema escuro em celular, tablet e desktop.
6. **Remover cores antigas e fechar checklist:** procurar valores diretos remanescentes, manter apenas exceções intencionais e marcar requisitos do checklist somente após verificação.

#### Paleta aplicada, baseada na teoria das cores

Foi adotada a harmonia **análoga fria ciano–azul–violeta**. Na roda HSV, as cores avançam pelo espectro frio: ciano `#0E7490` (cerca de 193°), azul `#2563EB` (221°) e violeta `#6D28D9` (263°). A separação entre ciano e azul é mais próxima; o violeta funciona como acento mais distante, sem competir com o ciano como cor principal. Essa combinação busca unidade e continuidade, adequada a uma interface de aprendizagem e tecnologia, sem depender de vários acentos concorrentes.

O ciano escuro é a cor de ação principal; azul e violeta entram como acentos limitados, não como fundos independentes para cada categoria. Cores quentes complementares poderiam dar mais contraste cromático, mas foram deixadas fora da marca principal para não se confundirem com o estado de atenção/aviso. A hierarquia deve vir primeiro de superfície, texto, espaçamento e forma; a cor reforça essa organização.

As razões abaixo foram calculadas sobre fundos sólidos de referência. Transparências, gradientes e estados reais devem continuar sendo verificados durante a revisão visual.

| Token | Proposta | Uso |
|---|---|---|
| `brand-primary` | `#0E7490` | Ação principal, seleção e links |
| `brand-primary-hover` | `#155E75` | Hover de ação primária |
| `brand-secondary` | `#6D28D9` | Acento violeta e gradientes pontuais |
| `brand-accent` | `#2563EB` | Acento azul pontual, não semântico |

| Token de estado | Tema claro | Tema escuro |
|---|---|---|
| `color-success` | `#047857` | `#34D399` |
| `color-warning` | `#B45309` | `#FBBF24` |
| `color-danger` | `#B91C1C` | `#F87171` |
| `color-info` | `#1D4ED8` | `#60A5FA` |

Os fundos e textos neutros permanecem nos valores já documentados nas seções 4.2 e 4.3.

Contrastes calculados para texto normal em combinações representativas:

- Branco sobre `brand-primary` `#0E7490`: **5,36:1**; branco sobre `brand-primary-hover` `#155E75`: **7,27:1**.
- Branco sobre `brand-secondary` `#6D28D9`: **7,10:1**; branco sobre `brand-accent` `#2563EB`: **5,17:1**.
- Estados do tema claro (`#047857`, `#B45309`, `#B91C1C`, `#1D4ED8`) sobre `#FFFFFF`: entre **5,48:1 e 6,70:1**.
- Estados do tema escuro (`#34D399`, `#FBBF24`, `#F87171`, `#60A5FA`) sobre `#111827`: entre **6,41:1 e 10,63:1**.

Esses resultados atendem a 4,5:1 para os pares medidos, mas não garantem contraste suficiente em fundos coloridos, gradientes, transparências ou componentes com outros estados.

## 5. Tipografia

Usar uma família sem serifa disponível no sistema, com fallbacks. Manter boa legibilidade e evitar depender de texto em gradiente.

| Nível | Tamanho de referência | Peso |
|---|---:|---:|
| Título da página | `32–40px` | 700 |
| Título de seção | `24–28px` | 600–700 |
| Título de card | `18–20px` | 600 |
| Texto principal | `16px` | 400 |
| Texto auxiliar | `14px` | 400 |
| Metadados | `12–13px` | 500 |

Manter hierarquia semântica dos títulos e evitar pular níveis sem necessidade.

## 6. Espaçamento e formas

Usar uma escala baseada em múltiplos de `4px`:

| Token | Valor |
|---|---:|
| `space-1` | `4px` |
| `space-2` | `8px` |
| `space-3` | `12px` |
| `space-4` | `16px` |
| `space-6` | `24px` |
| `space-8` | `32px` |
| `space-12` | `48px` |

| Token | Valor de referência | Uso |
|---|---:|---|
| `radius-sm` | `8px` | Campos e controles compactos |
| `radius-md` | `12px` | Botões e cards |
| `radius-lg` | `16px` | Painéis destacados |
| `radius-pill` | `999px` | Badges e etiquetas |

- Padding de card: `16–24px`.
- Distância entre seções: `24–32px`.
- Área interativa: buscar pelo menos `40px` de altura e espaço suficiente entre alvos clicáveis.

## 7. Biblioteca de ícones

### Diretriz

Adotar **Lucide** como família visual de ícones. Os SVGs iniciais, obtidos do [repositório oficial Lucide](https://github.com/lucide-icons/lucide), estão versionados em `static/icons/`, sem dependência de CDN em tempo de execução. A licença Lucide (ISC) e a licença MIT aplicável aos ícones derivados de Feather foram verificadas e incluídas em `static/icons/LICENSE`.

Os ícones já foram aplicados ao cabeçalho, perfil, navegação, autenticação, quiz, roadmap, categorias de aprendizagem, estados vazios e ações principais. Novas áreas ou ícones devem continuar sendo adicionados gradualmente, revisando legibilidade e acessibilidade a cada alteração.

### Regras de uso

- Manter a mesma família, estilo de traço e proporções.
- Usar como referência `18–20px` para controles e `24px` para destaques.
- Usar a cor do texto ou uma cor semântica pertinente.
- Acompanhar ícones funcionais com rótulos visíveis ou nomes acessíveis.
- Não usar ícone isolado quando a ação puder ser ambígua.
- Evitar misturar emojis, Material Icons e Lucide no mesmo grupo de navegação.
- Para a interface, usar os SVGs locais por meio dos helpers de `app/ui.py`; não passar emojis antigos ao renderizador de ícones.
- Substituir emojis existentes gradualmente, priorizando navegação e ações; não fazer uma troca em massa sem validar a renderização e acessibilidade.

### Vocabulário inicial

| Contexto | Nome Lucide sugerido |
|---|---|
| Início | `house` |
| Aprendizagem | `book-open` |
| Roadmap | `map` |
| Perfil | `user-round` |
| Progresso | `chart-no-axes-column-increasing` |
| Concluído | `circle-check` |
| Próxima etapa | `arrow-right` |
| Tema claro / escuro | `sun` / `moon` |
| Configurações | `settings-2` |
| Aviso | `triangle-alert` |
| Ajuda | `circle-help` |
| Entrar / cadastrar | `log-in` / `user-round-plus` |
| Fundamentos / programação | `brain` / `code` |
| Tecnologia / ferramentas | `monitor` / `wrench` |
| Dicas / download | `lightbulb` / `download` |

## 8. Padrões de componentes

### Botões

- **Primário:** ação principal da área, com `brand-primary` e texto legível.
- **Secundário:** ação alternativa, com superfície ou borda distinta.
- **Destrutivo:** somente para ações irreversíveis; rótulo deve explicar a consequência.
- Definir estados de foco, hover, desabilitado e carregamento.
- O rótulo deve começar com uma ação clara, como “Continuar” ou “Abrir material”.

### Cards

- Agrupar apenas informações relacionadas, seguindo proximidade e região comum.
- Usar uma superfície, uma borda e um raio consistentes em ambos os temas.
- Priorizar título, descrição e ação nessa ordem.
- Usar acentos de cor para indicar categoria ou estado, não como decoração arbitrária.
- Evitar diferenças de altura que dificultem comparar itens equivalentes; em telas estreitas, empilhar os cards.

### Campos e filtros

- Manter rótulo explícito, estado de foco visível e contraste adequado.
- Posicionar filtros perto dos resultados controlados.
- Explicar erros junto ao campo e indicar como corrigi-los.
- Preservar a leitura do texto selecionado nos temas claro e escuro.

### Roadmap e progresso

- Mostrar etapas em ordem e distinguir claramente atual, concluída e futura.
- Combinar cor com texto, numeração ou ícone de estado.
- Manter conectores ou indicadores visuais alinhados para reforçar continuidade.
- Em telas pequenas, reorganizar sem alterar a sequência nem esconder estados.

## 9. Acessibilidade

- Buscar contraste WCAG AA: `4.5:1` para texto normal e `3:1` para texto grande e componentes gráficos.
- Verificar contraste em cada tema e estado, inclusive hover, foco e desabilitado.
- Garantir navegação por teclado e foco perceptível.
- Não depender exclusivamente de cor, posição ou ícone para comunicar informação.
- Manter textos auxiliares legíveis e não reduzir metadados abaixo de `12px`.
- Dar nomes acessíveis a controles representados por ícones.
- Links de ação e botões de download devem manter contraste entre texto e superfície nos dois temas, incluindo hover e foco.
- Na barra lateral escura, itens inativos e a ação de sair devem ter superfície e borda distinguíveis do fundo, com texto legível e foco visível; o item atual mantém o destaque primário.

Os valores desta proposta não dispensam a medição do contraste das combinações reais antes da adoção.

## 10. Responsividade

- Usar uma coluna em telas estreitas quando múltiplas colunas comprimirem o conteúdo.
- Permitir que cards, filtros e botões ocupem a largura disponível no celular.
- Evitar texto cortado; permitir quebra de linha em títulos, descrições e ações.
- Reduzir espaços decorativos em telas pequenas, sem reduzir legibilidade ou área interativa.
- Preservar agrupamento, hierarquia e ordem do conteúdo ao mudar o layout.

## 11. Manutenção e evolução

- Manter tokens em um ponto central de referência e reutilizá-los nos componentes.
- Evitar valores hexadecimais e estilos inline repetidos quando um token ou componente compartilhado atender.
- Aplicar qualquer mudança de paleta nos temas claro e escuro.
- Ao criar um componente, definir sua finalidade, hierarquia, estados e comportamento responsivo.
- Ao incluir um ícone, verificar consistência visual, licença e nome acessível.
- Fazer alterações visuais em etapas pequenas e validar telas principais antes de publicar.

## 12. Checklist de revisão

- [ ] A hierarquia permite identificar rapidamente título, conteúdo e ação.
- [ ] Proximidade e limites agrupam apenas elementos relacionados.
- [ ] Elementos equivalentes mantêm aparência e comportamento semelhantes.
- [ ] A ordem do roadmap continua clara e sequencial.
- [ ] Cores e textos são legíveis nos dois temas.
- [ ] Contraste foi verificado para texto, controles e estados.
- [ ] Ícones pertencem à mesma família e têm rótulos acessíveis quando necessário.
- [ ] Foco por teclado e estados de interação são perceptíveis.
- [ ] Layout funciona em desktop, tablet e celular.
- [ ] A solução visual não depende apenas de cor, sombra ou decoração.
