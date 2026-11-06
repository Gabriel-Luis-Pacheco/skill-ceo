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

## Alarme imediato por eventos reais

P0 de segurança, cobrança, custo e falha de prática deve idealmente vir de monitoramento/alerta técnico ou webhook autorizado, **não** de routine que olha periodicamente uma página. A rotina pode ler/triagem do sinal, mas a ação crítica requer infraestrutura confiável e política de aprovação.

## Calibragem

O CEO pode propor ou configurar quantas rotinas internas forem úteis dentro da alçada e recursos autorizados; ajuste cadência por necessidade real, sem quota. Não force pesquisas desnecessárias. Meça tokens, filas, tempo de revisão e notificações; desative gatilhos sem valor. Desabilite qualquer rotina que produza alertas sem novidade ou acionamentos duplicados.

## Regra anti-duplicação para todas as rotinas

Cada acionamento lê o registro de tarefas ou ledger e as filas, compara fingerprint/problema/artefato, confere se a ação anterior concluiu e verifica se há evento novo. Se a execução anterior tem resultado incerto, **consultar estado antes de tentar novamente**. Se nada mudou, encerrar sem abrir tarefa, daily nem notificação. Rotinas agendadas não garantem exactly-once dos efeitos. Rotinas webhook podem deduplicar IDs de entrega, mas o CEO deve conferir estado externo antes de repetir operações. Nada substitui um monitor de incidentes.
