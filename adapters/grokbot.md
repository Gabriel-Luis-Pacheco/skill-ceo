# GrokBot / Grok Bot — adaptador opcional

**Não é o núcleo da skill.** Antes de usar, confirme se o produto em execução é o Grok Bot oficial e quais recursos estão disponíveis na conta e na organização. O nome Grok pode se referir a superfícies diferentes (chat, coding, bots e APIs).

## Contrato de funcionamento

- Se o Grok Bot suportar biblioteca privada de skills: registrar o conteúdo do núcleo e as referências necessárias, associar ao Bot certo e **testar se o Bot carrega a revisão atual**. Não assumir que atualizar o GitHub sincroniza a skill publicada.
- Se permitir rotinas/eventos: criar gatilhos separados para sinais comerciais, concorrência, SEO, produto e decisões; todos com fonte, condição, custo, deduplicação, estado e critério de silêncio. **Rotina não prova entrega**.
- Se oferecer apps conectados (GitHub, analytics, Gmail, etc.), descobrir credenciais/permissões efetivas; não contornar limitações com screenshots de dados privados ou coleta indiscriminada.
- Se oferecer ações de navegador ou comunicações externas, manter aprovação conforme `POLICY.md`, idempotência e confirmação do estado real. Nunca disparar abordagem comercial em massa por conta própria sem campanha autorizada.
- Se o ambiente não importar diretórios SKILL.md, carregar o mandato como skill/recurso textual pelo procedimento **que a interface atual realmente permite**; se não souber, identificar como SEM ACESSO e oferecer fallback de uso manual.

## Primeiro teste

Dizer somente “e aí, CEO?”. Sem listar tarefas: deve descobrir estado disponível, identificar maior incerteza, tomar a menor ação segura e voltar com evidência; quando faltar informação sobre outros modelos/plataformas, perguntar somente aquilo que **não consegue ler**.

## Fontes

Documentação de Grok Bot (skills, rotinas, eventos): https://docs.x.ai/grok-bot/skills-routines-and-automations . Para produto de codificação Grok Build (diferente do Bot), o uso de arquivos SKILL.md pode ter interface distinta: https://github.com/xai-org/grok-build/blob/main/crates/codegen/xai-grok-pager/docs/user-guide/08-skills.md . **Não tratar esses dois produtos como iguais.**
