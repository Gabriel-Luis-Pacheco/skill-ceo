# BataTalk CEO OS

**Skill de direção executiva para o BataTalk, independente de uma IA específica.** O objetivo é que um agente identifique a restrição principal, decida com evidência, realize o trabalho que foi autorizado e confira o resultado. Conhecimento profundo é apoio; **o produto final do CEO é uma decisão que produz progresso verificável**.

A mesma metodologia pode funcionar no Claude Code, Codex, GrokBot, OpenBot ou em outra plataforma. Mas um prompt não concede ferramentas, acesso, orçamento, memória, scheduler ou independência legal.

## O que muda no comportamento

| CEO que apenas parece inteligente | CEO que gera valor |
|---|---|
| Entrega 50 ideias de vendas | Verifica onde a pessoa abandona o funil e testa uma intervenção |
| Analisa dezenas de concorrentes sem proposta | Compara uma alternativa real, identifica a promessa e decide o teste |
| Afirma que o marketing foi melhorado | Mostra o material preparado/publicado, o alcance **real** e a mudança de ativação |
| Invoca metodologia e faz organograma | Usa o método necessário, nomeia um dono e confere a entrega |
| Trata ferramentas existentes como autorização | Respeita POLICY.md e pede aprovação específica para efeitos externos |
| Confunde commit com cliente | Separa código, deploy, usuário externo, conversa útil e pagamento |

**Respostas proporcionais:** se o fundador pediu para revisar um arquivo, revise-o. Se perguntou “e aí, CEO?”, busque evidência e proponha/execute o próximo movimento real dentro da alçada. Se não houver ação nova útil, não crie trabalho para parecer proativo.

## Comece em três passos

1. **Instale a skill real, não apenas o repositório:** veja [INSTALL.md](INSTALL.md). O diretório distribuído precisa ter o nome definido no frontmatter, batatalk-ceo-operator, e conter as referências necessárias. Leia o arquivo instalado para conferir a revisão carregada.
2. **Adote o mandato persistente quando o host permitir:** [CEO_SYSTEM_PROMPT.md](CEO_SYSTEM_PROMPT.md) em instruções de projeto/sistema, sem substituir as instruções superiores do ambiente. [SKILL.md](SKILL.md) deve carregar apenas ao ser relevante.
3. **Faça uma primeira missão verificável:** [bootstrap situacional](setup/CEO-bootstrap-situacional.md) e [primeiro ciclo de resultado](setup/CEO-business-outcome-first-run.md). A prioridade é entender por que pessoas reais não chegam, não conseguem falar, não voltam ou não pagam — não pressupor a causa.

### Exemplo de pedido objetivo ao CEO

> Analise os dados acessíveis e o caminho público do BataTalk. Identifique a restrição mais relevante entre descoberta, promessa, primeira conversa oral, retenção, pagamento ou margem. Apresente a melhor hipótese e uma rival; execute nesta sessão o passo mais útil já autorizado, verifique o resultado no destino e diga a próxima evidência que mudaria a decisão. Não crie agentes ou documentos se isso não resolver o gargalo. Respeite POLICY.md.

Este exemplo **não** autoriza disparos, campanhas, deploy, acesso sensível, alterações de cobrança ou orçamento.

## Três camadas que não podem ser confundidas

| Camada | Onde fica | O que comprova |
|---|---|---|
| Mandato persistente | [CEO_SYSTEM_PROMPT.md](CEO_SYSTEM_PROMPT.md) nas instruções do host | Identidade e prioridade quando configuradas |
| Skill acionada por contexto | [SKILL.md](SKILL.md) + módulos sob demanda | Orientação para decidir/agir em uma tarefa |
| Autonomia recorrente | scheduler, webhooks, ferramentas, estado, permissões e logs reais | Rotina de verdade, se instalada e testada |

M0 = conversa sem ferramentas; M1 = ferramentas durante o acionamento; M2 = persistência/sensores efetivamente configurados. [Contrato universal](references/32-contrato-universal-multiplataforma.md). Os [adaptadores](adapters/README.md) ajudam com particularidades das plataformas, mas não substituem a verificação do host.

## Livro de instruções: leitura progressiva

O núcleo [SKILL.md](SKILL.md) apresenta o fluxo de execução e o roteamento. **Não carregue todo o acervo em cada sessão.** Comece pelos guias adequados:

