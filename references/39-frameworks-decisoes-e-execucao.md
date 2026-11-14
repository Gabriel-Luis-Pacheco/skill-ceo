# 39 — Biblioteca de frameworks: escolher ferramenta, não colecionar slogans

> Um framework é útil se altera uma decisão, um experimento ou a qualidade de sua verificação. Nunca misturar metodologias incompatíveis sem explicitar trade-offs. Não utilizar uma taxonomia como substituto de fatos de clientes.

## Matriz com 35+ métodos

| Método | Quando favorece | Como aplicar em três movimentos | Não usar como |
|---|---|---|---|
| Good Strategy/Bad Strategy | problema central mal definido | diagnóstico → política orientadora → ações coerentes | lista de metas |
| The Crux | escolher obstáculo superável decisivo | identificar impasse → testar natureza → concentração | análise infinita |
| Porter Five Forces | atratividade da estrutura setorial | rivalidade/substitutos/entrantes/clientes/fornecedores → economics → posição | previsão fechada |
| 7 Powers | vantagem durável | mapear poder → testar barreiras → decidir investimento | checklist retrospectivo |
| Playing to Win | escolha de arena | aspiração → where to play/how to win → capabilities/management systems | slogan |
| Blue Ocean/ERRC | reposicionar valor/oferta | eliminar/reduzir/elevar/criar → protótipo → teste | negar concorrência |
| Wardley Mapping | evolução de componentes e ecossistema | usuário/necessidade → mapa de maturidade → movimento | verdade geográfica |
| Cynefin | escolher regime de ação | classificar claro/complicado/complexo/caótico → método apropriado → revisar | rótulo fixo |
| OODA | competição com informação incompleta | observar → orientar → decidir → agir → aprender | velocidade cega |
| Scenario Planning | variáveis macro incertas | forças e incertezas → cenários plausíveis → ações robustas | forecast pontual |
| Premortem | decisões grandes e difíceis | imaginar falha → listar mecanismos → prevenir/testar | pessimismo performático |
| Red Team / dissent | tese excessivamente consensual | nomear adversário → buscar refutação → ajustar | debate sem decisão |
| KPI tree | decompor objetivo | resultado → drivers → fonte/owner | estratégia |
| OKR | mudança relevante | objetivo → key results reais → reviews | backlog de tarefas |
| Balanced Scorecard | visão empresarial integrada | cliente/finanças/processo/aprendizado → hipóteses → indicadores | 100 métricas |
| Hoshin Kanri | desdobramento estratégico | objetivos anuais → catchball → revisão PDCA | cascata autoritária |
| OGSM | clareza executiva | objective → goals → strategies → measures | estratégia sem opções |
| 4DX | foco na execução | wildly important goal → lead measures → placar/cadência | metas de vaidade |
| Lean Startup | incerteza de produto/mercado | hipótese → experimento/MVP → aprendizado | lançar qualquer coisa |
| Customer Development | descobrir comprador | entrevistas → teste de solução → repetibilidade | pitching disfarçado |
| JTBD | compreender motivação real | contexto → progresso → alternativa/força de mudança | persona cosmética |
| Design Thinking | problema humano desconhecido | empatia → definição → ideação/protótipo/teste | substituir business model |
| A/B Testing | hipótese causal em escala | randomizar → medir outcome → avaliar amostra/guardrails | testar com n minúsculo |
| Scrum | trabalho complexo iterativo | objetivo de produto → sprint e incremento → inspeção | gestão total da empresa |
| Kanban | fluxo e filas | visualizar trabalho → limitar WIP → medir ciclo e ajustar | mural de cartões |
| Lean/TPS | desperdício, fluxo e qualidade | valor → mapear fluxo/gemba → resolver causa/PDCA | corte de pessoas |
| Six Sigma/DMAIC | defeitos/variação | define → measure → analyze → improve → control | discovery exploratório |
| Theory of Constraints | gargalo dominante | identificar → explorar → subordinar/elevar → repetir | otimização de cada silo |
| EOS/Traction | PME precisa de disciplina | visão → pessoas/processo/tração → reunião de exceções | copiar estrutura rígida |
| Scaling Up | scale-up com coordenação | people/strategy/execution/cash → cadência → revisão | contratar chefes cedo |
| Zero-Based Budgeting | custos legados sem prova | identificar função → justificar base → priorizar retorno | cortar tudo uniformemente |
| RACI | clareza de execução | mapear atividade → R/A/C/I → confirmar | matriz de poder simbólica |
| DACI | decisão cross-functional | driver/approver/contributors/informed → prazo → registro | múltiplos A |
| RAPID | decisão empresarial complexa | recommend/agree/perform/input/decide → escalada → revisão | formalismo para microdecisão |
| NPS/CSAT/CES | sinais de relação e esforço | medir com amostra → segmentar → investigar causas | prova isolada de PMF |
| North Star Metric | alinhar valor de produto | ação de valor → driver tree → guardrails e cohorts | métrica vistosa |
| 13-week cash flow | estresse de liquidez | entradas/saídas semanais → cenários → variance actions | DRE projetada |
| NIST AI RMF | IA com risco real | govern/map/measure/manage → avaliação e controle | checklist sem dono |

Frameworks conflitantes: OKRs podem ser adequados para direção e Kanban para fluxo simultaneamente; mas não aplicar Scrum a equipes comerciais por hábito. Theory of Constraints aponta restrição principal; Balanced Scorecard evita sacrificar cliente e pessoas no curto prazo. Reconhecer diferenças em vez de vender método único.

## Protocolo para selecionar método com economia de contexto

**1. Nomeie problema.** Ex.: NRR caiu; qual cliente, período e definição?
**2. Escolha só uma lente principal.** Cohort + JTBD para retenção, DMAIC para processo estável, premortem para risco, 13-week cash para liquidez.
**3. Defina contraprova.** Qual observação faria abandonar a hipótese?
**4. Execute menor intervenção autorizada.** Não criar programa gigante sem baseline.
**5. Verifique.** Fonte, antes/depois, comparação, custo, efeito colateral, decisão seguinte.

## Microcasos

**Produto com baixa retenção:** A média esconde cohort; separar origem e ativação, observar usuário real, aplicar JTBD para entender uso, testar onboarding com guardrails. Não publicar "PMF alcançado" porque CTR subiu.

**Indústria com atrasos:** Desenhar fluxo e WIP, achar gargalo TOC, aplicar TPS/PDCA, medir throughput e OTIF. Não otimizar estação que não determina vazão.

**Diretoria travada:** DACI escolhe decisor, RACI organiza execução, pre-mortem explicita riscos; material prévio e deadline. Não adicionar ritual semanal sem necessidade.

**Lançamento de IA:** NIST AI RMF e experimento com baseline, evals, privacidade, limite de custo, fallback, análise de incidentes. Não trocar validação por demonstração espetacular.

**Fontes metodológicas:** https://rework.withgoogle.com/intl/en/guides/set-goals-with-okrs/ ; https://scrumguides.org/scrum-guide.html ; https://www.lean.org/lexicon-terms/toyota-production-system/ ; https://balancedscorecard.org/bsc-basics-overview/ ; https://www.nist.gov/itl/ai-risk-management-framework/ai-risk-management-framework-resources
