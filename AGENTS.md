# Diretrizes para modificar a skill BataTalk CEO OS

Esta skill deve ser usada **enquanto é aperfeiçoada**. Não apenas planejar melhoria: executar análise real, localizar maior falha, comparar alternativas, escolher a correção, gravar, verificar e registrar limite da evidência.

## Compromissos normativos

- **Portabilidade total de pensamento**: o núcleo `SKILL.md` e o mandato `CEO_SYSTEM_PROMPT.md` não podem presumir OpenBot, GrokBot, Claude Code, Codex ou qualquer runtime como dependência. Usar `references/32-contrato-universal-multiplataforma.md` e `adapters/` para detalhes de ambiente.
- **Conteúdo executivo substantivo**: `references/33-julgamento-executivo-competencias-e-aprendizado.md` e os guias temáticos unem estratégia, finanças, psicologia humana, marketing, vendas, aprendizagem, produto, risco, concorrentes e decisão; não trocar conhecimento por listas de jargão.
- **Proatividade demonstrada**: explorar oportunidades não solicitadas, descobrir ferramentas/contas/limites visíveis, estudar o que falta, executar o passo autorizado e verificar. Não substituir execução por “vou pesquisar” ou mais prompts.
- **Segurança imutável**: `POLICY.md` prevalece; nenhuma revisão concede acesso, dinheiro, publicação, contato, pagamento ou reativação do Reels Creator por conta própria.
- **Sem teatro de agentes**: orquestração pode ajudar, mas não é missão; CEO único não inventa times. Em plataforma com time, usar capacidade realmente existente, custo e alçada.
- **Provas**: deixar explícito `NÃO TESTADO`, `PR ABERTO`, `DEPLOY`, `RESULTADO` e avaliações reais. Skills com CI verde não significam CEO inteligente.

## Para cada alteração importante

1. Identificar falha observada e o que a refutaria.
2. Ler apenas as referências necessárias; usar fontes atuais de fora quando valiosas e seguras.
3. Comparar patch mínimo versus revisão estrutural; preservar regras boas.
4. Alterar **uma fonte canônica**; adaptadores não reescrevem o núcleo.
5. Testar sintaxe, links, regressões de segurança, cenários de portabilidade e qualidade executiva.
6. Registrar decisão, diff, evidência, custo/risco, próximos testes no runtime real.
7. Se houver falha persistente, analisar conhecimento/modelo/ambiente/incentivo, não aumentar texto sem critério.

Comandos de CI: `python scripts/validate_skill.py`; `python scripts/validate_work_graph.py templates/orchestration-plan.example.json --ready`; `python -m unittest discover -s tests -p 'test_*.py' -v`. Execução de cenários em plataformas reais requer log e avaliação independente.

**Não existem cotas artificiais** de agentes, equipes ou frentes, mas não devem ser criados sem benefício real. O CEO do BataTalk é a mesma competência, seja no GrokBot, Claude, Codex, OpenBot ou outra ferramenta.

## Engenharia de skill como software testável

- Se mudar `SKILL.md`, preservar orçamento conservador de contexto e carregamento progressivo; remover redundância antes de adicionar instruções. A descrição deve explicitar **quando acionar e quando não acionar**.
- Distinguir 3 camadas: mandato persistente do CEO no host, skill sob demanda, sensores/workflows que executam realmente; texto não cria daemon.
- Usar `scripts/package_skill.py` para distribuir uma pasta chamada `batatalk-ceo-operator` (mesmo nome do frontmatter); verificar manifesto e links. Não tratar clone `skill-ceo` como instalação validada.
- `tests/skill-trigger-evals.jsonl` deve conter casos positivos **e negativos**. Avaliar ativações a partir de traces reais com `scripts/score_skill_routing.py`, nunca por palpites ou cenários escritos.
- Pesquisa dos livros e limitações: `research/LIVROS-E-ENGENHARIA-DE-SKILLS-2026-11-13.md`. Não afirmar leitura integral, receita ou mudança de comportamento não medida.

## Integração executiva de 14/11/2026

A biblioteca 36–45 incorpora pesquisa de CEO/C-suite em módulos consultados por necessidade. Não duplicar o conteúdo no núcleo, não inventar leituras integrais e não inferir que governança de companhia aberta se aplica ao BataTalk. `tests/test_executive_knowledge.py` valida existência, roteamento, catálogo e cenários de competência; avaliações no host continuam necessárias.


## Núcleo de repertório executivo 2026-11-14

A integração da pesquisa de CEO/C-suite usa referências 36–45 com leitura progressiva. Manter catálogos de livros e estudos biográficos **fora** do SKILL.md. Novas alegações precisam de fonte e qualificação do acesso; nunca alegar leitura integral ou efeito empresarial não observado. Antes de alterar esta parte verificar [pesquisa e fontes](research/PESQUISA-CEO-C-SUITE-2026-11-14.md) e [avaliações de campo](tests/ceo-csuite-behavior-cases.md). Crises devem preservar segurança, alçada e comunicação transparente; materiais dos EUA não constituem regra aplicável ao Brasil por padrão.
