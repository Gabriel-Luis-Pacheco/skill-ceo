# 11 — Adaptação prática ao OpenBot

Este pacote foi desenhado para **OpenBot de openbot.run** (workspace local-first com OpenCode, Codex etc.), não para outros projetos que usam o nome OpenBot, nem para OpenClaw. Confirme a versão e as ferramentas disponíveis antes de supor que uma ação está instalada.

## Componentes verificáveis do produto

- Cada agente tem seu próprio workspace, conversa e fila; há canais compartilhados, transferências e coordenação entre agentes.
- Skills locais são pastas com `SKILL.md`, referências e scripts opcionais. A biblioteca local pode ter versões e ser adicionada aos agentes.
- O agente pode usar funcionalidades de skills como `create_skill`, `list_local_skills`, `read_local_skill`, `revise_skill` e `install_local_skill` se estiverem expostas na instalação/versão.
- Rotinas são instruções agendadas que executam o agente; criar arquivos de rotina não as agenda automaticamente. Eventos de webhook do OpenBot podem ser deduplicados pelo ID de entrega documentado, mas **não** garantem execução única dos efeitos da tarefa; cada integração sensível precisa de sua idempotência.
- Dependendo da versão/configuração, existem navegação, Computer Use e ferramentas externas. Conferir cada capacidade em vez de inventar um comando.
- A documentação oficial informa que **deletar um agente remove workspace, anexos e algumas entregas**. Para liberar capacidade, preferir pausar/arquivar; verificar backup/transferência e alçada antes de exclusão definitiva.
- Nas versões de desenvolvimento, agentes podem rodar com `danger-full-access` e `approvalPolicy: never`. A política escrita não substitui isolamento, ACLs ou autorização prévia.

## Primeiro inventário de capacidades

O CEO deve perguntar às ferramentas/ambiente, não ao usuário se os dados puderem ser obtidos: listar agentes e status quando interface permitir, filas, canais, skills disponíveis, rotinas, fontes de negócio e acessos. Deixar campos `SEM ACESSO` se não houver ferramenta. Não tentar escrever diretamente no banco interno do OpenBot ou manipular seus arquivos de configuração para simular criação de agentes.

## Compartilhamento

Usar workspace compartilhado do OpenBot para registros de decisões e handoffs **se existir e estiver autorizado**. Definir um único local para `ceo/`. Evitar segredos no shared. A pasta `~/OpenBot/Shared` é indicada pela documentação do projeto como diretório compartilhado típico, mas validar no host antes de escrever; em instalações remotas o caminho pode ser diferente. Não mover/destruir o workspace de outros agentes.

## Skill autoevolutiva

Se `revise_skill` estiver disponível: obter versão atual, preparar diff, testar, chamar revisão com versão conhecida, verificar se a nova revisão está instalada no CEO e nos agentes certos. A documentação indica que uma biblioteca revisada não atualiza automaticamente cópias instaladas; verificar instalação/atualização. Se a ferramenta não existir, preparar pasta versionada e instrução para o operador.

## Cuidado com autopropagação

Não instalar esta skill em todos os 14 agentes: ela concede mandato executivo e pode causar múltiplos “CEOs” conflitantes. Deixar no **CEO**. Para áreas especializadas, distribuir somente playbooks específicos como referência ou skills separadas sem autoridade organizacional.

## Teste após instalação

Pedir ao CEO um diagnóstico restrito, conferir se ele leu `SKILL.md`, se consulta a referência correta, se separa fatos de hipóteses e se não assume ferramentas ausentes. Em seguida configurar apenas rotinas com valor comprovado.

Fontes: https://github.com/nightly-labs/openbot ; https://openbot.run/news/routines-give-an-agent-a-schedule ; https://openbot.run/guides/openbot-marketplace
