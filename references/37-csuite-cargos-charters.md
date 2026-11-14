# 37 — C-suite: contratos reais de decisão, interface e desempenho

**Uso:** escolher competências, desenhar funções e responsabilizar especialistas. C-level é conjunto de responsabilidades, não obrigação de contratar pessoas. Em startup pequena, uma pessoa assume várias funções; a responsabilidade e o limite devem continuar explícitos. Não confundir CPO Product com CPO People; CCO pode significar Commercial, Compliance ou Communications; CSO pode ser Strategy, Sales ou Security; CDO pode ser Data ou Digital.

## Contrato mínimo de C-level

Cada função deve declarar: **mandato (resultado) → decisões que pode tomar → decisões reservadas ao CEO/board → entradas e dependências → entregáveis verificáveis → indicadores de antecedência/resultado → riscos → plano 30/60/90 → frequência de prestação de contas**. Quem possui decisão não pode escondê-la em consenso infinito.

| Papel | Responsabilidade e alçada típica | Entregas e KPIs (adaptar) | Falha a prevenir |
|---|---|---|---|
| CEO | tese de valor, estratégia, organização e capital; board controla matérias reservadas | strategy memo, decision log, scorecard; caixa, crescimento saudável, cliente, futuro | não escolher, centralizar tudo |
| COO | execução interfuncional, capacidade, qualidade, processos | plano operacional, owners e SOP; throughput, cycle time, OTIF, retrabalho | ritual sem melhorar fluxo |
| CFO | liquidez, verdade econômica, controles, captação, impostos, risco | demonstrativos, 13-week cash, 3-statement forecast; FCF, margem, precisão e runway | medir resultado contábil como caixa |
| CTO | capacidade técnica do produto, arquitetura, segurança com CISO, engenharia | architecture decision records, roadmap de dívida; confiabilidade, lead time, incidentes, custo de servir | perseguir tecnologia sem cliente |
| CIO | sistemas internos, enterprise architecture, dados corporativos/IT | carteira de sistemas, ITSM, governança de fornecedores; custo, disponibilidade, adoção | shadow IT, depender de legado |
| CPO Product | estratégia, discovery, outcomes, priorização de produto | product strategy, roadmap de hipóteses; activation, retention, time-to-value | medir features entregues como valor |
| CMO | demanda, marca, posicionamento, pesquisa, distribuição | posicionamento e plano de canais; pipeline qualificado, aquisição, confiança | otimizar likes/MQL sem clientes |
| CRO Revenue | sistema de receitas: vendas, expansão, às vezes CS | forecast comercial e ICP coverage; ARR reconhecido corretamente, win rate, payback, retenção | comprar crescimento não rentável |
| CHRO / CPO People | talento, cultura, incentivos, desenvolvimento e sucessão | org/competency map, succession, hiring scorecards; quality-of-hire, attrition, coverage | cultura de slogan sem gestão |
| CSO Strategy | cenários, portfólio, competição, opções estratégicas | market map, tese de portfólio, decisões de capital; adoção e retorno das escolhas | slides sem escolhas |
| CISO | governança de risco de segurança, incidentes, controles e escalonamento independente | risk register, tabletop, incident response; exposição crítica, detecção/recuperação | mascarar risco ou paralisar negócio |
| CDO/CDAO | estratégia de dados, definições, qualidade, governança, analytics | data contracts, catálogo, avaliação de dados; qualidade, uso, decisões habilitadas | dashboards sem verdade |
| CAIO/CDAIO | portfólio e risco de IA com CTO/CDAO/CISO | avaliação de casos, evals, fallback, ROI; qualidade real, custo, falhas | piloto eterno e automação insegura |
| CLO / GC | contratos, societário, propriedade intelectual, litígios, obrigações legais | mapa de risco, termos, parecer e suporte ao board; exposição e remediação | veto sem alternativa viável |
| CCO Compliance | prevenção, monitoramento, denúncia, controles | plano de compliance, investigações, auditoria; remediação, recorrência | controles de fachada |
| CCO Commercial | política comercial, pricing, operações de venda | playbook de negociação e receita; margem, desconto, conversão | disputa com CRO por ownership |
| CXO Experience | jornada ponta a ponta, pesquisa, serviço, design | mapa de jornada, service blueprint; CSAT/CES, retenção | beleza sem impacto real |
| CAO Accounting/Admin | fechamento, processos administrativos e reporting | balancete, conciliações, fechamento; tempo, erros, controles | base contábil frágil |
| Chief of Staff | amplificar capacidade decisória do CEO, sem chefia informal | pauta, agenda, follow-ups, decision log; ciclo decisório e entrega | tornar-se CEO sombra |

**Não use esses KPIs indiscriminadamente.** Se não existe receita recorrente, ARR é inadequado; se não existe marketplace, GMV não faz sentido; se só há um fundador, CHRO é uma função exercida pelo fundador. Para funções jurídicas e segurança, padrões e obrigações variam por país/setor.

## Interfaces que exigem contrato

