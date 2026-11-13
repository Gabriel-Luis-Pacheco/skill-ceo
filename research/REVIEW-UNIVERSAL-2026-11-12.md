# Revisão executiva independente de software — 12/11/2026

## Missão original preservada

O fundador pediu um CEO que **descubra problemas e oportunidades antes dele**, faça perguntas inteligentes sobre todas as IAs disponíveis e suas quotas, conheça profundamente negócios, psicologia, produto, marketing, vendas, SEO/GEO, concorrentes, tendências e design, construa uma empresa competitiva, aprenda, execute, gere primeiros clientes e tome iniciativa em etapas. **Não quer uma IA apenas organizando outros bots nem uma skill condicionada ao OpenBot.**

Esta revisão é um exemplo deliberado de **aplicar a skill para melhorar a própria skill**. Foi executada no ambiente de ChatGPT com ferramentas GitHub conectadas. O ambiente atual **não** representa execução real do CEO nos aplicativos citados; a avaliação de campo permanece pendente.

## Diagnóstico observado antes do patch

Inspeção do branch `intervencao-tracao-humana-2026-11-12`:
- `README.md` apresentava o produto como “Skill de direção executiva proativa para OpenBot” e dependia de biblioteca OpenBot como única instalação;
- `INSTALL.md` só ensinava instalação e update no OpenBot;
- `CEO_SYSTEM_PROMPT.md` mandava “dirigir os agentes OpenBot” como identidade básica;
- `SKILL.md` referia canais/filas OpenBot como método e permitia que a orquestração ocupasse o centro;
- testes e guia de validação priorizavam “no OpenBot” em vez de capacidade universal;
- havia **bastante conhecimento temático** e bons limites de alçada, mas o núcleo não especificava claramente como manter qualidade de CEO sem ferramentas ou com um único modelo.

**Falha de produto da própria skill:** o fundador pediu *competência executiva autônoma e portável*; a entrega estava excessivamente configurada como *manual de um orquestrador*. O erro não se corrige só adicionando “funciona também no GrokBot” ao título.

## Contrafactual e decisão

**Alternativa A: quatro cópias completas de skill** (GrokBot, Claude Code, Codex, OpenBot). Rejeitada: divergência de objetivo, conhecimento e política, manutenção cara, regressões difíceis de comparar.

**Alternativa B: mesmo SKILL.md com uma linha “é multiplataforma”.** Rejeitada: instalação, memória, testes e rotina continuariam presumindo runtime único; manteria falha de causa.

**Alternativa C (escolhida): um núcleo universal + referências especializadas + adaptadores opcionais + validação entre modos M0/M1/M2.** A mesma inteligência decide o que fazer, mas cada host executa dentro de sua capacidade e autorização. Escolhida por redução de divergência e teste mais claro.

## Pesquisa de base que realmente influenciou a escolha

- **Anthropic, Building Effective Agents (19/12/2024)**: agentes e workflows são diferentes; soluções simples e componíveis frequentemente entregam mais valor que orchestration complexa. Impacto: não exigir 14 agentes ou um SDK para pensar como CEO. https://www.anthropic.com/research/building-effective-agents
- **OpenAI, Testing Agent Skills Systematically with Evals (22/01/2026)**: testar comportamento, seleção de skill, regressões e efeitos, não somente o texto. Impacto: adicionar casos estruturados de portabilidade e exigir testes em ambientes reais. https://developers.openai.com/blog/eval-skills
- **Google, A Survey on Agent Skills (2026)**: skills como conhecimento processual modular externo, com discovery, execução, avaliação, memória e segurança. Impacto: núcleo pequeno, referências on demand e adaptadores separados. https://research.google/pubs/a-survey-on-agent-skills-externalized-procedural-knowledge-in-language-models/
- **Anthropic, Agent Skills overview**: diretórios `SKILL.md` e recursos progressivos, com formatos de instalação dependentes do produto. https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
- **OpenAI Skills docs**: suporte ao padrão de skills; diferenças de descoberta e instalação por ferramenta. https://developers.openai.com/api/docs/guides/tools-skills
- **Grok Bot, Skills and routines**: skills e rotinas próprias do Bot; verificar conexão real e revisão instalada. https://docs.x.ai/grok-bot/skills-routines-and-automations
- **OpenAI, Building agents**: instructions + guardrails + tools, com limites de ação e necessidade de acesso. https://developers.openai.com/tracks/building-agents

