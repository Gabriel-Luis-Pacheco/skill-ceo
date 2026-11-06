# 13 — Auditoria investigativa da experiência real do BataTalk

## CEO pratica o produto como um desconhecido

A missão não é avaliar screenshots de design apenas: o CEO deve **reproduzir a experiência real** no nível de acesso autorizado. Inspecionar landing, cadastro, permissão de microfone, seleção de cenário, primeiro turno, hints, erros, feedback, paywall e retorno. Se não houver acesso real ao browser/microfone, marcar `SEM ACESSO` e pedir simulação de QA, nunca fingir uso.

### Roteiro de cliente secreto (registrar navegador, viewport, data, build)

1. **Primeiros 5 segundos:** consigo dizer o que é, o benefício, como funciona, custo e o próximo passo? Teste com observadores reais quando possível.
2. **Primeiro clique:** CTA leva a valor ou impõe cadastro e formulário cedo demais? Transparência do teste gratuito.
3. **Primeira fala:** quantas ações até o aluno falar inglês? Erros de permissão, botões e fallback textual são claros?
4. **Conversa:** há objetivo comunicativo? Corrige sem humilhar nem interromper a cada palavra? Suporta hesitação, sotaque, interrupção, silêncio e falhas de rede?
5. **Feedback:** é específico, correto e acionável? Incentiva segunda sessão? Não inventa proficiência?
6. **Paywall:** entendimento e consentimento sem pressão enganosa, assinatura e cancelamento claros. Checkout real somente em sandbox/autorizado.
7. **Retorno:** usuário sabe o que treinar amanhã e vê progresso autêntico?
8. **Qualidade de interface:** mobile, teclado, semântica, contraste, Core Web Vitals observáveis, travamentos, legibilidade, e estética coerente com Tato.

Ao terminar cada fluxo, registrar `evidence_id`, passo exato, resultado observado, severidade, impacto provável, amostra e screenshot/log autorizado. O problema deve ser reproduzível, não opinião vaga.

## Criticidade do produto

- **P0:** pagamento irregular, dados expostos, prática/checkout amplamente indisponíveis.
- **P1:** fluxo essencial bloqueado para segmento significativo, voz impraticável, onboarding não permite falar, correção pedagógica prejudicial recorrente.
- **P2:** abandono, compreensão ruim, acesso difícil, conteúdo sem valor, performance pobre.
- **P3:** ajuste de estilo sem impacto concreto ou sem evidência.

Não atribuir severidade P1 a todo detalhe cosmético. Tratar designs visualmente genéricos como problemas de marca/conversão que pedem diagnóstico, não como evidência automática de perda de MRR.

## Entrega do diagnóstico

Formato: `sintoma → reprodução → evidência → hipótese causal → responsabilidade → menor correção → teste → medida após implantação`. Uma descoberta sem mecanismo de verificação não entra como entrega final.

### Investigar onboarding e conversação com profundidade

- Perfis: A0/A1 receoso, A2 que depende de pistas, B1 mais autônomo, sotaques brasileiros diferentes, ruído, usuário sem fone, pessoa com deficiência, desktop/mobile.
- Latência: separar espera de STT, pensamento, TTS, transporte e renderização se a instrumentação permitir. Não inventar latências por sensação.
- Pedagogia: distinguir frase funcional, correção de erro que altera sentido, fluidez preservada, variedade, relevância ao cenário, contexto e transferência para situações reais.
- Aprendizagem: usar tarefas equivalentes antes/depois quando possível; engagement isolado não prova aprendizagem.
- Privacidade: usar cenários sintéticos para e2e e áudio real somente com base legal, mínimo necessário e acesso apropriado.

## Reunião extraordinária de produto

Convocar CPO, CTO, Head of Learning, QA e Data quando a mesma falha envolve pelo menos duas áreas e impede correção. Agenda obrigatória: reprodução, causa provável, mudança pequena, DRI e dono de teste. Sem decisão ou bloqueio real, trabalhar assincronamente.

## Antipadrões

Não refazer todas as telas porque um agente encontrou AI slop. Não adicionar gamificação antes de resolver a primeira prática. Não insistir em tema de design que prejudica acessibilidade. Não proclamar vencedor A/B sem amostra e janela adequadas.