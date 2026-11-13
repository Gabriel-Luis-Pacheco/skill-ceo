# Sensores executivos universais — funcionam com qualquer host que os suporte

**Este arquivo é um contrato de sensoriamento, não um agendador.** Nenhuma rotina fica ativa pelo fato de a skill existir. Instale os gatilhos no host real — GrokBot, OpenBot, cron externo, backend de automação ou outro — se disponível, útil e autorizado. Em Claude/Codex sem rotina persistente, execute manualmente quando acionado. Não mentir que monitora 24/7.

## Contrato mínimo de cada sensor

`id | fonte | pergunta | condição de disparo | frequência/evento | janela de comparação | custo/limite | deduplicação | DRI | alçada | resultado esperado | próxima checagem`

Apenas um sinal novo e material deve mobilizar o CEO. Se não houve mudança, registrar silenciosamente quando o host permitir; não mandar “tudo certo” sem inspeção. Se fonte falhar, marcar `SEM_ACESSO`, não `ZERO`.

## 1. Pulso de clientes, receita e experiência

Cadência proporcional ao volume do negócio (ex.: dias úteis). Ler apenas dados permitidos e comparáveis:
- novos usuários externos, primeira fala útil, conclusão/retorno;
- compra realmente paga, receita/margem depois de custos;
- pipeline comercial: identificados, **contatados**, respostas, testes reais, afiliados ativos;
- erros de microfone, checkout e voz.

**Ação:** identificar a maior restrição e executar uma intervenção segura/permitida, registrar evidência. Se dados não estão disponíveis, não criar relatório falso.

## 2. Radar concorrentes, marketing, SEO/GEO e tendências

Cadência normalmente mais lenta e com fontes atuais: mudanças observáveis de oferta/preço/copy/primeira experiência, conteúdo relevante ao ICP, Search Console quando acessível, busca/crawling técnico, comportamento de canais e novos formatos.

**Ação:** para cada alteração material, explicar `mecanismo → impacto plausível → evidência → custo → decisão TESTAR/OBSERVAR/IGNORAR`. Evitar “trending!” sem data, FOMO, scraping indevido ou postagem automática.

## 3. Radar de qualidade, conhecimento e organização

Baseado em entregas recentes e reclamações recorrentes:
- AI slop, textos técnicos demais, UX interna confusa, design que não converte em entendimento, código quebrado;
- tarefas duplicadas, custo por entrega, erros de contexto, qualidade de modelos e skills;
- qual conhecimento de estratégia, finanças, psicologia ou aprendizagem está faltando para decidir melhor.

**Ação:** encontrar a causa, melhorar procedimento/modelo/brief/prova e testar. Não criar gerência ou documento por inércia.

## 4. Gatilhos de incidentes

Voz, cobrança, segurança, perda de dados, credenciais e gasto anormal são prioridade crítica. Idealmente webhook/monitor real, não polling de IA como detector único. Investigar e conter somente dentro de alçada; preservar logs, não prometer que recuperou antes de teste.

## Sensor de omissões do CEO

Disparar por evidência, não por calendário decorativo: fundador precisou repetir correção, tarefa marcada “concluída” sem prova, linha de receita não avança, mensagens ficam apenas em rascunho, mesma fricção reaparece, agentes produzem relatórios sem cliente. Inspecionar o episódio, registrar **falha do próprio CEO**, identificar causa verificável e realizar correção dentro da alçada. Usar [protocolo 34](../references/34-proatividade-autocalibracao-e-execucao.md). Não confundir sensor descrito com automação realmente instalada.

## Economia e limites

- Começar pelo menor conjunto de sensores que detecte mudanças de alto valor; ampliar por evidência.
- Verificar primeira execução e registrar IDs/resultado; falha sem logs não autoriza afirmar monitoramento.
- Contato externo, publicação, mudança de preço/cobrança e gasto fora do orçamento exigem autorização apropriada.
- Em ambientes com processo intermitente, não manter uma rotina “ativa” no papel; usar checklist e checkpoint na retomada.
- Quando há várias plataformas, um sistema é a fonte da verdade do estado; não duplicar alerta entre quatro bots.

Adaptadores opcionais: [../adapters/README.md](../adapters/README.md). Núcleo: [../references/32-contrato-universal-multiplataforma.md](../references/32-contrato-universal-multiplataforma.md).
