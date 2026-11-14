# Dossiê de pesquisa: SEO, GEO, AEO, AI Search e crescimento orgânico — 14/11/2026

**Origem:** síntese operacional original do relatório de Pesquisa Aprofundada solicitado em 14/11/2026. Este documento NÃO representa leitura integral de todos os sites, papers e livros mencionados, nem auditoria do tráfego real do BataTalk. Nas referências 46–52 o material está convertido em decisões, provas e checklists.

## Pergunta de pesquisa

Como aumentar a probabilidade de uma marca ser **descoberta → recuperada → compreendida → citada/mencionada → escolhida → usada → recomendada**, com receita, confiança e qualidade, em Search, buscas com IA e outros canais de descoberta, sem depender de hacks, spam ou garantias?

**Tese central:** SEO técnico permanece a infraestrutura de descoberta, mas ranking, cliques, citações e conversões são resultados diferentes. Conteúdo proprietário e reputação distribuída aumentam a utilidade e a probabilidade de ser fonte; oferta, UX e produto determinam resultado econômico. A IA pode sintetizar respostas sem enviar tráfego; uma empresa precisa também de marca lembrada e relações diretas.

## Evidência que deve afetar decisões

1. **Google Search Central, documentação oficial (consultada na pesquisa em novembro de 2026):** AI Overviews e AI Mode permanecem conectados a sistemas de Search, com grounding/RAG e possível query fan-out. Não exigem schema GEO separado, llms.txt, chunking mecânico ou otimização secreta. É necessário que o conteúdo relevante seja acessível e elegível conforme regras do Search. Fonte: https://developers.google.com/search/docs/fundamentals/ai-optimization-guide .
2. **OpenAI, documentação oficial:** OAI-SearchBot para descoberta de Search e GPTBot ligado a potencial treinamento têm finalidades/controlos distintos. ChatGPT Search pode reformular buscas e utilizar terceiros. Fontes: https://developers.openai.com/api/docs/bots ; https://help.openai.com/en/articles/9237897-searching-the-web-with-chatgpt .
3. **Anthropic, documentação oficial:** ClaudeBot, Claude-SearchBot e Claude-User não são a mesma finalidade. A decisão de crawling deve ser configurada com conhecimento e verificada em logs, sem prometer que isso force menções. Fonte: https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler .
4. **Microsoft/Bing, documentação e anúncios em 2026:** fundamentos de crawling/indexação continuam centrais para Search/Copilot; Bing Webmaster introduziu AI Performance (fevereiro de 2026) e recursos como Citation Share, intents e topics (junho de 2026), com extensão de tópicos em outubro de 2026. Disponibilidade por conta e superfície precisa ser confirmada. Fontes: https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a ; https://blogs.bing.com/webmaster/2026/2/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview/ ; https://blogs.bing.com/search/2026/6/New-AI-Visibility-Insights-in-Bing-Webmaster-Tools-Intents-Topics-Citation-Share-Compare/ ; https://blogs.bing.com/webmaster/2026/10/introducing-topics-portfolio-beta-in-ai-performance/ .
5. **Pew Research, estudo observacional com buscas de março de 2025, publicado em julho:** entre visitas Google observadas, houve clique em resultado tradicional em 8% dos casos com AI Overview, comparado a 15% sem esse resumo; clique em fonte dentro do resumo ocorreu em cerca de 1% dos casos com AI Overview. **Não extrapolar** para toda a população ou atribuir causalidade integral à interface. Fonte: https://www.pewresearch.org/short-reads/2025/07/21/google-users-are-less-likely-to-click-on-links-when-an-ai-summary-appears-in-the-results/ .
6. **Ahrefs, análise de fevereiro de 2026:** associação de AI Overview com redução de cerca de 58% no CTR do resultado orgânico de primeira posição em seu recorte de dados. **Observação, não experimento causal universal.** Fonte: https://ahrefs.com/blog/ai-overviews-reduce-clicks-update/ .
7. **Seer Interactive, atualização de abril de 2026:** observou recuperação de CTR de consultas com AI Overviews entre dezembro de 2025 e fevereiro de 2026 em sua amostra. Isso desafia a ideia de uma queda linear e invariável; ferramentas e períodos usam desenhos diferentes. Fonte: https://www.seerinteractive.com/insights/aio-impact-on-google-ctr-2026-update .
8. **Paper GEO KDD 2024:** métodos de apresentação/evidência elevaram visibilidade em cenários experimentais, com ganhos de até 40% em determinadas condições. Não é “+40% garantido” para Google/ChatGPT atuais. DOI: https://doi.org/10.1145/3637528.3671900 .
9. **Preprints de 2026:** pesquisas sobre seleção/absorção de citações e sobre retrieval/alinhamento semântico ajudam a gerar hipóteses, mas não descrevem algoritmos proprietários e carecem de replicação. https://arxiv.org/abs/2604.25707 ; https://arxiv.org/abs/2610.15033 .
10. **Semrush, AI Visibility Index 2026:** análise comercial com volume amplo de prompts reporta divergência entre marcas mencionadas e domínios citados. Amostra, países, tópicos e metodologia impedem extrapolar proporções a qualquer nicho. https://www.semrush.com/news/463141-semrush-releases-expanded-2026-ai-visibility-index-analyzing-126-million-ai-search-prompts/ .
11. **McKinsey, State of the Consumer 2026:** estudo de citações para bens de consumo sugere grande importância de fontes de terceiros; percentuais do setor não devem ser transformados em lei universal. https://www.mckinsey.com/~/media/mckinsey/industries/consumer%20packaged%20goods/our%20insights/state%20of%20consumer/2026/state%20of%20the%20consumer%202026_when%20tech%20acceleration%20and%20cost%20pressures%20collide.pdf .
12. **Reuters Institute, 2026:** documenta mudanças na distribuição de notícias e preocupação com tráfego vindo de buscas. Evidência de publishers não equivale a previsão para SaaS, loja ou empresa local. https://reutersinstitute.politics.ox.ac.uk/digital-news-report/2026/dnr-executive-summary ; https://reutersinstitute.politics.ox.ac.uk/journalism-media-and-technology-trends-and-predictions-2026 .
13. **Nielsen Norman Group, pesquisa de uso em 2026:** IA é usada para sínteses/perguntas complexas, enquanto busca tradicional ainda é buscada para certos fatos e verificações. Amostra qualitativa é insumo de UX, não fórmula universal de CTR. https://www.nngroup.com/articles/ai-search-infoseeking/ .

