# Auditoria crítica integral da skill — 06/11/2026

**Escopo:** repositório `Gabriel-Luis-Pacheco/skill-ceo`; foram examinados os 46 arquivos existentes no começo desta revisão, além da documentação pública atual do OpenBot, de padrões de agentes e de fontes sobre SEO, faturamento e ensino de línguas. O trabalho consistiu em revisão textual, refatoração, verificações estáticas e testes unitários dos utilitários. **Não foi executado um CEO real no OpenBot nem foram acessados dados comerciais internos do BataTalk.**

## Diagnóstico e correções

| Gravidade | Falha encontrada | Correção implementada |
|---|---|---|
| Alta | `SKILL.md` extenso, com comandos repetidos e política dispersa pelos guias | Núcleo mais compacto, orientado a observação → decisão → execução → prova, referências por gatilho e `POLICY.md` como fonte normativa |
| Alta | O prompt persistente repetia parte do manual, criando risco de divergência | Prompt curto, com missão, iniciativa, alçada e continuidade alinhadas ao núcleo |
| Alta | Instalação via Git confundida com instalação/atualização de Local Skill | README e INSTALL corrigidos: checkout do GitHub é fonte, instalação e Update da cópia no OpenBot são etapas verificáveis distintas |
| Alta | Exclusão de agentes tratada como reorganização reversível | Verificada a possibilidade de exclusão de workspace/anexos pelo OpenBot; preferência por pausa/arquivo, preservação e aprovação adequada antes de exclusão definitiva |
| Alta | Teste CI superficial podia dar falsa confiança de que a IA era um CEO capaz | Validação de links e estrutura, 46 cenários, testes de regressão do validador e agregador de notas **humanas**, mantendo avaliação real no OpenBot obrigatória |
| Alta | Estado em JSONL sugeria idempotência sem controle transacional | Documentada diferença entre fingerprint, fila/ownership, deduplicação de webhook e idempotência no sistema de destino |
| Média | Limites arbitrários apareciam em textos, templates e testes | Mantida autonomia para dimensionar agentes, hierarquia e frentes; guardrails são custo/risco/alçada reais, não números inventados |
| Média | MRR era chamado de “realizado”, apesar de não ser caixa recebido | MRR contratual mensalizado, pagamentos efetivos, contribuição e churn passam a ter definições separadas e dados auditáveis |
| Média | Guia GEO não considerava orientações oficiais mais recentes | Incluída documentação de 2026 do Google contra atalhos de llms.txt/schema para AI Search e a favor de conteúdo útil e indexável |
| Média | Qualidade da conversação podia ser interpretada como quantidade de tempo ou satisfação | Reforço de objetivos comunicativos, descritores CEFR, avaliação de fala, feedback específico, retenção e progresso mensurável |
| Média | Artefatos de delegação e avaliação não distinguiam alegação, tarefa e prova | Templates agora registram DRI, alçada, fingerprint, artefatos, revisão e evidências independente |

## Revisão adicional de orquestração — 06/11/2026

Pesquisa primária em OpenBot, OpenAI, Anthropic, Microsoft, LangGraph, Temporal, Netflix, YC, Amazon e Google SRE documentada em [research/ORCHESTRATION-RESEARCH-2026.md](research/ORCHESTRATION-RESEARCH-2026.md). Esta revisão acrescentou:

- Um seletor de topologia de execução e a distinção explícita entre organograma e fluxo de trabalho.
- Contratos de tarefa, dependências em DAG, handoffs com ACK, integração e ownership de arquivos/branches.
- Recuperação para timeouts, retry, resultado de ferramenta incerto, bloqueios, fila cheia e falhas parciais.
- Engenharia de contexto normativo/operacional/episódico para reduzir perda de fatos e custo.
- Traces e avaliação multiagente em quatro níveis, mais custo por entrega integrada.
- CEO como capitão de trade-offs e estratégia, com líderes especialistas autônomos.
- Aplicação dos recursos documentados do OpenBot sem fingir que existem APIs de outros SDKs.
- 24 casos novos de avaliação e um validador offline de contratos/DAG com testes unitários.

Nenhuma dessas adições configura sozinha scheduler, engine DAG, ferramentas de produção, observabilidade completa ou orçamento real; exigem implementação/runtime. **Nenhum teste comportamental real do CEO foi executado nesta revisão.**

## Questões que continuam abertas

1. **Autonomia real no OpenBot:** não foi possível confirmar as permissões, rotinas, versões de skills e resultados dos agentes da instalação do usuário. A disponibilidade de ferramentas e comportamento não pode ser garantida por Markdown.
2. **Proteções técnicas:** a documentação pública do OpenBot indica versões de desenvolvimento com acesso amplo e sem confirmação individual; é preciso isolamento do ambiente, credenciais mínimas, backup e orçamento/alertas nos provedores para ações sensíveis.
3. **Teste comportamental:** os cenários são casos de avaliação, **não execuções completas**. É necessário coletar traces, artefatos, resultados e revisão independente antes de afirmar superioridade sobre a versão anterior.
4. **Resultado comercial:** funil, MRR, custos reais de voz, retenção, customer discovery e dados do Search Console não foram auditados nesta revisão. Não há base para afirmar crescimento, rentabilidade ou ganho de ranqueamento.
5. **Desdobramento da skill:** depois de atualizar no GitHub, atualizar a cópia de Local Skill instalada no CEO e verificar a revisão efetivamente carregada.

## Critérios para a próxima evolução

Uma melhoria futura deve surgir de **falha real observada**, ter hipótese, diff, avaliação antes/depois, custo, segurança e decisão de manter/reverter. A skill não deve crescer em número de arquivos apenas para parecer completa. Diante de uma nova necessidade, primeiro procurar se um guia existente pode ser melhorado.

## Referências oficiais conferidas

- OpenBot: https://github.com/nightly-labs/openbot
- OpenAI: https://developers.openai.com/api/docs/guides/agent-evals
- OpenAI — revisão/aprovações de ferramentas: https://developers.openai.com/api/docs/guides/agents/guardrails-approvals
- Anthropic — padrões de agentes: https://www.anthropic.com/research/building-effective-agents
- Google Search Central 2026: https://developers.google.com/search/docs/fundamentals/ai-optimization-guide
- Conselho da Europa — CEFR: https://www.coe.int/en/web/common-european-framework-reference-languages/cefr-descriptors

## Revisão incremental — 08/11/2026

A evolução atual acrescenta conferência de pacotes locais de evidências da instalação real (IDs, arquivos existentes e revisor distinto do agente), comparador de avaliações humanas baseline/candidata, bloqueio de cobertura incompleta por padrão e missão de negócio baseada no funil de aquisição até prática oral, assinatura e margem. O planejador não trata tarefas canceladas/concluídas como proprietárias de recursos ativos, rejeita referências de aprovação em branco e protege a validação contra tipos inválidos. Inconsistências de links e contagens foram corrigidas. Há regressões unitárias novas e CI para o grafo de exemplo.

**Limitações:** checar caminhos de trace não autentica a origem dos arquivos. Não foi executado CEO de verdade no OpenBot nesta alteração, não houve coleta de avaliações reais nem acesso a métricas de clientes; a prova comportamental e comercial está pendente de execução em ambiente autorizado. Não confundir CI aprovado com melhora de negócio.
