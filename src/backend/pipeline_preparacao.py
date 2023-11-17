import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
import logging
from os import path, makedirs

LIMITE_PERCENTUAL_NULOS = 49

colunas_irrelevantes = [
    'CNPJ',
    'Data_Entrega',
    'SK_Documento',
    'ID_Documento',
    'Nome_Administrador',
    'Sistema_Origem',
    'Ativo_Direitos_Sem_Aquisicao_Creditos_Empresas_Recuperacao',
    'Ativo_Direitos_Sem_Aquisicao_Creditos_Receitas_Publicas',
    'Ativo_Direitos_Sem_Aquisicao_Creditos_Fator_Risco',
    'Ativo_Coberturas_Prestadas',
    'Carteira_Creditos_Tributarios',
    'Carteira_Royalties',
    'Taxas_Titulos_Federais_Juros_Venda_Minina',
    'Taxas_Titulos_Federais_Juros_Venda_Maxima',
    'Taxas_CDB_Desconto_Venda_Minina',
    'Taxas_CDB_Desconto_Venda_Media_Ponderada',
    'Taxas_CDB_Desconto_Venda_Maxima',
    'Taxas_CDB_Juros_Venda_Minina',
    'Taxas_CDB_Juros_Venda_Media_Ponderada',
    'Taxas_CDB_Juros_Venda_Maxima',
    'Negocios_Substituicoes_Quantidade',
    'Negocios_Substituicoes_Valor_Contabil',
    'Negocios_Recompras_Quantidade',
    'Negocios_Recompras_Valor_Contabil',
    'Negocios_Alienacoes_Cedente_Quantidade',
    'Negocios_Alienacoes_Cedente_Valor_Contabil',
    'Negocios_Alienacoes_Prestadores_Quantidade',
    'Negocios_Alienacoes_Prestadores_Valor_Contabil',
    'Negocios_Alienacoes_Terceiros_Quantidade',
    'Negocios_Alienacoes_Terceiros_Valor_Contabil',
    'Negocios_Aquisicoes_Direitos_Aquisicao_Quantidade',
    'Negocios_Aquisicoes_Direitos_Sem_Aquisicao_Quantidade',
    'Negocios_Aquisicoes_Direitos_Vencer_Parcelas_Adimplentes_Quantidade',
    'Negocios_Aquisicoes_Direitos_Vencer_Parcelas_Inadimplentes_Quantidade',
    'Negocios_Aquisicoes_Direitos_Inadimplentes_Quantidade',
    'Garantias_Percentual',
    'Garantias_Valor_Total',
    'Prazo_Conversao_Cotas',
    'Tipo_Prazo_Conversao_Cotas',
    'Prazo_Pagamento_Resgate',
    'Tipo_Prazo_Pagamento_Resgate',
    'Numero_Cotistas_Senior_Banco_Comercial',
    'Numero_Cotistas_Senior_Corretora_Distribuidora',
    'Numero_Cotistas_Senior_Pessoa_Juridica_Financeira',
    'Numero_Cotistas_Senior_Investidor_Nao_Residente',
    'Numero_Cotistas_Senior_Entidade_Aberta_Previdencia_Complementar',
    'Numero_Cotistas_Senior_Entidade_Fechada_Previdencia_Complementar',
    'Numero_Cotistas_Senior_Regime_Proprio_Previdencia_Servidores_Publicos',
    'Numero_Cotistas_Senior_Sociedade_Seguradora',
    'Numero_Cotistas_Senior_Sociedade_Capitalizacao',
    'Numero_Cotistas_Senior_FIC_FIDC',
    'Numero_Cotistas_Senior_FII',
    'Numero_Cotistas_Senior_Clube_Investimento',
    'Numero_Cotistas_Senior_Outros',
    'Numero_Cotistas_Subordinada_Banco_Comercial',
    'Numero_Cotistas_Subordinada_Corretora_Distribuidora',
    'Numero_Cotistas_Subordinada_Pessoa_Juridica_Financeira',
    'Numero_Cotistas_Subordinada_Investidor_Nao_Residente',
    'Numero_Cotistas_Subordinada_Entidade_Aberta_Previdencia_Complementar',
    'Numero_Cotistas_Subordinada_Entidade_Fechada_Previdencia_Complementar',
    'Numero_Cotistas_Subordinada_Regime_Proprio_Previdencia_Servidores_Publicos',
    'Numero_Cotistas_Subordinada_Sociedade_Seguradora',
    'Numero_Cotistas_Subordinada_Sociedade_Capitalizacao',
    'Numero_Cotistas_Subordinada_FIC_FIDC',
    'Numero_Cotistas_Subordinada_FII',
    'Numero_Cotistas_Subordinada_Clube_Investimento',
    'Numero_Cotistas_Subordinada_Outros'
]


