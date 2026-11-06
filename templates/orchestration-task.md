# Contrato de execução entre agentes — [TASK_ID]

**Initiative ID / Task ID / versão:**  
**Objetivo do cliente e do negócio:**  
**Resultado verificável (não atividade):**  
**DRI/owner agent e superior:**  
**Decision captain e integrador final:**  
**Agentes consultados e revisor independente:**  
**Topologia escolhida:** single / sequential / fan-out-fan-in / orchestrator-workers / handoff / evaluator-optimizer / incident
**Motivo da escolha versus executar sozinho:**  
**Dependências aceitas (`depends_on`):**  
**Inputs: URLs, artefatos, commits e fontes confiáveis:**  
**Hipóteses e incertezas, com data:**  
**Ownership exclusivo (arquivos/branches/ferramentas):**  
**Critérios e provas de aceite:**  
**Contrato de saída (artefato, path, formato e resumo):**  
**Limites reais: tempo, capacidade, custo, alçada e dados:**  
**Aprovação para efeitos externos (se necessária):**  
**Condição de parada, fallback, erro e rollback/compensação:**  
**Checkpoint ou gatilho de revisão, não “ping de status”:**  

## Mensagem de saída
`[TASK_ID] [CONTRACT_VERSION] [STATE] [OWNER] [ARTIFACT_REF] [BLOCKER_OR_NEXT]`

**Estado da tarefa:** PROPOSED / ACCEPTED / RUNNING / BLOCKED / SUBMITTED / REVIEW_CHANGES / VERIFIED / CANCELLED.

**Estado da evidência:** OBSERVADO / RELATADO / HIPÓTESE / SEM DADOS / SEM ACESSO / BLOQUEADO.

A passagem de `SUBMITTED` a `VERIFIED` exige inspeção independente adequada. `SENT` não é handoff aceito sem confirmação do novo dono. Registre resultado observado de ferramenta e versão contratual.
