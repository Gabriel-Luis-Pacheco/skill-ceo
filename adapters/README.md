# Adaptadores: interface com o mundo, não identidade da skill

**O núcleo está em [../SKILL.md](../SKILL.md).** Os arquivos aqui são opcionais e apresentam procedimentos para descobrir e utilizar recursos de ferramentas. Nunca modificar missão, critérios de prova, valor humano, comportamento comercial nem alçada por causa do ambiente.

## Escolha e uso

1. Descubra qual software/versão hospeda o agente e **quais ferramentas ele realmente expõe**, sem adivinhar API.
2. Leia o adaptador pertinente **se existir**, senão [generic.md](generic.md). Pode combinar dois adaptadores para trabalho que usa Claude Code em repositório + GrokBot para pesquisa, mas **um DRI** continua responsável.
3. Confirme o caminho real de instalação de skill, qual revisão está carregada e se há acesso a `references/`.
4. Escolha o melhor modo de execução M0/M1/M2 conforme [../references/32-contrato-universal-multiplataforma.md](../references/32-contrato-universal-multiplataforma.md).
5. Antes de ação externa, cheque [../POLICY.md](../POLICY.md) e autorização no contexto atual. Instalação ou token não são consentimento.

## Adaptadores disponíveis

- [grokbot.md](grokbot.md) — Grok Bot/GrokBot com skills e rotinas, se habilitadas.
- [claude-code.md](claude-code.md) — Claude Code, ambiente de desenvolvimento com skills locais.
- [codex.md](codex.md) — OpenAI Codex, skills e ferramentas conforme harness.
- [openbot.md](openbot.md) — OpenBot, filas, canais, agentes e rotinas quando disponíveis.
- [generic.md](generic.md) — qualquer IA, ambiente só-chat ou sistema desconhecido.

**Não existe requisito de instalar OpenBot.** O design do produto, a estratégia de marketing, conhecimento empresarial e decisões não ficam nesses adaptadores.

Fontes de padrões portáteis: https://agentskills.io ; https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview ; https://developers.openai.com/api/docs/guides/tools-skills ; https://docs.x.ai/grok-bot/skills-routines-and-automations .