def carrega_dados(arquivo: str) -> pd.DataFrame:
    '''
    Carrega dados de um arquivo CSV.

    Args:
        caminho (str): O caminho do arquivo CSV.

    Returns:
        pd.DataFrame: Um DataFrame contendo os dados carregados.
    '''
    logging.debug(f'Carregando dados de {arquivo}')
    dados = pd.read_csv(arquivo, low_memory=False)
    return dados


def remover_colunas_irrelevantes(
        dados: pd.DataFrame,
        colunas_a_dropar: list
) -> pd.DataFrame:
    '''
    Remove colunas irrelevantes do DataFrame.

    Args:
        dados (pd.DataFrame): O DataFrame com os dados.
        colunas_a_dropar (list): Lista de nomes de colunas a serem removidas.

    Returns:
        pd.DataFrame: O DataFrame com as colunas irrelevantes removidas.
    '''
    logging.debug('Removendo colunas irrelevantes')
    dados_processados = dados.drop(colunas_a_dropar, axis=1)
    return dados_processados


def calcular_inadimplencia_total(dados: pd.DataFrame) -> pd.Series:
    '''
    Calcula a coluna 'Inadimplencia_Total'.

    Args:
        dados (pd.DataFrame): O DataFrame com os dados.

    Returns:
        pd.Series: A coluna calculada.
    '''
    inadimplencia_total = (
        dados['Carteira_Direitos_Aquisicao_Inadimplentes'] +
        dados['Carteira_Direitos_Sem_Aquisicao_Inadimplentes']
    )
    return inadimplencia_total


def calcular_provisao_total(dados: pd.DataFrame) -> pd.Series:
    '''
    Calcula a coluna 'Provisao_Total'.

    Args:
        dados (pd.DataFrame): O DataFrame com os dados.

    Returns:
        pd.Series: A coluna calculada.
    '''
    provisao_total = (
        dados['Ativo_Direitos_Aquisicao_Provisao_Reducao'] +
        dados['Ativo_Direitos_Sem_Aquisicao_Provisao_Reducao']
    )
    return provisao_total


def calcular_vr_sem_riscos_e_beneficios(dados: pd.DataFrame) -> pd.Series:
    '''
    Calcula a coluna 'vr_sem_riscos_e_beneficios'.

    Args:
        dados (pd.DataFrame): O DataFrame com os dados.

    Returns:
        pd.Series: A coluna calculada.
    '''
    vr_sem_riscos_e_beneficios = (
        dados['Ativo_Direitos_Sem_Aquisicao_Parcelas_Inadimplentes'] +
        dados['Ativo_Direitos_Sem_Aquisicao_Creditos_Inadimplentes'] -
        dados['Carteira_Direitos_Sem_Aquisicao_Inadimplentes_1_30_Dias'] -
        dados['Ativo_Direitos_Sem_Aquisicao_Provisao_Reducao']
    )
    return vr_sem_riscos_e_beneficios


def calcular_vr_com_riscos_e_beneficios(dados: pd.DataFrame) -> pd.Series:
    '''
    Calcula a coluna 'vr_com_riscos_e_beneficios'.

    Args:
        dados (pd.DataFrame): O DataFrame com os dados.

    Returns:
        pd.Series: A coluna calculada.
    '''
    vr_com_riscos_e_beneficios = (
        dados['Ativo_Direitos_Aquisicao_Parcelas_Inadimplentes'] +
        dados['Ativo_Direitos_Aquisicao_Creditos_Inadimplentes'] -
        dados['Carteira_Direitos_Aquisicao_Inadimplentes_1_30_Dias'] -
        dados['Ativo_Direitos_Aquisicao_Provisao_Reducao']
    )
    return vr_com_riscos_e_beneficios


