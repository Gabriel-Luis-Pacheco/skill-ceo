# 24 — Confiabilidade da orquestração: timeouts, falhas, retries, incidentes

## Não há execução exatamente uma vez por mágica

Uma rotina, arquivo JSONL ou prompt não fornece transações. OpenBot oferece fila persistente, pausa/cancelamento e mensagens; **não assumir** que resolve retry de efeito externo, compensação, idempotência no Stripe, controle de locks ou dead-letter queues para cada integração.

## Classifique a falha antes de agir

| Falha | Conduta |
|---|---|
| Temporária clara: rede, rate limit, disponibilidade | Respeitar janela de recuperação/backoff quando suportado; reexecutar apenas a etapa idempotente |
| Permanente: entrada inválida, acesso negado, contrato impossível | Corrigir causa ou escalar; não repetir |
| Qualidade: resultado ruim, teste reprovado | Alterar hipótese/brief/ferramenta/modelo com avaliação; não “tente de novo” indiscriminado |
| Resultado desconhecido: timeout após comando de envio/publicação | **Consultar destino e registro antes de repetir**; nunca inferir “não executou” |
| Dependência bloqueada: dono ausente, fila parada | Ver estado real no OpenBot; reatribuir explicitamente e atualizar downstream |
| Conflito de arquivo/branch | Reconciliar versões e autor responsável; não sobrescrever silenciosamente |
| Contexto truncado ou agente reiniciado | Reidratar a partir de checkpoint/artefatos; não repetir efeitos colaterais |
| Incidente financeiro/privacidade | P0 e política de alçada; congelar mudanças de risco, preservar evidências |

## Política de tentativas adaptativa

Antes de retry pergunte: é seguro repetir? é idempotente? falhou antes ou depois do efeito? houve mudança de entrada? provedor impôs `Retry-After`? Uma nova tentativa tem esperança de valor positiva?

Repetir somente se houver **sinal técnico** de recuperação e custo aceitável. Use limite de tentativas/tempo/custo **decidido por risco e operação**, não quota fixa global de agentes. Em caso de progresso impossível, `BLOCKED_BY_ACCESS`, `NEEDS_ROOT_CAUSE` ou `PREPARED_AWAITING_APPROVAL`.

Em sistemas que aceitam chave idempotente, usar `task_id + operation + target + approved_scope` para registrar intenção e resultado da operação; não supor que todos APIs aceitem chaves. Side effects de alta gravidade exigem ferramenta adequada com garantia real e aprovação. **Reversão (rollback) não reverte e-mails enviados nem cobranças já liquidadas**; registrar plano de compensação e responsáveis.

## Stalls, deadlocks e filas

- Monitorar tempo desde o **último progresso verificável**, não apenas desde a última mensagem.
- Para tarefas aguardando resposta, consultar fila OpenBot: o agente pode estar ocupado em FIFO, não necessariamente falhou.
- Detectar espera circular de recursos/decisões; quebrar dependência sob um capitão informado.
- Enfileirar menos mensagens repetidas; se `queue depth` cresce e o throughput cai, reduzir inflow e revisar capacidade.
- Não cancelar execução segura sem entender se um side effect já aconteceu.
- Para progresso crítico e execução durável, considerar um **workflow engine dedicado** (Temporal/LangGraph ou código próprio) implementado fora da skill. Isso é proposta de arquitetura, não capacidade que ela já disponibiliza.

## Degradação parcial

Se uma subequipe falha mas outras entregaram:
1. Classificar quais resultados continuam utilizáveis.
2. Não declarar objetivo completo se depende da parte falha.
3. Replanejar dependências, revisão e custo.
4. Se for possível, entregar uma versão menor de valor real, com escopo explicitamente reduzido.
5. Recuperação = sistema final observado e testado, não aviso de agente.

## Operação em crise

Um comandante de incidente, comunicação separada, congelar mudanças não essenciais e abrir canal compartilhado **somente** quando colaboração de vários agentes for necessária. CTO ou autoridade técnica oferece opções, CEO resolve trade-offs; ações em produção conforme `POLICY.md`. Toda promessa de recuperação exige teste.

Fontes: Temporal retry https://docs.temporal.io/encyclopedia/retry-policies ; LangGraph https://langchain-ai.github.io/langgraph/how-tos/multi-agent-network/ ; Google SRE https://sre.google/sre-book/monitoring-distributed-systems/
