# 37 — C-suite: mandatos, scorecards, interfaces e planos de entrada

> Usar para assumir papel funcional, auditar C-level, decidir organograma, alinhar lideranças e resolver conflito entre áreas. **Cargo é uma função, não uma obrigação de contratar pessoas ou criar agentes.** Em startup, uma pessoa pode cobrir funções; responsabilidades permanecem nomeadas.

## Contrato universal para qualquer C-level

**Mandato** (resultado econômico/humano), **decisões exclusivas** (autoridade), **interfaces** (quem consulta), **leading indicators** (sinais), **lagging KPIs** (resultado), **artefatos** (prova), **riscos** (escalada), **cadência** (revisão), **plano 30/60/90**. Não chamar especialista de CEO informal; não dar autoridade por título de agente. Todos precisam mapear dados de clientes, economia e risco.

| Papel | Resultado e decisões centrais | Métricas + artefato | Falha típica |
|---|---|---|---|
| **CEO** | estratégia, capital, time e riscos; resolver conflitos entre funções | valor/FCF/retention; tese, board pack | metas sem escolhas |
| **COO** | throughput, qualidade, capacidade e execução | cycle time, OTIF, produtividade, variação; operating plan/SOP | gerenciar status e não gargalos |
| **CFO** | caixa, forecast, financiamento, alocação e controles | cash, FCF, ROIC, forecast error, burn; 3 statements/13-week cash | confundir lucro com liquidez |
| **CTO** | arquitetura e tecnologia do produto | uptime, defeitos, lead time, custo de servir; ADR/roadmap | engenharia sem cliente/segurança |
| **CIO** | sistemas, produtividade e dados corporativos internos | adoção, disponibilidade, custo IT, cyber posture; IT portfolio | infraestrutura sem valor |
| **CPO (produto)** | proposta de valor, discovery e outcomes | activation, retention, time-to-value; estratégia de produto | roadmap como lista de features |
| **CMO** | posicionamento, marca, geração/captura de demanda | demanda qualificada, eficiência, qualidade de pipeline; GTM plan | maximizar leads ruins |
| **CRO (revenue)** | vendas, expansão e receita repetível | win rate, ciclo, bookings, NRR, payback; forecast de vendas | vender contratos inviáveis |
| **CHRO/CPO (people)** | talento, desempenho, cultura e sucessão | quality of hire, regrettable attrition, bench; workforce plan | RH separado da estratégia |
| **CSO (strategy)** | inteligência de mercado, opções e portfólio | escolhas adotadas, retorno de iniciativas; strategy memo | slides que ninguém decide |
| **CISO** | risco cibernético, resiliência e resposta | exposição crítica, MTTD/MTTR, cobertura; risk register | risco escondido ou burocracia |
| **CDO/CDAO** | governança/qualidade/valor de dados e analytics | qualidade, disponibilidade, uso e ROI; data portfolio | data lake sem decisão |
| **CLO/GC (legal)** | aconselhamento jurídico e governança institucional | material legal risk e remediações; legal risk map | veto sem opções legais |
| **CCO (compliance)** | integridade, controles, investigações | incidências, time-to-remediate, cobertura; compliance plan | programa de fachada |
| **CCO (commercial)** | excelência de preços/canais e acordos | margem, desconto, pipeline; commercial plan | sobreposição com CRO |
| **CXO (experience)** | jornada end-to-end, fricção e confiança | CSAT/CES, abandono, retenção; journey map | UX sem resultados |
| **CAO (admin/accounting)** | contabilidade, controles e administração | close time, exceções e auditoria; close pack | relatórios sem precisão |
| **Chief of Staff** | fluxo de decisões do CEO e coordenação | atrasos de decisões, owners claros; decision log | virar autoridade paralela |
| **CAIO/CDAIO** | portfólio de IA, governança, avaliação e retorno | ROI real, adoção, falhas e incidentes; evals/model cards | pilotos infinitos |

Títulos colidem. **CPO** = produto ou people, **CCO** = compliance/commercial, **CDO** = data ou digital, **CSO** = strategy/security/sales. Sempre desambiguar por mandato, não sigla.

## Pergunta difícil, leading signal, ação típica

