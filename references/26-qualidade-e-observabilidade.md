# 26 — Observabilidade, qualidade e aprendizagem do sistema multiagente

## Instrumentar a orquestração, não só a resposta final

O CEO e COO precisam rastrear **o que foi solicitado, como foi roteado, quem executou, quantas vezes, custo, risco e evidência final**. O OpenBot dispõe de filas, mensagens e canais; informações detalhadas de tokens e execução só podem ser declaradas quando o runtime/provedor as expõe.

## Modelo conceitual de trace

`initiative_id → task_id → agent_id → model/version → route/pattern → tool_calls → handoffs → artifacts → independent_review → final_outcome`.

Cada evento relevante registra data, status, duração observada, custo conhecido ou estimado com premissas, versão de contrato, dependências e identificador do resultado. Não registrar conteúdo pessoal, segredos, prompts privados ou áudio identificável em log compartilhado.

**Quatro níveis de validação**:
1. **Integridade:** arquivos, JSON/links/schema válidos.
2. **Ferramentas:** ação enviada e resultado confirmado, sem inventar execução.
3. **Artefato:** qualidade do que foi produzido, testes, UX, pedagogia, segurança e compatibilidade.
4. **Negócio/cliente:** efeito observado após janela real, retenção, margem e confiança — não inferir causalidade sem desenho adequado.

GitHub Actions neste repositório testa **só níveis 1 e parte da lógica de scripts**. Os 70 cenários são **especificações**, não 70 execuções de IA. Usar `tests/REVIEW-PROTOCOL.md` e `scripts/score_evaluations.py` para avaliações humanas controladas.

## Scorecard de orquestrador

Avalie com fonte e janela:
- **Taxa de conclusão verificável**: tarefas com critérios aceitos e evidência / tarefas elegíveis; separar abortadas, bloqueadas e não começadas.
- **Handoff quality**: entradas aceitas sem rebrief/retrabalho por falta de contexto.
- **Tempo de ciclo e caminho crítico**: até resultado integrado, não até o primeiro agente responder.
- **Retrabalho e taxa de regressão**: correções por defeito real, incluindo merges/reversões.
- **Proatividade útil**: novos problemas/oportunidades descobertos que levaram a decisão ou experimento válido.
- **Qualidade de decisão**: decisões reversíveis rápidas com resultados medidos; decisões irreversíveis fundamentadas com aprovação.
- **Token/custo total por resultado**, e não só tokens individuais: incluir múltiplos modelos, reviewers e coordenação.
- **Incidentes e desvios de alçada**, com tolerância zero a efeitos externos não autorizados.
- **Resultados de negócio**: ativação, primeira prática, retenção, assinaturas recebidas e margem com denominador e incerteza.

**Benchmark cego:** comparar A (skill antiga) vs B (nova), mesmo modelo e casos quando possível; ter revisor que desconhece a variante e examina traces/artefatos, não apenas a retórica do CEO.

## Anti-consenso e auditor independente

Três agentes do mesmo modelo, com mesmo prompt e mesmas premissas, não constituem três provas independentes. Para decisão difícil, usar perspectivas/competências contrastantes, verificar fatos com ferramentas e exigir que o crítico **procure a hipótese que faria a recomendação fracassar**. Nenhuma votação de IA substitui observação de usuário ou experimento.

No produto de voz, separar correção linguística, naturalidade, latência, segurança e aprendizagem. Um `pass` em testes de backend não comprova qualidade da fala, nem retenção/receita.

## Feedback para evoluir agentes

Quando um agente falha: 1) reproduzir; 2) localizar se foi roteamento, contexto, ferramenta, modelo, instrução ou ausência de teste; 3) corrigir menor causa; 4) testar antes/depois; 5) revisar em produção autorizada; 6) atualizar contrato/skill; 7) descartar mudança que piora custo, risco ou qualidade.

Fontes: OpenAI trace/evals https://developers.openai.com/api/docs/guides/agent-evals ; Anthropic multi-agent https://www.anthropic.com/research/multi-agent-research-system
