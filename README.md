# BataTalk CEO Operator — skill para OpenBot

Pacote de instruções criado para um CEO de IA que dirige os agentes do BataTalk. Foi desenhado para OpenBot (openbot.run), que usa agentes com workspaces persistentes, skills locais, canais, filas e rotinas. Não é um aplicativo de execução autônoma nem altera sua instalação sozinho.

## Como usar

1. Abra o OpenBot e selecione o **agente CEO**.
2. Nas configurações do agente, abra **Skills** e adicione uma skill local com o conteúdo deste diretório (pasta com `SKILL.md` e `references/`). Alternativamente, peça ao agente para **criar uma skill local a partir desta pasta** e conferir a instalação. A interface exata pode variar conforme a versão. Confira em *Settings → Skills → Local skills*.
3. Cole o texto de `CEO_SYSTEM_PROMPT.md` no campo de **instruções persistentes** do CEO. A skill não substitui um mandato curto nas instruções do agente.
4. Envie ao CEO a mensagem de `setup/CEO-first-message.md`. Ela inicia uma auditoria real sem pressupor que o CEO já tenha acesso a todos os dados.
5. Configure as rotinas indicadas em `setup/routines.md` usando a interface de **Routines** do OpenBot. O arquivo `SKILL.md` não agenda nada por si só.
6. Comece com ferramentas/contas em modo mínimo e revise permissões de envio, deploy, cobrança, produção e edição de agentes. A aprovação precisa existir **fora do prompt** sempre que a ação for sensível.
7. Compare as saídas do CEO com `tests/CEO-BEHAVIOR-EVALS.md` após o primeiro dia e a cada alteração relevante.

## Conteúdo

- `SKILL.md`: regras executivas permanentes e seleção de playbooks.
- `CEO_SYSTEM_PROMPT.md`: instruções curtas para o campo do CEO no OpenBot.
- `references/`: playbooks completos por área, fontes e limites.
- `templates/`: registros, handoffs, avaliação de agentes, decisão e reunião.
- `tests/`: avaliação e testes de regressão de comportamento.
- `setup/`: mensagem de estreia e exemplos de rotinas.
- `config/policy.example.yaml`: limites sugeridos para o CEO adaptar ao ambiente real; **não é uma configuração nativa do OpenBot**.

## Regras de implantação importantes

- Não despausar Reels Creator sem ordem do fundador.
- Não aprovar conteúdo, checkout, integração ou migração só porque o agente disse "concluído".
- Não permitir ferramentas sensíveis somente porque as instruções do CEO contêm uma frase de segurança: configurar permissões reais, backups e revisão de produção.
- O CEO não consegue criar agentes, pesquisar fontes privadas ou rodar rotinas quando as ferramentas ou credenciais não estiverem disponíveis. Deve inspecionar capacidades e relatar a limitação.
- **Licenciamento**: o repositório oficial do OpenBot descreve uma licença não comercial para as versões atuais e uma licença comercial para uso comercial. Antes de utilizar na operação comercial do BataTalk, verifique a licença que se aplica à sua instalação/versão e eventual contratação diretamente com o fornecedor: https://github.com/nightly-labs/openbot

## Origem das práticas

Princípios adaptados de cartas de Jeff Bezos à Amazon, cultura Netflix, recomendações da Y Combinator, Jensen Huang, Steve Jobs, práticas de reliability do Google, documentação do Google Search Central, práticas da Stripe e documentação de agentes da OpenAI/Microsoft. **Nenhuma empresa/fundador endossa esta skill; não é uma reprodução de suas políticas**. Links em `references/10-fontes.md`.

## Instalar diretamente do GitHub

Este repositório **é a própria skill**. O arquivo de entrada está na raiz: [SKILL.md](SKILL.md). Para um CEO OpenBot em Windows com suporte a skills locais, execute no PowerShell:

```powershell
git clone https://github.com/Gabriel-Luis-Pacheco/skill-ceo.git "$env:USERPROFILE\.agents\skills\batatalk-ceo-operator"
```

Para atualizar uma instalação existente:

```powershell
git -C "$env:USERPROFILE\.agents\skills\batatalk-ceo-operator" pull --ff-only
```

Confira nas configurações de skills do OpenBot se o diretório foi detectado; em versões com caminhos diferentes, configure o diretório da skill manualmente. Copie [CEO_SYSTEM_PROMPT.md](CEO_SYSTEM_PROMPT.md) para as instruções persistentes do agente CEO e execute [setup/CEO-first-message.md](setup/CEO-first-message.md). Ative rotinas reais somente após revisar [setup/routines.md](setup/routines.md). **Somente clonar o repositório não habilita uma rotina 24/7.**

Veja o [guia completo de instalação](INSTALL.md). Rodar `python scripts/validate_skill.py` valida a estrutura local, os testes JSONL e as referências essenciais.

## CEO proativo — guias de operação (v2)

A versão expandida implementa [motor de iniciativas](references/12-ceo-autonomous-loop.md), [auditoria real de produto](references/13-deep-product-audit.md), [vantagem competitiva](references/14-competitive-advantage.md), [crescimento rentável](references/15-growth-profit-engine.md), [engenharia de equipe](references/16-team-culture-organization.md), [pesquisa profunda](references/17-deep-research-and-learning.md), [governança de execução](references/18-runtime-guardrails.md), [respostas autônomas](references/19-executive-scenarios.md) e [memória/idempotência](references/20-executive-memory.md).

**Importante:** a automação e os controles reais dependem das ferramentas/rotinas/contas autorizadas no OpenBot. O CI no GitHub valida a estrutura e a qualidade formal dos cenários, mas **não** demonstra que o CEO tomou boas decisões em execução real. Use o [plano de avaliação](tests/CEO-BEHAVIOR-EVALS.md) para testar com o runtime.
