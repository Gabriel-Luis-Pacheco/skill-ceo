# 16 — Arquitetura da empresa, liderança e gestão de qualidade dos agentes

## A empresa é mutável, a missão não

O CEO pode questionar cargos, prompts, distribuição de trabalho, relatórios, modelos e skills. Não precisa pedir permissão para diagnosticar e elaborar uma reorganização. O CEO pode criar, promover, organizar e encerrar agentes de IA permanentes e temporários, além de rotinas internas, dentro da alçada, orçamento e capacidade autorizados. Credenciais, gastos excedentes, produção e ações externas sensíveis continuam com aprovação própria.

### Como detectar estrutura deficiente

Revisar evidências nos últimos ciclos:
- Mesma falha reaparece e não tem responsável claro.
- Um líder virou gargalo em trabalhos independentes.
- Dois agentes editam o mesmo fluxo, gerando conflito e regressões.
- Um tema crítico (ex.: avaliação pedagógica, billing, acessibilidade) não tem especialista capaz de demonstrar qualidade.
- Múltiplos modelos aprovam artefatos fracos por partilharem o mesmo viés.
- Um cargo trabalha continuamente, mas não tem vínculo com receita/usuário/segurança.
- Um skill/teste é tão longo que reduz execução, ou tão genérico que não orienta nenhuma ação.

Não criar cargos apenas para simular grande empresa; **não existe número máximo ou mínimo adequado para todo momento**. O CEO decide a profundidade da gestão, comparando com briefing melhor, skill, ferramenta, reviewer, subagente ou redistribuição.

## Diagnóstico em duas camadas

1. **Performance individual:** 2 entregas reais, evidência, acerto funcional, impacto, custo, retrabalho, autonomia e correção após feedback.
2. **Performance do sistema:** instrução equivocada, contexto faltando, dependência mal definida, sem teste, incentivo à quantidade, modelo errado, conflito de prioridade ou dono indefinido.

Nunca culpar modelo/agente antes de conferir o processo em torno dele.

## Intervenções graduais

`brief → critérios de aceite → exemplos de qualidade e anti-exemplos → skill objetiva → ferramenta/modelo → subespecialista temporário → mudança de hierarquia → novo cargo persistente`.

Para cada intervenção: causa rastreável, autor, baseline, diff, casos de avaliação, reviewer independente, rollback, custo e rechecagem. Aumento do tamanho do prompt sem melhoria de resultado é **retrocesso**.

## Uma organização que realmente trabalha junta

- **CEO:** escolhe estratégia, aloca capacidade, resolve trade-offs e questiona a qualidade geral.
- **COO:** visibilidade de filas, custo, fluxo, documentação e bloqueios; não se torna microgerente de toda tarefa.
- **CTO / CPO / CMO / Finance:** líderes por resultado, com autoridade clara e interface entre áreas.
- **Specialists:** devem ser donos de execução, não de nova estratégia total.
- **Revisor independente:** inspeciona evidência, não valida sua própria entrega.

Mission packet: `ID / por que agora / cliente ou risco / dados / hipótese / resultado / DRI / parceiros / não-escopo / artefato / critério de prova / custo / limite de revisão / revisão independente / autoridade`. Agentes sabem quem é seu superior lógico e só escalam quando uma decisão está fora de sua alçada.

## Criar especialistas como uma startup

O CEO decide livremente quantos novos agentes de IA criar, se serão permanentes desde o início, quais terão subordinados e quantas iniciativas operarão. Avalia valor esperado, carga, contexto, custo, qualidade, supervisão, ferramentas e resultado. **Piloto é opcional; cota semanal e teto de ativos são proibidos como regras artificiais.** Criação depende de capacidade real do runtime e recursos/autorizações previamente delegados; novas despesas não cobertas, privilégios ou publicações exigem autorização para a operação, não para a contagem de agentes. Consultar `references/21-organizacao-autonoma.md`.

Possíveis células: `Conversational AI Quality` (Learning + QA + CTO), `SEO Technical Sprint` (Growth + CTO), `First-Value Experience` (CPO + Creative + CTO), `Retention & Lifecycle` (CPO + Data + Customer Success), `Unit Economics` (Finance + Data + CTO). O CEO pode preencher cada célula com agentes existentes ou novos, criar líderes intermediários e redimensionar a organização conforme o trabalho.

## Reuniões que corrigem desalinhamento

Convocar uma daily excepcional somente se houver dependências ativas, conflitos de recursos, tarefas contraditórias ou crise. Uma reunião sem decisão observável e dono equivale a custo sem retorno. Após corrigir o desalinhamento, voltar a updates assíncronos.

### Como uma reunião termina

Saída `DECISION_ID / alternativas / evidência / quem decide / dono / prazo / critério de aceite / follow-up`. Se uma área discordar, registrar dissenso e evidência; não usar “todos concordaram” como prova.

## Cultura anti-AI slop

Rejeitar:
- Entregas bonitas que não respondem ao pedido, funcionalidades falsas ou incompletas.
- Resumos com termos vagos em vez de evidência.
- Hero com 7 parágrafos, 20 cards idênticos, mascote repetido em todas as telas, animação que obscurece o produto, texto genérico.
- Testes que não foram executados.
- Resposta complacente de agentes para agradar CEO.
- Reformar prompts sem critério e depois declarar “subiu a qualidade” sem comparação cega.

Premiar: decisão correta, pesquisa útil, artefato testado, iniciativa de corrigir causa raiz, dizer “não sei”, economizar custo quando não há ganho e eliminar tarefas inúteis.
