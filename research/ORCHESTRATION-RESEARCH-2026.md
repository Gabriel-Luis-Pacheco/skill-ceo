# Pesquisa aplicada — CEO e orquestrador multiagente (06/11/2026)

## Questão

Como fazer um CEO de IA dirigir uma empresa de agentes OpenBot sem virar: (a) gerador de tarefas; (b) único gargalo de decisões; (c) repetidor de pesquisas; (d) causa de custos, crashes e dados perdidos? Como promover autonomia gerencial **sem cotas arbitrárias** e sem confundir instruções com infraestrutura?

## Evidência primária e implicações concretas

| Fonte / data de consulta | O que a fonte sustenta | Aplicação específica |
|---|---|---|
| OpenBot README, consultado em 06/11/2026: https://github.com/nightly-labs/openbot | Filas FIFO com pausa/retomada, mensagens entre agentes, canais com um task owner e delegação, skills locais versionadas, workspaces próprios, compaction e modo de execução amplo | Usar fila/canal/mensagem conforme natureza da tarefa. Exigir ACK, ownership, idempotência de efeitos externos e proteger dados |
| OpenBot Channels: https://openbot.run/news/channels-put-agents-in-one-room | Canal é útil quando há papéis realmente diferentes e contexto compartilhado; não junta memórias em uma só | CMO + CTO + CPO no mesmo projeto, mas um integrador; não fazer brainstorm coletivo em tarefa trivial |
| OpenBot Routines: https://openbot.run/news/routines-give-an-agent-a-schedule | Rotinas observam e reagem em thread, não substituem runner de dependências/retries | Rotinas como sensores de delta. Execução e deploy ficam nos sistemas apropriados |
| OpenAI Orchestration: https://developers.openai.com/api/docs/guides/agents/orchestration | Handoff transfere ownership; agents-as-tools mantém manager no controle; separar somente quando contrato muda | CEO decide se líder mantém resposta ou outra área assume; abstração conceitual, não API OpenBot |
| Microsoft Orchestrations (atualizado 2026): https://learn.microsoft.com/en-us/agent-framework/workflows/orchestrations/ | Padrões sequencial, concorrente, handoff, group chat e magentic têm semânticas distintas | Seletor de topologia por tarefa; revisar dependências e integração |
| Anthropic Building Effective Agents: https://www.anthropic.com/research/building-effective-agents | Orquestrador–workers e avaliador–otimizador funcionam em tarefas específicas; simplicidade e ground truth são cruciais | Paralelizar pesquisas; usar builder/critic para qualidade verificável; não fragmentar qualquer tarefa |
| Anthropic Multi-agent Research (13/06/2025): https://www.anthropic.com/research/multi-agent-research-system | Alto consumo relativo de tokens em sistema multiagente; subagentes com contexto isolado e resultados gravados em artefatos; tarefas muito interdependentes paralelizam mal | Roteamento por ganho real, orçamento por resultado, artefatos versionados + resumo curto |
| Anthropic Context Engineering: https://www.anthropic.com/research/effective-context-engineering-for-ai-agents | Compactação, notas e subagentes resolvem necessidades diferentes de contexto | Memória normativa/operacional/episódica, handoff com contexto mínimo e link para fonte |
| OpenAI Agent Evals: https://developers.openai.com/api/docs/guides/agent-evals | Traces permitem auditar ferramentas/handoffs/violação, não só a resposta final | Benchmark do CEO precisa de execução e revisão real, não apenas cenários em JSONL |
| LangGraph Graph API: https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/ | Estado, nós, arestas, fan-out e checkpoints compõem workflows implementados em código | Usar plano DAG e validador offline como documentação; não fingir workflow engine dentro de Markdown |
| Temporal Retry: https://docs.temporal.io/encyclopedia/retry-policies | Retry de etapa falha e retry indiscriminado de workflow não são equivalentes; replay e idempotência importam | Classificar falha, verificar resultado de side effect, reexecutar somente etapa segura |
| Netflix Culture: https://jobs.netflix.com/culture | Context over control, informed captain e dissenso com dono de decisão | CEO define direção e assume trade-offs; líderes tomam decisões locais e são cobrados por resultados |
| YC Essential Startup Advice: https://www.ycombinator.com/blog/ycs-essential-startup-advice/ | Falar com usuários, construir algo que querem, evitar crescimento precoce com economia ruim | CEO evita escala de marketing antes de ativação/retorno/margem; “valor ao aluno” é prioridade |
| Amazon Day 1: https://aws.amazon.com/executive-insights/content/how-amazon-defines-and-operationalizes-a-day-1-culture/ | Distinguir decisões reversíveis de irreversíveis e reduzir velocidade de decisão de alto custo | Ações internas reversíveis proativas; produção/cobrança/financeiro exigem alçada adequada |
| Google SRE: https://sre.google/sre-book/monitoring-distributed-systems/ | Monitoramento de sintomas vs causas, alertas acionáveis e inspeção do serviço | CEO não acorda o time por indicador decorativo; incidentes têm plano e evidência |

