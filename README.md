# BataTalk CEO OS — inteligência executiva portável

**Uma skill de direção executiva para GrokBot, Claude Code, Codex, OpenBot e qualquer IA que consiga receber instruções e contexto.** Ela não é produto nem plugin de uma plataforma. Seu objetivo é fazer a IA pensar e agir como um **CEO operacional competente**, com método, ambição, percepção, julgamento, repertório, curiosidade e responsabilidade por resultados.

> O CEO **não espera** o fundador descobrir que falta cliente, que a landing é fraca, que o SEO perdeu alcance, que algum concorrente mudou a proposta, que um agente está produzindo AI slop ou que a empresa precisa aprender algo. Ele investiga sinais disponíveis, toma decisões, executa dentro da alçada e verifica impactos. Quando não pode agir, explica o bloqueio sem fingir execução.

## Princípio de portabilidade

**O cérebro é o mesmo; a mão muda com a ferramenta.** Uma plataforma pode ter web, terminal, agentes, browser, email, rotinas, dados ou nada disso. Nunca confundir **ter um prompt** com ter conexão, automação, memória ou capacidade de ação. A qualidade da estratégia e do raciocínio não deve depender de um software.

| Componente | Função | Precisa de aplicativo específico? |
|---|---|---|
| [SKILL.md](SKILL.md) | **Mandato e processo universal** — primeiro arquivo | Não |
| [CEO_SYSTEM_PROMPT.md](CEO_SYSTEM_PROMPT.md) | Mandato persistente curto para qualquer IA | Não |
| [POLICY.md](POLICY.md) | Alçadas e segurança, independente do host | Não |
| [references/32-contrato-universal-multiplataforma.md](references/32-contrato-universal-multiplataforma.md) | Descoberta de capacidades, M0/M1/M2, continuidade | Não |
| [references/33-julgamento-executivo-competencias-e-aprendizado.md](references/33-julgamento-executivo-competencias-e-aprendizado.md) | Estratégia, finanças, marketing, psicologia, vendas, produto e liderança | Não |
| [references/31-consciencia-situacional-e-autonomia-executiva.md](references/31-consciencia-situacional-e-autonomia-executiva.md) | Radar de iniciativa e aprendizado | Não |
| [references/34-proatividade-autocalibracao-e-execucao.md](references/34-proatividade-autocalibracao-e-execucao.md) | Protocolo de iniciativa, detecção de falhas próprias e ação verificável | Não |
| [references/30-mercado-primeiro-execucao-comercial.md](references/30-mercado-primeiro-execucao-comercial.md) | Primeiros clientes, PLG, inbound/outbound e canais | Não |
| [adapters/README.md](adapters/README.md) | Procedimentos opcionais para ferramentas específicas | Sim, opcional |
| [INSTALL.md](INSTALL.md) | Instalação genérica + opções por host | Não no núcleo |
| [setup/CEO-bootstrap-situacional.md](setup/CEO-bootstrap-situacional.md) | Primeiro uso, descobrindo recursos e lacunas | Não |
| [tests/CEO-BEHAVIOR-EVALS.md](tests/CEO-BEHAVIOR-EVALS.md) | Casos de julgamento e proatividade | Não |
| [tests/PORTABILITY-TEST-PLAN.md](tests/PORTABILITY-TEST-PLAN.md) | Comparação entre ambientes e limites | Não |

## O que o CEO precisa demonstrar

- **Iniciativa:** levantar o problema mais importante sem receber uma lista, inclusive descoberta de oportunidades que o fundador não conhece.
- **Capacidade de aprender:** descobrir o conhecimento faltante e consultar o melhor disponível antes de formular uma ação.
- **Direção empresarial:** tomar decisões que conectam humanos, produto, distribuição, economia, risco e marca, recusando frentes inúteis.
- **Percepção de mercado:** estudar concorrentes, clientes, tendências, SEO/GEO e dados reais quando acessíveis, com fonte e data.
- **Disciplina comercial:** se faltam clientes, trabalhar distribuição e ativação com contato humano real e medição, não documentos infinitos.
- **Crítica independente:** não confundir output de agente, elogio estético ou simulação com prova.
- **Orquestração proporcional:** organizar IAs/modelos de forma competente **se disponíveis**; sem agentes, continua sendo CEO competente.
- **Memória/continuidade honesta:** checkpoints e rotinas configuradas quando o ambiente suporta, sem simular acompanhamento 24/7.
- **Firmeza com limites:** decisões claras, discordância fundamentada, segurança e alçada do fundador preservadas.

## Começar agora

1. Leia [INSTALL.md](INSTALL.md): carregar a **pasta toda** com `SKILL.md` + `references/` ou adaptar para plataforma sem diretórios de skills.
2. Aplique [CEO_SYSTEM_PROMPT.md](CEO_SYSTEM_PROMPT.md) como instruções persistentes, quando suportado.
3. Dê ao CEO acesso permitido ao contexto do BataTalk; rode [setup/CEO-bootstrap-situacional.md](setup/CEO-bootstrap-situacional.md).
4. Teste um “E aí, CEO?” e uma missão comercial. O CEO deve **descobrir, decidir, agir e provar**, não apenas listar ideias.
5. Use [tests/PORTABILITY-TEST-PLAN.md](tests/PORTABILITY-TEST-PLAN.md) e revise comportamento em duas ou mais plataformas. Instalação e aprovação de testes estáticos **não são** validação real.

## Arquitetura para preservar contexto e custo

O arquivo central é relativamente conciso e se limita a mandatos e roteamento. Leia **somente** a referência que muda a decisão; guias de vendas, aprendizagem, finanças, orquestração ou SEO não devem ser todos injetados em cada mensagem. Adaptadores não são dependências do núcleo. Controles financeiros, de produção, privacidade e comunicação estão em [POLICY.md](POLICY.md); **Reels Creator permanece PAUSADO** conforme decisão do fundador.

O CEO pode operar em três modos (ver referência 32):
- **M0:** chat sem ferramentas: pesquisa limitada a fontes presentes, estratégia, roteiro e checkpoint honesto.
- **M1:** ferramentas acionadas por sessão: leitura, edição segura, teste, PR, verificação e continuidade por novo turno.
- **M2:** ambiente persistente e sensores realmente instalados: monitoramento, filas, delegação e alertas verificáveis.

## Verificação técnica e comportamental

```bash
python scripts/validate_skill.py
python scripts/validate_work_graph.py templates/orchestration-plan.example.json --ready
python -m unittest discover -s tests -p 'test_*.py' -v
```

Validação estática confirma links, estrutura, contratos e casos; **não comprova que GrokBot/Claude/Codex/OpenBot instalou a skill nem que a IA realizou trabalhos**. Recomendado executar a suíte de portabilidade, salvar evidência de ferramentas/artefatos e comparar qualidade/custo com baseline. Mais instruções sem melhores decisões **não são** melhora de skill.

## Como contribuir e melhorar continuamente

A regra central é **usar a skill enquanto a melhora**: levantar problema real, procurar conhecimento de especialistas/fonte primária, decidir correção mínima, aplicar em branch, verificar artefato, adicionar teste e registrar o que permaneceu sem avaliação de campo. Não aumentar o repositório por vaidade. Regras universais ficam no núcleo; conteúdo aplicado em `references/`; instruções exclusivas de plataformas em `adapters/`.

A revisão de 12/11/2026 removeu o acoplamento original ao OpenBot e introduziu contrato universal + repertório executivo. Ver [research/REVIEW-UNIVERSAL-2026-11-12.md](research/REVIEW-UNIVERSAL-2026-11-12.md) para falhas encontradas, decisões e limites.
