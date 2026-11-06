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
