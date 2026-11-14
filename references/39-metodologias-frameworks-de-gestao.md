# 39 — Frameworks executivos: quando aplicar, quando rejeitar e como provar valor

**Uso:** escolher UM instrumento para o gargalo observado; não aplicar a biblioteca toda. Métodos são modelos incompletos: a finalidade é uma decisão melhor, um experimento mais barato ou uma execução mais confiável. Fontes primárias ao final.

| Método | Problema certo / passos essenciais | Quando NÃO usar ou risco dominante |
|---|---|---|
| OKR | poucos outcomes e resultados mensuráveis: objetivo → KR → revisão | backlog, projeto pré-PMF sem baseline confiável |
| KPI tree | decompor variável-alvo em drivers, owners e denominadores | confundir causalidade com correlação |
| Balanced Scorecard | ligar estratégia a finanças, cliente, processos, capacidades | inventário de 100 KPIs sem escolhas |
| Hoshin Kanri | desdobrar prioridades estratégicas com diálogo catchball | ritual anual congelado sem aprendizado |
| OGSM | objetivo, metas, estratégias e medidas numa página | substituto de diagnóstico e trade-offs |
| Lean Startup | hipóteses → MVP/experimento → comportamento → aprendizagem | usar “MVP” para justificar qualidade ruim |
| Customer Development | entrevistas e validação sequencial de problema/mercado | tratar respostas educadas como compromissos |
| JTBD | situação → progresso → alternativas → barreira; redesenhar oferta | personificação sem episódio real |
| Design Thinking | observar humano → definir problema → idear → prototipar → testar | ignorar custos, distribuição e regulação |
| Scrum | meta de produto/sprint, time pequeno, inspeção/adaptação | aplicar mecanicamente à diretoria |
| Kanban | visualizar fluxo, limitar WIP, medir lead/cycle time | quadro de tarefas sem política nem entrega |
| Agile | feedback e adaptação em trabalho complexo | ausência de estratégia, de arquitetura e qualidade |
| EOS/Traction | scorecard, reuniões, responsabilidades e prioridades | burocracia para founder sem clientes |
| Scaling Up | people, strategy, execution, cash em fase de escala | escalar antes de PMF |
| 4DX | poucos objetivos e leading measures com scoreboard | atribuir causalidade falsa ao lead measure |
| Theory of Constraints | identificar gargalo → explorar → subordinar → elevar → repetir | otimização local do que não limita sistema |
| Lean/TPS | fluxo, padronização, gemba, reduzir desperdício e melhorar qualidade | corte indiscriminado de pessoas |
| Six Sigma/DMAIC | definir, medir, analisar, melhorar e controlar variação | experimentação exploratória rápida |
| OODA | observar, orientar, decidir, agir e revisar em competição veloz | agir sem observação |
| Cynefin | classificar domínio claro/complicado/complexo/caótico e decidir modo | enquadrar toda incerteza como simples |
| Wardley Mapping | mapear cadeia de valor e evolução de componentes | pretender precisão preditiva |
| Porter 5 Forces | rivalidade, entrantes, substitutos, clientes, fornecedores | ignorar velocidade e ecossistemas |
| 7 Powers | avaliar retornos duráveis: escala, rede, counter-positioning, switching, branding, cornered resource, process power | vantagem imaginada pré-PMF |
| Blue Ocean | redesenhar proposta via eliminar/reduzir/elevar/criar | declarar competição irrelevante |
| SWOT | sintetizar forças e riscos após pesquisa | lista subjetiva sem escolhas |
| RACI | clareza de responsabilidade de execução | decisão estratégica que exige DACI |
| DACI | Driver, Approver, Contributors, Informed | criar falso consenso ou vários aprovadores |
| RAPID | decisões difíceis cross-functional com autoridade explícita | reuniões para decisões triviais |
| North Star Metric | comportamento único de valor com guardrails | vanity metric isolada |
| NPS/CSAT/CES | percepção de recomendação/satisfação/esforço em contexto | prova isolada de PMF, retenção ou receita |
| Premortem | imaginar fracasso, listar razões e mitigá-las antes da aposta | paralisar iniciativa pequena reversível |
| Scenario Planning | sinais e planos contingentes em alta incerteza | única previsão disfarçada de cenário |
| Zero-Based Budgeting | revalidar grandes rubricas e custos por driver | corte geral que destrói capacidade |
| 13-week cash forecast | caixa semanal direto, variância e ações | substituir DRE/fluxo de longo prazo |
| A/B test | comparar alternativas com exposição e medida adequada | amostra minúscula, testes contínuos opcionais não planejados |
| Growth loops | modelar mecanismo que gera uso/recomendação sustentável | crescimento fabricado por incentivo sem retenção |

## Escolha condicional, não culto ao método

- **Zero clientes externos:** The Mom Test/JTBD, observação de primeiro uso, Founder-led sales; não priorizar Balanced Scorecard ou centenas de OKRs.
- **Tráfego sem ativação:** UX research + funil instrumentado + inspeção técnica; não comprar tráfego primeiro.
- **Uso sem retorno:** coortes, entrevistas de abandono, análise de hábito/valor; não mais features indiscriminadas.
- **Receita sem margem:** unit economics, preço e contribuição por cohort; não celebrar faturamento.
- **Crescimento com caos:** Theory of Constraints, Kanban, gestão de capacidade e clareza RACI/DACI.
- **Sistema estável com defeitos recorrentes:** Lean/TPS ou DMAIC, conforme natureza do trabalho.
- **Mercado em ruptura:** OODA, cenários, Wardley, 7 Powers e opção de realocação.
- **Sem liquidez:** 13-week cash, reconciliação bancária e opções de continuidade; não planejar growth sem caixa.
- **Big Tech:** portfólio, ROIC, governo de plataformas, security/compliance, inovação e efeitos de segunda ordem.

## Exemplos de aplicação

**Exemplo 1 — SaaS pequeno com pouca prática de voz:** evento "sessão iniciada" duplicado? Primeiro KPI tree e definição de usuário/coorte. Hipótese: produto não funciona no celular; rival: público não entende promessa. Teste: seis observações de jornada real de público consentido com instrumento confiável. Mudança: reparar áudio ou mensagem conforme o que os dados mostrarem. Evitar OKR ornamental.

**Exemplo 2 — Indústria:** entregas atrasam. Mapear fluxo end-to-end; medir fila e OEE; testar se fornecedor, setup ou lote é gargalo. Elevar apenas restrição atual; acompanhar throughput, scrap e prazo. Evitar aumentar máquinas fora do gargalo.

**Exemplo 3 — Big Tech:** nova IA afeta produto existente. Combinar cenários (regulação/custo/capacidade), 7 Powers (moat real), capital allocation e NIST AI RMF. Não lançar sem evals, supervisão, rollback e análise de impacto.

## Formato de decisão para frameworks

Problema observado | hipótese causal | ferramenta escolhida | por que ela e não outra | premissas | decisão que produzirá | experimento/ação | guardrail | limite de confiança | critério de abandonar. Para trabalho pequeno, esse raciocínio pode ficar interno.

Fontes: [Google re:Work OKRs](https://rework.withgoogle.com/intl/en/guides/set-goals-with-okrs/), [Scrum Guide](https://scrumguides.org/scrum-guide.html), [Lean Enterprise Institute](https://www.lean.org/lexicon-terms/toyota-production-system/), [Balanced Scorecard Institute](https://balancedscorecard.org/strategy-execution-and-the-balanced-scorecard/), [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework/ai-risk-management-framework-resources).