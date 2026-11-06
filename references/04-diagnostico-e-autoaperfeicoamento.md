# 04 — Sistema imunológico anti-mediocridade e evolução de prompts/skills

## Falha de qualidade: detectar antes do fundador

A cada entrega relevante, audite amostras reais. Abra páginas em mobile e desktop, leia textos como um visitante novo, execute fluxos essenciais, escute/reproduza amostras de conversa autorizadas ou use cenários sintéticos, teste checkout em sandbox, inspecione diffs, reabra dados e valide alegações. Não dependa da autoavaliação de quem criou.

### Sinais de AI slop em copy/LP/design

- Textos que poderiam pertencer a qualquer curso ou SaaS; palavras vazias sem evidência; blocos enormes de prosa; repetição da mesma mensagem.
- Layout de template, cartões repetidos, iconografia/emojis como substitutos de experiência, hero estática sem demonstração, mascote repetido em excesso, CTAs confusos.
- Promessas vagas (“fluência garantida”), falsos números/depoimentos, visual sofisticado mas prova inexistente.
- Ausência de vídeo/visualização real da prática, fluxo fragmentado, onboarding genérico, mobile quebrado, baixa velocidade/acessibilidade.
- Inovação cenográfica: animação que atrasa a mensagem, 3D que prejudica performance, textos que ignoram público brasileiro.

### Rubrica de qualidade (1–5, com provas)

**Clareza da oferta**, **distintividade da marca**, **efetividade do CTA**, **demonstrabilidade do produto**, **fluidez narrativa**, **legibilidade/visual**, **mobile/acessibilidade**, **integridade de promessa**, **performance/SEO**. Não somar mecanicamente para decidir: falha crítica em acessibilidade, credibilidade ou checkout reprova. Compare com screenshot antes/depois e comportamento de usuários, não com gosto subjetivo sozinho.

### Protocolo anti-slop

1. Capture artefato, trecho/screenshot e repro/URL; descreva o problema específico.
2. Peça revisão adversarial com 3 perspectivas: usuário iniciante cético, especialista de área e responsável por conversão/negócio. Simulações de personas são **hipóteses**, não entrevistas reais.
3. Reúna referências externas reais e padrões de alto nível; não copiar assets nem claims sem direitos.
4. Escreva direção criativa ou requisito que resolva **causa**, não “deixe mais premium”. Exemplos concretos, restrições, design de informação, linha de texto, fluxo e métrica.
5. Faça mudança menor que teste a hipótese; capture e compare; revise em mobile e desktop.
6. Se qualidade ainda falha, mude processo/modelo/responsável; evite loops de “faça melhor”.

## Reparar agentes ou skills

### Diagnóstico de causa

- **Mal explicado?** Brief ambíguo → refinar escopo, contexto, exemplos e não-exemplos.
- **Tem instruções, mas ignora?** Observação da execução → prompt mais conciso, prioridades explícitas, checklists perto da ação, menos conflito.
- **Sabe o que fazer, mas não sabe como?** Skill com procedimento e referências, ferramenta necessária, treino/eval.
- **Sabe como, mas entrega pior?** Modelo inadequado, contexto enorme, ferramentas ruins, tarefa larga demais ou revisão insuficiente.
- **Repete erro com aprovação automática?** Quebrar auto-homologação; revisor independente e teste final.
- **Produz trabalho inútil?** Meta errada, incentivo ao volume, sem feedback de usuário/negócio.

### Ciclo de melhoria testável

**Baseline:** escolha 6–12 casos representativos, com falhas reais, incluindo pelo menos um caso adversarial e um de custo. Faça versões antes/depois no mesmo contexto e, quando possível, mesmo modelo. **Hipótese:** o que mudará e por quê. **Patch:** altere instruções/skill em arquivo versionado, anote diff e backup. **Avaliação cega:** revisores pontuam artefatos por critérios objetivos sem saber a versão. **Implementação:** comece com baixo risco; monitore regressões, tempo e custo. **Rollback:** se piorar qualidade/risco, restaure versão anterior. Toda alteração entra em `ceo/LEARNINGS.md`.

Não permita que um agente **melhore a própria prompt sem revisão** e conclua que ficou melhor. Um especialista independente ou teste externo precisa validar.

### Melhorar a skill sem loop

O CEO pode propor novos playbooks quando observa uma lacuna. Exigir `lacuna observada → 2 casos → proposta → diff → testes → decisão` e limite inicial de **uma revisão estrutural por semana**, salvo falha de segurança. Skills não são um fim: uma melhoria só vale se elevar desempenho de tarefas reais. Revisões grandes precisam preservar contexto e não conflitar com política superior.

## Pesquisa profunda orientada a decisão

Quando lacuna for conhecimento: definir perguntas, corpus de fontes, consenso/divergências, hipóteses, mecanismo causal, exemplos, custo de adoção, teste e implicação para BataTalk. Preferir fontes primárias: docs técnicas, sites concorrentes atuais, estudos credíveis, entrevistas com usuários e métricas próprias. Registrar data e incerteza. Pesquisa nunca termina em um mural de links; termina em **uma decisão, uma experiência ou uma recusa fundamentada**.

## Sistema de crítica com conflito controlado

Três papéis diferentes quando a decisão for importante:
- **Construtor:** propõe solução e artefato.
- **Cético:** tenta provar que a solução falhará, encontra objeções, dados ausentes e defeitos.
- **Auditor:** verifica fatos, escopo, riscos, testes e impacto.

CEO decide após ouvir o contraditório. Limite a **uma rodada de debate**; só reabra por evidência nova. Não transformar subagentes em teatro.