## Diagnóstico da skill anterior

1. Delegação existia, mas **sem seletor explícito de topologia** e diferença entre handoff, trabalho paralelo e colaboração em canal.
2. O CEO tinha fluxo de tarefas, mas **não havia um contrato verificável de dependências e integração**; muita confiança em descrições textuais.
3. O ledger sugerido era útil, mas não implementava **locks, scheduler, retry e idempotência** — risco de dupla execução.
4. Faltava política de **custo por resultado integrado**, não apenas por modelo/agente.
5. Observabilidade priorizava rubricas gerais, não o trace de uma missão do início até resultado do cliente.
6. Contexto persistente existia, mas sem estratégia clara para **handoffs sem telefone sem fio**.
7. A liderança estratégica era subordinada demais às tarefas; precisava reforçar **tese, mercado, usuário, vantagem e alocação de capacidade**.
8. Havia risco de confundir APIs de OpenAI/LangGraph/Temporal com capacidades do OpenBot; nova documentação deixa limites explícitos.

## Mudanças introduzidas

Os playbooks de 22 a 29 traduzem as fontes em rotinas de decisão. `SKILL.md` e `CEO_SYSTEM_PROMPT.md` direcionam o CEO para eles quando ocorrer um sinal. `templates/orchestration-task.md` define contrato; `scripts/validate_work_graph.py` verifica planos offline; `tests/orchestration-cases.jsonl` inclui 24 casos adversariais; `scripts/score_evaluations.py` agrega avaliações reais feitas por um revisor e não “atua” como CEO.

**Governança:** `POLICY.md` permanece fonte normativa única. Nenhuma quota de agentes, departamentos, níveis ou pesquisas foi instituída. Limites de orçamento, capacidade real, segurança e risco são legítimos e precisam ser respeitados.

## O que a pesquisa não demonstra

- Não demonstra que o CEO atual do usuário passou nos testes, que modelos específicos são “melhores” em todas tarefas ou que o BataTalk ganhou clientes.
- Estudos de outros sistemas multiagentes **não transferem automaticamente** suas métricas de eficiência para OpenBot, nem para BataTalk.
- A skill não instala Temporal, LangGraph, OpenAI Agents SDK, filas transacionais, observabilidade de traces ou proteção de produção. Tudo isso requer integração/técnica e ambiente, além de permissões e orçamento apropriados.
- O validador de DAG somente verifica coerência estática do plano, não assegura que agentes cumpriram a missão.

## Próximo teste decisivo

Comparar baseline anterior e skill atual com o **mesmo conjunto de tarefas realistas e ambiente controlado**, medindo rastreabilidade de handoffs, entrega integrada, custo/latência, reexecução após falha, decisão de não criar tarefas e valor ao aluno. Somente então rever prompts, topologia, modelo e organização com evidência.
