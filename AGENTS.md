# Instruções para qualquer agente que edite este repositório

O repositório inteiro é uma skill para o CEO de IA do BataTalk. `SKILL.md` na raiz é o ponto de entrada operacional; **`POLICY.md` é a fonte normativa única de segurança, orçamento e alçadas**; `CEO_SYSTEM_PROMPT.md` é o mandato persistente que o usuário copia para o CEO.

Ao alterar comportamentos: preservar missão (valor ao aluno e sustentabilidade econômica), não ampliar permissões de produção/gastos sem aprovação do fundador, preservar a pausa do Reels Creator, manter honestidade entre resultados verificados e hipóteses, não substituir evidências por autoavaliação.

Atualize os guias correspondentes em `references/`, documentação de instalação se necessário, e os testes de regressão em `tests/`. Execute `python scripts/validate_skill.py` e `python -m unittest discover -s tests -p 'test_*.py'` antes de propor publicação. Nenhum desses comandos comprova bom julgamento do CEO; o protocolo de avaliação real exige traces e revisão. Considere trabalho incompleto se novo comportamento não tiver critério de aceitação e mecanismo de verificação.

Evite cargos sem missão, cerimônias sem decisão, relatórios sem evidência, iteração inútil de prompts e AI slop. **Não reintroduza tetos fixos de agentes, cargos, frentes, subequipes, níveis ou mudanças de skill.** O CEO dimensiona por mérito, capacidade e orçamento delegado, com liberdade para criar agentes de IA permanentes e sublideranças. Não apagar agente sem verificar e preservar workspace/anexos, pois o OpenBot pode removê-los definitivamente. Mudanças em configuração local do OpenBot exigem inspeção da ferramenta e permissões reais, nunca suposição.
