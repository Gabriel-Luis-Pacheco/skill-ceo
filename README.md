# BataTalk CEO Operator

**Skill de direção executiva proativa para OpenBot.** O CEO audita o BataTalk sem esperar ordens, investiga problemas, compara mercado, organiza subagentes, eleva a qualidade de produto, marketing e aprendizagem, e exige melhorias verificadas que sustentem receita e margem.

A skill **não é um aplicativo executável**, não cria agentes ou rotinas sozinha e não substitui acesso real, revisão independente, configurações de segurança ou autorização humana para decisões sensíveis.

## O diferencial

- **Iniciativa real:** detectar LP genérica, experiência de fala fraca, SEO/GEO sem prova, falhas no funil, margens negativas, lacunas organizacionais e AI slop antes do fundador.
- **Autonomia estrutural:** o CEO decide quantidade de agentes, líderes, subequipes, profundidade da hierarquia e paralelismo conforme custo-benefício e recursos delegados; **nenhum teto numérico arbitrário**.
- **Execução verificável:** decisão, DRI, artefato, revisão, custo, evidência, medição, aprendizado ou descarte. Nunca tomar “feito” como evidência.
- **Empresa que aprende:** pesquisa profunda e contra-argumentos, versões testadas de prompts/skills, melhoria contínua dos especialistas e memória entre ciclos.
- **Negócio sustentável:** trabalhar aquisição → primeira prática útil → retorno → assinatura → contribuição após voz, IA, taxas e parcerias, sem inventar métricas.

## Onde começar

| Arquivo | Para que serve |
|---|---|
| [SKILL.md](SKILL.md) | Núcleo operacional que o CEO deve consultar |
| [AUDIT.md](AUDIT.md) | Auditoria crítica, correções e limitações verificadas |
| [CEO_SYSTEM_PROMPT.md](CEO_SYSTEM_PROMPT.md) | Texto curto para instruções persistentes do CEO |
| [POLICY.md](POLICY.md) | **Fonte única** de limites financeiros, segurança e autorização |
| [INSTALL.md](INSTALL.md) | Instalação pelo repositório e verificação de versão no OpenBot |
| [setup/CEO-first-message.md](setup/CEO-first-message.md) | Auditoria inicial com fatos e ações seguras |
| [setup/routines.md](setup/routines.md) | Sugestões de gatilhos, eventos e cadência |
| [references/21-organizacao-autonoma.md](references/21-organizacao-autonoma.md) | Delegação e gestão de agentes, líderes e departamentos sem cotas |
| [tests/CEO-BEHAVIOR-EVALS.md](tests/CEO-BEHAVIOR-EVALS.md) | Cenários e rubricas de julgamento executivo |

Há procedimentos temáticos em [references/](references/) e modelos reutilizáveis em [templates/](templates/). Carregue somente o guia relevante, em vez de anexar todos os documentos a cada turno.

## Instalação

O repositório do GitHub é a **fonte**; a cópia instalada da skill na biblioteca do OpenBot pode ser independente. Veja [INSTALL.md](INSTALL.md) para registrar e ativar a skill no CEO, colar o prompt persistente e confirmar que a revisão correta está ativa. **Clonar a pasta não garante instalação no agente, e atualizar o GitHub não atualiza a skill já instalada.** Consulte o funcionamento de *Local skills* na [documentação oficial do OpenBot](https://github.com/nightly-labs/openbot).

## Limites reais, não obstáculos inventados

A responsabilidade de gerir quantos agentes de IA forem necessários pertence ao CEO; ele pode formar hierarquias e desativar recursos sem valor. A alçada não inclui gastos fora de orçamento, acesso novo a dados/segredos, publicação não autorizada, cobrança ou intervenções críticas em produção. O **Reels Creator permanece pausado**.

O OpenBot em determinadas versões de desenvolvimento pode operar com acesso amplo e sem confirmações individuais. Para operação comercial, use permissões mínimas, backups, monitoramento de custo, proteção de branch e aprovação técnica fora do prompt. Consulte também a [licença do OpenBot](https://github.com/nightly-labs/openbot), que diferencia versões antigas e uso comercial.

## Qualidade e testes

Execute `python scripts/validate_skill.py` e `python -m unittest discover -s tests -p 'test_*.py'` para integridade e testes dos utilitários. O conjunto inclui 30 cenários executivos, 16 de autonomia organizacional e 11 casos críticos de fumaça (subconjunto dos 30). Depois de **avaliar de verdade** o CEO no OpenBot, use `python scripts/score_evaluations.py caminho/avaliacoes.jsonl` para agregar notas humanas com evidências. Os cenários do CEO em `tests/` **precisam ser executados separadamente no OpenBot, em ambiente controlado**: CI aprovado não significa que o CEO executou uma tarefa real, nem demonstra aumento de receita.

Origens e limites dos princípios de gestão, plataformas, SEO e produto estão em [references/10-fontes.md](references/10-fontes.md). Nenhuma empresa ou fundador citado endossa a skill.
