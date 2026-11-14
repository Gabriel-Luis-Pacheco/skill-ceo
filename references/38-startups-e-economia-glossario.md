# 38 — Como a empresa funciona: startup, finanças, capital e glossário executivo

> Acione para validação, oferta, funil, investimento, unit economics, métricas, SaaS, marketplace, indústria e Big Tech. Valores e fórmulas exigem definição, período, cohort e moeda. Nunca inventar dados da empresa.

## Sistema de criação de valor

Dor real → segmento/ICP → pesquisa de comportamento → menor teste honesto (MVP) → ativação → retenção e disposição real de pagar → distribuição repetível → economics → capacidade operacional → vantagem → realocação. **PMF não é financiamento, elogio, cadastro ou cobertura de mídia**. Para produto gratuito, verificar retorno e progresso do usuário antes de monetização.

Fases de capital: bootstrapping (receita própria), angel, pre-seed, seed, Série A/B/C, venture debt, private equity, IPO, dívida/mercado público. Cada instrumento altera controle, obrigações, diluição, liquidez e custo de capital. SAFE (instrumento conversível, especialmente estrutura americana) não é equivalente a participação já emitida; simular cap table fully diluted e sensibilidade a novos rounds. Consultar jurídico local.

## Glossário operacional PT/EN com erros e fórmulas

| Termo | Significado / cálculo básico | Erro a evitar |
|---|---|---|
| ICP — ideal customer profile | comprador/usuário com dor, contexto, valor e canal semelhantes | persona demográfica vazia |
| JTBD — jobs to be done | progresso buscado em circunstância real | lista de funcionalidades |
| Discovery | descobrir problema e alternativa por comportamento passado | pesquisa só com amigos |
| MVP | menor experimento útil para hipótese específica | lançar produto ruim como fim |
| PMF | demanda com sinais persistentes de uso/retorno/pagamento | declarar após investimento |
| TAM | mercado endereçável total sob premissas explícitas | população total × preço arbitrário |
| SAM | fatia que oferta pode servir | ignorar idioma e regulação |
| SOM | fatia possível de conquistar | forecast disfarçado de mercado |
| GTM | go-to-market: aquisição, vendas, entrega e expansão | apenas mídia |
| PLG | produto como principal motor de aquisição/adoção | achar que elimina marketing/vendas |
| Inbound | demanda que procura a empresa via conteúdo/busca/referrals | esperar tráfego sem distribuição |
| Outbound | prospectar diretamente dentro de regras/consentimento | spam como escala |
| BDR/SDR/AE/Closer | prospecção/qualificação/venda: funções ajustadas ao ticket/ciclo | contratar estrutura antes do PMF |
| MRR | receita recorrente mensal normalizada, sem evento pontual | contabilizar checkout isolado |
| ARR | MRR recorrente × 12, no mesmo critério | incluir serviços não recorrentes |
| Bookings | valor comercial fechado contratualmente | confundir com receita reconhecida |
| Billings | valor faturado/cobrado | confundir com caixa recebido |
| Revenue | receita reconhecida conforme regime contábil | confundir com recebimento |
| ARPA/ARPU | receita média por conta/usuário em período | misturar conta e pessoa |
| ACV/TCV | valor anual / total de contrato | confundir desconto ou termo |
| CAC | custo de vendas + marketing atribuíveis / novos clientes | excluir trabalho e janela |
| CAC payback | CAC / contribuição bruta mensal inicial por cliente | payback sem margem ou churn |
| LTV | valor presente de margem de contribuição esperada na vida cliente | fórmula receita/churn com amostra pequena |
| LTV/CAC | eficiência econômica com metodologia consistente | ótimo em cohorts minúsculos |
| Logo churn | contas perdidas / contas iniciais | confundir com receita |
| Revenue churn | receita recorrente perdida / base inicial | ignorar expansão quando se diz net churn |
| GRR | (MRR inicial – churn – contraction) / MRR inicial | adicionar upsell |
| NRR | (MRR inicial – churn – contraction + expansion) / MRR inicial | misturar novos clientes |
| Gross margin | (receita – COGS) / receita | custos inconsistentes |
| Contribution margin | receita líquida – custos variáveis incrementais | misturar custo fixo |
| Burn (net) | caixa operacional líquido consumido por mês | usar resultado contábil |
| Runway | caixa disponível / burn futuro médio, se burn positivo e estável | fingir precisão com burn variável |
| EBITDA | resultado operacional antes de juros, impostos, depreciação e amortização | tratá-lo como caixa |
| FCF | fluxo de caixa operacional – capex, segundo convenção definida | omitir capital de giro |
| ROIC | NOPAT / capital investido médio (definir metodologia) | comparar períodos/bases diferentes |
| GMV | valor bruto transacionado no marketplace | contar GMV como receita |
| Take rate | receita da plataforma / GMV elegível | ignorar devoluções e incentivos |
| OEE | disponibilidade × performance × qualidade de equipamento | tratar como KPI universal |
| OTIF | entregas no prazo e completas / total elegível | confundir pontualidade com qualidade |
| Cohort | grupo que começou em mesmo período/canal | olhar só média agregada |
| North Star Metric | atividade correlacionada a valor entregue ao cliente | métrica de vaidade |
| WTP | willingness to pay, disposição a pagar demonstrada | pergunta hipotética como compra |
| NPS / CSAT / CES | recomendação / satisfação / facilidade | medir sem retenção/resultado |
| Burn multiple | net burn / net new ARR, quando adequado | dividir por zero ou métricas incompatíveis |
| NDR/NRR | nomenclatura de retenção líquida | usar definições distintas sem avisar |
| Cap table | tabela de propriedade atual e potencial | esquecer opções e convertíveis |
| Vesting / cliff | aquisição gradual / primeira carência de equity | concessão irrevogável imediata |
| Dilution | queda percentual de participação após emissão | confundir com perda automática de valor |
| SAFE | instrumento que pode converter em equity | ignorar valuation cap/discount |
| Term sheet | termos preliminares de investimento | tratar tudo como não vinculante |
| Covenant | obrigação contratual de dívida | esquecer gatilhos e vencimentos |
| Working capital | ativo circulante operacional – passivo circulante operacional | olhar lucro sem caixa |
| Cash conversion cycle | DIO + DSO – DPO (em dias) | negociar prazo sem fornecedor |
| CAC blended/paid | combinado de canais vs aquisição paga | comparar sem distinguir |
| Win rate | negócios ganhos / oportunidades elegíveis | mudar denominador entre meses |
| Pipeline coverage | pipeline qualificado / meta de vendas do período | inflar oportunidades |
| Net dollar retention | variante de NRR | comparar metodologias diferentes |