Nenhum desses documentos prova que nossa skill gerou receita. Não alegar ter lido 200 biografias ou estudos não consultados.

## Ações executadas neste branch

- Reescrito `SKILL.md` como **CEO OS universal**, com foco em valor humano, estratégia, economia, percepção, iniciativa e execução.
- Reescrito `CEO_SYSTEM_PROMPT.md` de forma neutra entre provedores.
- Criado `references/32-contrato-universal-multiplataforma.md`, com camadas A–D e M0/M1/M2, fallback e checkpoint.
- Criado `references/33-julgamento-executivo-competencias-e-aprendizado.md`, com prática decisória de estratégia, finanças, posicionamento, growth, produto, psicologia humana, pesquisa, liderança e risco.
- Criados `adapters/README.md`, `generic.md`, `grokbot.md`, `claude-code.md`, `codex.md`, `openbot.md`. Adaptadores não reescrevem identidade.
- Atualizados `README.md`, `INSTALL.md`, `AGENTS.md`, `setup/CEO-bootstrap-situacional.md`, `setup/CEO-first-message.md`, `setup/routines.md`.
- Atualizado `POLICY.md` somente para linguagem neutra de runtime, **sem ampliar alçadas**. A decisão do Reels Creator pausado permanece.
- Criados `tests/portability-24-scenarios.jsonl` e `tests/PORTABILITY-TEST-PLAN.md`; expandido `scripts/validate_skill.py` para verificar presença e formato dos novos casos e ausência de frases de dependência de host no núcleo.
- Preservados estudos e guias válidos anteriores; referências antigas específicas ao OpenBot foram enquadradas como **adaptador opcional**, não condição de uso.

## Estado de verificação e próximo movimento

- **Executado:** inspeção do repositório por ferramenta, análise causal, comparação de alternativas, pesquisa de fontes, modificações reais no branch, leitura de volta/validação estática.
- **Não executado ainda:** instalação da skill nos hosts do fundador; invocação real da skill em GrokBot, Claude Code, Codex e OpenBot; benchmark de comportamento; medição de usuários/receita causada por esta revisão.
- **Risco:** normas em referências antigas ainda podem conter exemplos OpenBot; devem ser tratadas como referência específica e receber limpeza gradual somente se bloquearem entendimento. Evitar remover documentação útil para parecer neutro.
- **Critério de sucesso posterior:** mesmo cenário empresarial com julgamento estratégico equivalente em pelo menos dois ambientes, ação proporcional a cada capacidade, nenhuma invenção de acesso/permissão, menos retrabalho e mais primeiros resultados com usuários reais.

**Aprendizado acumulado:** autonomia executiva não é um número de agentes nem uma personalidade confiante. Ela resulta de percepção do mundo com fonte, conhecimento empresarial integrado, capacidade de decidir e agir, honestidade sobre ferramentas, validação e memória útil. **A portabilidade é um requisito de arquitetura, não só compatibilidade de Markdown.**

---

## Segunda revisão adversarial no mesmo dia — CEO usa a skill na própria empresa

**Missão reafirmada:** o fundador pediu estudo profundo de conversas sobre PLG/self-service/inbound/outbound/enterprise, urgência de receita, conhecimento, personalidade executiva, design humano, concorrentes, antecipação, modelos e continuidade em GrokBot/Claude/Codex/OpenBot. O trabalho anterior estava tecnicamente bom, mas podia apenas gerar mais instruções sem clientes.

### Ato de diagnóstico em produção, não ficção

Consulta agregada e somente leitura ao Supabase produtivo em 12/11/2026. Janela desde **08/11/2026 00:00 UTC-03**:
- 119 eventos `landing_view`; 14 `onboarding_started`;
- 3 `onboarding_voice_attempt` e 3 `onboarding_feedback_shown`;
- 0 novos registros em `voice_sessions.started_at` e 0 novas faturas em `paid_subscription_invoices.paid_at`;
- último `voice_sessions.started_at` histórico observado: **08/11/2026 00:16 UTC** (07/11 no fuso de Brasília).
- Não inferir 119 visitantes únicos, zero fala real, inexistência de procura, penalização SEO ou causalidade comercial sem verificar identidade, eventos e origem do dado.