- CFO: "Qual linha do downside quebra primeiro?" → recebíveis atrasados → ajustar 13-week cash e opções de liquidez.
- COO: "Qual é o gargalo do fluxo inteiro?" → WIP crescente → reduzir filas antes de aumentar headcount.
- CTO: "Qual risco técnico pode destruir valor?" → incidentes repetidos → melhorar arquitetura, testes e fallback.
- CIO: "Que ferramenta corporativa não é adotada?" → baixo uso + custo → consolidar ou corrigir workflow.
- CPO: "Que uso prova valor real?" → retenção do cohort de usuários ativados → ajustar onboarding/discovery.
- CMO: "Qual situação torna a oferta relevante hoje?" → mensagens com baixo fit → testar positioning com pessoa real.
- CRO: "Por que o segmento paga e renova?" → queda de win rate → comparar perdas por preço, concorrente, produto.
- CHRO: "Qual posição-chave põe o plano em risco?" → fuga de talentos → agir em gestão, sucessão e incentivos.
- CISO: "Qual evento material é plausível?" → exposição crítica aberta → contenção e elevação conforme política.
- CDAO: "Qual decisão melhorou por causa do dado?" → baixa confiança em instrumentação → reparar lineage.
- CLO: "Que contrato muda irreversivelmente o risco?" → cláusula concentrada → revisão jurídica local.
- Chief of Staff: "Qual decisão está sem dono?" → backlog decisório → DACI, remover reuniões inúteis.
- CAIO: "Que uso de IA supera baseline com segurança?" → baixa qualidade em evals → segurar rollout e testar.

## Interfaces com accountability

| Conflito | Decisão de referência | Regra de cooperação |
|---|---|---|
| CPO × CTO | outcome de produto vs viabilidade técnica | CPO define problema/resultado; CTO arquitetura/limites; CEO resolve trade-off econômico |
| CMO × CRO | demanda vs conversão e expansão | métrica compartilhada de cliente qualificado e margem, não MQL isolado |
| CFO × CRO | crescimento vs risco de crédito/desconto | economics e política aprovadas antes de comprometer preço |
| CIO × CTO | IT corporativo vs produto | explicitar sistemas sob responsabilidade de cada um |
| CISO × CTO/CIO | velocidade vs risco | CISO tem canal independente de escalada; risco aceito por autoridade definida |
| CHRO × líderes | headcount vs capacidade | budget, outcomes de função e sucessão justificados |
| CEO × Board | administração vs fiscalização | reportar com transparência; board supervisiona, não vira operador da rotina |
| CDAO × todos | qualidade de dados compartilhada | donos de fonte + definições + SLAs, não somente "time de BI" |

**RACI** para execução: Responsible produz, Accountable responde pelo resultado, Consulted contribui, Informed é comunicado. **DACI** para decisão: Driver conduz, Approver decide, Contributors apresentam perspectivas, Informed é avisado. **RAPID**: Recommend, Agree, Perform, Input, Decide. Não criar múltiplos decisores finais sem regra de desempate.

## 30 / 60 / 90 por função (não é calendário obrigatório)

**D0–30 — descobrir a verdade:** entrevistar stakeholders, baseline e data lineage, riscos, compromissos anteriores, talento, 3 problemas. Cada cargo produz um factbook funcional: CFO reconcilia caixa/contas; COO mapeia fluxos; CPO valida cohorts; CMO/CRO investiga a jornada até receita; CTO/CISO mapeia reliability/riscos; CHRO mapeia posições críticas.

**D31–60 — escolher e estabilizar:** provar causas, corrigir P0, definir decisão/owner, arquitetura de indicadores, políticas e prioridades; fechar lacunas legais sem decisões não autorizadas.

**D61–90 — demonstrar melhoria:** entregar 1–3 outcomes concretos com comparação antes/depois e qualidade das evidências; retirar aposta que não funciona, atualizar portfólio e desenhar próxima janela de 90 dias. Nem todo CFO/CTO precisa de 90 dias para corrigir risco grave.

## Proposta de scorecard e rotina por estágio

**Micro-startup:** poucos donos, revisão semanal curta com fatos de cliente/caixa/produto; funções combinadas. **Scale-up:** scorecard por função, orçamento, leaders, forecast, revisão mensal. **Big Tech:** portfólio, métricas comparáveis por unidade, governança de riscos, comitês enxutos e board. O mesmo dashboard não serve a uma startup sem clientes e a uma companhia pública.

**Contrato de reunião:** decisão requerida, material prévio, owner, duração proporcional, divergência registrada, decisão e data de revisão. Reunião sem decisão ou aprendizado necessário pode virar atualização assíncrona.

**Fontes:** https://www.spencerstuart.com/research-and-insight/sp-500-c-suite-snapshot-2025-profiles-in-functional-leadership ; https://www.gartner.com/en/newsroom/press-releases/2025-05-12-gartner-survey-finds-seventy-percent-of-cdaos-are-responsible-for-artificial-intelligence-strategy-and-operating-model ; https://store.hbr.org/product/people-before-strategy-a-new-role-for-the-chro/R1507D ; https://www.spencerstuart.com/research-and-insight/succession-planning-strategies-for-building-the-pipeline
