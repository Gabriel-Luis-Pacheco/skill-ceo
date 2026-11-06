# Primeira missão de orquestração para enviar ao CEO do OpenBot

Ative a revisão instalada da skill `batatalk-ceo-operator`, confira que lê `SKILL.md` e `POLICY.md` e execute **um diagnóstico real de orquestração da equipe do BataTalk**. Trabalhe em português. Você decide quantos agentes e equipes são necessários; esta missão **não** institui um teto de criação, mensagens ou frentes.

## 1. Descubra o ambiente sem supor poderes

Inspecione os agentes realmente existentes, modelos, alçadas, skills, status, filas FIFO, canais, tarefas compartilhadas, rotinas, workspaces e ferramentas que podem ser usadas. Confirme a revisão efetivamente instalada, não só o commit no GitHub. Não alegue acesso a algo que não conseguiu consultar. Verifique custos e limites do provedor quando disponíveis.

## 2. Identifique gargalos de orquestração

Revise tarefas e entregas reais. Procure: duplicações, duas áreas editando mesmo arquivo, agente preso na fila, delegação sem aceite, retrabalho, “feito” sem prova, contexto perdido, mensagens excessivas, revisão complacente, agente sem missão, competência faltante, excessos de token e decisões que só o CEO está tomando desnecessariamente. Escolha problemas **observados**, não uma auditoria fictícia.

## 3. Escolha topologia por missão

A partir do maior problema relevante do BataTalk — experiência de primeira fala, retenção, SEO/LP, custos ou confiabilidade — decida se é melhor um especialista, sequência, fan-out/fan-in, handoff ou equipe em canal. Consulte `references/22-orquestracao-padroes.md` até `references/29-modelos-custo-capacidade.md` conforme a necessidade.

Para cada tarefa, crie contrato com ID, DRI, dependências, recursos exclusivos, resultado, prova e revisão. Se houver infraestrutura local que permite preparar JSON, use `templates/orchestration-plan.example.json` como exemplo e valide o plano com `scripts/validate_work_graph.py`. O script valida **plano**, não executa tarefas.

## 4. Faça acontecer dentro da alçada

Delegue e acompanhe uma **melhoria reversível e útil** se houver dados/ferramentas/recursos autorizados. Use um canal somente quando haja colaboração real. Verifique ACK dos handoffs, artefato final e teste por revisor independente. Se um efeito externo for necessário, deixe PR/protótipo/decisão pronto e peça aprovação específica, sem realizar o efeito.

Crie, promova ou pause agentes de IA quando houver benefício, sem cota arbitrária, e sem apagar workspaces indevidamente. Não reative o Reels Creator. Evite criar agentes para simular crescimento corporativo.

## 5. Reporte fatos, e não teatro

Entregue: topologia escolhida e motivo; mapa de dependências; agentes envolvidos e suas responsabilidades; handoffs confirmados; links de artefatos; problemas de fila/custo; resultados `OBSERVADO`, `RELATADO`, `HIPÓTESE`, `SEM DADOS` ou `SEM ACESSO`; decisões e aprovações pendentes. Diga especificamente **o que mudou na experiência do aluno ou na eficiência da equipe** e qual evidência sustenta a afirmação. Se nada foi executado, explique o bloqueio — não invente sucesso.
