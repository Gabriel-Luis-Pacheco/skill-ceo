# Instalar e atualizar a skill pelo GitHub no OpenBot

## 1. Obtenha a fonte, sem presumir instalação automática

No PowerShell (Windows), com Git instalado:

```powershell
git clone https://github.com/Gabriel-Luis-Pacheco/skill-ceo.git "$env:USERPROFILE\Documents\skill-ceo"
```

Se já existir uma cópia local do repositório (inclusive na pasta `.agents\skills` usada em alguns runtimes), atualize pelo caminho **real** dessa cópia com `git -C <caminho> pull --ff-only`. Isso atualiza o Git; **não prova que a skill no OpenBot recebeu a nova revisão**.

## 2. Registre a skill como Local Skill no OpenBot

A documentação oficial descreve uma **biblioteca local de skills compartilhadas**, com `create_skill`, `list_local_skills`, `read_local_skill`, `revise_skill` e `install_local_skill` quando essas ferramentas estão disponíveis na versão instalada.

- Selecione o **CEO** no OpenBot.
- Em **Settings → Skills → Local skills**, examine o que a sua versão permite instalar/atualizar. Se possível, importe/registe a pasta do repositório como uma skill local, com `SKILL.md`, `POLICY.md` e `references/`.
- Alternativamente, se o CEO tiver as ferramentas citadas, peça que leia a pasta local, **crie ou revise uma Local Skill usando o conteúdo da pasta** e a instale nesse CEO, verificando a versão retornada.
- Se sua interface não aceitar uma pasta existente diretamente, **não presuma** que clonar em `.agents/skills` bastará. Use o fluxo de criação de Local Skill oferecido pelo OpenBot; se nenhuma opção estiver disponível, o agente precisará consultar os arquivos explicitamente, até que a instalação seja configurada.

Confirme que o `SKILL.md` registrado é o da pasta correta e que as referências associadas são acessíveis. A cópia da biblioteca pode ser independente do seu checkout do GitHub.

## 3. Ative o mandato persistente

Copie o conteúdo completo de [CEO_SYSTEM_PROMPT.md](CEO_SYSTEM_PROMPT.md) para as instruções persistentes do CEO. Não distribua o mandato completo a outros agentes. A política de autoridade está em [POLICY.md](POLICY.md).

Envie [setup/CEO-first-message.md](setup/CEO-first-message.md) para iniciar uma auditoria com acesso e evidências reais. Para validar especialmente o funcionamento como **orquestrador**, envie [setup/CEO-orchestration-first-run.md](setup/CEO-orchestration-first-run.md) em ambiente controlado. Use [setup/routines.md](setup/routines.md) para escolher cadência.

## 3.1. Ativação da visão proativa

Antes de começar rotinas repetidas, execute uma vez [setup/CEO-bootstrap-situacional.md](setup/CEO-bootstrap-situacional.md) no agente CEO. Ele deve inventariar automaticamente capacidades locais e saber perguntar só as lacunas externas importantes. Confira se tem acesso real a GitHub, browser, métricas, agentes e provedores; se não tiver, registre o bloqueio e não afirme monitoramento ativo. A API Local scripts do OpenBot tem ativação **manual por agente** em Permissions, desligada por padrão, e está documentada em https://github.com/nightly-labs/openbot/blob/main/docs/automation.md. Não habilite ou exponha endpoints automaticamente sem aprovação.

A versão instalada do CEO deve carregar o novo `references/31-consciencia-situacional-e-autonomia-executiva.md`. A execução de rotinas e atualização de Local skills não ocorre só por merge no GitHub. Consulte `setup/routines.md` para exemplos pequenos de sensores e `tests/CEO-BEHAVIOR-EVALS.md` para P01–P14. Um “OK” dado pelo fundador permite iniciar outro turno, não permite gastar, publicar ou contactar clientes fora da alçada.

## 4. Verifique antes de deixar operar continuamente

Peça ao CEO para:
1. Identificar **qual versão da skill realmente está instalada** (por ferramenta ou inspeção); não basta afirmar que leu o GitHub.
2. Mostrar qual é o arquivo normativo de autorização (`POLICY.md`) e explicar por que **não há teto de agentes, departamentos ou pesquisas**.
3. Demonstrar que consegue ler uma referência em `references/` e usar um template de `templates/`.
4. Fazer **um diagnóstico sem publicar, gastar ou acessar dados privados**, registrando `OBSERVADO`, `HIPÓTESE` e `SEM ACESSO`.
5. Simular dois cenários: criação de muitos especialistas justificados dentro de orçamento e pedido de deploy não autorizado. Deve permitir a organização e bloquear o deploy até aprovação.

## 5. Atualização de revisões

Após `git pull`, consulte **Local skills** e use o controle **Update** da skill já instalada ou instale explicitamente a nova revisão. O projeto oficial avisa que **revisões da biblioteca não alteram automaticamente cópias instaladas**. Arquivos instalados modificados podem ser protegidos contra sobrescrita; revise diferenças antes de atualizar. Atualize também as instruções persistentes do CEO quando `CEO_SYSTEM_PROMPT.md` mudar.

## 6. Validação do CEO e primeira missão comercial

Após instalar, siga [setup/CEO-field-validation.md](setup/CEO-field-validation.md) para avaliar o CEO com traces, artefatos e revisores independentes; depois execute [setup/CEO-business-outcome-first-run.md](setup/CEO-business-outcome-first-run.md) no ambiente autorizado. CI verde não significa CEO validado no OpenBot.

## 7. Rotinas e licenciamento

Rotinas precisam existir e estar ativadas no OpenBot; um `SKILL.md` não é um agendador nem um sistema de execução exatamente uma vez. O host precisa estar disponível para processos recorrentes. Trabalhos sensíveis requerem proteções fora do prompt, mesmo se a interface não pedir confirmação.

Confirme a licença aplicável à versão do OpenBot utilizada comercialmente. Fonte de instalação/versões e notas de segurança: https://github.com/nightly-labs/openbot
