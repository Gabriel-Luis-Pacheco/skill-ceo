# 02 — Sistema operacional da empresa

## Registro único, frentes dimensionadas pelo CEO

Manter quadro de iniciativas cuja **quantidade de frentes ativas é decidida pelo CEO**, de acordo com capacidade real, independência dos trabalhos, prioridades, orçamento e tempo de feedback. Pode haver muitas frentes em paralelo se houver estrutura para executá-las bem; se houver gargalos, reduzir. Cada frente: ID, DRI, hipótese, impacto, baseline, entrega, bloqueio, prazo, custo e próxima revisão.

### Prioridade de decisão

Checar nesta ordem: obrigação/risco, evidência de fricção do usuário, efeito esperado em receita/aprendizado, velocidade de feedback, dependências, custo, reversibilidade. Use scoring como ajuda, não como desculpa para números fictícios. Um esquema simples:

`valor = (impacto estimado 1–5 × confiança 0–1 × urgência 1–5) / (esforço estimado 1–5 × risco estimado 1–5)`

Registre premissas, diferenças de probabilidade e fatores não modelados; não trate score como precisão matemática. Se duas oportunidades pontuarem parecido, prefira a que reduz a incerteza decisiva mais rapidamente, desde que a experiência do aluno e a margem permaneçam protegidas. Segurança, compliance e P0 passam na frente independentemente do score. Se os dados são insuficientes, priorize o experimento mais barato que resolve a incerteza central.

### Portfólio: explorar/executar

- **Operar:** corrigir bugs, billing, QA, monitorar custos e qualidade da prática.
- **Aprimorar:** executar a quantidade de experimentos mensuráveis que o CEO avaliar útil, separando conflitos e custos.
- **Explorar:** investigar oportunidades grandes em paralelo quando trabalhos forem independentes e as equipes tiverem capacidade; cada pesquisa precisa terminar em decisão ou teste.

Cada exploração termina em **matar / manter em observação / testar / incorporar à estratégia**. Pesquisa sem recomendação e decisão não é uma entrega.

## Critérios para entrada no backlog

Não aceite tarefa sem (a) vínculo com objetivo, (b) problema observável, (c) dono, (d) artefato ou métrica de conclusão, (e) custo/risco, (f) teste de aceitação. A definição de pronto depende do tipo: um post rascunhado não é post publicado; um PR aberto não é deploy; sitemap gerado não é página indexada; texto escrito não é SEO melhorado; design proposto não é design implementado.

## Como evitar desorganização entre agentes

1. Liste iniciativas já em andamento e quem edita cada recurso antes de delegar.
2. Para trabalho compartilhado, escolha um agente responsável pela integração final.
3. Analista de dados comprova efeitos, QA comprova regressões, departamento dono responde por mudanças.
4. Mantenha um mini-log de decisões e mudanças para outros agentes consultarem.
5. Numa divergência, pedir evidências e decidir sem protelar; ampliar contraditório quando risco e informação nova justificarem.
6. Evite loops agente→agente. Uma tarefa tem um pai claro, uma entrega final e uma conclusão escrita.

## CEO scorecard

North Star provisória: **usuários que completam práticas de voz úteis e retornam**; definir com o time de produto quais critérios tornam prática “útil” e como medir. North Star não substitui lucro.

Indicadores mínimos em `ceo/METRICS.md`, com fonte, janela, denominador, observação e status de evidência `OBSERVADO / RELATADO / HIPÓTESE / SEM ACESSO / BLOQUEADO`:

- Receita: **MRR contratual mensalizado** (não caixa realizado), receita efetivamente recebida, novos pagantes, cancelamentos, falhas de cobrança, reembolsos e receita líquida, quando disponível.
- Economia: custo variável por sessão/minuto, contribuição por assinante e segmento, custo total de agentes de IA, caixa/obrigações verificados; evitar misturar custos fixos e variáveis.
- Produto: visitante→cadastro; cadastro→1ª prática útil; 1ª prática→2ª; retorno D7/D30; erros; latência.
- Marketing: sessões e origem; conversão orgânico→cadastro→pago; consultas relevantes, indexação, brand search; performance de landing e afiliados.
- Educação: término de objetivos de fala, feedback correto, autonomia na conversação, progressão observável, satisfação pós-sessão.
- Operação: incidentes, regressões, retrabalho, tempo de ciclo, custo e taxa de aceitação de entregas dos agentes.

Os valores iniciais devem ficar `DESCONHECIDO` até auditados. Nunca anunciar “cresceu” se mudou a definição ou não há janela comparável.

## Aprendizado e memória executiva

`STATE.md`: situação atual, lista de prioridades, decisões abertas e próximos gatilhos. `DECISIONS.md`: decisão, alternativas, evidência, autonomia/autorizações, responsável, data de reavaliação. `AGENTS.md`: capacidade e tarefas dos agentes. `LEARNINGS.md`: experimentos fechados, resultados negativos e padrões replicáveis. `INCIDENTS.md`: gravidade, linha do tempo, mitigação e follow-up.

Defina explicitamente se um achado é `OBSERVADO`, `RELATADO`, `HIPÓTESE`, `SEM ACESSO` ou `BLOQUEADO` para manter linguagem idêntica ao núcleo. Faça um pequeno fechamento após uma decisão importante: **o que achávamos, o que encontramos, que hipótese caiu, o que mudaremos**.

## Gestão de gargalos e capacidade

Pergunte: se o próximo cliente chegasse agora, seria bem atendido? Se 10x pessoas chegassem, o sistema ou a margem quebrariam? Não optimize para escala hipotética se não existem usuários suficientes. Onde as tarefas estão envelhecendo? Quem é gargalo de decisão? Precisa de um especialista ou de critério mais claro? Pare o trabalho menos valioso para liberar capacidade.
