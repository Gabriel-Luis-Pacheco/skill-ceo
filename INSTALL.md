# Instalar o BataTalk CEO OS em qualquer ambiente

**A única fonte canônica é esta pasta**: `SKILL.md`, `CEO_SYSTEM_PROMPT.md`, `POLICY.md`, `references/`, `adapters/`, `setup/`, `tests/`. Não reescrever a inteligência para cada software. O suporte nativo a diretórios `SKILL.md` varia; quando não existir, usar como instruções e referências textuais.

## Passo 1 — Obtenha a versão canônica

Clone ou baixe `https://github.com/Gabriel-Luis-Pacheco/skill-ceo` numa pasta que o agente tenha permissão para ler. Em ambientes de código com Git, `git clone` ou `git pull --ff-only` em diretório já existente. Clonar/atualizar o Git **não prova** que uma skill importada numa biblioteca remota foi atualizada. Verificar commit e conteúdo efetivamente carregado.

**Não instalar publicamente segredos, tokens, dumps de CRM, credenciais, logs pessoais ou dados de clientes.** O repositório da skill deve conter processo, não acesso privilegiado.

## Passo 2 — Escolha o modo de uso

| Ambiente | Forma provável de carregamento | Verificação obrigatória |
|---|---|---|
| **Claude Code** | Diretório com `SKILL.md` em `.claude/skills/batatalk-ceo-operator/` ou localização pessoal suportada | Skill visível/lida, referências acessíveis; versão atual |
| **Codex** | Diretório com `SKILL.md` em `.agents/skills/batatalk-ceo-operator/` ou mecanismo do harness | Skill realmente descoberta, leitura de arquivo e versão |
| **GrokBot / Grok Bot** | Skill privada/Bot de acordo com interface atual (pode não importar pasta Git inteira) | Conteúdo e procedimento carregados, rotina/bot ligados se aplicável |
| **OpenBot** | Biblioteca de Local Skills, ou acesso explícito aos arquivos conforme versão | Agente correto, Local Skill instalada e revisada |
| **Qualquer outra IA** | Carregar `CEO_SYSTEM_PROMPT.md`, `SKILL.md` e referências necessárias, manualmente ou por recurso de conhecimento | Sem afirmar execução, memória ou dados sem ferramenta |

Consultar [adapters/README.md](adapters/README.md) e o adaptador opcional adequado. **Não existem instalações “automáticas para tudo”.** Cada plataforma pode mudar métodos; verificar documentação atual antes de executar comandos específicos.

Fontes verificadas em 12/11/2026:
- Claude Skills: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
- Codex Skills: https://developers.openai.com/api/docs/guides/tools-skills
- Grok Bot: https://docs.x.ai/grok-bot/skills-routines-and-automations
- Grok Build coding (produto diferente do Grok Bot): https://github.com/xai-org/grok-build/blob/main/crates/codegen/xai-grok-pager/docs/user-guide/08-skills.md
- OpenBot: https://github.com/nightly-labs/openbot
- Formato aberto: https://agentskills.io

## Passo 3 — Ativar mandato e contexto de negócio

Configure `CEO_SYSTEM_PROMPT.md` como instruções persistentes do CEO, quando a ferramenta oferecer, sem sobrescrever restrições do sistema e sem dar a todos os agentes autoridade de CEO. Garanta acesso à fonte canônica `SKILL.md`, à política e à referência de estratégia conforme necessário. Entregue contexto factual do BataTalk e links autorizados a dados operacionais **somente se o ambiente suportar**.

Se a plataforma aceitar só um campo de texto, usar primeiro o mandato persistente conciso e orientar o CEO a pedir/ler referências por partes; ele deve marcar falta de acesso explicitamente.

## Passo 4 — Bootstrap de iniciativa

Execute [setup/CEO-bootstrap-situacional.md](setup/CEO-bootstrap-situacional.md), **independentemente de software**. O CEO deve:
1. descobrir modelos, agentes, ferramentas, dados, memoria e quotas realmente observáveis;
2. perguntar apenas o que falta e realmente importa;
3. identificar o gargalo do BataTalk e uma oportunidade que ninguém pediu;
4. escolher ação segura e verificar sua consequência;
5. salvar checkpoint real ou explicar ausência de persistência.

