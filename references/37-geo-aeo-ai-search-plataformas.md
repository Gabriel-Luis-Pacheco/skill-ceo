# 37 — GEO, AEO, LLMO e busca por IA: o que fazer e o que não sabemos

**Quando ler:** objetivo de aparecer em ChatGPT, Gemini, Google AI Overviews/AI Mode, Copilot, Claude, Perplexity ou outro mecanismo de respostas. Tratar como extensão de descoberta e reputação, não como promessa de manipular um LLM.

## 1. Pipeline mental útil

Busca generativa com grounding pode seguir: intenção → reformulação em subconsultas → busca lexical/semântica → recuperação de passagens → seleção/reranking → contexto → geração → associação de citações → resposta. Algumas plataformas fazem query fan-out. Embeddings são representações vetoriais úteis a sistemas semânticos, **não** scores de marketing observáveis que alguém possa otimizar diretamente. Arquitetura varia por produto, modelo e data; mecanismos proprietários não são completamente públicos.

Separar quatro resultados:
1. **Elegibilidade/recuperação** — informação acessível e relevante foi encontrada.
2. **Menção** — a resposta menciona a marca, mesmo sem link.
3. **Citação** — há link para uma página; não implica necessariamente que sua informação fundamentou a resposta.
4. **Influência/ação** — evidência da marca foi usada ou o usuário clicou/converteu. Atribuição parcial é comum.

Não confundir menção da marca com citação de domínio, nem citação com venda. O conteúdo proprietário é só uma parte: publishers, reviews, comunidades e comparadores frequentemente fazem parte do conjunto de evidências recuperadas.

## 2. O que varia por plataforma

| Produto | Conhecimento público e cautela | Ação controlável |
|---|---|---|
| Google Search, AI Overviews e AI Mode | Integram sistemas centrais de Search; podem usar RAG/grounding e query fan-out. Google não exige schema próprio de GEO, llms.txt ou chunking artificial. | páginas indexáveis e elegíveis a snippet, conteúdo não comoditizado, arquitetura, confiança, imagens/vídeos, dados estruturados pertinentes |
| Bing e Copilot | Compartilham fundamentos de crawling, indexação e ranking; Bing Webmaster inclui sinais de performance de citações/temas conforme disponibilidade. | sitemap, IndexNow, Bingbot, dados claros, páginas úteis, Bing Webmaster |
| ChatGPT Search | OAI-SearchBot é separado de GPTBot (uso de treinamento); consultas podem ser reescritas e processadas com provedores de busca. | permitir bot de busca conforme política do proprietário, não bloquear indevidamente WAF/IP, construir presença em fontes recuperáveis |
| Perplexity | Mecanismo de respostas com pesquisa na web e citações; detalhes de seleção variam. | conteúdo verificável, dados originais, atualização, distribuição e boa acessibilidade |
| Claude | Claude-SearchBot, ClaudeBot e Claude-User têm finalidades distintas; uso de web search depende do contexto do usuário. | respeitar política de crawl e conferir acesso às fontes, sem presumir seleção |
| Gemini | Pode apresentar fontes; ecossistema Google importa, mas critérios completos não são públicos. | páginas claras, indexação, autoria, multimodal, distribuição e informação factual coerente |

**Crawler de busca não é crawler de treinamento.** Nunca abrir todos os bots por reflexo nem bloquear todos por medo. Fazer decisão de governança explícita para cada bot, consultar documentações e testar acesso em logs. Não prometer que permissão garante citação. Para Google, distinguir Googlebot, Google-Extended e eventuais controles específicos de Search conforme versão da documentação.

## 3. Estratégia GEO defensável

**Recuperabilidade:** HTML com entidade e resposta compreensíveis; canonical, indexação e acessibilidade compatíveis com cada mecanismo; blocos importantes não escondidos atrás de login/JS inacessível, quando devem ser públicos.

**Correspondência semântica:** mapear as perguntas reais do cliente, suas reformulações e critérios. Uma única página útil pode responder diferentes variações. Evitar criar páginas quase idênticas para toda versão de prompt.

**Informação citável:** dados próprios com método e limites, procedimentos verificáveis, definições precisas, comparativos transparentes, FAQ real, estudos de caso, benchmark, testes e demonstrações. Citar fontes primárias para fatos externos. Clareza estrutural beneficia humanos e recuperação; tamanho de parágrafo ou markup mágico não é requisito.

**Coerência de entidade:** nome oficial, URL, produto, categoria, pessoas e atributos alinhados em site, perfis, imprensa, parceiros, diretórios e avaliações autênticas. Erros de nome ou promessas contraditórias prejudicam confiança e desambiguação.

**Autoridade distribuída:** conquistar menções editoriais e presença em fontes que clientes realmente consultam. PR, comunidades, YouTube e reviews precisam agregar valor; jamais posts anônimos fingindo ser clientes, citações compradas ou conteúdo parasita.

