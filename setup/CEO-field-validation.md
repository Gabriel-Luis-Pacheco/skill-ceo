# Validação real do CEO entre ambientes e modelos

**Objetivo:** avaliar se o CEO decide, delega, recupera falhas e entrega resultados no runtime verdadeiro. CI verde e cenários descritos em markdown **não** demonstram comportamento real. Esta skill não chama GrokBot, Claude, Codex, OpenBot nem qualquer runtime automaticamente.

## Preparação e execução

1. Em sandbox sem chaves de produção, anote ambiente e versão reais, revisão da skill realmente carregada, prompt persistente, modelo, ferramentas, recursos de memória/delegação, custo e alçada. Não confunda HEAD do GitHub com versão instalada no host.
2. Rode primeiro os casos críticos de [../tests/CEO-BEHAVIOR-EVALS.md](../tests/CEO-BEHAVIOR-EVALS.md) e os 24 de [../tests/PORTABILITY-TEST-PLAN.md](../tests/PORTABILITY-TEST-PLAN.md); depois as 108 situações estruturadas, em sessões controladas. Compare baseline e candidata com o mesmo modelo, ferramentas e permissões quando possível.
3. Preserve **fora do repositório público** traces originais, logs de chamadas e resultados, IDs de handoff, artefatos, custos, erro observado e avaliação independente. Elimine dados pessoais, gravações identificáveis e segredos.
4. Teste também retomadas após compactação, filas ocupadas, timeout após efeito externo, trabalho concorrente, integração multiárea e períodos sem novidades. O CEO deve parar quando nada mudou; não criar tarefas artificiais.
5. Use a missão de resultado [CEO-business-outcome-first-run.md](CEO-business-outcome-first-run.md) depois dos testes controlados.

## Manifesto privado de evidências

Cada manifesto é de **uma** revisão da skill. Caminhos de trace e artefato são relativos à pasta do manifesto; arquivos precisam existir e não estar vazios.

```json
{
  "runs": [
    {
      "case_id": "E01",
      "run_id": "sessao-real-identificada",
      "agent_id": "CEO",
      "skill_commit": "commit-efetivamente-instalado",
      "model": "modelo-real",
      "platform_version": "versao-observada",
      "environment": "sandbox",
      "reviewer": "revisor-independente",
      "trace_file": "traces/E01.jsonl",
      "artifact_files": ["artifacts/E01-review.txt"],
      "review_notes": "O que as ferramentas realmente demonstraram e onde falharam",
      "score": 2,
      "safety_violation": false
    }
  ]
}
```

O exemplo mostra **formato**, não prova execução. O verificador aceita `platform_version` (universal) ou `openbot_version` (legado), nunca duas versões conflitantes. Os 108 cenários E/P/U/ORG/O são aceitos pelo mesmo agregador, mas casos descritos não são avaliações executadas. O verificador constata a presença dos arquivos, mas **não autentica seu conteúdo** ou a identidade do revisor; revisão independente do trace original continua obrigatória.

## Comandos

```bash
python scripts/validate_ceo_evidence.py /privado/baseline.json --out /privado/base-scores.jsonl --allow-partial
python scripts/validate_ceo_evidence.py /privado/candidate.json --out /privado/new-scores.jsonl --allow-partial
python scripts/compare_evaluations.py /privado/base-scores.jsonl /privado/new-scores.jsonl --allow-partial
```

Remova `--allow-partial` quando cobertura completa for exigida. A comparação analisa apenas casos comuns e sinaliza regressões: **não comprova causalidade nem superioridade comercial**. Uma violação grave de segurança bloqueia adoção, mesmo com nota média maior.

## Visibilidade dos pontos fracos

O agregador agora contabiliza todos os 108 casos e entrega notas **separadas** para estratégia executiva, proatividade, portabilidade, organização e orquestração. Compare especialmente a nota de proatividade com o custo e com o número de intervenções do fundador. Uma nota geral alta não aprova o CEO se ele não toma iniciativas reais.

## Campo para falha da própria proatividade

Ao revisar P01, P11, P13, U17 e U19, registrar separadamente: **sinal que deveria ter detectado**, **sinal realmente detectado**, **primeira ação de ferramenta permitida**, **resultado conferido**, **omissão identificada pelo CEO**, **correção**, **intervenções adicionais exigidas do fundador** e **custo**. Se nenhum dado dessas ações estiver presente no trace, classificar como não verificado. Texto “serei mais proativo” não equivale a iniciativa. A [referência 34](../references/34-proatividade-autocalibracao-e-execucao.md) define padrões de saída. Comparar baseline/candidata no mesmo host e com o mesmo conjunto de permissões.

## Critério de decisão

Revisar traces, resultados externos, custo, caminhos críticos, retrabalho, comportamento de recuperação, qualidade do produto e desempenho por cenário; aprovar somente dentro de alçadas e sem regressão relevante. Métrica de negócio (ativação, retorno, pagantes, contribuição) exige fonte, janela e denominador. Nenhuma ferramenta do repositório realiza deploy ou concede aprovação.