def calcular_target(dados: pd.DataFrame) -> pd.Series:
    '''
    Calcula a coluna 'target'.

    Args:
        dados (pd.DataFrame): O DataFrame com os dados.

    Returns:
        pd.Series: A coluna calculada.
    '''
    target = (
        dados['vr_sem_riscos_e_beneficios'] +
        dados['vr_com_riscos_e_beneficios']
    )
    return target


def criar_variaveis(dados: pd.DataFrame) -> pd.DataFrame:
    '''
    Cria variáveis no DataFrame.

    Args:
        dados (pd.DataFrame): O DataFrame com os dados.

    Returns:
        pd.DataFrame: O DataFrame com as variáveis criadas.
    '''
    dados['Inadimplencia_Total'] = calcular_inadimplencia_total(dados)
    dados['Provisao_Total'] = calcular_provisao_total(dados)
    dados['vr_sem_riscos_e_beneficios'] = calcular_vr_sem_riscos_e_beneficios(
        dados)
    dados['vr_com_riscos_e_beneficios'] = calcular_vr_com_riscos_e_beneficios(
        dados)
    dados['target'] = calcular_target(dados)
    dados['Inadimplencia_Total_Nao_Normalizada'] = dados['Inadimplencia_Total']
    dados['Provisao_Total_Nao_Normalizada'] = dados['Provisao_Total']
    dados['Recompra_Nao_Normalizada'] = dados['Negocios_Recompras_Valor']
    dados['Substituicao_Nao_Normalizada'] = dados['Negocios_Substituicoes_Valor']
    dados.drop(['vr_sem_riscos_e_beneficios',
               'vr_com_riscos_e_beneficios'], axis=1, inplace=True)

    return dados


def processar_carteira(dados: pd.DataFrame) -> pd.DataFrame:
    '''
    Processa a coluna 'Carteira' e cria a coluna 'Carteira_Classificação'.

    Args:
        dados (pd.DataFrame): O DataFrame com os dados.

    Returns:
        pd.DataFrame: O DataFrame com a coluna 'Carteira_Classificação' criada.
    '''
    logging.debug('Processando carteira')

    carteiras = [
        'Industrial',
        'Comercial_Total',
        'Servicos_Total',
        'Agronegocio',
        'Financeiro',
        'Cartao_Credito',
        'Factoring',
        'Setor_Publico',
        'Acoes_Judiciais',
        'Propriedade_Intelectual',
        'Mercado_Imobiliario',
        'Middle_Market',
        'Credito_Pessoal_Consignado'
    ]

    def classificar_carteira(fundo):
        for carteira in carteiras:
            if fundo[f'Carteira_{carteira}'] > 0.99 * fundo['Carteira']:
                return carteira

        return 'Multimercado'

    dados['Carteira_Classificação'] = dados.apply(classificar_carteira, axis=1)
    return dados


def calcula_patrimonio_positivo(dados: pd.DataFrame) -> pd.DataFrame:
    '''
    Calcula a coluna 'Patrimonio_Real' com base na coluna
    'Patrimonio_Liquido' e remove a coluna original.

    Args:
        dados (pd.DataFrame): O DataFrame com os dados.

    Returns:
        pd.DataFrame: O DataFrame com a coluna 'Patrimonio_Real'
        calculada e a original removida.
    '''
    logging.debug('Calculando patrimônio positivo')
    dados['Patrimonio_Liquido'].fillna(0, inplace=True)
    dados['Patrimonio_Real'] = dados.query('Patrimonio_Liquido > 0')[
        'Patrimonio_Liquido']
    dados = dados.drop(columns=['Patrimonio_Liquido'])
    dados.reset_index(drop=True, inplace=True)
    return dados


def remove_colunas_iniciadas_com(
        dados: pd.DataFrame,
        inicio_coluna: str,
        excecoes: list = []
) -> pd.DataFrame:
    '''
    Remove colunas iniciadas com um prefixo, exceto as colunas especificadas.

    Args:
        dados (pd.DataFrame): O DataFrame com os dados.
        inicio_coluna (str): O prefixo das colunas a serem removidas.
        excecoes (list): Lista de nomes de colunas a serem mantidas.

    Returns:
        pd.DataFrame: O DataFrame com as colunas removidas.
    '''
    logging.debug(
        f'Removendo colunas iniciadas com {inicio_coluna} exceto {excecoes}')
    colunas = dados.columns
    if len(excecoes) > 0:
        colunas = [coluna for coluna in colunas if coluna not in excecoes]
    colunas_a_dropar = [
        coluna for coluna in colunas if coluna.startswith(inicio_coluna)]
    dados = dados.drop(columns=colunas_a_dropar)
    return dados


