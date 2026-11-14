# 43 — Governança, pessoas, IA, risco e visão macro

> Leitura para decisões que mudam controle, risco, relação com board, cultura, dados ou tecnologias. Não substitui advogado, contador, profissional de cibersegurança ou conselho. Aplicar lei da jurisdição real; referências americanas não regem automaticamente empresas brasileiras.

## Conselho e deveres de administração

Board supervisiona estratégia, risco, desempenho do CEO, grandes investimentos, sucessão e prestação de contas; gestão executa dentro de alçada. Empresas brasileiras variam conforme estrutura societária, acordo de sócios e normas locais. Em Delaware há deveres fiduciários de cuidado/lealdade; em companhias públicas dos EUA há regras SEC/Sarbanes-Oxley e controles. Não importar regras sem verificar.

**Board pack útil:** tese da empresa, desempenho vs plano, caixa/forecast, clientes/cohorts, operações, pessoas/sucessão, risco/controles, capital allocation, cenários, decisões solicitadas. Separar eventos materiais de anedotas, uso de caixa de EBITDA e escolhas de dados. Conselho precisa ouvir contradições reais, não só boas notícias.

## Alocação de capital

Comparar incrementos de investimento pelo retorno ajustado ao risco, cenário downside, tempo, irreversibilidade e custo de oportunidade. Capex, P&D, equipe, M&A, marketing, recompras e redução da dívida concorrem por recursos; selecionar pelo contexto. Não usar valuation elevado como autorização para desperdiçar caixa. Pedidos de orçamento precisam trazer hipóteses, milestones e kill criteria.

## Pessoas e cultura

A melhor cultura é comportamento observável: recompensar bom julgamento, respeitar pessoas, admitir erro, reportar incidentes, ouvir cliente e concluir trabalho. Cultura permissiva com abuso cobra custo de rotatividade, qualidade e risco. Contratar por scorecard do trabalho e referências, evitar discriminação e acessar informação humana só com base legítima. Criar sucessão para funções cuja saída ameaça continuidade. CEO, CFO e CHRO precisam discutir capacidade organizacional **junto com economics**.

**Fato → feedback → mudança:** em 1:1 observar evento, impacto, ouvir contraponto, acordar expectativa, prazo e revisão; não substituir por julgamento de personalidade.

## AI como portfólio gerido

Quatro fontes de valor: eficiência interna, melhoria de produto, novo negócio e mitigação de risco. Para cada uso: hipótese econômica, baseline, owner, dados e direitos, classe de risco, evals em amostras representativas, segurança, privacidade, custo marginal, monitoramento, falhas, fallback, kill switch e rota de incidentes. Para agentes: permissões técnicas mínimas, proteção contra prompt injection, logs, autorização de efeitos externos, idempotência e verificação de destino.

Adaptação do **NIST AI RMF**: Govern (papéis e regras), Map (contexto e riscos), Measure (métricas e avaliação), Manage (controle e resposta). NIST não concede conformidade automática nem prova ausência de dano. Se dados pessoais são tratados, observar LGPD e normas aplicáveis. CISO deve poder elevar riscos críticos com independência; o CEO não pode esconder um risco para preservar KPI.

## Radar de cenário externo

| Sinal | Mecanismo | Pergunta ao CEO |
|---|---|---|
| juros sobem | capital mais caro/pressão de caixa | quais apostas dependem de funding? |
| câmbio oscila | fornecedor/modelo/hosting em moeda estrangeira | margem de contribuição está exposta? |
| recessão/setor retrai | maior fricção de compra/churn | ICP e oferta resistem? |
| regulação muda | obrigação legal/custo/prazo | o que exige adequação imediata? |
| plataforma altera termos | tráfego/APIs/preços | existe dependência concentrada? |
| AI commoditiza feature | diferenciação e custo de servir | qual vantagem não desaparece? |
| conflito geopolítico | suprimento, energia, acesso | alternativa e continuidade? |
| benchmark do concorrente | expectativa de cliente muda | que problema real ficou mal resolvido? |

Não gerar alertas fictícios; consultar fontes atuais quando decisão depende delas. Se há incerteza, explicitar horizontes e cenários adversos.

## Risco e escala

Mapear riscos por probabilidade, impacto, detectabilidade, velocidade e controle, sem fingir precisão em números arbitrários. Incidentes de alta severidade requerem runbook, responsável e escalada. Empresa pequena usa controles proporcionais; Big Tech requer compliance global, resiliency, gestão de terceiros e conselho. A **defesa é um sistema**, não apenas treinamento de prompts ou boa intenção.

## Macro para micro

Uma mudança de câmbio só importa se altera custo de inferência, preço, caixa ou investimento. Uma mudança cultural só importa se muda contratação, incentivos, retenção, produção ou confiança. Uma aposta tecnológica só importa se existe baseline, avaliação e ROI provável. Não criar apresentações sem ponte causal.

**Fontes-base:** https://www.oecd.org/en/publications/g20-oecd-principles-of-corporate-governance-2023_ed750b30-en/full-report/component-8.html ; https://www.nist.gov/itl/ai-risk-management-framework/ai-risk-management-framework-resources ; https://www.sec.gov/newsroom/press-releases/2023-139 ; https://www.spencerstuart.com/research-and-insight/chro-at-the-center-maximizing-the-impact-of-ceo-succession-planning ; https://www.mckinsey.com/capabilities/strategy-and-corporate-finance/our-insights/capital-allocation-starts-with-governance-and-should-be-led-by-the-ceo
