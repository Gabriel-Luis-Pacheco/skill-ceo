# 22 — Arquiteturas de orquestração: o CEO escolhe a forma do trabalho

## Princípio

**O organograma não é o fluxo de execução.** Um agente pode ser chefe de outros e, em uma iniciativa específica, atuar como colaborador ou auditor. O CEO decide quantos agentes existem **sem teto arbitrário**, mas cada tarefa precisa de uma topologia adequada ao problema. Mais agentes só valem a pena se a separação acrescentar conhecimento, velocidade, independência de contexto ou qualidade.

O OpenBot dispõe de agentes com workspaces privados, filas FIFO, mensagens diretas, canais e delegação explícita. Isso **não equivale** automaticamente às APIs `agent.asTool()` ou `handoff()` da OpenAI, aos grafos de LangGraph ou aos orquestradores da Microsoft. Use os princípios; **não invente APIs ou comandos nativos**.

## Seletor de topologia orientado a evidência

| Tipo real de tarefa | Padrão | Controle / aceitação | Evite |
|---|---|---|---|
| Questão simples, um domínio e uma ferramenta | Especialista único | Supervisor revisa somente exceções e resultado | Montar comitê |
| Etapas com pré-requisitos | Sequencial / pipeline | Saída validada de A é entrada para B | Iniciar B sem contrato |
| Componentes independentes | Fan-out / fan-in | Propriedade exclusiva de artefatos; integrador verifica | Agentes sobrescrevendo arquivo |
| Problema aberto que precisa ser dividido dinamicamente | Orchestrator–workers | CEO ou líder decompõe, delega, recolhe, sintetiza | Mandar todos fazer tudo |
| Uma área assume a interlocução e tem autorização apropriada | Handoff | Dono e retorno formal mudam; CEO não microgerencia | Responsabilidade ambígua |
| Área fornece competência delimitada ao líder | Agent-as-tool **conceitual** | Líder mantém decisão final; especialista retorna artefato | Fingir que OpenBot tem API `asTool()` |
| Falha de qualidade verificável | Builder → critic → verifier | Crítica baseada em rubrica, teste independente, rollback | IA elogiando a si mesma |
| Divergência material, risco ou ambiguidade | Debate adversarial com capitão | Evidências distintas, decisão com um DRI | Votação por volume de agentes |
| Incidente crítico | Incident commander | Um comando, triagem, contenção, verificação | Vários agentes alterando produção |
| Observação recorrente de sinais | Routine/read-only → decisão | Ler deltas; abrir trabalho somente por evento relevante | Rotina de “gere tarefas” |

O CEO pode combinar padrões: pesquisa concorrente paralela → síntese por Growth → hipótese de produto → engenharia sequencial → avaliação adversarial. **Altere a topologia se o fluxo provar que está errado**.

## Heurística para decompor

1. Defina o resultado em termos do cliente/empresa e a evidência de término.
2. Liste dependências técnicas, dados de entrada, decisões e efeitos externos.
3. Diferencie partes realmente independentes das que precisam do mesmo contexto ou arquivo.
4. Escolha agentes pelos resultados históricos e pelas ferramentas/skills úteis — não só pelo cargo.
5. Decida paralelismo pela redução de caminho crítico versus custo de sincronização, não por número fixo.
6. Atribua **um DRI por entrega** e um integrador para o resultado agregado; revisores independentes quando o risco merecer.
7. Registre ownership e mensagens de handoff; rode somente tarefas com pré-requisitos aceitos.
8. Verifique **o resultado integrado**, não apenas entregas isoladas.
9. Se o fluxo produziu retrabalho, mude topologia/contrato e registre aprendizado.

## Contexto, controle e hierarquia

A Netflix recomenda um *informed captain* por decisão importante e contexto em vez de microcontrole. Traduzindo: o CEO explica propósito, restrições e como medir valor; o responsável escolhe implementação dentro da alçada. CEO intervém em conflito, padrão de qualidade, custo ou risco material, não em cada decisão de CSS.

**Divisão saudável:** CEO define estratégia + trade-offs; COO orquestra filas/capacidade/depêndencias; CTO/CPO/CMO e demais líderes executam seus pipelines; especialistas fazem o trabalho. Isso é sugestão inicial, **não estrutura obrigatória**. CEO pode alterar a equipe e a profundidade sem cotas.

## Quando criar novo agente ou sublíder

Criar quantos forem úteis, dentro de recursos e alçadas já delegadas, quando há: escopo independente, habilidade ausente, contexto que congestiona o líder, auditoria independente necessária ou demanda suficiente para especialização. Não criar quando o problema é um brief confuso, dependência única, fila mal coordenada, falta de cliente ou ausência de ferramentas.

**A escolha não é “muitos versus poucos”; é “valor criado por coordenação versus custo de coordenação”.**

Fontes: OpenAI Orchestration https://developers.openai.com/api/docs/guides/agents/orchestration ; Microsoft https://learn.microsoft.com/en-us/agent-framework/workflows/orchestrations/ ; Anthropic https://www.anthropic.com/research/building-effective-agents ; OpenBot https://github.com/nightly-labs/openbot ; Netflix https://jobs.netflix.com/culture
