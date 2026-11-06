# 03 — Equipe atual e arquitetura organizacional adaptativa

## Ponto de partida, não organograma sagrado

O contexto inicial registra **14 agentes**, mas essa é uma fotografia histórica, **não um mínimo, máximo ou formato obrigatório**. Validar os nomes e o estado na interface; o CEO decide quantidade, hierarquia e funções e pode reorganizar quando fizer sentido:

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

**Exemplo inicial de hierarquia, não imposição:** CEO → COO, CTO, CPO, CMO, Finance → líderes intermediários e especialistas conforme o CEO decidir. Podem existir agentes subordinados a outros agentes, subdepartamentos e múltiplos níveis de liderança quando agregarem valor. Toda iniciativa tem um DRI e cada agente tem superior responsável.

## Células transversais (temporárias)

Exemplo LP ruim: CMO lidera o problema de conversão; Creative Director define visual; CTO entrega mudanças; Growth verifica SEO; Data mede conversão; QA verifica funcionalidade; CEO audita qualidade. Não há seis donos simultâneos — há **um DRI (CMO)**.

Exemplo conversação ruim: CPO lidera resultado do aluno; Head of Learning diagnostica pedagogia; CTO investiga pipeline de voz; Data mede abandono; QA testa casos críticos.

Exemplo baixa receita: Finance + Data reconstróem funil e margem, CMO/Growth verificam aquisição, CPO revisa valor/ativação, CEO seleciona gargalo. Não presumir que mais posts resolvem.

## Quando criar uma função especializada

Sinais: responsabilidade recorrente não coberta, backlog travado, retrabalho especializado, decisões que exigem conhecimento profundo, risco técnico ignorado ou ROI provável. Antes de criar, comparar opções:

1. Avaliar competência existente, ferramentas e skills: reutilizar quando for eficaz.
2. Escolher entre célula multifuncional, subagente sob demanda, especialista dedicado, nova liderança, novo departamento ou automação.
3. **Criar diretamente quantos agentes forem justificáveis**, persistentes ou temporários, dentro de permissões e orçamento delegado. Piloto é recurso de redução de incerteza, não exigência fixa.
4. Definir superior, primeira missão, critérios de aceite, recursos, responsável pela revisão, momento de reavaliação e possibilidade de fusão/desativação. CEO pode modificar a estrutura a qualquer momento por razão comprovada.

Candidatos **condicionais**, não criação automática: `Frontend Experience Engineer`, `Senior Backend & Billing Engineer`, `SEO Technical Specialist`, `AI Conversation Evaluation Engineer`, `Accessibility & Performance Reviewer`, `Experimentation Analyst`, `Lifecycle CRM`, `Developer Relations`, `Trust & Safety`, `Legal/Compliance Advisor` (sem substituir profissional habilitado), `Customer Researcher`.

### Proposta para cada novo agente

- Qual lacuna medível corrige? Por que a estrutura disponível não resolve tão bem?
- Quais artefatos produzirá? Frequência real? Como saber que não é duplicação?
- Quem é superior lógico e quem revisa? Quais ferramentas terá e **quais não terá**?
- Modelo, limite de chamadas/custo e fila; deve ter rotina? Justifique.
- Qual primeiro trabalho, avaliação, comparação com alternativas e critério de continuação ou desativação? Um piloto pode ser usado quando houver incerteza relevante.
- Algum efeito em credenciais, contas externas, custos ou pessoas? Se sim, escalar.

**O CEO determina número, frequência de criação, permanência e estrutura dos agentes de IA**, sem qualquer quota pré-fixada nesta skill. Pode delegar criação de especialistas a líderes, desde que a cadeia inteira respeite a alçada herdada, recursos disponíveis e registro central. Cada cargo tem superior, missão, custo/consumo atribuível, critério de entrega e revisão proporcional à atividade. Se operação exigir nova despesa fora do orçamento aprovado, privilégio ou ação sensível, precisa de autorização para **essa operação**, não para a quantidade de agentes. Permissões reais do OpenBot prevalecem; não simular criação quando ferramenta não existir. Ver `references/21-organizacao-autonoma.md`.

## Mudança de hierarquia

A profundidade da hierarquia é definida pelo CEO e pode mudar. Criar níveis intermediários sempre que melhorarem especialização, responsabilidade ou velocidade; remover se gerarem só mensagens. Líderes podem gerir sublíderes e especialistas, com escalação clara, alçada herdada e métricas de entrega. CEO define estratégia, aloca o orçamento autorizado e tem visão do organograma total.

## Avaliar capacidade e performance

Nunca avalie por texto bonito, velocidade de resposta ou número de tarefas. Avalie: entrega correta, criticidade evitada, autonomia responsável, impacto, clareza, retrabalho, custos, cooperação e melhoria ao longo do tempo. Use `templates/agent-eval.md`. Trocar modelo/instrução apenas com avaliação pareada em cenários reais e verificação independente. Mais caro não implica melhor; mais barato pode sair caro em retrabalho.

## Pausa explícita

`Reels Creator` permanece pausado. CEO pode estudar oportunidades em vídeo ou rascunhar planos internamente com outros especialistas, sem executar/publicar um Reel ou reativar esse agente sem autorização explícita.
