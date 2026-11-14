# 40 — CEO em crise: preservar opções, pessoas, fatos e caixa

**Uso:** queda de receita, churn, crise de caixa, fraude, falha grave, segurança, reputação, regulação, concorrência, dívida ou possível insolvência. **Não prometa salvar toda empresa.** Às vezes venda, reestruturação ou encerramento ordenado preserva mais valor; consultar especialistas e lei aplicável. Não executar congelamento financeiro, comunicação a terceiros ou alteração irreversível sem autorização e direitos legais (POLICY.md).

## Triagem das primeiras 24 horas

1. **Segurança e integridade:** há risco de vida, dados sensíveis, ilegalidade, fraude, indisponibilidade?
2. **Liquidez:** saldo bancário reconciliado, caixa restrito/desimpedido, pagamentos essenciais, payroll, tributos, fornecedores, recebíveis, covenants, obrigações futuras.
3. **Continuidade:** usuários/clientes impactados, produtos críticos, contratos, infra, pessoas-chave.
4. **Fatos:** separar observado de estimado; registrar hipótese rival; preservar evidência.
5. **Governança:** quem tem autoridade, quem deve ser notificado (board, regulador, seguradora, clientes), quem aprova. Não inventar isenções.
6. **Resposta:** war room com DRI, horário de atualização, incident log, decisão, dono, rollback e vencimento.
7. **Preservar opções:** suspender somente gastos discricionários cabíveis sem quebrar contrato/lei/receita; não anunciar demissões antes de análise.

## Relógio 7/30/90/365

| Prazo | Produto concreto | Pergunta a responder |
|---|---|---|
| 24h | truth room + liquidez inicial + incident log | o que ameaça continuidade primeiro? |
| 7 dias | fluxo de caixa direto 13 semanas + análise de clientes e riscos | em que semana falta dinheiro e o que muda isso? |
| 30 dias | diagnóstico da economia e estrutura; cenários + decisões | problema de mercado, balanço, execução ou produto? |
| 90 dias | plano corrigido, nova cadência, estabilização, owners | as causas fundamentais foram atacadas? |
| 1 ano | sistema normal sustentável, prevenção, investimento seletivo | dependemos ainda da sala de guerra? |

### Modelo de caixa direto de 13 semanas

Colunas S01...S13. Linhas: saldo inicial disponível; recebimentos confirmados/prováveis em linhas separadas; folha; fornecedores por criticidade; impostos; financiamento/juros/principal; capex essencial/discricionário; outros; saldo final. Cada semana: **saldo final = inicial + entradas − saídas**; saldo inicial seguinte = final anterior; reconciliação com banco e fluxo real. Semanas com saldo abaixo do mínimo operacional devem gerar decisão imediata, não somente alerta visual.

Semanal: forecast anterior → realizado → variância por linha → causa → medida → novo forecast; cenários base, downside e choque; atrasos de recebimentos e concentração são testes fundamentais. **Caixa não é EBITDA; runway não é garantia.**

## Árvores diagnósticas

**Receita ↓**
- base existente? logo churn, contração, downgrade, inadimplência, uso menor, falha de produto, mudança de preço, concorrência;
- novos? pipeline menor (oferta, ICP, canal, mercado) ou win rate menor (preço, prova, concorrência, vendedor, procurement);
- ticket/mix mudou? margem mudou? dados mudaram?
- identificar coorte, causa provável e teste discriminatório; só então sales/marketing/produto recebem ação.

**Churn ↑**
- qual cliente, motivo documentado e alternativa escolhida?
- problema de onboarding/valor percebido, promessa falsa, suporte, preço, performance, competição ou aquisição de público errado?
- comparar coorte e momento de mudança; recuperar cliente quando apropriado sem manipular.

**Caixa ↓**
- negócio bom com balanço ruim? examinar capital de giro e dívida;
- negócio bom com execução ruim? capacidade, produto, cobrança e liderança;
- negócio ruim com balanço bom? testar pivot/novo ICP controlado;
- unit economics estruturalmente ruins? crescer pode acelerar perda.
- examinar obrigações e alternativas legais antes de assumir continuidade.

