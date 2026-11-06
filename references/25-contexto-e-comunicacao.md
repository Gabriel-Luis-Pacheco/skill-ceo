# 25 — Engenharia de contexto e comunicação interagentes

## O problema real

Cada agente tem janela de contexto, memória própria, histórico parcial e ferramenta/modelo potencialmente diferente. O CEO não deve agir como transmissor manual de todo histórico; precisa manter **um plano compartilhado e artefatos verificáveis**. Resumos sucessivos sem fonte geram “telefone sem fio”; contexto excessivo eleva custo, latência e confusão.

## Três camadas de memória

1. **Normativa:** `POLICY.md`, mandato, restrições do fundador e contratos duradouros. Não resumir a ponto de remover proibições.
2. **Operacional:** estado e decisões versionadas por iniciativa (`ceo/STATE.md`, ledger, owners, próximas verificações, PRs e artefatos).
3. **Episódica:** traces, testes, pesquisas, discussões e logs autorizados por task ID; consultados só quando relevantes.

Não criar um segundo “banco da verdade” se o OpenBot já oferece fila, memória e canal que atendem. Os documentos executivos são índices/handoffs e não substituem sistemas transacionais ou dados de produção.

## Context packet — somente o necessário

Enviar a cada agente:
- objetivo e usuário, restrições, tarefa/contrato/versionamento;
- fatos com **fonte e data**; hipóteses rotuladas;
- entradas exatas, arquivos/projetos/branches corretos;
- definição de pronto, testes, modelo de saída;
- status de dependências e quem decide impasses;
- orçamento/alçada; apontamento a `POLICY.md` quando apropriado.

Não transmitir histórico de meses, dados de usuário ou todo o conteúdo da skill. Se o agente pedir mais, fornecer **apenas a parte faltante**. Para subagentes que investigam hipóteses independentes, usar contextos isolados e pedir resumos com links para os artefatos-fonte.

## Comunicação: canal vs mensagem direta

- **Canal OpenBot** quando dois ou mais agentes devem ler continuamente as decisões e criar uma entrega conjunta com **um task owner**. Ex.: LP (CMO/CPO/Creative/CTO/QA).
- **Mensagem direta** quando a competência tem objetivo isolado, sem necessidade de sincronizar todos; usar ID, versão e ack.
- **Fila individual** para executar tarefas; não enviar a mesma missão para chat, canal e rotina sem deduplicação.
- **Arquivo compartilhado versionado** para evidências e entregas; não usar canal como armazenamento exclusivo de resultados importantes.
- **CEO** deve sintetizar trade-offs entre áreas, mas decisões técnicas locais cabem ao líder com alçada.

Uma mensagem “acabou?” não é checkpoint. Checkpoints existem por **mudança significativa, bloqueio, risco, aceitação e término**, não por frequência teatral.

## Compactação e reinício

Ao aproximar limite de contexto, salvar primeiro:
`missão → decisão atual → provas → dependências → o que já foi executado → efeitos externos/ids → próxima ação → condição de parada`.
Depois compactar. Não perder IDs, aprovações, riscos e links de artefatos. Ao retomar, conferir o estado de ferramentas antes de executar novamente.

**Regra de fidelidade:** resumo é um índice para a evidência. Sempre que decisão material depender de detalhe omitido, reabrir a fonte e validar. Nunca transformar `RELATADO` em `OBSERVADO` durante a compactação.

## Pesquisa e trabalho paralelo

Subagentes de pesquisa trabalham em perguntas distintas; cada um entrega evidência, links, incertezas e hipótese rival. O integrador não concatena parágrafos: deduplica fatos, checa inconsistências, revisa fontes primárias, e escreve a **decisão** que mudará o BataTalk.

Fontes: Anthropic context engineering https://www.anthropic.com/research/effective-context-engineering-for-ai-agents ; Anthropic multi-agent https://www.anthropic.com/research/multi-agent-research-system ; OpenBot channels https://openbot.run/news/channels-put-agents-in-one-room
