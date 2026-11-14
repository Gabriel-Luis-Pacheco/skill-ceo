# 40 — Mensuração de SEO/GEO, experimentos, atribuição e painel executivo

**Quando ler:** CEO precisa provar se a descoberta orgânica está trazendo compradores, identificar gargalos, avaliar GEO, criar dashboard ou decidir orçamento. Não confundir ser citado por IA com geração de receita.

## 1. Árvore de métricas

**Descoberta:** número de URLs realmente indexadas, cobertura de páginas críticas, impressões, posição e CTR segmentados por intenção, termos de marca vs não marca, geografia, dispositivo, tópicos, canais e comparativos.

**Visibilidade em respostas:** menções de marca por plataforma e conjunto de prompts, URLs citadas, domínios citados, citation share (quando houver definição verificável), cobertura por job, proporção de respostas com dados próprios usados, variação por modelo/idioma/região e concorrentes.

**Engajamento:** visitas orgânicas de qualidade, engaged sessions, taxa de início de jornada, retorno, uso da ferramenta/conteúdo, envio de formulário, conversas iniciadas e buscas pela marca. Bot, crawler e teste automatizado não são pessoa.

**Negócio:** leads qualificados, trials, primeira experiência significativa, segundo uso, compra confirmada, margem de contribuição, churn, LTV quando estimável, custo completo de conteúdo/PR/operação, CAC por canal com atribuição explícita, payback e pipeline influenciado.

**Marca:** branded search, pesquisas diretas, share of search em amostra de categorias, menções espontâneas, reviews, qualidade da narrativa, confiança e preferência em entrevistas.

Não usar um único “SEO score” como north star. Escolher KPI norteador conforme negócio (ex.: primeiras práticas úteis vindas de orgânico e convertidas em receita). KPIs de diagnóstico explicam o resultado, não o substituem.

## 2. Instrumentação mínima e definições

Tabela de eventos para o funil do negócio: page_view legítimo → CTA qualificado → cadastro real → primeira ação de valor → retorno útil → conversão confirmada → receita líquida/margem. Definir nomes, exclusões (ambiente dev, bots, equipe, duplicatas), janela temporal e identificadores compatíveis com privacidade/consentimento. Evitar medir usuário único por IP cru.

Implementar:
- Google Search Console: busca, páginas, índices, consultas, países e dispositivos;
- Bing Webmaster Tools: crawling e, se disponível, AI Performance, citations e grounding queries;
- Analytics e conversões: separar utm/referrer/landing, definir eventos reais;
- CRM e faturamento: reconciliação de lead/cliente/receita, sem expor PII desnecessária;
- Logs de servidor/CDN: status de crawlers e falhas de acesso;
- Dashboard: baseline com data, janela, segmento, fonte, owner e limites.

Consentimento, retenção de dados e controles de acesso seguem política da empresa e legislação aplicável.

## 3. Atribuição de visitas de IA

Parte das visitas de plataformas pode aparecer por referrer ou parâmetros de origem; outra parte pode vir como direct, sem referrer ou atravessar múltiplos dispositivos. Identificar tráfego observável não equivale a medir toda influência da IA. Registrar fontes conhecidas, mas sem inventar uma lista fechada de domínios que sempre captura tudo.

Separar:
- **Referral confirmado:** sessão atribuída a plataforma pelo dado disponível.
- **Atribuição assistida:** touchpoints observados e associados por modelo conhecido.
- **Efeito de marca hipotético:** aumento de branded search/visitas diretas concomitante, sem nexo causal provado.
- **Sem visibilidade:** não é zero; é desconhecido.

Não concluir que “ChatGPT vendeu 30 assinaturas” por correlação em gráfico de buscas.

## 4. Protocolo científico para GEO e SEO

1. Escolher uma pergunta comercial concreta e hipótese falsificável.
2. Salvar população de páginas, consultas/prompts, contas e segmentos.
3. Medir baseline antes da intervenção.
4. Definir controle ou série comparável, onde viável.
5. Alterar um mecanismo predominante (conteúdo, navegação, autoridade, copy) ou registrar mudanças simultâneas.
6. Verificar deploy e rastreamento; observar tempo de recrawl/indexação.
7. Repetir coleta no mesmo protocolo e com amostra representativa.
8. Quantificar diferença, incerteza, custo e resultados de negócio.
9. Decidir expandir, manter, reverter ou repetir.

