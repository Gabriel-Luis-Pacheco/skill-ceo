# Claude Code — adaptador opcional

**Núcleo comum:** `SKILL.md`, `POLICY.md` e referências não são específicos de Claude. A qualidade de direção executiva permanece igual.

## Instalação — verificar docs da versão

A documentação da Anthropic descreve skills locais em `~/.claude/skills/` (pessoais) ou `.claude/skills/` (projeto). O diretório final precisa conter `SKILL.md` e as referências, não somente um link para arquivo solto. Colocar a **mesma pasta da skill** nesses locais quando suportado; evitar duas cópias divergentes. O carregamento automático depende de descrição/ativação; também é possível solicitar explicitamente a skill se a interface permitir.

## Uso executivo

1. Inspecionar projeto, branches, CI, ferramentas, permissões e contexto antes de afirmar capacidade.
2. Recuperar dados financeiros/marketing apenas se conectores reais e autorização existirem; Git não substitui CRM ou cliente.
3. Para tarefas grandes, trabalhar com checkpoints, branches e artefatos verificáveis, sem gastar toda janela em auditoria.
4. Não criar “CEO/CFO/CTO” fictícios como subagentes se ambiente não oferece agentes independentes.
5. Usar `references/33-julgamento-executivo-competencias-e-aprendizado.md` para decidir o quê e por quê; código é só uma forma de implementar estratégia.
6. Ferramentas/bash/arquivos não dão automaticamente acesso a serviços externos nem orçamento.

Fonte: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
