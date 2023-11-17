import pandas as pd
from sklearn.ensemble import IsolationForest


def detectar_outliers(dados_fit: pd.DataFrame, dados_predict: pd.DataFrame, contaminacao=0.05, random_state=42):
    # Construindo o modelo Isolation Forest
    clf = IsolationForest(n_estimators=100, max_samples='auto', contamination=contaminacao,
                          max_features=1.0, bootstrap=False, n_jobs=-1, random_state=random_state, verbose=0)
    clf.fit(dados_fit)

    # Predição dos outliers
    pred = clf.predict(dados_predict)
    dados_predict.loc[:, 'anomalias'] = pred

    # Filtrando os outliers
    outliers = dados_predict.loc[dados_predict['anomalias'] == -1]

    # Contagem dos outliers para cada valor único em 'ID_Participante'
    top_outliers = outliers['ID_Participante'].value_counts().head(5)

    return top_outliers


def pipeline_isolation_forest(dados_fit: pd.DataFrame, dados_predict: pd.DataFrame) -> pd.DataFrame:
    colunas_para_ignorar = [
        'Data_Competencia',
        'Provisao_Total_Nao_Normalizada',
        'Inadimplencia_Total_Nao_Normalizada',
        'Nome_Fundo',
        'CNPJ_Administrador',
        'Substituicao_Nao_Normalizada',
        'Recompra_Nao_Normalizada'
    ]

    dados_fit = dados_fit.drop(columns=colunas_para_ignorar)
    dados_predict = dados_predict.drop(columns=colunas_para_ignorar)

    carteira_encoding = [
        'Setor publico',
        'Agronegócio',
        'Cartão',
        'Comercial',
        'Imobiliário',
        'Financeiro',
        'Industrial',
        'Factoring',
        'Multimercado',
        'Serviços',
        'Ações judiciais'
    ]

    fundos_por_carteira = {
        'Serviços': {
            'fit': dados_fit.loc[dados_fit['Carteira_Classificação_encoded'] == carteira_encoding.index('Serviços')],
            'predict': dados_predict.loc[dados_predict['Carteira_Classificação_encoded'] == carteira_encoding.index('Serviços')]
        },
        'Industrial': {
            'fit': dados_fit.loc[dados_fit['Carteira_Classificação_encoded'] == carteira_encoding.index('Industrial')],
            'predict': dados_predict.loc[dados_predict['Carteira_Classificação_encoded'] == carteira_encoding.index('Industrial')]
        },
        'Cartão': {
            'fit': dados_fit.loc[dados_fit['Carteira_Classificação_encoded'] == carteira_encoding.index('Cartão')],
            'predict': dados_predict.loc[dados_predict['Carteira_Classificação_encoded'] == carteira_encoding.index('Cartão')]
        },
        'Agronegócio': {
            'fit': dados_fit.loc[dados_fit['Carteira_Classificação_encoded'] == carteira_encoding.index('Agronegócio')],
            'predict': dados_predict.loc[dados_predict['Carteira_Classificação_encoded'] == carteira_encoding.index('Agronegócio')]
        },
        'Factoring': {
            'fit': dados_fit.loc[dados_fit['Carteira_Classificação_encoded'] == carteira_encoding.index('Factoring')],
            'predict': dados_predict.loc[dados_predict['Carteira_Classificação_encoded'] == carteira_encoding.index('Factoring')]
        },
        'Imobiliário': {
            'fit': dados_fit.loc[dados_fit['Carteira_Classificação_encoded'] == carteira_encoding.index('Imobiliário')],
            'predict': dados_predict.loc[dados_predict['Carteira_Classificação_encoded'] == carteira_encoding.index('Imobiliário')]
        },
        'Comercial': {
            'fit': dados_fit.loc[dados_fit['Carteira_Classificação_encoded'] == carteira_encoding.index('Comercial')],
            'predict': dados_predict.loc[dados_predict['Carteira_Classificação_encoded'] == carteira_encoding.index('Comercial')]
        },
    }

    top_outliers = {}

    for carteira in fundos_por_carteira.keys():
        dados = {
            'fit': fundos_por_carteira.get(carteira).get('fit').drop(columns=['Carteira_Classificação_encoded']),
            'predict': fundos_por_carteira.get(carteira).get('predict').drop(columns=['Carteira_Classificação_encoded'])
        }

        if dados.get('fit') is None or dados.get('predict') is None:
            continue

        top_outliers[carteira] = detectar_outliers(
            dados.get('fit'),
            dados.get('predict')
        )

        top_outliers[carteira] = top_outliers[carteira].index.tolist()

    return top_outliers
