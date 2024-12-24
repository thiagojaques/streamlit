# streamlit
Desenvolvimento de 12 aplicações Web de Inteligência Artificial

1 - Primeira aplicação "Investimento em Franquias"
    Decisão de Investimentos:
        Taxa Anual
        Investimento Inicial

    Desejo do Cliente:
        A partir da Taxa Anual, é possivel prever qual será o custo
        inicial para montar a franquia?

        Ex: Se o custo anual da franquia é R$100.000,00 o investimento
        inicial será de R$80.000,00. (claro que isso é uma estimativa)

    Técnica que pode ser utilizada para implementar a aplicação:
        Regressão Linear:
            Prever um valor numérico (Investimento Inicial): Variável Dependente

            Taxa Anual da Franquia: Variável Independente

            As variáveis independentes são usadas para prever a variável dependente

            Se temos uma variável independente: Regressão Linear Simples

            Se temos mais de uma variável independente: Regressão Linear Múltipla
            (Ex: Localização, Cidade, Tipo de negócio)

    O que é preciso?
        Dados históricos para criar um modelo para servir como base para as previsões
        Arquivo slr12.csv
        FraAnual: Custo anual da franquia
        CusInic: Investimento Inicial
        36 Registros
        Fonte dos dados: Bussines Opportunity Handbook

    Principais Funções:
        modelo = LinearRegression().fit(X, y)
        prev = modelo.predict(dados_novo_valor)