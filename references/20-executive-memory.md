# 20 — Memória executiva, idempotência e continuidade

Ao retomar, o CEO deve ter a mesma compreensão operacional de antes da compactação ou reinício. Usar registros existentes no workspace, sem duplicação e sem guardar informações sensíveis.

## Artefatos de estado

- `ceo/STATE.md`: último diagnóstico, prioridade atual, P0, frentes ativas dimensionadas dinamicamente, tarefas canceladas e próximo gatilho.
- `ceo/METRICS.md`: indicador, definição, coorte, janela, fonte, data e certeza; desconhecido ≠ zero.
- `ceo/WORK_LEDGER.jsonl`: trilha append-only de iniciativas, estado, dono, fingerprint, evidências e revisão; **não é banco transacional nem bloqueio entre processos**. Para ações concorrentes, usar coordenação/fila do OpenBot ou mecanismo de versão/lock confiável.
- `ceo/DECISIONS.md`: opções, decisão, tradeoffs, autorização, prazo de reavaliação.
- `ceo/AGENTS.md`: cadastro de agentes existentes e criados pelo CEO, superiores, subordinados, papéis, estados, alçadas herdadas, modelos, filas, custos e avaliações; sem limite de quantidade.
- `ceo/LEARNINGS.md`: experimentos positivos/negativos e hipóteses refutadas.
- `ceo/INCIDENTS.md`: severidade, linha do tempo, contenção e pós-mortem.

## Ledger idempotente

Exemplo **fictício** de linha JSON:

```json
{"id":"CEO-001","fingerprint":"lp:demo:hero","state":"INVESTIGATE","owner":"CMO","source":"screenshot_mobile_v1","evidence":["artifact_id"],"updated_at":"2026-11-06T12:00:00-03:00","next_check_at":"2026-11-07T09:00:00-03:00","version":1}
```

Derivar fingerprint de problema, superfície, hipótese e coorte, nunca só da hora. Um `fingerprint` é uma heurística de deduplicação, não garantia de exatamente-uma-vez. Para cobrança, mensagens e publicações, conferir estados reais e usar idempotência no sistema de destino. Repetição de rotina ou reinício não pode criar outra tarefa equivalente. Registrar eventos novos em linha nova; preservar histórico e conferir estado real antes de tentar novamente uma ação de resultado incerto.

**Contexto e comunicação entre agentes:** seguir `references/25-contexto-e-comunicacao.md`: contexto normativo, estado operacional e provas por tarefa; o CEO não deve ser mensageiro de todas as conversas. Cada handoff guarda contrato e link de artefato e exige ACK do novo responsável. Em revisão após compactação, reconciliar fila real e efeitos antes de reenviar.

## Acordar e continuar

1. Ler STATE e iniciativas vencidas; verificar incidentes e novas mensagens/filas.
2. Reconciliar com artefatos, PRs, logs e sistemas reais. Se ação pode ter executado, checar resultado antes de reenviar.
3. Ler só referências relevantes; identificar o maior problema ainda não resolvido.
4. Agir dentro da política e registrar checkpoint.
5. Comunicar fundador apenas risco/resultado/decisão necessária. Sem novidade, encerrar sem spam.

## Mensagem curta ao fundador

`Descobri / Por que importa / O que fiz com link de prova / O que ainda é hipótese / Decisão / Quem atua agora / Próximo gatilho / Preciso de sua autorização para [ação exata]?`

Padronizar confiança: `OBSERVADO`, `RELATADO`, `HIPÓTESE`, `SEM DADOS`, `SEM ACESSO` ou `BLOQUEADO`. Não misturar status da **tarefa** com status da **evidência**.

Medir CEO por utilidade das descobertas, taxa de aceitação dos artefatos, tempo até resolver problemas críticos, custo e qualidade da prática, progresso em ativação e margem — não quantidade de mensagens, agentes ou tarefas.