# OpenAI Codex — adaptador opcional

**Núcleo comum:** o mesmo `SKILL.md` e mesmas referências usadas nos demais ambientes. O Codex pode ser especialista de implementação ou o próprio CEO em uma sessão com acesso adequado.

## Carregamento

A documentação de skills no Codex usa pasta de skill com `SKILL.md` e recursos associados, em diretórios `.agents/skills/` quando suportados. Conferir se o harness (CLI, app, nuvem, integração) efetivamente descobre e lê a skill; não tratar o arquivo `AGENTS.md` como substituto da biblioteca de referências. Repositório atualizado não é automaticamente configuração ativa em todas as sessões.

## Contrato de execução

- Inspecionar estado real do repo, histórico, logs de testes, CI e branch. Não anunciar deploy por PR.
- Usar modelos/ferramentas reais, sem supor acesso ao banco, Search Console ou Gmail.
- Se for CEO, considerar empresa e cliente **antes de editar código**: maior restrição de receita, risco, produto/retorno, distribuição e efeito esperado.
- Aplicar testes de comportamento quando disponíveis; o cenário pode exigir navegador/dados ou revisão humana, não apenas teste de unit de software.
- Para missões longas, checkpoint no workspace com evidência/decisão/next trigger. Não afirmar execução persistente sem processo real.

Fontes: https://developers.openai.com/api/docs/guides/tools-skills ; https://developers.openai.com/blog/eval-skills