def mapeia_variaveis_categoricas(dados: pd.DataFrame) -> pd.DataFrame:
    '''
    Mapeia variáveis categóricas para valores numéricos no DataFrame.

    Args:
        dados (pd.DataFrame): O DataFrame com os dados.

    Returns:
        pd.DataFrame: O DataFrame com as variáveis categóricas mapeadas.
    '''
    logging.debug('Mapeando variáveis categóricas')
    mapeamento = {'Sim': 1, 'Não': 0, 'ABERTO': 1, 'FECHADO': 0}
    dados = dados.replace(mapeamento)
    return dados


def data_object_para_datetime(dados: pd.DataFrame, coluna: str) -> pd.DataFrame:
    '''
    Converte uma coluna de objetos de data em datetime.

    Args:
        dados (pd.DataFrame): O DataFrame com os dados.
        coluna (str): O nome da coluna a ser convertida.

    Returns:
        pd.DataFrame: O DataFrame com a coluna convertida.
    '''
    logging.debug(f'Convertendo coluna {coluna} para datetime')
    dados[coluna] = pd.to_datetime(dados[coluna]).dt.strftime('%Y-%m')
    return dados


def label_enconding(
        dados: pd.DataFrame,
        coluna_base: str,
        coluna_alvo: str
) -> pd.DataFrame:
    '''
    Aplica Label Encoding a uma coluna categórica e remove a coluna original.

    Args:
        dados (pd.DataFrame): O DataFrame com os dados.
        coluna_base (str): O nome da coluna original a ser codificada.
        coluna_alvo (str): O nome da nova coluna com os dados codificados.

    Returns:
        pd.DataFrame: O DataFrame com a coluna codificada e a original removida.
    '''
    logging.debug(f'Aplicando label encoding na coluna {coluna_base}')
    label_encoder = LabelEncoder()
    dados[coluna_alvo] = label_encoder.fit_transform(dados[coluna_base])
    dados.drop(columns=[coluna_base], inplace=True)
    return dados


def remove_fundos_exclusivos_e_duplicados(dados: pd.DataFrame) -> pd.DataFrame:
    '''
    Remove fundos exclusivos e duplicados do DataFrame.

    Args:
        dados (pd.DataFrame): O DataFrame com os dados.

    Returns:
        pd.DataFrame: O DataFrame com fundos exclusivos e duplicados removidos.
    '''
    logging.debug('Removendo fundos exclusivos e duplicados')
    # Exclusão de fundos exclusivos
    dados_v1 = dados.query('Fundo_Exclusivo == 0')
    dados_v1 = dados_v1.drop('Fundo_Exclusivo', axis=1)

    # Exclusão de fundos com cotistas vinculados por interesse
    dados_v2 = dados_v1.query('Cotistas_Vinculados_Interesse == 0')
    dados_v2 = dados_v2.drop('Cotistas_Vinculados_Interesse', axis=1)

    dados_finais = dados_v2.drop_duplicates()
    return dados_finais


def calcula_negocios_alienacoes(dados: pd.DataFrame) -> pd.DataFrame:
    '''
    Calcula a coluna 'Negocios_Alienacoes_Valor' com base
    em outras colunas e remove as colunas originais.

    Args:
        dados (pd.DataFrame): O DataFrame com os dados.

    Returns:
        pd.DataFrame: O DataFrame com as colunas calculadas e as originais removidas.
    '''
    logging.debug('Calculando negocios e alienacoes')
    colunas_uteis = [
        'Negocios_Alienacoes_Cedente_Valor',
        'Negocios_Alienacoes_Prestadores_Valor',
        'Negocios_Alienacoes_Terceiros_Valor'
    ]

    soma_colunas_uteis = dados[colunas_uteis].sum(axis=1)
    dados['Negocios_Alienacoes_Valor'] = soma_colunas_uteis
    dados = dados.drop(colunas_uteis, axis=1)
    return dados


