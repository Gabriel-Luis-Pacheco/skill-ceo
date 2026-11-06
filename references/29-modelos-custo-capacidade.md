# 29 — Model routing, eficiência e capacidade real de agentes

## Princípio de economia

A equipe pode crescer sem teto artificial, mas **não deve consumir tokens sem retorno**. Comparar custo total de resolver a tarefa: tempo de modelo + chamadas de ferramentas + revisores + retries + contexto + coordenação + regressões. Modelo barato com cinco falhas pode sair mais caro que um modelo forte acertando de primeira; modelo caro em tarefa trivial é desperdício.

## Roteador de modelos por tarefa

O CEO/COO/CTO seleciona modelo e esforço de raciocínio pela combinação:
- domínio, contexto necessário, ferramentas suportadas e dificuldade;
- criticidade e custo de erro;
- necessidade de imagem, voz, código, pesquisa ou precisão factual;
- latência alvo, confiabilidade, limites de provedor e comportamento já medido;
- custo estimado no plano **real** e qualidade nos mesmos casos de avaliação.

Não fixar nomes de modelos como se ofertas de 2026 fossem permanentes. No OpenBot, cada agente pode ter seu próprio provedor/modelo/esforço conforme instalação. Testar capacidades reais; `free` não significa uso sem fila, quota, indisponibilidade ou custo de coordenação.

## Estratégia de execução adaptativa

- Simples: uma chamada curta com ferramenta certa.
- Especialista difícil: modelo forte, contexto focado, teste e auditor quando necessário.
- Pesquisas independentes: subagentes contextualmente isolados em paralelo se custo/latência compensarem.
- Coding com conflitos de arquivo: dividir por subsistema, atribuir branch e sequência de integração em vez de muitos editores iguais.
- Auditoria de alto risco: revisor especializado com **independência real de premissas**; concordância entre clones não é prova.
- Iteração: se solução fraca por especificação, corrigir brief; se falta conhecimento, pesquisa; se limite de ferramenta, acesso; se falta raciocínio, elevar modelo — não repetir cegamente.

## Alocação sem cotas

Dimensionar paralelismo conforme `task value / probability of success / cost / dependencies / queue wait / failure risk`. Nenhum valor numérico fixo é universal: o CEO decide tamanho de equipes e quantos modelos trabalham simultaneamente, respeitando **capacidade efetiva e orçamento delegado**. Se um modelo congestionou, redistribuir a outros quando competência e alçada permitirem.

**Cache/contexto:** reutilizar referências e artefatos imutáveis, evitar reenvio de todo histórico, medir compaction e qualidade. Instruções mais longas podem elevar custo e reduzir clareza. Reservar contexto aprofundado para tarefa que dele precisa.

## Detectar desperdício

- Múltiplos agentes responderam ao mesmo pedido sem papéis independentes.
- Revisores repetem opinião do executor, sem artefato/reprodução.
- Fila cresce mais que entregas úteis.
- Agentes ficam abrindo relatórios, contratando agentes e convocando reuniões uns aos outros.
- Pesquisa não muda decisão.
- A mesma ferramenta com erro é chamada repetidamente após timeout de resultado desconhecido.
- Contexto longo contém mensagens sem importância e oculta a política.

Diante de desperdício, CEO pode redesenhar topologia, contexto, roteamento e time sem cotas ou pedir autorização para recursos realmente necessários.

## Métrica de resultado

Exigir custo por **entrega verificada e integrada**, e, quando disponível, custo por usuário com prática útil e margem de contribuição — não celebrar “milhões de tokens grátis”. Manter custo estimado vs observado separados e explicar dados ausentes.

Fonte: Anthropic multi-agent https://www.anthropic.com/research/multi-agent-research-system ; OpenAI orchestration https://developers.openai.com/api/docs/guides/agents/orchestration ; OpenBot https://github.com/nightly-labs/openbot
