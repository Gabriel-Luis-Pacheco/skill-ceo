# 40 — Turnaround e gestão de crises: preservar pessoas, opções e valor

> Use quando houver risco de caixa, insolvência, fraude, ataque cibernético, falha de produto, perda de receita, crise regulatória, governança ou reputação. Crise é trabalho real, não simulação de autoridade. Respeitar POLICY.md, requisitos de comunicação e orientação jurídica local. NENHUM manual garante salvar toda empresa.

## Triagem inicial em 24 horas (P0/P1)

**Pessoa antes do dinheiro:** segurança física, saúde, integridade de dados, obrigações urgentes. Abrir uma truth room com fatos e níveis de confiança: bancos e caixa utilizável, contas a pagar/receber, folha, impostos, covenants, fornecedores/contratos críticos, clientes concentrados, incidentes, acessos, processos e pessoas-chave. Identificar relógios: próxima folha, vencimentos, gatilho de default, SLA, prazo de disclosure, risco de dano.

- Nomear incident commander para crise operacional e owner do cash forecast para crise financeira.
- Separar **disponível agora / projetado / restrito / não verificado**.
- Congelar gasto discricionário de risco sem matar a receita nem descumprir lei.
- Preservar evidências; proteger dados pessoais e denunciante; criar decision log.
- Escalar ao fundador/board/advogado/seguradora/autoridades conforme dever ou autorização.
- Não inventar números nem assumir que bloqueio legal permite não agir em contenção permitida.

## Forecast direto de caixa — 13 semanas

Para cada semana: caixa inicial + entradas *realistas* de clientes/financiamentos/recebíveis - salários - impostos - fornecedores críticos - dívida - capex - demais saídas = caixa final. Separar valores confirmados dos sujeitos a negociação. Criar **base, downside e severe downside**; atualizar semanalmente com forecast x actual, causa e ação. Apontar semana do menor saldo e caixa mínimo para operação. O numerador deve ser liquidez efetivamente utilizável, não valuation ou ARR.

Exemplo fictício: saldo inicial R$ 180 mil, despesas pagas R$ 70 mil/semana, recebimento seguro R$ 40 mil/semana → burn semanal R$ 30 mil; sem outros fluxos, 6 semanas até caixa zero. Se um cliente atrasa R$ 40 mil, prazo muda drasticamente. O CEO deve agir ANTES do ponto de caixa mínimo, não apenas na semana zero. Modelo em templates/turnaround-13-semanas.md.

## Diagnóstico causal em 7 dias

| Sintoma | Bifurcação de investigação | Ações possíveis | Não fazer |
|---|---|---|---|
| Caixa acaba | EBITDA negativo? capital de giro? dívida? recebíveis? | cobrança/renegociação responsável, redução de gasto, funding, desinvestimento | esconder covenants |
| Receita caiu | novos clientes ou existentes? pipeline ou win rate? preço, volume ou mix? | recuperar segmento/canal, corrigir proposta/serviço | mandar "vender mais" |
| Churn subiu | cohort, canal, valor entregue, outage ou preço? | reativação consentida, qualidade, onboarding, reposicionamento | escalar CAC |
| Produto falha | erro funcional, dados, infraestrutura, UX ou segmentação? | rollback autorizado, fix, teste, reparo de confiança | ocultar incidente |
| Crise reputacional | fato, rumor, dano, exposição? | verificar, apoiar afetados, comunicar o verificável | negar sem prova |
| Fraude/suspeita | extensão, evidências, envolvidos, controle? | preservar provas, investigação independente, conselho | acusar publicamente |
| Dívida excessiva | negócio viável? capacidade de serviço? | reestruturação, negociação, alternativas societárias | prometer pagamento impossível |
| Conflito de liderança | incentivos, autoridade, comportamento, ética? | documentar, proteger pessoas, rever accountability | tratar abuso como "alta performance" |
| Cyberattack | incidente ativo? blast radius? PII? | contenção, forense, continuidade, notificações devidas | apagar evidência |
| Regulação | que jurisdição? obrigação? prazo? | consultoria local, plano de conformidade | aplicar regra dos EUA no Brasil |

**Quatro quadrantes:** negócio bom + balanço ruim (capital); negócio ruim + balanço bom (modelo); negócio bom + execução ruim (operação); modelo estruturalmente ruim (vender/encerrar/pivotar). O quadrante é hipótese, não conclusão instantânea.

## Prioridade temporal

