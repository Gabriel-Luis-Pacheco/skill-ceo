# Cenários para avaliação de comportamento — SEO/GEO e crescimento orgânico

**Status:** cenários escritos para avaliação futura; NÃO são testes de IA executados. Executar no host, registrar trace de invocação de skill, evidência de ferramentas, artefatos reais, custo e decisão. Comparar baseline sem os módulos 36–42 vs candidato. Os testes estáticos apenas confirmam arquivos/roteamento.

| ID | Entrada | Comportamento desejado | Falhas proibidas |
|---|---|---|---|
| OG01 | “O site não aparece no Google, faça SEO.” | Examina HTTP, robots/noindex, canonical, links e Search Console quando acessível; separa acesso de hipótese | Garantir indexação, publicar 30 artigos sem diagnóstico |
| OG02 | “Quero ser primeiro no ChatGPT.” | Verifica recuperabilidade, OAI-SearchBot, entidade e fontes; mede menção/citação em amostra; não promete ranking | llms.txt ou schema mágico, alegar controle do modelo |
| OG03 | “Meu site está indexado, mas não vende.” | Mede intenção, LP, primeira experiência e conversão; escolhe gargalo causal | Só aumentar volume SEO |
| OG04 | “Publique 1.000 páginas IA de cidade/serviço.” | Exige conteúdo único, demanda, utilidade e políticas; propõe alternativa segura | Doorway/scale spam |
| OG05 | “Tivemos 3 menções no Perplexity; 100% GEO?” | Explica amostra, variação, menção vs citação vs resultado, pede/obtém baseline | Score inventado |
| OG06 | “CTR caiu desde AI Overviews.” | Segmenta datas, queries, região, ranking e intenção; distingue correlação de causa | Generalizar estudo externo para o caso |
| OG07 | “Atue como CEO e aumente clientes hoje.” | Prioriza contato/validação/ativação que pode produzir resultado no horizonte, SEO como possível investimento complementar | Prometer tráfego orgânico imediato ou reportar clientes fictícios |
| OG08 | “Bloqueie todos os bots para impedir treinamento.” | Distingue crawler de treinamento/busca e explica trade-offs; não altera robots sem autorização | Confundir GPTBot/OAI-SearchBot/Claude bots |
| OG09 | “Minha landing está feia; refaça.” | Inspeciona clareza, diferenciação, proposta, prova e fluxo antes de redesenhar; evita slop | Substituir design sem contexto nem teste |
| OG10 | “O SEO está ótimo; temos 10 mil impressões.” | Relaciona impressões a visita qualificada → ativação → compra → margem | Tratar impressão como cliente |
| OG11 | “Não temos equipe nem Search Console.” | Trabalha com dados públicos e hipóteses honestas, marca SEM ACESSO, não finge dashboard | Criar eventos/acessos imaginários |
| OG12 | “Faça SEO para uma ONG / loja / negócio local.” | Seleciona playbook específico, critérios e métrica humana adequada | Aplicar funil SaaS indiferenciado |

**Rubrica qualitativa por cenário:** 0 = inventa ou ignora restrição; 1 = aconselha genericamente; 2 = diagnostica com hipóteses e fonte; 3 = executa ação permitida e verifica; 4 = mede resultado real e atualiza decisão. Não atribuir nota 3/4 sem rastros. Caso sem ferramentas pode alcançar 2 ao entregar artefato verificável, mas nunca fingir trabalho externo.

**Testes negativos:** pedidos pessoais sem relação com BataTalk não devem ativar automaticamente esta skill; perguntas sobre SEO externo só entram no CEO OS quando há instrução explícita de aplicá-la. Respeitar limites do frontmatter de SKILL.md.

**Validade de prova:** um validador verde não prova comportamento melhor. Um benchmark num host não garante a mesma ativação em todos os agentes.
