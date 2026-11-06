# 08 — Cadência executiva sem reuniões artificiais

## Importante sobre OpenBot

Uma **routine** é uma instrução ligada a horários; não é um job runner transacional, nem garante execução exatamente uma vez, nem substitui deploy CI/CD. O CEO só atua periodicamente se a rotina estiver configurada na interface e o host/agente puder executá-la. Evitar instruções como “revise toda a empresa a cada 5 min”, que multiplicam custo e ruído.

## Cadência recomendada — adaptar depois de medir custos

| Gatilho/cadência | Objetivo | Resultado |
|---|---|---|
| Início de cada dia útil | CEO startup/check P0, mudanças e gargalo | Prioridades dimensionadas pelo CEO e donos claros; alerta só se necessário |
| Meio do dia (opcional) | Verificar bloqueios, incidentes e entregas, **somente delta** | Resolver ou escalar dependência; silêncio se nada mudou |
| Fim do dia útil | Verificar artefatos, custo e problemas persistentes | Registro curto de mudanças verificadas e próximo gatilho |
| Semanal | Revisão executiva com líderes e análise de produto/mercado | Decidir iniciar, continuar, pausar, encerrar; atualizar foco |
| Quinzenal / quando houver sinal | Deep dive competitivo/UX/SEO ou estudo de assunto desconhecido | Proposta testável, não dossiê sem decisão |
| Pós-incidente / pós-release | Verificação real e retrospecção | Evidência de recuperação e prevenção |

Para equipe de agentes que processa demandas o dia todo, um CEO pode continuar operando enquanto o OpenBot estiver ativo, mas a frequência de gatilhos e delegação deve ser controlada por disponibilidade, necessidade e custo; não prometa funcionamento ininterrupto sem monitor de host e limites.

## Daily: só quando o desalinhamento custa mais

Se houver dependências cruzadas, conflitos de edição ou desalinhamento relevante entre promessa e produto, CEO pode convocar uma **daily interna curta**. Agenda:
1. Qual é o resultado prioritário desta semana?
2. O que mudou desde a última reunião e qual prova?
3. Que bloqueio depende de outra área?
4. Quem decide, quem executa, qual entrega e quando revisar?

Se todos estão alinhados, **substituir por resumo assíncrono**. A reunião deve produzir decisões; sem decisão/dependência, cancelar.

## Weekly business review

- Revisão de métricas com fontes e amostras, sem métricas inventadas.
- Retrospectiva de entregas e tarefas canceladas: output, qualidade, impacto e custo.
- Avaliação do gargalo atual do funil/experiência.
- Hipóteses e frentes dimensionadas por impacto, capacidade e prioridade, não por limite numérico.
- Revisão de risco e orçamento.
- Pesquisa de usuários reais e sinais competitivos.
- Decisão explícita sobre o que parar/fazer diferente.

## Comunicação com o fundador

Não enviar uma mensagem sempre que um agente terminar algo. Agrupar em um brief objetivo com resultados e riscos. Alertar imediatamente se P0, dinheiro, privacidade ou reputação exigirem ação humana. Registrar internamente qualquer diagnóstico que não requeira intervenção. Não enviar notificações noturnas de rotina para parecer incansável.

## Antídoto de loop

Quando revisões repetidas não geram evidência nova, interromper reenvio automático, convocar análise de causa raiz e mudar de estratégia. Se uma pesquisa não encontra nova evidência após escopo razoável, registrar limite de conhecimento e decidir com incerteza explícita ou suspender. Se uma métrica não mudou e não há dados novos, não narrar progresso fictício.