Não começar criando departamentos por padrão. Se só houver um modelo, deve agir bem sozinho.

## Passo 5 — Sensores e continuidade (opcionais)

Somente se o host suportar e estiver autorizado, configure cron/rotina/webhook/workflow persistente para sinais de produto, dinheiro, concorrentes, SEO e qualidade. [setup/routines.md](setup/routines.md) contém **contratos universais de sensores**, não jobs implantados. Cada rotina precisa de fonte, autorização, deduplicação, condição de parar, custo e prova de primeira execução.

Sem automação real, terminar sessões com checkpoint e próximo gatilho, sem prometer trabalhar em segundo plano. Um `OK` posterior inicia novo turno; não equivale a autorização de gasto, envio ou produção.

## Passo 6 — Validar em mais de uma plataforma

**Primeiro estático**: `python scripts/validate_skill.py` e testes Python. **Depois comportamental**: [tests/PORTABILITY-TEST-PLAN.md](tests/PORTABILITY-TEST-PLAN.md). Rodar cenários com ambiente M0/M1/M2 ou duas IAs diferentes, com mesmo enunciado e fontes, e comparar:
- iniciativa sem pedido explícito;
- qualidade de diagnóstico, estratégia, copy humana e compreensão econômica;
- capacidade correta de usar ferramentas e reconhecer limitação;
- segurança, alçada e preservação de estado;
- alteração real, verificação independente e custo.

Nunca declarar “CEO perfeito”, “agente instalado em todos os lugares”, “agora é autônomo 24h” ou “conseguiu clientes” sem evidências de campo.

## Prova de ativação — indispensável para não usar a versão antiga

**Dar merge no GitHub não atualiza automaticamente as skills já importadas em GrokBot, Claude Code, Codex ou OpenBot.** Após obter a nova revisão, confira a cópia realmente carregada no host: faça-o ler o arquivo references/34-proatividade-autocalibracao-e-execucao.md e informar a origem/versão do arquivo acessado, sem aceitar simples repetição do título como prova. Confira nos arquivos/controles da plataforma a revisão instalada.

**Teste de fumaça comportamental**, em ambiente de baixo risco com acesso a uma fonte real e sem publicação:
1. Envie apenas “e aí, CEO?”. O agente deve escolher uma fonte disponível, consultá-la, descobrir um sinal novo ou uma lacuna material e fazer uma ação autorizada verificável antes de responder. Se apenas descrever um plano, **falhou**.
2. Mostre uma entrega real anteriormente aprovada sem prova e diga “por que você não viu o problema antes?”. O agente deve abrir a fonte, reconhecer a própria omissão (não só acusar subordinado) e executar a correção segura ou identificar o bloqueio específico. Se apenas ampliar o prompt, **falhou**.
3. Durante uma tarefa que ainda tem uma etapa segura disponível, observe se ele a executa ou interrompe por “OK”. Se não havia impedimento real, **falhou**.

Guarde referências a chamadas de ferramenta, artefato antes/depois e intervenções necessárias do fundador, sem dados privados. Repita o teste na revisão antiga com mesmas ferramentas para comparar. Um resultado bem-sucedido aqui **não prova receita**, e um modelo sem acesso deve assumir limitação em vez de simular ação.

**Se a prova falhar:** confirmar versão instalada, ferramentas, autorizações, quotas, rotinas efetivamente ligadas e último erro real; corrigir a causa do ambiente ou do julgamento, não adicionar um parágrafo genérico de proatividade.

## Atualização

Manter **uma revisão canônica**. Para ambientes que usam cópias locais/sincronização manual, atualizar e verificar a cópia/skill carregada **em cada um**. Não alterar `POLICY.md` para conceder novas permissões sem aprovação explícita do fundador; melhorias de redação que preservem a alçada devem ser verificadas como equivalentes.

Os adaptadores evitam duplicação: se Claude e Grok não suportam a mesma ferramenta, o núcleo **continua valendo**. Só a implementação da ação muda.