def normaliza_dados(dados: pd.DataFrame) -> pd.DataFrame:
    '''
    Normaliza colunas numéricas no DataFrame usando Min-Max Scaling.

    Args:
        dados (pd.DataFrame): O DataFrame com os dados.

    Returns:
        pd.DataFrame: O DataFrame com as colunas normalizadas.
    '''
    logging.debug('Normalizando dados')
    # Inicialização do objeto MinMaxScaler
    scaler = MinMaxScaler()

    # Seleção das colunas numéricas dos dados
    dados["Taxas_Direitos_Aquisicao_Desconto_Compra_Media_Ponderada"] = pd.to_numeric(
        dados["Taxas_Direitos_Aquisicao_Desconto_Compra_Media_Ponderada"],
        errors='coerce'
    )
    colunas_numericas = dados.select_dtypes(include='number').columns
    colunas_numericas = colunas_numericas.drop([
        'ID_Participante',
        'Carteira_Classificação_encoded',
        'Forma_Condominio',
        'Provisao_Total_Nao_Normalizada',
        'Inadimplencia_Total_Nao_Normalizada',
        'Substituicao_Nao_Normalizada',
        'Recompra_Nao_Normalizada',
        'CNPJ_Administrador'
    ])

    # Aplicação da normalização Min Max às colunas numéricas
    dados[colunas_numericas] = scaler.fit_transform(dados[colunas_numericas])
    return dados


def exporta_dados(dados: pd.DataFrame, caminho: str) -> None:
    '''
    Exporta os dados para um arquivo CSV.

    Args:
        dados (pd.DataFrame): O DataFrame com os dados.
        caminho (str): O caminho do arquivo CSV.
    '''
    logging.debug(f'Exportando dados para {caminho}')
    caminho = path.join(
        path.dirname(__file__),
        caminho
    )

    if not path.exists(path.dirname(caminho)):
        makedirs(path.dirname(caminho))

    dados.to_csv(caminho, index=False)


def pipeline_preparacao(
        dados,
        log_level=logging.DEBUG,
        exportar_arquivo: bool = True
) -> pd.DataFrame:

    logging.basicConfig(
        level=log_level,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

    logging.info('Iniciando pipeline de preparação')

    dados = remover_colunas_irrelevantes(dados, colunas_irrelevantes)
    dados = processar_carteira(dados)
    dados = criar_variaveis(dados)
    dados = calcula_patrimonio_positivo(dados)
    dados = remove_colunas_iniciadas_com(
        dados,
        'Taxas_',
        [
            'Taxas_Direitos_Aquisicao_Desconto_Compra_Media_Ponderada',
            'Taxas_Direitos_Aquisicao_Juros_Compra_Media_Ponderada',
            'Taxas_Direitos_Sem_Aquisicao_Desconto_Compra_Media_Ponderada',
            'Taxas_Direitos_Sem_Aquisicao_Juros_Compra_Media_Ponderada'
        ]
    )

    dados = remove_colunas_iniciadas_com(dados, 'Liquidez_')
    dados = remove_colunas_iniciadas_com(dados, 'Ativo')
    dados = remove_colunas_iniciadas_com(dados, 'Passivo')
    dados = remove_colunas_iniciadas_com(dados, 'Carteira_Direitos')
    dados = calcula_negocios_alienacoes(dados)
    dados = mapeia_variaveis_categoricas(dados)
    dados = remove_fundos_exclusivos_e_duplicados(dados)
    dados = data_object_para_datetime(dados, 'Data_Competencia')
    dados = label_enconding(
        dados,
        'Carteira_Classificação',
        'Carteira_Classificação_encoded'
    )

    dados = normaliza_dados(dados)

    dados.fillna(0, inplace=True)

    if exportar_arquivo:
        exporta_dados(dados, '../../data/tratado/dados_cvm_tratados_novo.csv')

    dados = dados.sort_values(by=['Data_Competencia'])

    logging.info('Pipeline de preparação finalizado')
    logging.info(dados.shape)

    return dados


if __name__ == '__main__':
    pipeline_preparacao('../../data/dados_cvm.csv')
