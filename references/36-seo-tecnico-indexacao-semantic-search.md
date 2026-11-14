# 36 — SEO técnico, descoberta, indexação e arquitetura: manual de diagnóstico

**Quando ler:** site não aparece, perdeu tráfego, páginas não indexam, plataforma usa JavaScript, migração, e-commerce, SEO local/internacional ou auditoria técnica. Complementa a referência 05. **Não executar correções cegas.** Verificar versão publicada, ambiente, autorização e impacto comercial.

## 1. Modelo causal de Search

Fluxo abstrato: descoberta de URL → crawling → rendering (quando necessário) → extração → agrupamento/canonicalização → indexação → recuperação/ranking → apresentação. Uma URL pública não tem garantia de crawl, indexação ou posição. A localização do defeito define o tratamento:

| Sinal observado | Hipóteses concorrentes | Como provar | Ação com menor risco |
|---|---|---|---|
| Nenhuma URL no índice | site novo, robots, noindex, indisponibilidade, erro de propriedade | logs, HTTP, inspeção URL, Search Console | corrigir barreira comprovada e reenviar sitemap |
| Apenas home indexada | links internos, JS, qualidade, canônicas, isolamento | HTML renderizado, rastreamento interno, GSC | incluir caminhos HTML e melhorar páginas reais |
| URLs descobertas mas não indexadas | duplicação, pouca utilidade, crawl, canonical | amostra de páginas, HTML, duplicatas | consolidar e diferenciar; não forçar indexação em massa |
| Queda súbita | deploy, redirecionamento, mudança de intenção, concorrente, atualização, sazonalidade | compare períodos, notas de deploy, logs e SERPs | primeiro isolar causa; não reescrever tudo |
| Impressões sobem, cliques caem | SERP mudou, AI Overviews, posição, intenção, snippet | GSC por consulta/dispositivo/país | revisar intenção e captar valor também sem clique |
| SEO bom, zero vendas | tráfego desalinhado, UX, preço, produto, medição | origem → ativação → receita, entrevistas | corrigir funil, não publicar mais artigos |

## 2. Diagnóstico em ordem de dependência

**Disponibilidade/HTTP** — confirmar 200 para páginas úteis, 301/308 permanente em migrações, 404/410 para removidas, não transformar erros em 200 (soft 404), HTTPS e ausência de 5xx intermitentes. Checar WAF, Cloudflare, rate limit e bloqueio seletivo de crawlers legítimos. Crawlers devem receber conteúdo equivalente ao humano; não fazer cloaking.

**Crawl** — inspecionar robots.txt real; ele instrui rastreamento, não é mecanismo confiável para desindexar uma URL já descoberta. Para excluir do índice, usar noindex de modo que o robô consiga acessar a página, ou outros mecanismos oficiais. Confirmar anchors HTML com href, links internos, páginas órfãs, navegação e parâmetros. Não depender somente de botões JS para descobrir URLs.

**Canonical e duplicação** — escolher URL preferida, usar rel=canonical consistente com links internos e sitemap, redirecionamentos e versão HTML. Canonical é sinal, não comando absoluto. Para duplicação deliberada de variantes, testar política adequada; não apontar indiscriminadamente todas as páginas de produto à categoria.

**Indexação** — Search Console para cobertura, inspeção e canonical escolhida; Bing Webmaster para equivalente. Validar que URLs de sitemap sejam canônicas, indexáveis e atualizadas. Sitemap auxilia descoberta, não garante indexação. Remover URLs inúteis do sitemap; não bloquear por reflexo páginas de negócio relevantes.

**Renderização** — verificar HTML de resposta e DOM renderizado, especialmente H1, descrição, conteúdo principal, preço, links internos, schema e canonical. SSR/SSG/pré-renderização podem reduzir risco de conteúdo JS inacessível para agentes com menos capacidade de rendering; não são exigência universal. Conferir diferenças entre resultado no navegador e acesso sem JS.

**Arquitetura** — home → categorias/soluções → situações de uso/problemas → páginas específicas, breadcrumbs, ligações contextuais com âncoras descritivas. Organizar pelo raciocínio do cliente; evitar milhares de taxonomias sem conteúdo.