## Taxonomia de confiança obrigatória

- **OFICIAL / DOCUMENTADO:** declaração do operador da plataforma. Relatar o escopo exato; não converter em garantia.
- **EVIDÊNCIA INDEPENDENTE:** amostra, definição, método, país, período e limitações descritos.
- **PREPRINT / HIPÓTESE:** achado preliminar a testar com controles, não algoritmo confirmado.
- **EXPERIMENTO PRÓPRIO:** efeito observado sob condições registradas. Evitar extrapolar sem réplica.
- **MITO / NÃO VERIFICADO:** alegação de score secreto, schema mágico, número fixo de palavras por chunk ou manipulação garantida.
- **SEM DADOS / SEM ACESSO:** deixar explícito; não inventar dashboards nem disponibilidade.

## Cadeia de valor completa

**Demanda → descoberta → acesso de crawler → indexação → relevância/recuperação → atenção → compreensão → confiança → clique ou lembrança → primeira experiência útil → retenção → pagamento → margem → recomendação → nova demanda.**

Os gargalos são mutuamente diferentes. Em site novo, esforços SEO podem ter horizonte longo enquanto entrevistas, parcerias e contato humano geram aprendizado agora. Em sites com tráfego existente e taxa de conversão fraca, CRO/produto pode dominar. Em site bloqueado tecnicamente, conteúdo adicional não resolve.

## Metodologias cruzadas

- **Marketing estratégico:** segmentação/ICP/JTBD, escolha de categoria, alternativa atual, vantagem competitiva e proposta de valor.
- **SEO:** técnica, semântica, intenção, autoridade/editorial, local, internacional, e-commerce, programático quando há valor único.
- **GEO/AEO:** recuperação, menção, citação, fontes de terceiros, clareza, evidência, monitoramento longitudinal.
- **Copy:** consciência do comprador, AIDA/PAS como lentes, prova real, headline/CTA coerentes, não texto genérico.
- **CRO:** entendimento, confiança, fricção, risco, intenção e experimento com guardrails.
- **Distribuição:** owned/earned/social/communities, digital PR ético, relacionamento direto e efeito de marca.
- **Gestão:** restrição crítica, impacto/confiança/esforço, execução, verificação e aprendizagem.
- **Governança:** privacidade, licenças, políticas de plataforma, bots de busca vs treinamento, claims e anti-spam.

## Falhas observadas na prática de mercado — riscos a evitar

- “SEO = 500 posts” sem demanda, originalidade ou ativação;
- “GEO = llms.txt e schema novo” sem suporte oficial;
- “marca citada = marca recomendada = venda”;
- “E-E-A-T score 100” ou perfil de autor inventado;
- SEO técnico sem verificar HTML, canonicals, WAF ou JS;
- comprar links e avaliações, fingir ser consumidor em comunidade;
- usar dados de CTR de publishers para prever conversões de SaaS;
- confundir uma resposta de IA com amostra representativa;
- negligenciar experiência do cliente em nome de visitas;
- publicar caso, número, depoimento, áudio ou imagem sem direitos ou verificação;
- apresentar hipótese como resultado já medido.

## Questões que pesquisa adicional deverá responder por projeto

Qual parcela real do tráfego vem de mecanismos/IA? Qual é o modelo de receita e margem? Qual ICP tem maior benefício? Quais prompts são representativos? Qual página possui evidência original? Que terceiros são fontes citadas no nicho? Existe primeiro uso que impressiona? Há bloqueio de crawler? Como distinguir causalidade de correlação? Que canais geram retorno no horizonte financeiro da empresa?

Essas respostas não estão no relatório universal. Exigem dados do negócio; nenhuma skill sabe tudo sem consulta.

## Leitura e manutenção

**Primárias e atualizáveis:** Google Search Central (docs e updates), Bing Webmaster, OpenAI bots/ChatGPT Search, Anthropic crawlers, Google Business Profile, Web Vitals. **Acadêmica:** GEO KDD 2024, pesquisas de 2026 marcadas preprint. **Observacional:** Pew, Ahrefs, Seer, Semrush, McKinsey, Reuters Institute e NN/g. Sempre ler metodologia antes de citar número.

Rever este dossiê quando houver mudança de plataforma, produto, regras de crawling, padrões de métricas ou evidência conflitante. Nenhum novo artigo deve virar regra mandatória sem revisão de qualidade, custo, benefício e risco. Referências operacionais: 46 SEO técnico; 47 IA/Search; 48 demanda/conteúdo; 49 copy/CRO; 50 medição; 51 tipos de negócio; 52 execução.