**Conversão:** mesmo quando a IA responde sem clique, o usuário deve encontrar uma proposta clara ao buscar a marca: landing, demonstração, comparações honestas, preços e reputação coerentes.

## 4. Protocolo de medição de visibilidade por IA

Criar amostra de prompts estratificada por estágio: problema, solução, categorias, melhores alternativas, comparação, objeção, decisão e implementação. Fixar idioma, geografia, modo/versão, momento e sessão quando possível. Registrar amostra e fonte de cada prompt; preferir perguntas que usuários reais fazem, não só o nome da própria marca.

Para cada rodada armazenar: data/hora, plataforma, prompt, contexto, se houve busca, marcas mencionadas, links citados, domínios, narrativa sobre a marca, evidência textual absorvida, tipo de resposta, captura/URL, variações e limitações. Fazer repetição longitudinal e controles, em vez de testar uma pergunta só.

Métricas úteis:
- taxa de menção = respostas que mencionam a marca / respostas válidas da amostra;
- taxa de citação = respostas com URL da marca / respostas válidas;
- share de menções/citações dentro de conjunto de concorrentes **definido e fixo**;
- cobertura de jobs/intents, citations por tema e pages citadas;
- visitas referidas por IA quando mensuráveis (ex.: parâmetros de origem, referrers);
- branded search, receita e inscrições assistidas, **sem atribuição causal automática**.

Sinal de erro: prometer “visibilidade 98% no ChatGPT” sem informar amostra, região, plataforma, versões, sessões e viés.

## 5. Experimento de conteúdo para Search + IA

Hipótese testável: “Para perguntas de [job/intenção], melhorar [página] com [dado único/prova] aumentará a frequência de menção/citação e a conversão qualificada, comparada a [grupo de controle]”.

Etapas: baseline → amostra de perguntas e páginas → implementação → inspecionar publicação/indexação → aguardar recrawl razoável → repetir medições em mesmo protocolo → comparar controle → verificar resultados comerciais. Não atribuir efeito a uma alteração apenas porque resposta mudou após publicação.

Quando amostra for pequena: resultado **exploratório**. Quando houver múltiplas mudanças, concorrência, personalização ou atualização de modelo, mencionar confundidores. Evitar apresentar score de ferramentas de AI visibility como receita.

## 6. Mitos e níveis de evidência

- **Oficial**: Google não oferece exigência de schema GEO, llms.txt ou chunking para AI Overviews/AI Mode.
- **Oficial**: permissões de crawlers de busca e de treinamento podem ser distintas.
- **Pesquisa acadêmica**: GEO (KDD 2024) encontrou ganhos em benchmark experimental; resultados não se transferem automaticamente para 2026 e plataformas específicas.
- **Observacional/preprint**: alinhamento semântico e qualidades de conteúdo estão associados a citações em amostras; associação não revela algoritmo nem causalidade.
- **Mito**: “colocar o nome ChatGPT 100 vezes obriga a IA a citar”.
- **Mito**: “mil posts sintéticos garantem topical authority”.
- **Mito**: “schema especial ou llms.txt garante ranking”.
- **Mito**: “o mesmo prompt terá a mesma resposta em qualquer sessão”.

## 7. Prontidão para busca e agentes

Prepare páginas operáveis por humanos e agentes: navegação semântica, estados explícitos de botões, formulários rotulados, preços e termos transparentes, fluxo reversível quando possível, acessibilidade, APIs/feed se relevantes, segurança contra abuso e logs. **Não** afrouxar autenticação, CAPTCHA ou cobrança para “SEO de agentes”. Testar sob permissões adequadas.

## Fontes

- Google AI optimization: https://developers.google.com/search/docs/fundamentals/ai-optimization-guide
- Google AI features: https://developers.google.com/search/docs/appearance/ai-features
- OpenAI crawlers: https://developers.openai.com/api/docs/bots
- ChatGPT Search: https://help.openai.com/en/articles/9237897-searching-the-web-with-chatgpt
- Anthropic crawlers: https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler
- Bing Webmaster: https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a
- Bing AI Performance (2026): https://blogs.bing.com/webmaster/2026/2/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview/
- Bing Citation Share (2026): https://blogs.bing.com/search/2026/6/New-AI-Visibility-Insights-in-Bing-Webmaster-Tools-Intents-Topics-Citation-Share-Compare/
- GEO (KDD 2024): https://doi.org/10.1145/3637528.3671900
- Estudos emergentes, **preprint**: https://arxiv.org/abs/2610.15033 ; https://arxiv.org/abs/2604.25707

Pesquisa-base consolidada em 14/11/2026. Revalidar documentação atual antes de afirmações específicas.
