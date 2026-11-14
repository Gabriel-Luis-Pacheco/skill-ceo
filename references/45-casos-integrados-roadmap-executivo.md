# 45 — Casos integrados, contrafactuais e currículo de 12 meses

**Uso:** transformar os módulos 36–44 em ação por setor, estágio e restrição. Todos os valores abaixo são **cenários hipotéticos de treinamento**, não dados do BataTalk. Em qualquer caso, o CEO não aceita um número sem fonte, denominador, janela e possível viés.

## Caso 1 — SaaS de voz pré-PMF (analogia aplicável ao BataTalk)

**Fato dado (hipotético):** 1.000 visitas, 100 cadastros, 40 testes de microfone, 15 conversas úteis, 2 retornos e 0 pagamentos. Primeiro: verificar pessoas únicas, tráfego real, teste interno, instrumentação e a definição operacional de “conversa útil”. **Não** concluir que a LP é a causa só porque cadastro é 10%.

Hipóteses rivais: (A) público errado/pouca intenção; (B) mic/latência quebram primeira experiência; (C) aluno usa mas não percebe progresso; (D) proposta paga não distingue valor. Priorizar inspeção de experiência por usuário consentido e dados por coorte. Se só 15 falam, não comprar mídia nem criar 14 agentes de marketing. Corrigir primeiro o elo mais claramente quebrado. **Decisão de CEO:** qual experimento muda a hipótese e qual resultado humano prova melhoria? Área líder CPO/CTO; CEO em pré-PMF pode executar pessoalmente. Fonte de método: [YC](https://www.ycombinator.com/library/4D-yc-s-essential-startup-advice).

**Contrafactual:** se 100 de 100 completassem uma fala mas ninguém pagasse, a ordem seria diferente: investigar retorno, disposição a pagar, preço e diferenciação, não aumentar confiabilidade do mic que já funciona.

## Caso 2 — SaaS B2B pós-PMF com churn

Cenário: MRR inicial elegível R$ 500 mil. Na coorte houve churn de R$ 35 mil, contraction R$ 15 mil, expansion R$ 20 mil. **GRR = (500−35−15)/500 = 90%**; **NRR = (500−35−15+20)/500 = 94%**. Não somar novos clientes à coorte. CRO/CS mapeiam cancelamentos por segmento; CPO verifica time-to-value; CFO calcula margem, CEO decide se o custo de aquisição precisa cair enquanto retenção é reparada. Contrafactual: se problema se concentra em segmento adquirido por canal novo, ICP/GTM têm precedência; se em toda a base após release, produto/operação têm precedência.

## Caso 3 — Marketplace de dois lados

Cenário: 10 mil compradores, 500 fornecedores, GMV R$ 2 milhões/mês, take rate nominal 12%. **Receita bruta de plataforma hipotética de R$ 240 mil** antes de estornos e regras contábeis. Não confundir GMV com receita. Problema: matches pioram. COO/Produto verificam tempo até match, concentração por praça, taxa de cancelamento, qualidade de oferta; CMO não deve simplesmente aumentar o lado já abundante. CEO decide onde subsidia crescimento, se existe efeito de rede defensável e qual lado está escasso. Contrafactual: em demanda muito sazonal, a restrição pode ser calendário/coordenação, não aquisição.

## Caso 4 — Indústria sob restrição de capacidade

Demanda 1.000 unidades, linha A 1.200, linha B 700, linha C 1.100 por semana. Sem estoques intermediários: throughput potencial é limitado a **700**. Investir em linha A não resolve; engenharia/COO estudam perdas e melhorias na B; CFO valida custo/retorno; CEO protege segurança e qualidade. Contrafactual: se demanda efetiva é 600, a restrição está em vendas, não capacidade. Theory of Constraints não substitui investigação.

## Caso 5 — Big Tech e investimento em IA

Um portfólio tem core lucrativo, produtos adjacentes, pesquisa e apostas arriscadas. CAIO/CDAO estudam evals e qualidade, CTO COGS/infra, CISO riscos de segurança/privacidade, GC regulações, CPO outcomes, CFO retorno e CEO decide realocação. Desconsiderar condições macro (juros, energia, chips, antitruste, geopolítica) gera falsa segurança. Contrafactual: se modelo mais caro não aumenta retenção/qualidade, tecnologia melhor em benchmark não significa produto economicamente melhor.

## Caso 6 — Turnaround em tempo crítico

Cenário: R$ 300 mil em caixa livre, saídas inevitáveis de R$ 150 mil/mês, entradas incertas de R$ 40 mil/mês. Runway simplificada ≈ 300/(150−40) = **2,73 meses**, mas **não é previsão de solvência**: vencimentos concentrados podem causar falta de caixa antes. Montar fluxo direto 13 semanas, reconciliar bancos, falar com credores segundo alçada e aconselhamento, preservar clientes/capacidade. Não criar plano de marketing ambicioso sem analisar o relógio. Ver [40](40-turnaround-risco-e-crises.md).

## Roadmap de estudo deliberado — 12 meses

| Mês | Campo | Exercício observável |
|---|---|---|
| 1 | contabilidade, P&L, balanço, caixa | reconstruir 3 demonstrativos e verificar conciliações |
| 2 | estratégia e vantagem | escrever 3 opções mutuamente excludentes, decidir e justificar |
| 3 | discovery, JTBD, produto | 20–30 entrevistas autorizadas ou amostra pertinente; analisar coortes |
| 4 | GTM, branding, pricing, vendas | funil por ICP, objeções e teste de oferta |
| 5 | operações e qualidade | mapear gargalo, filas e custo de retrabalho |
| 6 | pessoas e cultura | charters, scorecards e sucessão de funções críticas |
| 7 | sistemas e arquitetura | revisar segurança/confiabilidade e custo de tecnologia |
| 8 | dados e IA | rodar caso com evals, guardrails, ROI e fallback |
| 9 | governança, direito e risco | simulação de board e incidente, legislação local |
| 10 | capital allocation, M&A | comparar 5 investimentos com cenários |
| 11 | turnaround | tabletop de crise de caixa + cyber + reputação |
| 12 | integração | manual pessoal CEO + simulação de tomada de decisão |

**Critério:** meses são trilha de aprendizado, não promessas de ler 20 livros completos em 30 dias. A prática real é mais importante que acumular resumos.

## Rubrica de qualidade do CEO

Avaliar por caso: (a) encontrou dados e distinguiu alegação; (b) diagnóstico e explicação rival; (c) estratégia e trade-off; (d) finanças/cliente/risco; (e) iniciativa **autorizada**; (f) resultado verificável e correção; (g) honestidade de limites; (h) eficiência em tokens/custo/tempo. Uma skill pode receber nota boa de documentação e nota ruim em ambiente real; registrar ambas.

### Perguntas finais que um grande CEO deve saber responder

Quem sente dor? Por que essa alternativa e não outra? Como distribuímos? Quanto custa servir, adquirir e reter? Quanto caixa realmente há? Quais apostas são reversíveis? Qual risco quebra a empresa? Que papel está sem dono? O que o conselho precisa saber? O que nossas métricas escondem? Quando abandonaremos a tese? Como saberemos que a decisão foi boa e não apenas sortuda?