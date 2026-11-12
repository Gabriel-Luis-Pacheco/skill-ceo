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
