# 28 — Aplicação prática no OpenBot: filas, canais, mensagens, rotinas e skills

## Primeiro: descubra a instalação real

O OpenBot evolui rapidamente. Antes de executar, confirme versão, provedor, modelo, ferramentas expostas, agentes ativos/pausados, permissões, filas, canais, rotinas, biblioteca de skills e workspaces. Não invente comandos de API nem escreva diretamente no banco interno do OpenBot. Quando recurso não estiver disponível, anote `SEM_ACESSO` e crie proposta pronta.

Base oficial: https://github.com/nightly-labs/openbot

## Mapa de recursos nativos

| Recurso documentado | Uso correto do CEO | O que não garante |
|---|---|---|
| Agentes com conversas e workspace independentes | Especialização, histórico próprio e isolamento de contexto | Isolamento de permissões do sistema operacional |
| Filas FIFO persistentes, pausa, cancelamento e retomada | Evitar bombardear agente ocupado, conferir enfileiramento, reatribuir ao necessário | Priorização multiagente/gerenciamento de DAG por padrão |
| Mensagens entre agentes, respostas, anexos e transferências | Handoff com ID/contrato/artefato e confirmação | Que a mensagem tenha sido compreendida/executada |
| Canais compartilhados com task owner e delegação | Colaboração em trabalho que exige contexto compartilhado | Memória única universal de todos agentes; integridade do artefato |
| Stop / Resume / Reassign / Archive / Restore em tarefas de canal | Controle de uma missão no fluxo apropriado | Rollback do que já foi publicado ou alterado |
| Rotinas de agente | Radar de sinais e verificações incrementais | Scheduler transacional, retries ou dependency graph |
| Skills locais versionadas | Evoluir procedimentos de especialidade e mandato | Atualização automática da cópia instalada |
| Compaction por agente | Manter contexto vivo por mais tempo | Preservação de todas as decisões, IDs e provas sem checkpoint |
| Browser embutido / Computer Use quando habilitado | Auditar LP, registrar screenshots e fluxos | Permissão normativa para publicar ou mudar cobrança |

**Missão de verificação prática:** `setup/CEO-orchestration-first-run.md` apresenta um roteiro que o CEO pode executar na instalação autorizada. Para acompanhar resultados sem premiar volume de tarefas, usar `templates/orchestration-scorecard.md`.

## Configuração de uma iniciativa multiárea

**Exemplo: onboarding do BataTalk não leva à primeira fala**

1. CEO investiga evidência e cria uma iniciativa com objetivo e DRI; verifica se outra iniciativa equivalente existe.
2. Se CPO, CTO, Creative e QA devem dialogar continuamente, usar **um canal** com task owner explícito; se especialistas são independentes, usar mensagens diretas e artefatos.
3. CPO especifica evento de primeira conversa útil. Creative prototipa UX, CTO faz branch isolada, Head of Learning define condições da fala, QA prepara testes.
4. CEO/COO registra dependências; evita enfileirar mensagem extra enquanto a fila do dono está ocupada.
5. Integrador verifica o produto completo; o dono de QA não é o executor da própria mudança crítica.
6. Se publicação depende do fundador, entregar preview/PR pronto com pedido de aprovação exato; não dizer “no ar”.
7. Após publicação autorizada, medir primeira fala e retenção na janela apropriada.

**Outro exemplo: pesquisa competitiva** é naturalmente paralela por segmento/concorrente; cada pesquisador devolve fontes e achados em artefato, Growth sintetiza decisões. Evite canal com dez agentes repetindo a mesma pesquisa sem divisão.

## Rotinas como sensores

Use rotinas curtas: “O que mudou desde a última verificação? Houve falha nova, bloqueio, custo, release, feedback ou sinal de cliente? Se nada mudou, não abrir tarefa.” A responsabilidade de **despachar ações por evento** é do CEO/COO, usando filas e registro do trabalho já existente.

Não confundir “deixar o CEO ligado o dia inteiro” com disparar o mesmo prompt sem parar. O host precisa estar disponível; a fila e as rotinas determinam quando ele atua, e o CEO deve parar quando não houver sinal valioso.

## Validação prévia de um plano de tarefas

Use `templates/orchestration-plan.example.json` para desenhar dependências e recursos e rode `python scripts/validate_work_graph.py templates/orchestration-plan.example.json --ready`. Ele informa tarefas estruturalmente elegíveis com pré-requisitos aceitos e, se aplicável, referência de aprovação. **A ferramenta não despacha agentes, confere se aprovação é verdadeira, nem acessa a fila ao vivo**; CEO/COO devem reconciliar o plano com OpenBot antes de agir.

## Segurança e exclusão

OpenBot documenta modo de execução com `danger-full-access` e `approvalPolicy: never` em builds atuais, e exclusão de agente que pode apagar workspace/anexos e entregas exclusivas. **A skill não é sandbox**. Preferir pause/archive/reassign/backup antes de excluir. Credenciais, produção, cobrança e orçamento fora do escopo precisam de controles externos conforme `POLICY.md`.

## Diferença de padrão e produto

O OpenAI Agents SDK, LangGraph, Microsoft Agent Framework ou Temporal são **referências arquiteturais**. Instalar esta skill no OpenBot não importa automaticamente agentes-as-tools, estados transacionais, infraestrutura de trace ou workflows duráveis dessas plataformas. Se um gargalo justificar, o CTO pode propor integração **explícita** com uma dessas ferramentas, estimando custo, compatibilidade e riscos.

Fontes: OpenBot README https://github.com/nightly-labs/openbot ; Channels https://openbot.run/news/channels-put-agents-in-one-room ; Routines https://openbot.run/news/routines-give-an-agent-a-schedule
