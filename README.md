# CEI to Yahoo Finance

Ferramenta em Python que lê a planilha de ativos do CEI exportando para o formato de CSV esperado pelo Yahoo Finance.

## Funcionamento

1. Entre no site do CEI e exporte as notas de movimentação que você gostaria de importar no Yahoo Finance, ele deverá gerar o arquivo com nome `InfoCEI.xls`.
2. Adicione o arquivo `InfoCEI.xls` a pasta `CSV` e rode o código.
3. O sistema irá gerar 3 arquivos diferentes: `yahoo_FIIs_BR`, `yahoo_stocks_BR`, `yahoo_segmented_stocks_BR`.

### Tipos de arquivo gerado

- `yahoo_FIIs_BR`: Lista apenas com transações relativas a FIIs (Fundos Imobiliários);
- `yahoo_stocks_BR`: Lista com todas as transações de ações, excluindo as ações segmentadas;
- `yahoo_segmented_stocks_BR`: Lista com todas as ações segmentadas.

### Segmentando uma ação

Para segmentar ações da sua lista, é necessário apenas chamar a função `export_yahoo_csv()`, passando como argumento a lista de ações que você deseja segmentar. Exemplo: `export_yahoo_csv(['WEGE3', 'HGTX3', 'ITUB3'])`.
