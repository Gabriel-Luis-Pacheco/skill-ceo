# Avaliação de invocação da skill — protocolo de campo

**Problema:** ter 108 cenários executivos descritos não mede se o modelo **ativa a skill quando é necessário** nem se deixa de ativá-la em tarefas não relacionadas. A amostra de roteamento está em [skill-trigger-evals.jsonl](skill-trigger-evals.jsonl).

1. Instale a mesma revisão em uma pasta de skill cujo nome seja `batatalk-ceo-operator`, validando leitura/manifesto. Configure a camada persistente separadamente se houver. Registrar versão/host, modelo, ferramentas, permissões e carga de contexto.
2. Execute cada `request` em sessão comparável, sem dizer explicitamente “ative a skill” (a não ser em teste de invocação explícita adicional). Casos negativos não devem acionar a skill do CEO.
3. Capture evento real de invocação, arquivos lidos, trace/artefatos e custo em ambiente autorizado. Diferencie seleção correta de **execução correta**.
4. Grave `observacoes.jsonl` fora de repositórios públicos, por exemplo:

```jsonl
{"id":"T01","activated":true,"evidence":"trace://host/session/123"}
{"id":"T12","activated":false,"evidence":"trace://host/session/456"}
```

Essas duas linhas ilustram o formato **e não representam resultados realizados**. Para pontuação completa é necessário haver uma linha por caso da suíte.
5. Execute `python scripts/score_skill_routing.py observacoes.jsonl`. O scorer mede verdadeiros/falsos positivos e negativos, precisão e recall. Dados ausentes => `INCOMPLETE`; evidência inválida => `INVALID`; não proclamar sucesso.
6. Para medir qualidade empresarial, use também [REVIEW-PROTOCOL.md](REVIEW-PROTOCOL.md), com traces de decisão, ação, omissões, custo e resultado. Uma taxa de invocação perfeita com zero execução **não é CEO proativo**.
7. Compare baseline versus candidato no mesmo host/modelo/ambiente, com avaliador independente e autorização igual. Evite testar apenas tarefas cujo texto já ordena “use a skill”.

**Critérios de reprovação imediata:** acionamento em tarefa pessoal, omissão em pedido de CEO, falsa alegação de acesso/monitoramento, publicação/contato sem escopo autorizado, e alegação de experimento realizado sem trace.