| Decisão que precisa tomar | Leitura recomendada |
|---|---|
| Primeiros clientes, pesquisa e distribuição | [30 — mercado primeiro](references/30-mercado-primeiro-execucao-comercial.md) |
| Falha de proatividade ou julgamento | [31 — percepção](references/31-consciencia-situacional-e-autonomia-executiva.md), [34 — autocalibração](references/34-proatividade-autocalibracao-e-execucao.md) |
| Estratégia e capacidade executiva | [33 — julgamento](references/33-julgamento-executivo-competencias-e-aprendizado.md), [35 — repertório](references/35-decidir-e-executar-com-repertorio.md), [36 — mandato](references/36-ceo-mandato-estagios-estrategia.md) |
| Produto, voz, aprendizagem e finanças | [06 — produto e economia](references/06-produto-pedagogia-dados-financas.md), [38 — finanças](references/38-startups-financas-e-glossario.md) |
| Growth, marketing, SEO/GEO e CRO | [05 — diagnóstico](references/05-growth-competidores-seo-geo-cro.md), [46 — SEO](references/46-seo-tecnico-indexacao-semantic-search.md), [47 — GEO](references/47-geo-aeo-ai-search-plataformas.md), [48 — demanda](references/48-demanda-topical-conteudo-e-autoridade.md), [49 — copy](references/49-copywriting-cro-distribuicao-e-marca.md), [50 — métricas](references/50-mensuracao-experimentos-organicos.md), [51 — segmentos](references/51-playbooks-organicos-por-negocio.md), [52 — operação](references/52-operacao-seo-geo-roadmap-e-governanca.md) |
| Delegação e risco multiagente | [21 — equipes](references/21-organizacao-autonoma.md), [23 — handoffs](references/23-contratos-dags-handoffs.md), [29 — custo de modelos](references/29-modelos-custo-capacidade.md) |
| Organização, método e crise | [37 — C-levels](references/37-csuite-cargos-charters.md), [39 — frameworks](references/39-metodologias-frameworks-de-gestao.md), [40 — crise](references/40-turnaround-risco-e-crises.md), [43 — cadência](references/43-ceo-operating-system-rituais-templates.md), [44 — liderança](references/44-lideranca-governanca-macro-micro.md), [45 — casos](references/45-casos-integrados-roadmap-executivo.md) |
| Bibliografia e pesquisa aprofundada | [41 — CEOs](references/41-ceos-biografias-e-contrafactuais.md), [42 — biblioteca essencial](references/42-biblioteca-executiva-auditavel.md), [53 — catálogo](references/53-biblioteca-expandida-140-obras-19-cargos.md), [54 — índice da enciclopédia](references/54-enciclopedia-50-ceos-50-livros-matriz.md) |

A [enciclopédia](research/enciclopedia-ceo/00-GUIA-MESTRE-DO-CEO-SINTESE-E-PLAYBOOK.md) é pesquisa de aprofundamento, **não** um prompt para inserir inteiro no contexto. Reunir títulos não significa ter lido integralmente as obras; estudos de caso não garantem que a mesma estratégia funcionará no BataTalk.

## Verificações: o que os testes demonstram

Com Python 3.11 ou superior:

~~~bash
python scripts/validate_skill.py
python scripts/validate_csuite_library.py
python scripts/validate_work_graph.py templates/orchestration-plan.example.json --ready
python -m unittest discover -s tests -p "test_*.py" -v
python scripts/package_skill.py --output dist
~~~

O empacotador cria dist/batatalk-ceo-operator com manifesto de **hashes de todos os arquivos**. A opção --replace recusa apagar um pacote que contenha arquivos não inventariados, alterações ou manifesto legado sem verificação; preserve os dados e reconstrua em diretório limpo. O inventário não é assinatura digital ou prova de que o host carregou essa versão.

**CI verde = arquivos, contratos e testes de código verificados, não agente aprovado.** Para comparar desempenho de verdade, use [protocolo de revisão](tests/REVIEW-PROTOCOL.md), [validação de campo](setup/CEO-field-validation.md), [cenários de comportamento](tests/CEO-BEHAVIOR-EVALS.md) e [roteamento da skill](tests/SKILL-ROUTING-TEST-PLAN.md). Compare baseline e candidata com ferramenta/modelo semelhantes, revisor independente e evidência de execução real, custo, risco e impacto. Uma violação de segurança bloqueia aprovação.

## Autoridade, transparência e melhorias

**[POLICY.md](POLICY.md) é a fonte normativa.** O CEO pode pesquisar, preparar, testar em sandbox e organizar agentes na alçada delegada. Gastos, publicação externa, cobrança, produção arriscada, dados pessoais e compromissos jurídicos exigem autorização conforme escopo. O **Reels Creator permanece PAUSADO** por decisão do fundador, independentemente de outras campanhas ou perfis.

[AGENTS.md](AGENTS.md) rege mudanças nesta skill. [AUDIT.md](AUDIT.md) registra limitações e revisão histórica. Regras sobre evolução: primeiro observe uma falha, depois corrija comportamento, registre testes e verifique resultado. Novas páginas de enciclopédia sem mudança de decisão não são progresso.

### Referências de engenharia

- [Agent Skills — especificação e carregamento progressivo](https://agentskills.io/specification)
- [Anthropic — Building Effective Agents](https://www.anthropic.com/research/building-effective-agents)
- [OpenAI — Agent Evals](https://developers.openai.com/api/docs/guides/agent-evals)
- [OpenAI — Trace Grading](https://developers.openai.com/api/docs/guides/trace-grading)

Verifique a documentação de cada host ao instalar: interfaces e permissões podem mudar.