**Hipóteses rivais:** voz do onboarding/demo não persiste como sessão regular; fricção/erro de microfone ou produto; emissor/destino diferente; QA/bot/baixa qualificação. O agente deve investigar **significado do evento e fluxo real** antes de otimizar SEO ou declarar taxa. Foi criado issue de trabalho real, **não deploy**: https://github.com/Gabriel-Luis-Pacheco/BataTalk/issues/18 (reprodução em staging, emissores, semântica de primeira voz, provas e métricas).

### Inteligência de mercado: encontrar mecanismo, não clonar layout

Consulta pública datada de **12/11/2026**:
- `gliglish.com` anuncia prática grátis sem cadastro, plano gratuito limitado em 10 minutos/dia e recursos de fala/feedback — hipótese: primeiro valor e uso recorrente de baixo atrito. **Isso não prova desempenho do concorrente**.
- `speak.com` apresenta **Learn → Practice → Apply** com CTA gratuito e trial de 7 dias — hipótese: progressão de valor compreensível e demonstrável.
- `Praktika` confirma em help center de 01/09/2026 versão gratuita com 3 avatares e prática limitada — hipótese: o usuário percebe valor antes de upgrade.
- Duolingo (10-K 2025 e resultados 26/02/2026) enfatiza o modelo gratuito, ensino e recomendação; **não copiar estratégias de escala sem base de usuários**.

**Decisão:** o CEO deve diferenciar self-service (experiência) de PLG (mecanismo), inbound/outbound (descoberta), e vendas enterprise (economia). Não existe limiar universal de R$500; não criar SDR/BDR/closer para ticket B2C sem ACV/margem/ciclo.

### Falhas adicionais identificadas na skill e correções aplicadas

| Falha | Correção | Prova de artefato |
|---|---|---|
| Ideias de CEO sem diagnóstico de causa e sem alternativa real | Núcleo `SKILL.md`, seções 4.1–4.2: hipótese, contraditório, sinal discriminatório, ação, evidência, limite de meta-trabalho | Diff no branch, leitura de volta |
| Reel inbound vs outbound tratado como dicotomia | `SKILL.md` 7.1 e `references/30-mercado-primeiro-execucao-comercial.md`: matriz por comprador/usuário, primeiro valor, canal, CAC, ACV/margem e estágios | Diff e fontes públicas |
| Sessão de demo/onboarding confundida com voz real | Caso de teste U17 e issue #18; exigir semântica e comparação de fontes | Suite de casos, issue criado |
| 16 casos de portabilidade não cobriam decisões difíceis de negócio | Oito casos adicionais U17–U24, incluindo métricas contraditórias, free/PLG, urgência, jargão humano, meta-trabalho e priorização P0 | `tests/portability-24-scenarios.jsonl`, validator atualizado |
| Prompt persistente redundante com skill | `CEO_SYSTEM_PROMPT.md` simplificado de 5.475 para 2.721 caracteres (**−50%**), núcleo e referências sob demanda | Diff, integridade e CI |
| A própria melhoria da skill poderia virar loop que evita clientes | Núcleo exige separar ganho de método de resultado; próximo passo empresarial deve envolver usuários e valor, não mais documentação | Regra explícita + issue real |

### Evidência de avaliação técnica e limites

Após as modificações, o GitHub Actions passou para o commit `3324ecbdeace7fa078f5bb9494e9e671abdeb099` (https://github.com/Gabriel-Luis-Pacheco/skill-ceo/actions/runs/43290652775), incluindo integridade documental, contratos, testes Python e compilação. **A comparação real do mesmo CEO no GrokBot/Claude/Codex/OpenBot ainda não foi feita.** Um teste estático de casos JSONL **não julga** decisões/modelos.

### Decisão estratégica de encerramento deste ciclo

A próxima evidência valiosa não virá de acrescentar outra enciclopédia à skill. Virá de observar o CEO em contexto real e, no BataTalk, localizar a passagem de primeiro contato para primeira fala útil com pessoas externas. Antes de escalar campanhas, verificar se a experiência prometida efetivamente funciona para uma pessoa fria.

**Estado real:** skill em branch de PR, CI aprovada, issue de ativação criado; **sem merge**, sem instalação comprovada nos runtimes, sem abordagem enviada nesta revisão, sem deploy e sem venda nova comprovada. O CEO deve dizer isso com precisão.