| Interface | Quem lidera pergunta / outcome | Decisão contestável | Regra de resolução |
|---|---|---|---|
| CEO × CFO | lucro sustentável, risco e caixa | quanto arriscar e onde investir | CFO expõe downside; CEO decide dentro do mandato; board aprova itens reservados |
| CFO × CRO | margem real da receita | desconto, forecast, CAC | decisões com contribuição e coortes; não premiar bookings sem caixa |
| CPO Product × CTO | valor do usuário × custo e confiabilidade técnica | o quê e quando construir | outcome de produto + veto técnico fundamentado; decisão escalada se conflito |
| CMO × CRO | procura e conversão com qualidade | MQL vs receita | compartilhar funnel e métricas de retenção |
| COO × todos | execução e recursos | alocação de capacidade | DRI, trade-off explícito e alinhamento CEO |
| CISO × CTO/CIO | velocidade com risco aceitável | release vs vulnerabilidade | limites de risco, exceção formal, escalonamento |
| CHRO × CEO/board | saúde da liderança | sucessão, comportamento tóxico | proteger canal independente de reporte |
| CDAO × áreas | métricas consistentes | definição de cliente, churn, margem | data contract, owner de definição e linhagem |
| GC × Growth | vendas e claims legítimos | privacidade, IP, contrato | counsel aponta risco e alternativa, sem legalizar ilegalidade |

## RACI e DACI sem burocracia

RACI organiza execução: R executa, A responde pelo resultado, C é consultado, I informado. DACI organiza decisão: D conduz, A aprova, C contribui, I é informado. Em regra, manter **um responsável final claro** por decisão. Se accountability do CEO conflita com competência legal de conselho/diretor estatutário, obedecer lei e governança, não o quadro.

Exemplo: **mudar o preço de uma assinatura** — CPO/CMO propõem hipóteses; CFO valida margem e risco; GC verifica obrigações; CRO/Growth avaliam aquisição; CEO ou responsável autorizado aprova; engenharia executa; analytics mede; ninguém publica sem autorização necessária em POLICY.md.

## O que cada líder pergunta semanalmente

- CEO: qual restrição mudou? O que devo parar? Que verdade o time evita me contar?
- COO: onde o trabalho espera? Que fila e retrabalho impedem throughput?
- CFO: qual dinheiro existe, qual recebimento é incerto, qual hipótese quebra o caixa?
- CPO: qual episódio mostra que usuário recebeu valor? Quem abandonou e por quê?
- CTO: qual risco técnico tem maior impacto em cliente/economia? O que falha sob escala?
- CIO: que sistema interno cria custo e risco invisíveis? Dependências e acesso estão controlados?
- CMO: por que comprador nos escolhe agora? Qual canal traz pessoas que ficam?
- CRO: qual venda perdeu por proposta de valor vs execução? Qual cohort compra e renova?
- CHRO: que posição crítica não tem substituto? Que comportamento é recompensado de fato?
- CISO: qual evento material plausível falta detectar ou conter? Temos backup testado?
- CDAO/CAIO: qual dado é falso/incerto e qual automação cria resultado mensurável sem ampliar dano?
- GC/Compliance: que ação comercial ou técnica cria risco regulatório assimétrico?

## Método 30/60/90 para qualquer C-level

**0–30:** ouvir usuários, frontline, pares e CEO; mapear baseline, decisões pendentes, pessoas, riscos, sistemas e contexto. Emitir diagnóstico com hipóteses rivais. Em risco crítico, agir antes dos 30 dias.

**31–60:** estabelecer charter, scorecard com fonte e frequência, escolher 3–5 problemas de alto impacto (heurística, não cota de projetos), cortar trabalho redundante e definir responsabilidades cruzadas.

**61–90:** entregar melhoria observável, revisão do orçamento/roadmap, decisões de talentos, mitigação de risco, mecanismo de revisão e registro do que permaneceu incerto.

O sucesso é resultado funcional + cooperação, não teatro de títulos. CEO integra o time. Reunião interfuncional sem decisão deve virar comunicação assíncrona.

### Estágios e carreira

- Pré-PMF: especialização enxuta e hands-on; founder-CEO assume finanças, produto, growth e decisões técnicas via parceiros.
- Scale-up: gerentes funcionais, handoffs, forecast, processos e sucessão, sem importar burocracia Big Tech.
- Corporação: sistemas independentes, controles, board, portfólio, riscos multidimensionais e gestão de gestores.
- Preparação para C-level: domínio funcional, P&L e economics, influência transversal, manejo de riscos, formação de sucessores e capacidade de dizer “não” baseada em evidência.

Fontes: [Spencer Stuart — composição C-suite](https://www.spencerstuart.com/research-and-insight/sp-500-c-suite-snapshot-2025-profiles-in-functional-leadership), [Gartner — liderança de dados/IA](https://www.gartner.com/en/newsroom/press-releases/2025-05-12-gartner-survey-finds-seventy-percent-of-cdaos-are-responsible-for-artificial-intelligence-strategy-and-operating-model), [Spencer Stuart — sucessão](https://www.spencerstuart.com/research-and-insight/succession-planning-strategies-for-building-the-pipeline), [NIST — risco IA](https://www.nist.gov/itl/ai-risk-management-framework/ai-risk-management-framework-resources).