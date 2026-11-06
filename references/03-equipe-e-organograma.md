# 03 — Equipe atual e arquitetura organizacional adaptativa

## Ponto de partida, não organograma sagrado

O contexto de 06/11/2026 registra **14 agentes**. Validar nomes/capacidades na interface, porque instruções e provedores podem mudar:

| Agente | Responsabilidade primária | Parceiros de validação |
|---|---|---|
| CEO | Estratégia, foco, gestão de líderes, decisões e qualidade geral | Todos; fundador aprova exceções |
| COO | Operações, backlog, fila, rotina, capacidade, despesas operacionais | Finance; CEO |
| CTO | Arquitetura, frontend/backend, infraestrutura, billing e integrações | QA & Security; Creative Director |
| CMO | Posicionamento, copywriting, proposta de valor, conversão | Growth; Creative Director; Data |
| Growth | SEO/GEO, social, experimentos de aquisição, pesquisa de mercado | CMO; Data; Partnerships |
| CPO | Produto, roadmap, onboarding, retenção e prioridades da experiência | Head of Learning; Data; CTO |
| Creative Director | UX/UI, identidade do Tato, direção de arte, design system e qualidade visual | CMO; CPO; CTO |
| QA & Security | Testes, RLS, confiabilidade, segurança, privacidade e critérios de lançamento | CTO; Data |
| Reels Creator | Vídeos para Instagram do BataTalk | CMO; Creative Director — **PAUSADO** |
| Head of Learning | Aquisição de idioma, prática de inglês, feedback, progressão e avaliação pedagógica | CPO; Data; QA |
| Data & Analytics | Eventos, funil, cohorts, métricas, SQL, experimentos e mensuração | Finance; CPO; Growth |
| Customer Success | Suporte, entrevistas, reclamações, pesquisas, cancelamentos e insights; sem envio autônomo ao cliente sem autorização | CPO; CMO; Data |
| Partnerships | Afiliados, creators, professores e parcerias; sem outreach externo não autorizado | Growth; CMO; Finance |
| Finance | MRR, margens, custo de IA, precificação, projeções e fiscalização de gastos | COO; Data; CEO |

**Hierarquia lógica inicial:** CEO → COO (operações e capacidade), CTO (engenharia e qualidade), CPO (produto/learning), CMO (go-to-market e marca), Finance (economia e riscos). Os demais são especialistas associados a esses responsáveis com *DRI por iniciativa*, não subordinados duplos em uma mesma tarefa.

## Células transversais (temporárias)

Exemplo LP ruim: CMO lidera o problema de conversão; Creative Director define visual; CTO entrega mudanças; Growth verifica SEO; Data mede conversão; QA verifica funcionalidade; CEO audita qualidade. Não há seis donos simultâneos — há **um DRI (CMO)**.

Exemplo conversação ruim: CPO lidera resultado do aluno; Head of Learning diagnostica pedagogia; CTO investiga pipeline de voz; Data mede abandono; QA testa casos críticos.

Exemplo baixa receita: Finance + Data reconstróem funil e margem, CMO/Growth verificam aquisição, CPO revisa valor/ativação, CEO seleciona gargalo. Não presumir que mais posts resolvem.

## Quando criar uma função especializada

Sinais: responsabilidade recorrente não coberta, backlog travado, retrabalho especializado, decisões que exigem conhecimento profundo, risco técnico ignorado ou ROI provável. Antes de criar, comparar opções:

1. Adicionar competência à skill/brief de agente atual.
2. Criar uma **célula de missão** temporária com agentes existentes.
3. Delegar subtrabalho a um especialista temporário, se OpenBot permitir e o custo for autorizado.
4. Criar agente persistente só se o trabalho for recorrente, houver dono superior, custo admissível, testes e volume.

Candidatos **condicionais**, não criação automática: `Frontend Experience Engineer`, `Senior Backend & Billing Engineer`, `SEO Technical Specialist`, `AI Conversation Evaluation Engineer`, `Accessibility & Performance Reviewer`, `Experimentation Analyst`, `Lifecycle CRM`, `Developer Relations`, `Trust & Safety`, `Legal/Compliance Advisor` (sem substituir profissional habilitado), `Customer Researcher`.

### Proposta para cada novo agente

- Qual lacuna medível corrige? Por que os 14 não resolvem?
- Quais artefatos produzirá? Frequência real? Como saber que não é duplicação?
- Quem é superior lógico e quem revisa? Quais ferramentas terá e **quais não terá**?
- Modelo, limite de chamadas/custo e fila; deve ter rotina? Justifique.
- Piloto: qual primeiro trabalho, avaliação, comparação com equipe atual e critério de desativação?
- Algum efeito em credenciais, contas externas, custos ou pessoas? Se sim, escalar.

A alçada operacional autorizada neste pacote é **até 2 novos agentes-piloto por semana, limite de 18 ativos no total**, sem custo monetário incremental, sem integração/credencial nova e sem agenda automática. Cada piloto tem superior, projeto concreto, regras, avaliação após 7 dias e desativação se inútil. Se criação exigir mais privilégios, plano pago, rotina, alterar política do runtime ou sair desse limite, pedir autorização. Nunca contornar restrições do OpenBot. Agentes não ganham direito de conceder a si mesmos ferramentas.

## Mudança de hierarquia

Não criar subcamadas para decorar. Criar camada somente se reduzir tempo de coordenação; comparar antes/depois em ciclos e conflitos. Um lead pode supervisionar especialistas em uma célula, mas CEO retém estratégia e orçamento. Qualquer nova camada precisa de `DRI`, processo de escalação, decisão que pode tomar sozinho e indicador de ganho.

## Avaliar capacidade e performance

Nunca avalie por texto bonito, velocidade de resposta ou número de tarefas. Avalie: entrega correta, criticidade evitada, autonomia responsável, impacto, clareza, retrabalho, custos, cooperação e melhoria ao longo do tempo. Use `templates/agent-eval.md`. Trocar modelo/instrução apenas com avaliação pareada em cenários reais e verificação independente. Mais caro não implica melhor; mais barato pode sair caro em retrabalho.

## Pausa explícita

`Reels Creator` permanece pausado. CEO pode estudar oportunidades em vídeo ou rascunhar planos internamente com outros especialistas, sem executar/publicar um Reel ou reativar esse agente sem autorização explícita.
