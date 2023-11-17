import logging
import json
from flask import Flask, request, jsonify
from pipeline_preparacao import pipeline_preparacao
from isolation_forest import pipeline_isolation_forest
from flask_cors import CORS
import pandas as pd
from numpy import int64

CAMINHO_CSV = '../../data/dados_cvm.csv'

dados_historicos = None

with open(CAMINHO_CSV, 'r', encoding='utf-8') as arquivo:
    dados_historicos = pd.read_csv(arquivo)

app = Flask(__name__)
CORS(app)  

logging.basicConfig(level=logging.DEBUG)


def convert_int64_to_int(obj):
    if isinstance(obj, int64):
        return int(obj)
    return obj


def formatar_outliers(outliers: dict, dados: pd.DataFrame):
    fundos = {}
    for carteira in outliers:
        fundos[carteira] = []

        for id_participante in outliers[carteira]:
            fundo = dados.loc[dados['ID_Participante']
                              == id_participante]
            nome = fundo['Nome_Fundo'].values[0]
            cnpj = fundo['CNPJ_Administrador'].values[0]
            datas = fundo['Data_Competencia'].values
            inadimplencia_total = fundo['Inadimplencia_Total_Nao_Normalizada'].values
            provisao_total = fundo['Provisao_Total_Nao_Normalizada'].values
            substituicao_total = fundo['Substituicao_Nao_Normalizada'].values
            recompra_total = fundo['Recompra_Nao_Normalizada'].values

            datas = datas.tolist()
            inadimplencia_total = inadimplencia_total.tolist()
            provisao_total = provisao_total.tolist()
            substituicao_total = substituicao_total.tolist()
            recompra_total = recompra_total.tolist()
            fundos[carteira].append(
                {
                    'ID_Participante': id_participante,
                    'Nome': nome,
                    'CNPJ': cnpj,
                    'Dados': {
                        'labels': datas,
                        'datasets': [
                            {
                                'label': 'Inadimplência Total',
                                'data': inadimplencia_total
                            },
                            {
                                'label': 'Provisão Total',
                                'data': provisao_total
                            },
                            {
                                'label': 'Substituição Total',
                                'data': substituicao_total
                            },
                            {
                                'label': 'Recompra Total',
                                'data': recompra_total
                            }
                        ]
                    }
                }
            )

    return fundos


@app.route('/api', methods=['POST'])
def processar_csv():
    global dados_historicos
    try:
        dados_recebidos = request.files['file']

        if not dados_recebidos.filename.endswith('.csv'):
            return jsonify({'error': 'O arquivo enviado não é um arquivo CSV válido'}), 400

        dados_recebidos = pd.read_csv(dados_recebidos)

        logging.info('Iniciando pipeline de preparação dos dados')

        # adiciona linhas novas ao histórico 9dataframe
        dados_historicos = pd.concat(
            [dados_historicos, dados_recebidos],
            ignore_index=True
        )

        dados_historicos = pipeline_preparacao(
            dados_historicos, exportar_arquivo=False)
        dados_recebidos = pipeline_preparacao(
            dados_recebidos, exportar_arquivo=False)
        logging.info('Pipeline de preparação dos dados finalizado')

        logging.info('Iniciando pipeline de detecção de outliers')
        outliers_historicos = pipeline_isolation_forest(
            dados_historicos, dados_recebidos)
        outliers_novos = pipeline_isolation_forest(
            dados_recebidos, dados_recebidos)
        logging.info('Pipeline de detecção de outliers finalizado')

        logging.info('Formatando outliers')

        outliers_historicos = formatar_outliers(
            outliers_historicos, dados_historicos)

        outliers_novos = formatar_outliers(outliers_novos, dados_recebidos)
        logging.info('Outliers formatados')

        result = {
            'outliers_historicos': outliers_historicos,
            'outliers_novos': outliers_novos
        }

        result_json = json.dumps(result, default=convert_int64_to_int)

        return jsonify({'result': result_json})

    except Exception as e:
        print(e)
        return jsonify({'error': 'Unexpected error'}), 500


if __name__ == '__main__':
    app.run(debug=True)
