# 06 — Produto, aprendizagem, métricas e rentabilidade

## BataTalk como produto educacional, não só chatbot bonito

O core é **prática de inglês falado com IA em situações reais**. Experiências conhecidas do produto: locais/situações como cafeteria e aeroporto, mascote Tato, onboarding, sessões, planos Plus/Pro e Stripe. Verificar implementação atual antes de assumir que algo funciona ou está público.

Uma sessão precisa ter: objetivo comunicativo claro, entrada acessível ao nível do usuário, oportunidade real de produção oral, progressão de dificuldade, hints úteis quando travar, correção proporcional que preserve fluidez, feedback específico, registro de progresso e motivo para voltar. Use descritores `can-do` do CEFR para planejar tarefas de **interação oral** adequadas ao nível, como referência educacional, sem atribuir certificação CEFR automática ao aluno. Fonte: https://www.coe.int/en/web/common-european-framework-reference-languages/cefr-descriptors Fluência não deve ser prometida sem evidência.

### Suite de avaliação de conversação

Construir e manter testes *sintéticos* e, com autorização/privacidade, evidências agregadas reais. Perfis: iniciante A0/A1, A2 com vocabulário limitado, B1 conversacional, fala com sotaque, hesitação, ruído, timeout, erro de pronúncia, silêncio, pedido off-topic e tentativa adversarial.

Rubrica calibrável por amostra (ex.: escala 1–5): **compreensão da fala**, **latência**, **adequação ao nível**, **naturalidade**, **objetivo da missão**, **qualidade do hint**, **precisão de correções**, **não interrupção excessiva**, **segurança**, **custo**. Registrar input/condições esperadas, output e revisão independente do Head of Learning e QA. Não guardar áudio pessoal sem base legal e política apropriada.

### Distinção: diversão vs aprendizagem

Sessões longas e elogios frequentes não provam aprendizado. Procure evidências de mais fala espontânea, menos dependência de hints, redução de erros relevantes, conclusão de objetivos e retenção saudável. Não manipular usuários com gamificação agressiva que substitua progresso real.

## Funil e retenção

Esquema de eventos provisório, a validar com Data e CPO: `landing_view`, `signup_started`, `signup_completed`, `onboarding_completed`, `scenario_selected`, `voice_permission_granted/denied`, `session_started`, `first_meaningful_turn`, `session_completed`, `feedback_viewed`, `session_returned`, `paywall_viewed`, `checkout_started`, `subscription_activated`, `subscription_cancelled`. Cada evento precisa de definição, timestamp, contexto mínimo e privacidade; não coletar dados sensíveis sem necessidade.

Definições a aprovar:
- **Ativação:** usuário tem a primeira conversa útil, não só criou conta.
- **Retenção D7/D30:** coorte por data de ativação e retorno à prática útil, com denominador fixo, timezone e regra de janela explícitos; separar cohort incompleta de usuários que não retornaram.
- **Conversão paga:** assinatura efetivamente paga/ativa, excluindo tentativas e testes.
- **Taxa de conclusão:** sessão que atingiu objetivo e passou condições mínimas; não só fechou modal.

Problemas do funil exigem causalidade com ressalvas: se muitos abandonam na permissão de microfone, audite navegação e UX; se abandonam após 1a fala, teste latência e qualidade de IA; se não pagam após experimentar, investigue percepção de valor, limite, oferta e preços com pesquisa de cliente.

## Economia de SaaS/IA

MRR e churn só a partir de dados reais de assinaturas/invoices. Estabeleça claramente moeda, janela, plano, status e exclusões. Cálculos básicos com nomenclatura:

- **MRR:** soma mensalizada dos contratos recorrentes ativos sob definição documentada; não é receita bancária recebida. Não nomeie `MRR realizado`; compare separadamente com pagamentos liquidados, reembolsos e receitas de competência.
- **Margem de contribuição por assinante:** receita líquida atribuída − custos variáveis atribuíveis (inferência, STT/TTS/voz, serviços variáveis, taxas e reembolsos pertinentes).
- **Custo de sessão:** consumo de tokens/modelos + áudio/STT/TTS + infraestrutura incremental atribuível; estimar separadamente do custo fixo.
- **CAC por canal:** custo de aquisição verificável / novos pagantes atribuíveis, com janela e limitações; canais orgânicos também têm trabalho e custos operacionais atribuíveis, não presumir CAC zero.
- **Payback CAC:** custo de aquisição / contribuição mensal média por cliente adquirido; se a contribuição for ≤ 0, payback é inviável nas condições atuais.
- **Burn/runway:** custos de caixa versus disponibilidade de caixa, quando o fundador fornecer acesso/autorização; não presumir saldos.

Verificar webhooks/recebimentos de forma idempotente; política de cancelamento e dunning dentro das permissões. Não alterar preço/Stripe em produção sem autorização do fundador.

### Alerta de margem

Quando volume cresce, lucro por usuário pode cair. Antes de liberar prática “ilimitada”, simular faixas de minutos por usuário, proporção heavy users, custos de voz e taxa de pagamento. FinOps controla cache, contexto, model routing, prompts, qualidade versus custo e falhas de retries. Não sacrificar qualidade essencial apenas para reduzir tokens.

## Decisão executiva baseada em evidência

Se falta tráfego **mas** retenção/ativação ainda não comprovadas, não simplesmente intensifique aquisição. Se há forte valor e demanda mas SEO técnico bloqueia indexação, SEO vira prioridade. Se o maior problema é o funil do checkout, elimine fricção antes de redesenhar mascote. A missão é encontrar **o atual limitador de crescimento rentável** e resolvê-lo.

## Observabilidade do serviço

Definir monitoramento da prática, checkout, login, webhooks, latência e erros, com thresholds proporcionais à linha de base real. Manter taxa de falha e período; P0 em cobrança, segurança, indisponibilidade crítica ou corrupção de dados. Uma release só está completa com testes e observação pós-publicação. Para degradação séria, pausar novos features até recuperar confiabilidade.
