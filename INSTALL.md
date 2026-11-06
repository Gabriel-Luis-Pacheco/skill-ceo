# Instalação da skill CEO no OpenBot

## 1. Instalação via GitHub (Windows)

Pré-requisito: Git instalado. No PowerShell:

```powershell
git clone https://github.com/Gabriel-Luis-Pacheco/skill-ceo.git "$env:USERPROFILE\.agents\skills\batatalk-ceo-operator"
```

No Linux/macOS, se a sua versão usar o diretório convencional:

```bash
git clone https://github.com/Gabriel-Luis-Pacheco/skill-ceo.git "$HOME/.agents/skills/batatalk-ceo-operator"
```

Se o OpenBot usar outra pasta para skills, ajuste para o local configurado no aplicativo. Não copie o conteúdo de `references/` para outro local: os caminhos relativos são necessários.

## 2. Ativar no agente certo

Abra o CEO no OpenBot, confira em **Skills** que `batatalk-ceo-operator` aparece, e deixe o `SKILL.md` disponível ao CEO. Cole o conteúdo inteiro de [CEO_SYSTEM_PROMPT.md](CEO_SYSTEM_PROMPT.md) nas instruções persistentes do agente. Não presuma que só o clone automaticamente injete as instruções no contexto.

## 3. Primeira execução

Envie a mensagem em [setup/CEO-first-message.md](setup/CEO-first-message.md) para solicitar uma auditoria baseada em evidências, sem presumir credenciais e resultados. Depois configure [setup/routines.md](setup/routines.md) na ferramenta nativa de rotinas, se disponível.

## 4. Permissões reais e controle

O CEO pode pesquisar, avaliar, reorganizar trabalho e propor ações autonomamente conforme [SKILL.md](SKILL.md). Execução de deploy, cobranças, mudança de preços, acessos privilegiados, publicação de conteúdos, ações de clientes e alterações em produção depende das permissões efetivas e dos mecanismos de aprovação do seu ambiente. O arquivo `config/policy.example.yaml` é somente exemplo e não configura o OpenBot automaticamente.

## 5. Atualizações e validação

```powershell
git -C "$env:USERPROFILE\.agents\skills\batatalk-ceo-operator" pull --ff-only
python "$env:USERPROFILE\.agents\skills\batatalk-ceo-operator\scripts\validate_skill.py"
```

Reavalie mudanças de prompts e agentes usando os exemplos em `tests/`. Não faça autoedições cegas da skill diretamente em produção sem controle de versão, análise de diff e teste de regressão.

## 6. Gestão contínua

O GitHub mantém a **versão da skill**. O OpenBot é responsável pelas rotinas agendadas, persistência de estado, coordenação dos agentes e execução das ferramentas. Esta skill define comportamento e governança; não cria sozinha os processos recorrentes nem gera receita por conta própria.

### Atenção: atualizar o GitHub não atualiza automaticamente a skill instalada

Se você instalou a skill como **Local Skill** pela biblioteca do OpenBot, a instalação mantém uma cópia versionada. Após atualizar este repositório com `git pull`, **atualize também a skill no agente CEO pelo controle “Update” ou instale explicitamente a nova revisão**, conforme a interface da sua versão. Confirme que o CEO lê o `SKILL.md` atualizado e que seu prompt persistente foi atualizado. A documentação oficial do OpenBot informa que revisões da biblioteca não atualizam cópias instaladas automaticamente: https://github.com/nightly-labs/openbot