**Performance e acessibilidade** — medir dados reais de usuários: LCP bom até 2,5 s; INP até 200 ms; CLS até 0,1 no percentil 75. Analisar Core Web Vitals por dispositivos e templates; depois reduzir JS, imagens, fonts, scripts de terceiros e deslocamento visual. Não trocar confiança e clareza por uma pontuação de laboratório. HTML semântico, foco teclado, labels e contrastes também ajudam pessoas e agentes.

## 3. Camada semântica e sinais de confiança

Título e heading devem corresponder à pergunta, sem keyword stuffing. Dar nome explícito à empresa, categoria, produto, atributos, público, problemas que resolve, autores reais e entidades relacionadas; exemplos e fontes precisam estar no conteúdo. Links editoriais externos e reputação verdadeira complementam o site.

Dados estruturados **não** fabricam autoridade nem garantem rich result. Implementar somente tipos adequados e suportados, coerentes com o conteúdo visível: Organization, BreadcrumbList, Article, VideoObject, LocalBusiness, Product/Offer, conforme caso. Validar com ferramentas oficiais e monitorar relatórios. Não inventar estrelas, reviews ou FAQs.

E-E-A-T é lente de qualidade (experiência, expertise, autoridade, confiança), **não uma pontuação isolada** ou um atributo obtido ao adicionar bio fictícia.

## 4. Situações específicas

**SaaS:** páginas de problema, caso de uso, integração, comparação justa, documentação, recursos e segurança; indexar somente demonstrações públicas verdadeiras. Evitar indexar rotas de login, dados privados ou páginas finas.

**E-commerce:** páginas de categoria/variantes, filtros/facetas e URLs limpas, preços e estoque coerentes, Product/Offer quando elegíveis, Merchant Center e imagens originais. Controlar combinações infinitas de filtros e parâmetros; usar canonical/noindex/robots de acordo com necessidade e documentação, não regra automática.

**SEO local:** Google Business Profile com categoria, serviços, informações, horário e fotos reais; avaliações legítimas, referências locais e páginas por unidade/serviço real. Relevância, distância e proeminência influenciam resultados; não existe controle sobre distância do usuário.

**SEO internacional:** URLs por idioma/região quando pertinente; traduções localizadas para intenção, moeda, prova, normas e linguagem; hreflang correto e recíproco. Evitar depender somente de geolocalização/IP para exibir variante.

**Imagens/vídeos:** mídias úteis e originais com contexto textual, filename informativo, alt descritivo quando aplicável, thumbnail, transcript quando útil e VideoObject elegível. Multimodal não substitui texto acessível.

**Bing/IndexNow:** considerar IndexNow para URLs criadas/alteradas/removidas, especialmente sites dinâmicos; não presumir que submissão implique ranking.

## 5. Checklist de evidência do CEO

Entregar planilha ou quadro com: URL/template; sintomas; resultado HTTP; robots; meta noindex; canonical declarada/escolhida; sitemap; links de entrada; HTML/JS; schema; CWV; página de referência; impacto comercial; esforço; confiança; owner; evidência antes/depois. Priorizar desbloqueio técnico antes de volume editorial.

**Critério de aceite:** páginas essenciais recuperáveis por crawler autorizado, status e canonicals coerentes, links funcionais, ausência de bloqueios involuntários, monitoramento instalado e nenhuma afirmação de indexação/resultado sem confirmação real.

## Fontes oficiais para revalidação

- Google Search — funcionamento: https://developers.google.com/search/docs/fundamentals/how-search-works
- Google Search — SEO para JavaScript: https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics
- Google Search — helpful content: https://developers.google.com/search/docs/fundamentals/creating-helpful-content
- Google Search — spam: https://developers.google.com/search/docs/essentials/spam-policies
- Google Search — internacional: https://developers.google.com/search/docs/specialty/international
- Google Search — e-commerce: https://developers.google.com/search/docs/specialty/ecommerce
- Google Search — dados estruturados: https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data
- Web Vitals: https://web.dev/articles/vitals
- Google Business Profile — ranking local: https://support.google.com/business/answer/7091
- Bing Webmaster Guidelines: https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a

Revalidar documentação antes de mudança importante; publicado em 14/11/2026, sem garantia de que o ambiente do negócio corresponda ao manual.
