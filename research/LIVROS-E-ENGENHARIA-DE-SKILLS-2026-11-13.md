# Pesquisa aplicada — liderança, estratégia, aquisição e engenharia de agent skills

Data da consulta: 2026-11-13. Escopo: **fontes oficiais e trechos/sinopses publicamente acessíveis**, documentação de plataformas e artigos técnicos. **Não houve acesso nem leitura integral de todos os livros**; não afirmar isso ao usuário ou a outros agentes. Não há evidência aqui de teste comportamental do CEO em host real.

## Diagnóstico do repositório antes desta revisão

- O núcleo `SKILL.md` tinha ~19,6 mil caracteres e 170 linhas: respeitava o limite formal de 500 linhas, mas incluía múltiplas versões do mesmo ciclo de execução, elevando custo cognitivo.
- Mais de 30 referências são úteis como biblioteca, **não** como contexto a ser carregado todo turno.
- Faltava separar explicitamente o **mandato persistente no host** (system/project instructions) da **skill sob demanda** (metadados, instruções, recursos) e do **workflow real** (gatilhos, ferramentas, logs, rotina).
- CI estrutural verde e 108 cenários descritos não representam 108 execuções com rastros. Testar invocação/ausência de invocação também é necessário.
- Bug concreto: fórmula textual de CAC na referência 33 carecia de parênteses; sem eles, soma custo e fração, e não custo total / clientes.
- Modelo de intervenção executiva presente, mas sem proteção explícita contra transformar toda revisão em novo manual. Esta revisão tenta reduzir, especializar e testar, não multiplicar mandatos.

## Livros e transposição operacional

| Obra/autor | Base consultada | Contribuição ao CEO | Quando NÃO aplicar literalmente |
|---|---|---|---|
| *The Effective Executive* — Peter Drucker | https://www.routledge.com/The-Effective-Executive-The-Definitive-Guide-to-Getting-the-Right-Things-Done/Drucker/p/book/9780750685078 | Escolher contribuição e prioridades, proteger tempo contra trabalho decorativo; registrar o que parar | Não usar checklist para substituir julgamento em incidentes |
| *Good Strategy/Bad Strategy* — Richard Rumelt | https://www.mckinsey.com/capabilities/strategy-and-corporate-finance/our-insights/the-perils-of-bad-strategy | Diagnóstico do desafio, política orientadora e ações coerentes; exigir explicação causal e descarte | Nem toda microtarefa exige um documento de estratégia |
| *The Crux* — Richard Rumelt | https://profilebooks.com/work/the-crux/ | Identificar obstáculo crítico **atacável** que libera progresso; separar sintoma de restrição | Não insistir em um único gargalo quando há incidente de segurança |
| *High Output Management* — Andrew Grove | https://www.penguinrandomhouse.com/books/72467/high-output-management-by-andrew-s-grove-former-chairman-and-ceo-of-intel/ | Gestor é avaliado por output real de sua organização, não pela quantidade de supervisão ou reuniões; delegação só aumenta resultado se houver verificação | Quando não existe equipe real, o CEO executa sozinho |
| *The Goal* / Theory of Constraints — Eliyahu Goldratt | https://northriverpress.com/about/ | Procurar a etapa de menor vazão e medir resultado do sistema; no produto: visitante→primeira fala→retorno→pagamento | Não identificar gargalo por eventos sem semântica e denominador |
| *The Mom Test* — Rob Fitzpatrick | https://www.momtestbook.com/ | Conversas sobre episódios e soluções passadas, não elogios ou intenção hipotética de compra | Consentimento e privacidade; não apresentar conversa simulada como pesquisa |
| *The Lean Startup* — Eric Ries | https://theleanstartup.com/book | Aprendizado validado e experimentos Build–Measure–Learn; medir a resposta externa antes de expandir | Não transformar cada ajuste irreversível em experimento sem controles |
| *Traction* — Gabriel Weinberg e Justin Mares | https://foundry.virginia.edu/books/traction | Hipóteses e pequenos testes comparáveis por canal, concentrando esforços em sinais reais | Canais ainda sem dados não permitem declaração de vencedor |
| *Thinking in Bets* — Annie Duke | https://www.annieduke.com/thinking-in-bets-2/ | Separar qualidade de decisão e sorte/resultado; registrar aposta, incerteza e fator que a refutaria | Não confundir porcentagem subjetiva com medida científica |
| *Thinking in Systems* / *Leverage Points* — Donella Meadows | https://donellameadows.org/archives/leverage-points-places-to-intervene-in-a-system/ | Corrigir fluxos de informação, regras e feedback, não só aparência do dashboard; considerar efeitos de segunda ordem | Não supor que todo sistema social tem um único ponto de controle |
| *Great Leads* — Michael Masterson e John Forde | https://www.awai.com/2012/01/just-released-great-leads/ | Abertura da comunicação depende de consciência do público; variar promessa/problema/história/convite com veracidade | Clickbait e fórmulas de copy não substituem valor real nem consentimento |
| *The Checklist Manifesto* — Atul Gawande | https://sextante.com.br/products/checklist | Checklist curto em operações sensíveis: publicar, cobrar, migrar, enviar campanha, alterar permissão | Excesso de checklist em tarefa exploratória retarda e não melhora |