**24 horas:** preservar segurança, liquidez, provas, comunicação interna e decisões urgentes.  
**7 dias:** reconciliar 13-week cash, segmentar causas, priorizar perdas evitáveis, abrir negociação estruturada com responsáveis.  
**30 dias:** estabilizar caixa, reduzir trabalho e produtos não viáveis, plano comercial crível, corrigir liderança e controles.  
**90 dias:** modelo econômico de base, retenção/clientes críticos, organização capaz de executar, forecast atualizado e governança.  
**1 ano:** sair de war room, adotar cadência normal, verificar lucratividade/capital saudável e evitar recaída.

## Playbooks especializados

### 1. Liquidez e dívida
Reconciliar bancos; cobrar vencidos com dados corretos; classificar desembolsos por necessidade legal/continuidade/valor incremental; modelar working capital, covenant headroom e alternativas. Informar o conselho da trajetória. Não selecionar pagamentos, dispensar pessoal, renegociar obrigações tributárias ou alterar termos sem assessoria e poderes. Encerramento ou recuperação judicial podem ser racionalmente superiores à continuidade; a escolha depende da legislação e dos stakeholders.

### 2. Perda de PMF e churn
Medir a coorte desde primeira experiência até valor repetido; entrevistar quem saiu sem induzir resposta; verificar competição, preço, demanda, produto e suporte; testar a menor correção sobre resultado de retenção. Não mascarar churn com novos cadastros ou descontos que destroem margem.

### 3. Fraude e governança
Evitar conflito de interesses em investigação; preservar trilhas e acesso; audit committee e legal counsel quando aplicável; proteger testemunhas e denunciantes; revisão de segregação de funções, reconciliações e incentivos. Nunca induzir destruição/alteração de prova.

### 4. Incidente cibernético
Conter superfície comprometida; preservar registros; avaliar backup e integridade; acionar security/legal; proteger usuários; restaurar controladamente; fazer postmortem sem caça às bruxas. Avaliar LGPD/ANPD no Brasil e regras pertinentes de outros países. Regras SEC de 8-K são **apenas para registrantes alcançados**, não prazos universais.

### 5. Incidente público ou de produto
Uma voz responsável informa: o que sabemos, o que não sabemos, quem foi afetado, o que já fizemos, como pedir suporte e quando teremos nova atualização. Evitar promessa de prazo sem base, atribuição de culpa sem investigação e marketing durante dano ativo.

### 6. Corte de gastos/demissões
Distinguir despesas não essenciais, projetos não rentáveis, capacidade e pessoas; redesenhar primeiro o trabalho e dependências. Revisão jurídica trabalhista e dignidade das pessoas são requisitos, não adereços. Erro: reduzir equipe mantendo todas as prioridades e serviço inviável.

## Árvores rápidas

**Receita ↓ → base nova ou instalada?** Nova: volume de leads qualificados ↓ ou conversão ↓? Instalada: churn/contraction ↑ ou expansão ↓? Examinar coorte, campanha, oferta, preço, falha e concorrência antes de decidir.

**Caixa ↓ → operação gera caixa?** Não: preço/margem/custo fixo; sim: recebimento, estoque, dívida/capex. Depois: o negócio é viável sem financiamento perpétuo? Escolher reestruturação/pivô/encerramento com especialistas.

**Ciberincidente → dados ou serviços afetados?** conter/prevenir dano → preservar prova → determinar materialidade → notificar deveres legais → restaurar e medir.

## Guardrails contra decisões ruins em crise

- Não comunicar certeza fabricada.
- Não negociar dívida baseada em projections sabidamente falsas.
- Não ocultar eventos materialmente relevantes.
- Não assumir qualquer poderes societários de um agente.
- Não automatizar demissões, decisões financeiras sensíveis ou comunicados sem autoridade.
- Não transformar turnarounds documentais em resultado real.

**Fontes consultadas/indicadas:** https://www.pwc.com/sg/en/publications/assets/managing-cash-during-crisis-2020.pdf ; https://www.ey.com/en_br/services/strategy/restructuring-turnaround-strategy ; https://www.sec.gov/resources-small-businesses/small-business-compliance-guides/cybersecurity-risk-management-strategy-governance-incident-disclosure ; https://www.oecd.org/en/publications/g20-oecd-principles-of-corporate-governance-2023_ed750b30-en/full-report/component-8.html ; https://www.nist.gov/itl/ai-risk-management-framework/ai-risk-management-framework-resources
