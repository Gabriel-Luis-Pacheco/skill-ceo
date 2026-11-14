# 38 — Como empresas e startups funcionam: valor, finanças e vocabulário

**Uso:** diagnosticar estágio, produto-mercado, receita, investimento, riscos de crescimento, preços e economia unitária. Sempre declarar período, população, fonte e convenções contábeis de cada número. Exemplo numérico é hipotético; não atribuir ao BataTalk.

## A ordem causal: da dor ao caixa

Dor relevante → ICP → pesquisa de alternativas reais → proposta → MVP para testar hipótese → ativação → retenção por coorte → conversão paga → economia unitária → aquisição repetível → crescimento sustentável. Processo não é rigidamente linear: iterar. **PMF não é evento que o fundador declara**, tampouco funding, nota de usuário, cadastro, tráfego ou curtida.

Modelos:
- SaaS: receita recorrente e custo de servir, retenção/expansão; observar contratos vs dinheiro.
- Marketplace: liquidez de dois lados, GMV, take rate, qualidade de match, repetição, concentração.
- E-commerce: frequência, margem por pedido, logística, capital de giro, devolução.
- Indústria: capacidade, yield, OEE, segurança, estoques, lead time, ROIC.
- Big Tech/plataforma: core, adjacências, infra, pesquisa, network effects, competição, antitruste e externalidades.

## Glossário de trabalho (PT/EN), fórmula e cautela

| Termo | Definição / cálculo simplificado | Cuidado |
|---|---|---|
| ICP | perfil de cliente de maior adequação e valor | não é demografia genérica; validar com comportamento |
| Persona | arquétipo para comunicação/design | não substitui evidência |
| JTBD | progresso buscado em situação real | função, não lista de features |
| Discovery | descobrir trabalho, barreiras e alternativas | perguntas hipotéticas geram viés |
| MVP | menor teste útil da hipótese de valor | não autoriza experiência insegura |
| PMF | adequação produto-mercado demonstrada por demanda e retenção | nenhuma métrica isolada prova |
| GTM | como distribuir, vender e servir | canal + mensagem + economia |
| PLG | adoção/expansão lideradas pelo produto | não elimina marketing |
| Inbound/Outbound | demanda que chega / contato iniciado | usar mix conforme ICP e economia |
| TAM/SAM/SOM | mercado total / atendível / realisticamente conquistável | TAM inflado engana decisão |
| Funnel | progressão por etapa até valor/receita | etapas e denominadores únicos |
| Conversion | conclusões elegíveis / entradas elegíveis | janela e amostra importam |
| Activation | primeiro comportamento de valor | clique e login não bastam |
| Retention | proporção que retorna por coorte | não misturar coortes |
| Churn de logos | clientes perdidos / clientes iniciais | não confundir com receita perdida |
| Revenue churn | receita recorrente perdida / base | expansão pode compensar apenas no NRR |
| GRR | (MRR inicial − churn − contraction) / MRR inicial | exclui expansão |
| NRR | (MRR inicial − churn − contraction + expansion) / MRR inicial | medir mesma coorte; novos não entram |
| MRR | receita recorrente mensal contratada elegível | não é faturamento recebido |
| ARR | MRR elegível × 12 | sazonalidade/contratos especiais exigem cuidado |
| ACV/TCV | valor anual / total de contrato | bookings não são receita reconhecida |
| GMV | valor de mercadorias/serviços transacionados | marketplace não reconhece tudo como receita |
| Take rate | receita de plataforma / GMV relevante | ganhos podem reduzir liquidez |
| ASP/AOV/ARPU | preço médio / pedido médio / receita por usuário | não comparar bases diferentes |
| COGS | custo direto de prestação/produção | classificação consistente |
| Gross margin | (receita − COGS) / receita | exclui muitos custos de aquisição |
| Contribution margin | receita líquida − custos variáveis incrementais | definir custos e devoluções |
| CAC | despesas atribuíveis de aquisição / novos clientes atribuíveis | escopo, orgânico e salários |
| LTV | margem de contribuição esperada ao longo da vida | churn imaturo gera fantasia |
| LTV/CAC | economia esperada / aquisição | só com cohort e premissas sólidas |
| CAC payback | CAC / margem de contribuição mensal incremental | não calcular se margem não positiva |
| Burn líquido | saídas de caixa − entradas de caixa | EBITDA não é caixa |
| Runway | caixa disponível / burn líquido, se estável e positivo | use forecast de caixa em mudanças |
| FCF | caixa operacional menos capex | convenções variam |
| ROIC | lucro operacional após impostos / capital investido | capital e ajustes coerentes |
| EBITDA | lucro antes de juros, tributos, depreciação e amortização | não é geração de caixa |
| Working capital | ativos circulantes operacionais − passivos circulantes operacionais | recepção/pagamento importam |
| DSO/DPO/DIO | prazo de recebimento/pagamento/estoque | ciclo de caixa = DSO + DIO − DPO |
| Cap table | propriedade e direitos após diluição | fully diluted e instrumentos convertíveis |
| Equity/dilution | participação / redução percentual após emissão | diluir pode criar valor |
| Vesting/cliff | aquisição gradual / prazo mínimo inicial | acordos dependem de lei |
| SAFE/convertible | instrumento conversível em equity | valuation cap e discount acumulam diluição |
| Term sheet | termos preliminares de investimento | nem sempre é vinculante em tudo |
| Pre-money/post-money | valuation antes / depois de aporte | post = pre + novo aporte, no caso simples |
| Liquidation preference | prioridade de recebimento em saída | altera retorno do founder |
| Venture debt/covenant | dívida de growth / obrigação contratual | dívida não conserta PMF |
| Burn multiple | burn líquido / new net ARR no período | não serve em pré-receita |
| NPS/CSAT/CES | recomendação / satisfação / esforço | nunca inferir causalidade automaticamente |
| OEE | disponibilidade × performance × qualidade | métrica industrial |
| SLO/SLA | objetivo/compromisso de nível de serviço | erro e downtime têm custo |
| IPO/M&A | abertura de capital / fusões e aquisições | governança, assessoria e diligência |
| Network effects | produto mais valioso com participantes | distinguir efeito real de crescimento simples |
| Switching costs | custo de mudar fornecedor/solução | não confundir lock-in ruim com valor |