**Falha de crescimento apesar de melhorias visuais**
- há exposição ao público certo? o usuário entende em segundos? primeiro valor funciona? retorno existe? pagamento confiável? contribuição positiva?
- identificar primeiro elo quebrado; resolver antes de escalar promoção.

## Incidentes específicos — playbooks mínimos

| Evento | Ação prioritária | O que não fazer |
|---|---|---|
| Cyberattack/vazamento | conter, preservar logs, proteger pessoas, recuperar serviço, counsel, notificação conforme norma, postmortem | apagar evidência, prometer segurança não verificada |
| Fraude/contabilidade | preservar provas, limitar acesso, investigação independente e auditoria/board quando pertinente | encobrir, retaliar denúncia |
| PR/reputação | apurar quem foi afetado, o que sabemos/não sabemos, reparação e atualização | negar por reflexo, inventar certeza |
| Falha de produto | rollback/fallback, medir impacto, comunicação, causa sistêmica | alterar produção às cegas |
| Liderança tóxica | proteger denunciante, apurar com independência, reduzir risco, corrigir incentivos | vingança, normalizar assédio |
| Perda de cliente grande | mapear concentração, entender motivo, impedir cascata, ajustar oferta | desconto automático irrestrito |
| Concorrente agressivo | mapear substituição real e vantagem, reforçar nicho ou escolher reposicionamento | copiar cada feature |
| Regulação | congelar mudança irregular, buscar aconselhamento local, plano de conformidade | interpretar norma estrangeira como local |
| Dívida/covenants | liquidez, contrato, opções de renegociação, assessoria | esconder covenant quebrado |
| Insolvência possível | assessoria jurídica e contábil local urgente, deveres de administradores, preservação de documentos | transferir ativos irregularmente |
| Demissão/reorganização | eliminar trabalho e decidir capacidades antes de número de cortes, counsel trabalhista | reduzir pessoas e manter 100% de projetos |
| Crise de dados/IA | pausar decisão automatizada afetada, avaliar impacto, dados e modelos, fallback humano | continuar dano até “melhorar prompt” |

Para empresas abertas nos EUA, o Item 1.05 do Form 8-K em regra requer divulgação de incidentes cyber materiais em até quatro dias úteis após a **determinação de materialidade** (com exceções) — não é regra geral de aviso para toda startup. Brasil: verificar LGPD/ANPD, CDC, CLT, legislação societária/insolvência e contratos conforme o caso, com assessoria.

## Comunicação em crise

Mensagem interna/externa revisada pelos responsáveis apropriados:
**O que aconteceu e está verificado → quem foi afetado → o que fizemos para conter → o que ainda não sabemos → próximo marco de atualização → contato de suporte.** Não dar garantias falsas, nem divulgar detalhes que agravam risco ou prejudiquem investigação.

## Concluir a crise sem esquecer

Post-mortem: impacto, linha do tempo, pontos de decisão, causas contribuintes, condição organizacional, ações corretivas, owner, data, critério de teste, reavaliação. Manter accountability sem caça às bruxas. Ao melhorar, devolver poder a cadência normal; uma war room eterna indica falha gerencial.

Fontes: [PwC — managing cash in crisis](https://www.pwc.com/sg/en/publications/assets/managing-cash-during-crisis-2020.pdf), [EY — liquidez e capital de giro](https://www.ey.com/en_br/services/strategy-transactions/liquidity-working-capital-advisory), [EY — turnaround](https://www.ey.com/en_br/services/strategy/restructuring-turnaround-strategy), [SEC — cyber disclosure](https://www.sec.gov/resources-small-businesses/small-business-compliance-guides/cybersecurity-risk-management-strategy-governance-incident-disclosure), [OECD — governança](https://www.oecd.org/en/publications/g20-oecd-principles-of-corporate-governance-2023_ed750b30-en/full-report/component-8.html), [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework/ai-risk-management-framework-resources).