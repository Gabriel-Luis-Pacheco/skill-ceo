# 23 — Contratos de trabalho, dependências, handoffs e integração

## Missão

Transformar intenções em trabalho que **outro agente consiga executar e o CEO consiga auditar**. Não basta escrever “CTO: melhore o onboarding”. Cada missão tem entradas, ownership, saída, dependências, autorização, verificação e regra de conclusão.

## Pacote de missão mínimo e completo

Use `templates/orchestration-task.md` ou `templates/orchestration-task.json` como referência. Campos:
- `initiative_id`, `task_id`, `fingerprint`, objetivo empresarial e cliente afetado.
- `owner_agent_id`, `reviewer_agent_id` quando pertinente, `decision_captain` e `parent_task_id`.
- `depends_on` (IDs de tarefas que precisam estar aceitas), `priority`, `deadline_or_review_trigger`.
- `inputs` com referências a **artefatos/versionamentos**; hipótese e confiança.
- `output_contract` com formato, caminho/PR e definição de pronto.
- `owned_resources`: caminhos, branches, banco, serviços e integrações sob sua responsabilidade.
- `permissions`, `budget_scope`, `risk_class`, `approval_reference` quando aplicável.
- `tests` e `acceptance_criteria`, `fallback_or_rollback`, `status`, `observed_result`.

## DAG prático

**DAG = grafo direcionado sem ciclos**. Não é preciso obrigar um sistema inteiro a ser DAG quando há ciclos legítimos de feedback; represente *cada rodada executável* como tarefas sem dependências circulares e decisões de revisão explícitas.

- Se T3 depende de T1 e T2, não dispare T3 até aceitar o que T1 e T2 realmente entregaram.
- Se T1, T2 e T4 não compartilham arquivos e não têm dependências, podem rodar em paralelo.
- Uma tarefa bloqueada não obriga parar as demais; CEO replaneja o caminho crítico.
- Se T2 falha, replaneje seus descendentes e aceite resultados parciais se o contrato permitir.
- Se duas áreas editam o mesmo arquivo/branch, defina **dono exclusivo ou estratégia explícita de merge**. Não chamar `paralelo` o que é edição concorrente sobre um único arquivo.
- Após mudança de escopo, versão do contrato aumenta; rejeitar saídas contra versões antigas sem reconciliação.

## Protocolo de mensagem agente→agente

Mensagens curtas usam cabeçalho sem linguagem vaga:

`[TASK_ID] [CONTRACT_VERSION] [STATE] [OWNER] [ARTIFACT_REF] [BLOCKER_OR_NEXT]`

Estados sugeridos: `PROPOSED / ACCEPTED / RUNNING / BLOCKED / SUBMITTED / REVIEW_CHANGES / VERIFIED / CANCELLED`. **SUBMITTED não é VERIFIED**. Se ferramenta confirma upload mas o artefato não foi inspecionado, não declarar concluído. Handoff aceito exige confirmação do **novo dono**; marcar `SENT` sem ack é pendência, não transferência completa.

Exemplo compacto:
`[LP-014] [v2] [SUBMITTED] [CMO] [PR#42] [QA testar mobile; sem deploy]`.

### Handoff com preservação de contexto

Enviar **a pergunta certa, o contrato, o delta, referências e restrições**. Não encaminhar a conversa inteira. O especialista deve devolver achados observáveis, arquivos, alternativas, riscos e o que ficou sem resposta. Se a saída for grande, deixar no artefato e enviar link + síntese curta — reduzir perda de informação entre agentes.

## Revisão e fan-in

A integração final tem seu próprio DRI. Verificar **compatibilidade entre saídas**: copy que promete o que CPO/CTO realmente oferecem; API e UI com contratos iguais; SEO sem páginas quebradas; checkout sandbox íntegro. O CEO pergunta: *o conjunto resolve o problema do cliente?* Quatro artefatos bons isoladamente não significam uma experiência boa.

## Falhas de coordenação que precisam de gatilho

- Agente recebeu tarefa, mas não deu ack: verificar fila antes de reenviar, reatribuir se necessário.
- Dois donos disputam o mesmo escopo: suspender edições conflitantes, clarificar ownership e rebase/revisão.
- Dependência entrou em loop: quebrar o ciclo e registrar decisão de sequência.
- Entrega foi autoaprovada: exigir revisor externo quando risco/qualidade justificar.
- DRI sem tempo/capacidade: redistribuir conforme custo e caminho crítico.
- Aprovação externa pendente: outras tarefas reversíveis podem avançar; não contornar o gate.

**A skill define contratos e procedimentos, não instala um motor DAG no OpenBot.** O validador offline em `scripts/validate_work_graph.py` verifica plano JSON, detecta ciclos/dependências não aceitas e conflitos de arquivo; com `--ready` lista tarefas **candidatas** a atribuição, sem executar bots nem conceder aprovações. Exemplo: `python scripts/validate_work_graph.py templates/orchestration-plan.example.json --ready`. Para iniciar tarefa com `risk` externo/sensível, o contrato precisa trazer uma referência de aprovação válida e o mecanismo real deve conferi-la. **Referência no JSON não substitui validação externa da aprovação.**

Referências: OpenBot https://github.com/nightly-labs/openbot ; LangGraph https://docs.langchain.com/oss/python/langgraph/overview ; Microsoft https://learn.microsoft.com/en-us/agent-framework/workflows/orchestrations/