## Exemplo auditável de unit economics

Assuma uma assinatura de R$ 60/mês, impostos/taxas/reembolsos efetivos alocados R$ 8 e custos variáveis de voz/modelo/infra/suporte R$ 22: **contribuição mensal = R$ 30**. Se CAC completo = R$ 90, **payback simplificado = 3 meses**, sujeito a churn e estabilidade. Se a pessoa sair antes de três meses, o canal poderá perder dinheiro. Não use receita bruta de R$ 60 como contribuição de R$ 60.

Marketplace hipotético: GMV de R$ 1 milhão e take rate de 10% = receita bruta de plataforma de R$ 100 mil, antes de custos, estornos e reconhecimento contábil aplicável.

SaaS B2B hipotético: CAC R$ 40 mil; margem de contribuição incremental mensal R$ 8 mil → payback simplificado 5 meses. Se não se pode atribuir vendas/custos por cliente, sinalizar modelo, não fato. Receita que cresce enquanto NRR cai exige decomposição por coorte.

## Captação e administração

Bootstrapping: crescer com capital próprio/caixa, preservando controle e aumentando restrição de liquidez. Venture capital: alta assimetria e diluição em troca de capital para uma tese de alto crescimento; é escolha de modelo, não troféu. Antes de captar: calendário de runway, cap table fully diluted, métricas por coorte, cenário de redução, caixa e plano de uso com milestones. Consultar advogado/contador local antes de emitir equity, SAFE, dívida ou instrumento equivalente; modelos da NVCA são referência norte-americana, não contrato brasileiro pronto.

**Separar em toda reunião:** venda contratada, receita reconhecida, receita faturada, caixa recebido, receita recorrente elegível, margem de contribuição e resultado econômico. Não chame lead de comprador, trial de pagante ou transação de teste de receita.

Fontes: [YC — advice](https://www.ycombinator.com/library/4D-yc-s-essential-startup-advice), [YC — PMF](https://www.ycombinator.com/blog/the-real-product-market-fit/), [a16z — métricas](https://a16z.com/16-startup-metrics/), [NVCA — documentos de VC](https://nvca.org/model-legal-documents/).