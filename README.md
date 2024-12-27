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
        inicial será de R$80.000,00. (claro que isso é uma estimativa).

    Técnica que pode ser utilizada para implementar a aplicação:
        Regressão Linear:
            Prever um valor numérico (Investimento Inicial): Variável Dependente

            Taxa Anual da Franquia: Variável Independente

            As variáveis independentes são usadas para prever a variável dependente

            Se temos uma variável independente: Regressão Linear Simples

            Se temos mais de uma variável independente: Regressão Linear Múltipla
            (Ex: Localização, Cidade, Tipo de negócio)

    O que é preciso?
        Dados históricos para criar um modelo para servir como base para as previsões.
        Arquivo slr12.csv
        FraAnual: Custo anual da franquia
        CusInic: Investimento Inicial
        36 Registros
        Fonte dos dados: Bussines Opportunity Handbook

    Principais Funções:
        modelo = LinearRegression().fit(X, y)
        prev = modelo.predict(dados_novo_valor)

2 - Segunda Aplicação " Classificação de veículos "

    Desejo do Cliente:
        Uma revendedora de carros quer poder prever a qualidade do carro
        a partir de carros anteriores.

        Assim ela pode precificar de forma mais adequada o serviço 
        de assistência 24 horas.

        Aempresa possui uma grande base de dados de veículos adquiridos anteriormente,
        com características como exigência de manutenção, portas, tamanho do porta malas,
        segurança, etc.

    Técnica que pode ser utilizada para implementar a aplicação:
        Podemos usar Machine Learning, tarefa de classificação:
        Machine Learning são técnicas de prever ou classificar algo baseados em dados históricos.

    Implementação:
        Dividir dados em treino e teste
        Criar modelo com Naive Bayes
        Testar a performance do Modelo
        Prever

        X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.3, random_state=42)

        modelo = CategoricalNB()
        modelo.fit(X_train, y_train)
        y_pred = modelo.predict(X_test)
        acuracia = accuracy_score(y_test, y_pred)

    Atributos:
        Class: unacc, acc, good, vgood
        buying: vhigh, high, med, low
        maint: vhigh, high, med, low
        doors: 2, 3, 4, more
        persons: 2, 4, more
        lug_boot: small, med, big
        safety: low, med, high

3 - "Fazenda de produção de Leite"
    Desejo do Cliente:
        Uma fazenda deseja compreender a produção de leite, de preferência com dados mensais.

        Prever a produção para os próximos meses/anos, para que possa antecipar ações e investimentos.
        O período (meses para frente) deve ser flexível.

        A empresa possui dados mensais da produção, mas não vem datas.

        A empresa quer que a aplicação permita que novos dados sejam imputados, para que possa atualizar os dados e as previsões.

    Técnica que pode ser utilizada para implementar a aplicação:
        Transformar dados importantes em Series Temporais:
            Dados coletados em intervalos regulares de tempos.
                ts_data = pd.Series(data.iloc[:,0].calues, index= pd.date_ranger(
                    start = periodo, periods = len(data), ferq = 'M'))

        Decompor:
            decomposicao = seasonal_decompose(ts_data, model = 'additive')

        Criar modelo arima:
             modelo = SARIMAX(ts_data, order = (2,0,0), seasonal_order = (0,1,1,12))
             modelo_fit = modelo.fit()

        Fazer a previsão:
            previsao = modelo_fit.forecast(steps = periodo_previsao)

    Dados da Aplicação:
        monthly-milk-production-pounds-p.csv:
            Exite apenas uma coluna, não exite dadas informadas no arquivo
            O intervalo é de janeiro de 2000 e dezembro de 2013
            A aplicação deve servir para processar qualquer serie temporal com dados na mesma estrutua.

4 - Prever a quebra de equipamentos
    Desejo do cliente:
        Uma indústria tem vários equipamentos críticos na sua linha de produção.

        Existem dados fornecidos pela fabricante da média de quebras dos diferentes equipamentos a cada ano.

        A empresa quer uma aplicação que possa calcular a probabilidade de quebras.

        Por exemplo: se em média o equipamento quebra 2 vezes ao ano, a empresa quer saber qual é a probabilidade de quebrar 1, 3, 4 ou até nenhuma vez ao ano.

    Técnica que pode ser utilizada para implementar a aplicação:
        Distribuição de Poisson:
            Mede a probabilidade de ocorrência de eventos em intervalos de tempo

            Os eventos a cada intervalo dever ser independentes

            P(X = x)        --> Probabilidade exata
            P(X < x)        --> Menor ou igual
            P(X > x)        --> Maior

            Probabilidade Exata:
                probs = poisson.pmf(x_vals, lamb)
            
            Igual ou menor que:
                probs = poisson.cdf(x_vals, lamb)

            Maior que:
                probs = poisson.sf(x_vals, lamb)