## Exemplo quantitativo de SaaS B2B (fictício)

Receita recorrente mensal inicial por cliente = R$ 1.000; margem bruta = 80%; CAC = R$ 4.000. **Payback bruto simplificado = R$ 4.000 / (R$ 1.000 × 0,8) = 5 meses**. Isso ignora curva de uso, margem de contribuição incremental e churn. Se 20% dos clientes saem no primeiro mês, o payback observado do cohort pode ser bem pior. Diagnóstico: dividir por segmento/canal/cohort; medir ativação, churn, suporte e cash payback antes de dobrar aquisição.

## Modelos de empresa: o que comparar

- **SaaS B2B:** ARR, NRR/GRR, logo churn, ACV, payback, time-to-value, suporte, pipeline, gross margin.
- **B2C assinatura:** primeira experiência, retenção D7/D30, contribuição por sessão, reembolso, expansão, referrals e confiança.
- **Marketplace:** ambos os lados, liquidez, match rate, supply/demand, GMV, take rate, repeat e custo de incentivos.
- **Indústria:** demanda, capacidade, OEE, yield, lead time, scrap, capital de giro, energia, logística, segurança, ROIC.
- **Big Tech/plataforma:** core cash engine, complementos, efeitos de rede, custos de infraestrutura, concentração, falhas sistêmicas, M&A, regulação.

## Diagnóstico quando crescimento não vira valor

1. Validar dados, unidade e período.
2. Separar preço, volume, mix, retenção e crescimento de base.
3. Comparar custo marginal e contribuição por cohort (não só receita).
4. Examinar capital de giro, cobranças e caixa.
5. Verificar qualidade, churn, regressão e risco reputacional.
6. Escolher o gargalo com evidência; planejar teste, dono e stop condition.

**Fontes:** https://www.ycombinator.com/library/4D-yc-s-essential-startup-advice ; https://www.ycombinator.com/blog/the-real-product-market-fit/ ; https://a16z.com/16-startup-metrics/ ; https://nvca.org/model-legal-documents/