Diferença temporal não prova causalidade. SERP e respostas de IA dependem também de concorrência, sazonalidade, produto, intenção, atualizações de modelos, localização e personalização.

## 5. Amostragem e variabilidade de respostas

Criar painel longitudinal, não prints isolados. Estratificar prompts por:
- problema, aprendizado, comparação, transação e pós-compra;
- marca própria, alternativas e pesquisa neutra;
- principal mercado/idioma/local;
- dispositivos, quando relevantes.

Amostra inicial ilustrativa: 20 perguntas reais para um diagnóstico rápido, depois ampliar conforme custo e precisão desejada. **Não é cota obrigatória nem garantia estatística.** Preferir repetição semanal ou período estável sem alegar que o fornecedor retorna determinismo. Guardar prompts, versões quando visíveis, links, capturas e resultados brutos. Separar teste exploratório de comparação robusta.

Exemplo de registro:
| Data | Plataforma | Prompt/cluster | Marca mencionada? | Domínio citado? | Evidência usada? | Nota de incerteza |
|---|---|---|---|---|---|---|
| AAAA-MM-DD | sistema | intenção | sim/não | URL/nenhuma | trecho validado/indeterminado | modo/região |

Um painel comercial pode medir menção/citação; não significa que toda plataforma ofereça API ou métricas oficiais.

## 6. Painel executivo e alertas

Visão semanal:
- O que mudou no **resultado humano/econômico**?
- Qual canal trouxe pessoas certas?
- Qual cluster converteu?
- Onde o funil vazou?
- Houve variação técnica de indexação/servidor?
- A marca apareceu em prompts de compra?
- Quais ações foram realmente executadas, custos e trade-offs?
- Qual hipótese mudou? Próximo experimento e dono?

Alertas que importam: página de dinheiro desindexada, checkout quebrado, queda anormal de tráfego qualificado, perda de reputação, violação de fonte, mudança de preço/inventário ou queda de ativação. Emitir alerta só com sensor instalado, limiar definido e alçada documentada. Não se apresentar como monitor 24/7 por ter escrito um checklist.

## 7. Quadro de decisão

Prioridade exploratória = impacto esperado × confiança ÷ esforço. É uma heurística de ordenação, **não ROI calculado**. Também considerar risco, dependência, velocidade de aprendizado e oportunidade de mercado. Exemplo hipotético:
- corrigir noindex acidental em página comercial: alto impacto provável, baixo esforço;
- melhorar oferta e CTA de página com muito tráfego qualificado: alto potencial, requer teste;
- criar benchmark único: potencial de links/PR, esforço maior;
- publicar 500 posts repetitivos de IA: risco alto, valor marginal baixo.

**Critério de aceite:** baseline auditável, definições estáveis, série antes/depois, custos considerados e decisão explícita baseada em métrica comercial. Sem acesso aos dados, marcar SEM ACESSO.

## Fontes para instrumentos e evidência

- Google Search Console: https://support.google.com/webmasters/
- Bing AI Performance: https://blogs.bing.com/webmaster/2026/2/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview/
- Bing Citation Share (2026): https://blogs.bing.com/search/2026/6/New-AI-Visibility-Insights-in-Bing-Webmaster-Tools-Intents-Topics-Citation-Share-Compare/
- Pew — clique com AI Overview: https://www.pewresearch.org/short-reads/2025/07/21/google-users-are-less-likely-to-click-on-links-when-an-ai-summary-appears-in-the-results/
- Ahrefs (amostra/correlação de CTR): https://ahrefs.com/blog/ai-overviews-reduce-clicks-update/
- Seer (estudo de CTR e variação): https://www.seerinteractive.com/insights/aio-impact-on-google-ctr-2026-update

Nenhuma estimativa desses estudos representa toda a internet ou prova causalidade isolada.