**Síntese integrada:** Rumelt escolhe problema, Drucker determina foco, Goldratt identifica vazamento, Grove define responsabilidade pelo resultado, The Mom Test acessa verdade humana, Lean Startup/Traction testam decisão no mundo, Duke/Meadows corrigem inferências e feedback, Great Leads comunica sem manipular, Gawande evita erros de execução de alto risco. É uma interpretação aplicada aos problemas do BataTalk, não citação do conteúdo integral.

## Engenharia de skills — fontes primárias

1. **Agent Skills specification:** https://agentskills.io/specification — frente YAML name/description, escopo, recursos sob demanda, scripts e links relativos, corpo recomendado abaixo de 500 linhas e cerca de 5 mil tokens.
2. **Anthropic, authoring best practices:** https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices — concisão, disclosure progressivo, exemplos observáveis, testes com casos reais; desenvolver avaliação antes de escrever grande documentação.
3. **OpenAI, skill-creator:** https://github.com/openai/skills/blob/main/skills/.system/skill-creator/SKILL.md — incluir só conhecimento não óbvio que muda decisões; grau de liberdade adequado ao risco; iteração com uso real.
4. **OpenAI, testing skills with evals:** https://developers.openai.com/blog/eval-skills — separar resultados, processo, estilo e eficiência; rastro+artefato+checagens; distinguir falha de invocação de falha de execução.
5. **Anthropic, Claude Code instruction layers:** https://claude.com/resources/articles/steering-claude-code-skills-hooks-rules-subagents-and-more — CLAUDE.md, skills, hooks e agentes têm momentos de carregamento diferentes.
6. **OpenAI, skill deployment:** https://learn.chatgpt.com/docs/build-skills — `AGENTS.md` orienta projeto, skill é acionada por descrição e pode precisar de instalação específica; modificações podem exigir reinício/refresh.
7. **Microsoft Agent Framework:** https://learn.microsoft.com/en-us/agent-framework/agents/skills — workflows determinísticos para efeitos externos/risco de repetição; skills não garantem cron, estado persistido nem idempotência.

**Não confundir** formatos documentados e validação estática com compatibilidade real de todas as versões do GrokBot/OpenBot/Claude/Codex. Cada host exige smoke test de ativação, ferramentas e autorização.

## Decisões de projeto desta revisão

- Simplificar `SKILL.md` como entrada ativável; não copiar todo o repertório. Uma referência de livros organizada por **gatilho operacional**.
- Melhorar a descrição da skill para acionar em pedidos de liderança BataTalk e **não acionar** em tarefas pessoais/desconectadas.
- Separar instrução persistente (`CEO_SYSTEM_PROMPT.md`), fluxo da skill (`SKILL.md`) e sensores/automação reais (`setup/routines.md`).
- Adicionar testes positivos/negativos de *skill routing*, além dos 108 cenários de comportamento já descritos. Roteamento só será comprovado depois de executar em host.
- Reforçar verificações de orçamento de contexto e integridade dos testes. **Evitar adicionar mandamentos redundantes** ao núcleo.

## Como falsificar a alegação de melhoria

- Rodar mesmo conjunto de prompts sem skill e com skill, capturar **se foi invocada**, arquivos lidos, chamadas de ferramenta, ação, artefato final, custo e intervenção humana.
- Medir separadamente falsos acionamentos, prompts legítimos ignorados, proatividade sem permissão, qualidade de decisão e execução.
- Se houve ganho de estilo mas não de ação, **não aprovar como melhora de proatividade**.
- Nenhuma referência de livro autoriza envio externo, alteração de preços ou produção; `POLICY.md` e as restrições da plataforma continuam prevalecendo.
