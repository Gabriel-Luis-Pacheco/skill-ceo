# Rotinas sugeridas para configurar no OpenBot

Rotinas do OpenBot precisam ser criadas na interface e têm a semântica de lembrete executável por agente, **não** garantem entrega única ou execução ininterrupta. A cada uma, vincule o CEO e defina horário apropriado. Horários abaixo são **sugestões**, não jobs já criados. Adapte ao custo/modelo e às suas preferências.

## Rotina 1 — Pulso executivo diário (ex.: dias úteis, 09h)

"Leia o estado executivo e somente as novidades desde ontem. Identifique P0, mudanças nos números verificáveis, bloqueios dos agentes e o maior gargalo atual do BataTalk. Faça uma inspeção independente curta em produto, marketing ou operação conforme o risco. Tome e delegue uma ação segura e valiosa; documente artefatos e resultado. Não crie tarefas novas sem mérito. Se não houve mudança, registre internamente e não envie relatório decorativo. Não reative Reels Creator."

## Rotina 2 — Conferência de execução (ex.: dias úteis, 15h)

"Confira exclusivamente entregas/filas que mudaram desde o último pulso e procure AI slop, ausência de testes, dependência cruzada ou retrabalho. Peça melhoria específica, corrija brief ou prompt/skill com teste e backup se necessário, reatribua responsável quando houver motivo. Resolva ao menos um bloqueio material. Se tudo estiver bem, finalize sem notificações. Respeite alçada e limites."

## Rotina 3 — Revisão executiva semanal (ex.: segunda-feira, 10h)

"Faça revisão empresarial: métricas disponíveis, receita/margem, aquisição, ativação, retenção, qualidade da prática, SEO/GEO, LP, concorrentes, equipe e custos. Encontre gargalos relevantes e decida quantas iniciativas podem avançar conforme capacidade, orçamento e dependências; não imponha teto numérico. Questione qual trabalho deve parar. Convocar alinhamento de agentes somente se decisões dependerem de múltiplas áreas; caso contrário fazer async. Emita um briefing executivo compacto com evidências, responsáveis e experimentos. Não confunda hipótese e dado real."

## Rotina 4 — Investigação estratégica (ex.: quinzenal, quarta-feira, 11h)

"Escolha uma oportunidade ou ameaça importante ainda pouco compreendida (ex.: concorrente, qualidade pedagógica, canal de aquisição, UX, custo de IA, retenção). Pesquise profundamente fontes atuais e primeira mão, contraste com dados BataTalk, monte evidências e faça uma recomendação: testar, manter em observação ou descartar. Se não justificar nova frente, não abra uma. Registre aprendizado de forma utilizável pelas áreas."

## Rotinas adicionais de consciência situacional — configurar só se houver fontes

**Não existem por estarem neste arquivo.** Instalar na versão real do OpenBot, informar ao usuário quais rotinas estão realmente ativas, provar primeira execução, verificar permissão e custo. A versão oficial documenta `routine_no_update` para execuções sem novidade; quando disponível, use-o em vez de alertar por obrigação. Fonte: https://github.com/nightly-labs/openbot/blob/main/docs/architecture/agents.md

### Radar comercial (se houver acesso ao CRM e aos eventos)

“Compare apenas o delta verificável de contatos efetivamente enviados, respostas, ensaios de primeira fala, retornos, compradores externos e custo. Distinga drafts, eventos e pessoas únicas. Identifique a ação autorizada mais próxima de dinheiro/usuários reais e execute; se a decisão exigir aprovação, prepare o material e uma pergunta pontual. Não invente leads.”

### Radar competitivo e tendências (periodicidade semanal, custo controlado)

“Inspecione fontes atuais de concorrentes relevantes ao mesmo job do usuário e tendências emergentes de aprendizagem, canais e comportamento do ICP. Apresente apenas mudanças novas, datadas, com mecanismo de impacto para o BataTalk e recomendação TESTAR / OBSERVAR / IGNORAR. Nada de listas de notícias ou copiar tendências sem encaixe.”

### Radar da competência executiva (periodicidade vinculada a falhas reais)

“Revise uma decisão importante recente e seu resultado: o que eu supus? o que aprendi? o que faltou estudar? que ferramenta, skill ou modelo falhou? Tome uma melhoria pequena e testável do sistema de execução se o desvio se repetir. Se nenhuma falha nova relevante, não gerar arquivo.”

### Radar de ferramentas e quotas (após mudança de modelo/conta, ou revisão periódica)

“Confirme pelos metadados do OpenBot quais agentes, modelos, skills, provedores e quotas realmente são visíveis; compare custo por entrega verificada e fila. Identifique capacidade nova ou gargalo. Nunca ler tokens/chaves, fingir quota que o runtime não mostra nem perguntar ao fundador uma informação já disponível.”

### Condições de notificação

Informe o fundador se houver P0, risco financeiro/material, decisão estratégica a aprovar, oportunidade com urgência genuína ou resultado externo importante **com evidência**. Para todo o resto, atualize estado e encerre silenciosamente. Sensores quebrados ou sem permissão não podem informar “tudo OK”; devem gerar registro privado `SEM_ACESSO` e pedido específico quando houver relevância.

## Alarme imediato por eventos reais

P0 de segurança, cobrança, custo e falha de prática deve idealmente vir de monitoramento/alerta técnico ou webhook autorizado, **não** de routine que olha periodicamente uma página. A rotina pode ler/triagem do sinal, mas a ação crítica requer infraestrutura confiável e política de aprovação.

## Calibragem

O CEO pode propor ou configurar quantas rotinas internas forem úteis dentro da alçada e recursos autorizados; ajuste cadência por necessidade real, sem quota. Não force pesquisas desnecessárias. Meça tokens, filas, tempo de revisão e notificações; desative gatilhos sem valor. Desabilite qualquer rotina que produza alertas sem novidade ou acionamentos duplicados.

## Rotinas como sensores e entrada para orquestração

Uma rotina útil observa **delta verificável**: falhas recém-abertas, entregas recebidas, dependências bloqueadas, PRs preparados ou custos fora do padrão. Se houver evento real, o CEO escolhe topologia e cria contrato de missão; se não, fecha o ciclo sem nova tarefa. **Rotina não é motor DAG, transação nem escalonador de dependências**. Consulte `references/28-openbot-playbook-operacional.md`.

## Regra anti-duplicação para todas as rotinas

Cada acionamento lê o registro de tarefas ou ledger e as filas, compara fingerprint/problema/artefato, confere se a ação anterior concluiu e verifica se há evento novo. Se a execução anterior tem resultado incerto, **consultar estado antes de tentar novamente**. Se nada mudou, encerrar sem abrir tarefa, daily nem notificação. Rotinas agendadas não garantem exactly-once dos efeitos. Rotinas webhook podem deduplicar IDs de entrega, mas o CEO deve conferir estado externo antes de repetir operações. Nada substitui um monitor de incidentes.
