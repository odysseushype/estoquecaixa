import pandas as pd
import streamlit as st
from datetime import timedelta
import re
import unicodedata

# =========================
# Mapeamento de Caixa para Fornecedor
# =========================
mapa_fornecedor = {
    "11.000.00003": "GUAÇU",
    "11.000.00003V1": "GUAÇU",
    "11.000.00163": "GUAÇU",
    "11.000.00165": "GUAÇU",
    "11.000.00180": "GUAÇU",
    "11.000.00182": "GUAÇU",
    "11.000.00184": "GUAÇU",
    "11.000.00185": "GUAÇU",
    "11.000.00189": "GUAÇU",
    "11.000.00249": "MAET",
    "11.000.00250": "GUAÇU",
    "11.000.00252": "GUAÇU",
    "11.000.00263": "GUAÇU",
    "11.000.00269": "IRANI",
    "11.000.00270": "GUAÇU",
    "11.000.00274": "IRANI",
    "11.000.00290": "GUAÇU",
    "11.000.00291": "GUAÇU",
    "11.000.00292": "GUAÇU",
    "11.000.00293": "GUAÇU",
    "11.000.00295": "GUAÇU",
    "11.000.00297": "GUAÇU",
    "11.000.00298": "GUAÇU",
    "11.000.00303": "GUAÇU",
    "11.000.00304": "GUAÇU",
    "11.000.00305": "GUAÇU",
    "11.000.00306": "GUAÇU",
    "11.000.00309": "GUAÇU",
    "11.000.00311": "GUAÇU",
    "11.000.00313": "GUAÇU",
    "11.000.00314": "GUAÇU",
    "11.000.00315": "GUAÇU",
    "11.000.00316": "GUAÇU",
    "11.000.00317": "GUAÇU",
    "11.000.00318": "GUAÇU",
    "11.000.00319": "GUAÇU",
    "11.000.00323": "IRANI",
    "11.000.00324": "IRANI",
    "11.000.00325": "GUAÇU",
    "11.000.00326": "IRANI",
    "11.000.00327": "GUAÇU",
    "11.000.00328": "GUAÇU",
    "11.000.00329": "MAET",
    "11.000.00330": "MAET",
    "11.000.00331": "MAET",
    "11.000.00332": "MAET",
    "11.000.00333": "MAET",
    "11.000.00334": "GUAÇU",
    "11.000.00335": "GUAÇU",
    "11.000.00336": "IRANI",
    "11.001.00011": "IRANI",
    "11.001.00012": "IRANI",
    "11.001.00017": "IRANI",
    "11.001.00033": "GUAÇU",
    "11.001.00047": "IRANI",
    "11.001.00049": "IRANI",
    "11.001.00053": "IRANI",
    "11.001.00064": "GUAÇU",
    "11.001.00066": "IRANI",
    "11.001.00070": "IRANI",
    "11.001.00071": "GUAÇU",
    "11.001.00075": "MAET",
    "11.001.00078": "IRANI",
    "11.001.00125": "IRANI",
    "11.001.00185": "GUAÇU",
    "11.001.00186": "GUAÇU",
    "11.001.00188": "IRANI",
    "11.001.00189V69": "GUAÇU",
    "11.001.00191": "IRANI",
    "11.001.00213": "IRANI",
    "11.001.00226": "GUAÇU",
    "11.001.00237": "GUAÇU",
    "11.001.00245": "IRANI",
    "11.001.00247": "GUAÇU",
    "11.001.00250": "GUAÇU",
    "11.001.00252": "GUAÇU",
    "11.001.00253": "GUAÇU",
    "11.001.00254": "IRANI",
    "11.001.00255": "GUAÇU",
    "11.001.00261": "IRANI",
    "11.001.00263": "GUAÇU",
    "11.001.00269": "IRANI",
    "11.001.00270": "GUAÇU",
    "11.001.00271": "GUAÇU",
    "11.001.00279": "GUAÇU",
    "11.001.00282": "IRANI",
    "11.001.00283": "IRANI",
    "11.001.00288": "GUAÇU",
    "11.001.00290": "GUAÇU",
    "11.001.00292": "GUAÇU",
    "11.001.00293": "GUAÇU",
    "11.001.00296": "GUAÇU",
    "11.001.00298": "GUAÇU",
    "11.001.00299": "GUAÇU",
    "11.001.00301": "GUAÇU",
    "11.001.00302": "GUAÇU",
    "11.001.00305": "GUAÇU",
    "11.001.00306": "GUAÇU",
    "11.001.00307": "GUAÇU",
    "11.001.00308": "GUAÇU",
    "11.001.00309": "GUAÇU",
    "11.001.00310": "GUAÇU",
    "11.001.00311": "GUAÇU",
    "11.001.00312": "GUAÇU",
    "11.001.00314": "GUAÇU",
    "11.001.00315": "GUAÇU",
    "11.001.00317": "GUAÇU",
    "11.001.00319": "MAET",
    "11.001.00320": "GUAÇU",
    "11.001.00321": "GUAÇU",
    "11.001.00322": "IRANI",
    "11.001.00323": "GUAÇU",
    "11.001.00324": "GUAÇU",
    "11.001.00325": "GUAÇU",
    "11.001.00326": "IRANI",
    "11.001.00329": "GUAÇU",
    "11.001.00330": "GUAÇU",
    "11.001.00331": "GUAÇU",
    "11.001.00338": "IRANI",
    "11.001.00339": "GUAÇU",
    "11.001.00340": "IRANI",
    "11.001.00341": "GUAÇU",
    "11.001.00344": "IRANI",
    "11.001.00346": "GUAÇU",
    "11.001.00347": "GUAÇU",
    "11.001.00349": "GUAÇU",
    "11.001.00351": "MAET",
    "11.001.00353": "MAET",
    "11.001.00354": "MAET",
    "11.001.00355": "MAET",
    "11.001.00356": "IRANI",
    "11.001.00357": "MAET",
    "11.001.00358": "IRANI",
    "11.001.00360": "IRANI",
    "11.001.00361": "MAET",
    "11.001.00363": "IRANI",
    "11.001.00364": "IRANI",
    "11.001.00365": "IRANI",
    "11.001.00366": "MAET",
    "11.001.00367": "MAET",
    "11.001.00369": "IRANI",
    "11.001.00370": "GUAÇU",
    "11.001.00371": "GUAÇU",
    "11.001.00372": "GUAÇU",
    "11.001.00373": "GUAÇU",
    "11.001.00374": "GUAÇU",
    "11.001.00375": "GUAÇU"
}
# =========================
# Função para calcular Dia Entrega
# =========================
def calcular_dia_entrega(dt):
    if pd.isna(dt):
        return None
    if dt.weekday() == 0 and dt.hour < 19:
        entrega = dt - timedelta(days=3)
    elif dt.weekday() == 5:
        entrega = dt - timedelta(days=1)
    elif dt.weekday() == 6:
        entrega = dt - timedelta(days=2)
    elif dt.hour < 19:
        entrega = dt - timedelta(days=1)
    else:
        entrega = dt
    return entrega.replace(hour=19, minute=0, second=0, microsecond=0)

# =========================
# Função para expandir produção por dia útil
# =========================
# Na função expandir_producao, adicionar uma chave única
def expandir_producao(row):
    try:
        inicio = row['Inicio']
        termino = row['Termino']
        qtd_total = row['Quantidade']
        caixa = str(row.get('Caixa', 'Caixa Padrão')).strip()
        fornecedor = mapa_fornecedor.get(caixa, 'Fornecedor Desconhecido')

        dias_uteis = []
        dia_atual = inicio
        while dia_atual <= termino:
            if dia_atual.weekday() != 6:
                dias_uteis.append(dia_atual)
            dia_atual += timedelta(days=1)

        if not dias_uteis or pd.isna(qtd_total) or qtd_total == 0:
            return pd.DataFrame()

        qtd_por_dia = qtd_total / len(dias_uteis)
        linhas = []
        for dia in dias_uteis:
            dia_entrega = calcular_dia_entrega(dia)
            ordem_unica = extrair_ordem_unica(row.get('Ordem / oper / split / Descrição', ''))
            linhas.append({
                'Ordem / oper / split / Descrição': str(row.get('Ordem / oper / split / Descrição', '')).strip(),
                'Item/descrição': str(row.get('Item/descrição', '')).strip(),
                'Data Produção': dia.strftime('%d/%m/%Y'),
                'Caixa': caixa,
                'Fornecedor': fornecedor,
                'Quantidade': qtd_por_dia,
                'Dia Entrega': dia_entrega,
                'OrdemUnica': ordem_unica,
                'ChaveUnica': f"{ordem_unica}_{caixa}_{dia_entrega.strftime('%Y%m%d')}"  # Adiciona chave única
            })
        return pd.DataFrame(linhas)
    except Exception as e:
        st.error(f"Erro ao processar linha: {e}")
        return pd.DataFrame()

# =========================
# Função para gerar CSV
# =========================
def gerar_csv(df):
    df_export = df.copy()
    if 'Caixa' in df_export.columns:
        df_export['Caixa'] = df_export['Caixa'].astype(str)
    if 'Quantidade' in df_export.columns:
        df_export['Quantidade'] = df_export['Quantidade'].map(
            lambda x: f"{x:.2f}".replace('.', ',') if pd.notna(x) else ''
        )
    return df_export.to_csv(index=False, sep=";", encoding="utf-8-sig")

# =========================
# Função para processar arquivo de estoque
# =========================
def processar_estoque(uploaded_stock_file):
    try:
        if uploaded_stock_file is None:
            return {}, None, None, None, None
        
        # Identificar tipo de arquivo e ler adequadamente
        nome_arquivo = uploaded_stock_file.name.lower()
        if nome_arquivo.endswith('.csv'):
            df = pd.read_csv(uploaded_stock_file, sep=None, engine='python')
        else:  # Excel
            df = pd.read_excel(uploaded_stock_file)
        
        # Normalizar nomes das colunas
        df.columns = [str(col).strip().upper() for col in df.columns]
        
        # Verificar se as colunas de recebimento existem
        colunas_acuracidade = ['ENTREGA_PROG', 'RECEBIDO']
        tem_colunas_acuracidade = all(any(col_req in col for col in df.columns) for col_req in colunas_acuracidade)
        
        # USAR ESTAS COLUNAS ESPECÍFICAS:
        col_caixa = 'SKU'          # Coluna que contém o código da caixa
        col_qtd = 'EST_TOTAL'      # Coluna que contém a quantidade em estoque
        col_data = 'DATA'          # Coluna que contém a data do estoque
        col_qtd_anterior = 'ESTQ_ANT'  # Coluna que contém a quantidade anterior
        
        # Verificar se as colunas existem
        colunas_necessarias = [col_caixa, col_qtd]
        colunas_faltantes = [col for col in colunas_necessarias if col not in df.columns]
        
        if colunas_faltantes:
            st.error(f"Colunas necessárias não encontradas no arquivo de estoque: {', '.join(colunas_faltantes)}")
            st.write("Colunas disponíveis:", list(df.columns))
            return {}, None, None, None
        
        # Obter a data mais recente no arquivo de estoque
        if col_data in df.columns:
            df['DATA_FORMATADA'] = pd.to_datetime(df[col_data], errors='coerce')
            data_atual = df['DATA_FORMATADA'].max()
            
            if pd.notnull(data_atual):
                # Filtrar apenas os dados da data mais recente
                df_atual = df[df['DATA_FORMATADA'] == data_atual]
                data_atual_str = data_atual.strftime('%d/%m/%Y')
            else:
                df_atual = df
                data_atual_str = "Data não identificada"
        else:
            df_atual = df
            data_atual_str = "Data não disponível"
        
        # Criar mapeamento de caixa para quantidade
        mapa_estoque = {}
        mapa_estoque_anterior = {}
        linhas_processadas = 0
        
        for _, row in df_atual.iterrows():
            try:
                caixa = str(row[col_caixa]).strip()
                qtd_str = str(row[col_qtd]).strip().replace(',', '.')
                
                if caixa and qtd_str and caixa.lower() != 'nan' and qtd_str.lower() != 'nan':
                    try:
                        qtd = float(qtd_str)
                        mapa_estoque[caixa] = qtd
                        linhas_processadas += 1
                        
                        # Obter estoque anterior, se disponível
                        if col_qtd_anterior in df.columns:
                            qtd_ant_str = str(row[col_qtd_anterior]).strip().replace(',', '.')
                            if qtd_ant_str and qtd_ant_str.lower() != 'nan':
                                try:
                                    mapa_estoque_anterior[caixa] = float(qtd_ant_str)
                                except ValueError:
                                    pass
                    except ValueError:
                        pass
            except Exception:
                pass
        
        # Calcular totais
        total_estoque = sum(mapa_estoque.values())
        total_anterior = sum(mapa_estoque_anterior.values())
        
        # Calcular variação
        variacao = total_estoque - total_anterior
        variacao_percentual = (variacao / total_anterior) * 100 if total_anterior > 0 else 0
        
        st.success(f"✅ Estoque carregado: {linhas_processadas} itens processados")
        
        # Processar dados de acuracidade se existirem as colunas necessárias
        dados_acuracidade = None
        if 'ENTREGA_PROG' in df.columns and 'RECEBIDO' in df.columns and 'SKU' in df.columns:
            try:
                # Identificar coluna de data 
                col_data = None
                for col in df.columns:
                    if 'DATA' in col:
                        col_data = col
                        break
                
                if not col_data:
                    st.warning("⚠️ Coluna de data não encontrada no arquivo de estoque")
                    col_data = 'DATA'  # Usar um nome padrão para evitar erros
                    df[col_data] = None
                
                # Converter colunas para numérico
                df['ENTREGA_PROG'] = pd.to_numeric(df['ENTREGA_PROG'].astype(str).str.replace(',', '.'), errors='coerce').fillna(0)
                df['RECEBIDO'] = pd.to_numeric(df['RECEBIDO'].astype(str).str.replace(',', '.'), errors='coerce').fillna(0)
                
                # Adicionar coluna de fornecedor
                df['FORNECEDOR'] = df['SKU'].astype(str).map(lambda x: mapa_fornecedor.get(x, "Desconhecido"))
                
                # Formatar datas para comparação
                df['DATA_FORMATADA'] = pd.to_datetime(df[col_data], errors='coerce')
                
                # Preparar os dados para cruzamento com o programa
                df['SKU'] = df['SKU'].astype(str).str.strip()
                df['DATA_STR'] = df['DATA_FORMATADA'].dt.strftime('%Y-%m-%d')
                
                # Calcular acuracidade
                df['DIFERENCA'] = df['RECEBIDO'] - df['ENTREGA_PROG']
                df['ACURACIDADE'] = ((df['RECEBIDO'] / df['ENTREGA_PROG']) * 100).fillna(0)
                df['ACURACIDADE'] = df['ACURACIDADE'].apply(lambda x: min(100, x) if x > 0 else x)
                
                dados_acuracidade = df
                st.success("✅ Dados de acuracidade de entrega processados com sucesso")
            except Exception as e:
                st.warning(f"Não foi possível processar dados de acuracidade: {str(e)}")
        
        return mapa_estoque, data_atual_str, variacao, variacao_percentual, dados_acuracidade
    
    except Exception as e:
        st.error(f"Erro ao processar o arquivo de estoque: {str(e)}")
        return {}, None, None, None, None

# =========================
# Configuração Streamlit
# =========================
st.set_page_config(page_title="Cronograma de Produção", layout="wide")
st.title("📅 Cronograma de Produção - Detalhado por Dia")

# =========================
# Adicionar CSS personalizado
# =========================
st.markdown("""
<style>
    /* Personalização para texto em itálico nas descrições */
    em {
        color: #666666 !important;  /* Cinza médio */
        font-style: italic;
    }
</style>
""", unsafe_allow_html=True)

# =========================
# Função para processar Excel (RESTAURADA DO CÓDIGO ORIGINAL)
# =========================
def processar_excel(uploaded_file, tipo="novo"):
    df_raw = pd.read_excel(uploaded_file, sheet_name=0, header=None)
    if str(df_raw.iloc[0,0]).strip() != "Centro trabalho":
        df_raw = df_raw.drop(index=[0,1]).reset_index(drop=True)
    df_raw.columns = df_raw.iloc[0]
    df_raw = df_raw.drop(index=0).reset_index(drop=True)

    prefixos_validos = ("CA","JA","CH","SP","MC","GR")
    df_raw = df_raw[df_raw.iloc[:,0].astype(str).str.startswith(prefixos_validos)]
    df_raw.columns = df_raw.columns.str.strip()

    if tipo in ["novo","antigo"]:
        if 'Data / hora programada' in df_raw.columns:
            df_raw[['Inicio','Termino']] = df_raw['Data / hora programada'].astype(str).str.split(' - ', expand=True)
            df_raw['Inicio'] = pd.to_datetime(df_raw['Inicio'], dayfirst=True, errors='coerce')
            df_raw['Termino'] = pd.to_datetime(df_raw['Termino'], dayfirst=True, errors='coerce')
        else:
            df_raw['Inicio'] = pd.NaT
            df_raw['Termino'] = pd.NaT
        if 'Caixa' not in df_raw.columns:
            df_raw['Caixa'] = 'Caixa Padrão'
    return df_raw


# =========================
# Funções auxiliares
# =========================
# Adicionar esta função de limpeza na seção de funções auxiliares (aproximadamente linha 310)
def limpar_descricao(desc):
    """Remove o código do item e limpa a descrição"""
    if not desc or not isinstance(desc, str):
        return ""
    
    # Procura por um hífen e remove tudo antes dele (incluindo o código do item)
    partes = desc.split(' - ', 1)
    if len(partes) > 1:
        # Se encontrou o hífen, retorna apenas a parte após o primeiro hífen
        return partes[1].strip()
    return desc.strip()

def extrair_ordem_unica(ordem_completa):
    """
    Extrai a identificação única da ordem, baseada em XXXXXX / YY / Z
    Retorna apenas a parte que identifica unicamente o item
    """
    if not ordem_completa or not isinstance(ordem_completa, str):
        return ""
    partes = ordem_completa.split(' / ')
    if len(partes) >= 3:
        return f"{partes[0].strip()} / {partes[1].strip()} / {partes[2].strip()}"
    return ordem_completa.strip()

def extrair_codigo_base_sem_split(ordem_completa):
    """
    Extrai apenas o código base da ordem (sem o split)
    Ex: '123456 / 10 / 1' -> '123456 / 10'
    """
    if not ordem_completa or not isinstance(ordem_completa, str):
        return ""
    partes = ordem_completa.split(' / ')
    if len(partes) >= 2:
        return f"{partes[0].strip()} / {partes[1].strip()}"
    return ordem_completa.strip()

def normalizar_texto(txt):
    if txt is None:
        return ""
    txt = str(txt).strip().lower()
    txt = " ".join(txt.split())
    # remove acentos
    txt = unicodedata.normalize("NFKD", txt).encode("ascii", "ignore").decode("ascii")
    return txt

# NOVO: utilidades para mapear datas antigo -> novo por (Caixa, OrdemUnica)
def _mediana_int(nums):
    nums = sorted(nums)
    n = len(nums)
    if n == 0:
        return 0
    if n % 2 == 1:
        return int(round(nums[n//2]))
    return int(round((nums[n//2 - 1] + nums[n//2]) / 2))

def _nearest_not_used(target, candidates, usados):
    # retorna a data de candidates mais próxima de target que não esteja em 'usados'
    disponiveis = [c for c in candidates if c not in usados]
    if not disponiveis:
        return None
    return min(disponiveis, key=lambda d: abs((d - target).days))

def criar_mapeamento_datas_ordem_caixa(df_atual, df_antigo):
    """
    Retorna dict com chaves (caixa, ordem_unica) e valor {data_nova(date) -> data_antiga(date)}.
    Usa mediana do deslocamento para alinhar sequências e faz fallback para data antiga mais próxima.
    """
    mapeamentos = {}
    if df_antigo is None or df_antigo.empty or df_atual is None or df_atual.empty:
        return mapeamentos

    # garantir colunas
    if 'OrdemUnica' not in df_atual.columns:
        df_atual = df_atual.copy()
        df_atual['OrdemUnica'] = df_atual['Ordem / oper / split / Descrição'].apply(extrair_ordem_unica)
    if 'OrdemUnica' not in df_antigo.columns:
        df_antigo = df_antigo.copy()
        df_antigo['OrdemUnica'] = df_antigo['Ordem / oper / split / Descrição'].apply(extrair_ordem_unica)

    pares = set(zip(df_atual['Caixa'], df_atual['OrdemUnica'])) | set(zip(df_antigo['Caixa'], df_antigo['OrdemUnica']))

    for cx, ou in pares:
        new_dates = sorted(set(pd.to_datetime(
            df_atual[(df_atual['Caixa'] == cx) & (df_atual['OrdemUnica'] == ou)]['Dia Entrega']
        ).dt.date))

        old_dates = sorted(set(pd.to_datetime(
            df_antigo[(df_antigo['Caixa'] == cx) & (df_antigo['OrdemUnica'] == ou)]['Dia Entrega']
        ).dt.date))

        if not new_dates or not old_dates:
            mapeamentos[(cx, ou)] = {}
            continue

        # estimar deslocamento global pela mediana das diferenças índice-a-índice
        min_len = min(len(new_dates), len(old_dates))
        diffs = [(old_dates[i] - new_dates[i]).days for i in range(min_len)]
        shift = _mediana_int(diffs) if diffs else 0

        mapping = {}
        usados_old = set()
        old_set = set(old_dates)

        for nd in new_dates:
            candidato = nd + timedelta(days=shift)
            if candidato in old_set and candidato not in usados_old:
                mapping[nd] = candidato
                usados_old.add(candidato)
            else:
                prox = _nearest_not_used(nd, old_dates, usados_old)
                if prox is not None:
                    mapping[nd] = prox
                    usados_old.add(prox)
                else:
                    # sem correspondente
                    mapping[nd] = None

        mapeamentos[(cx, ou)] = mapping

    return mapeamentos

def encontrar_proximos_splits(ordem_unica, caixa, df_novo):
    """
    Procura por ordens similares (mesmo código base, diferente split) 
    quando um item é removido
    """
    if not ordem_unica or not isinstance(ordem_unica, str) or df_novo is None or df_novo.empty:
        return []
    
    # Extrair código base (sem o split)
    codigo_base = extrair_codigo_base_sem_split(ordem_unica)
    if not codigo_base:
        return []
    
    # Procurar por itens com o mesmo código base (independente do split) e a mesma caix
    if 'OrdemUnica' not in df_novo.columns:
        df_novo = df_novo.copy()
        df_novo['OrdemUnica'] = df_novo['Ordem / oper / split / Descrição'].apply(extrair_ordem_unica)
    
    df_novo['CodigoBase'] = df_novo['OrdemUnica'].apply(extrair_codigo_base_sem_split)
    
    # Encontrar todos os registros desta caixa com o mesmo código base
    splits_relacionados = df_novo[(df_novo['CodigoBase'] == codigo_base) & (df_novo['Caixa'] == caixa)]
    
    if splits_relacionados.empty:
        return []
        
    # Retornar as datas encontradas
    return sorted(set(pd.to_datetime(splits_relacionados['Dia Entrega']).dt.strftime('%d/%m')))


# =========================
# Layout principal
# =========================
col_prog, col_estoque, col_prog_ant = st.columns([1, 1, 1])

with col_prog:
    uploaded_file = st.file_uploader("📂 Selecione o arquivo Excel principal", type=["xlsx"])

with col_estoque:
    uploaded_stock_file = st.file_uploader("📦 Arquivo de Estoque", type=["xlsx", "csv"])

with col_prog_ant:
    uploaded_old_file = st.file_uploader("🔄 Arquivo do Programa Anterior", type=["xlsx"])

# Inicializar variáveis para o programa anterior
df_antigo = None
df_antigo_expandidos = None

# Processar programa anterior se for carregado
if uploaded_old_file:
    with st.spinner("Processando programa anterior..."):
        # Processar programa anterior
        df_antigo = processar_excel(uploaded_old_file, tipo="antigo")
        
        # Expandir programa anterior
        df_antigo_expandidos = pd.concat([expandir_producao(row) for _,row in df_antigo.iterrows()], ignore_index=True)
        
        if not df_antigo_expandidos.empty:
            df_antigo_expandidos['Dia Entrega'] = pd.to_datetime(df_antigo_expandidos['Dia Entrega'])
            st.success("✅ Programa anterior processado com sucesso")
        else:
            st.warning("⚠️ Programa anterior não contém dados válidos para exibição.")

# Inicializar mapa de estoque e histórico
mapa_estoque = {}
dados_acuracidade = None
if 'historico_estoque' not in st.session_state:
    st.session_state.historico_estoque = []
    st.session_state.datas_estoque = []

if uploaded_stock_file:
    # Processar o estoque atual - retorna os valores corretos e dados de acuracidade
    mapa_estoque, data_estoque, variacao_total, variacao_percentual, dados_acuracidade = processar_estoque(uploaded_stock_file)
    
    # Calcular estatísticas do estoque
    total_itens = len(mapa_estoque)
    quantidade_total = sum(mapa_estoque.values())
    
    # Mostrar resumo do estoque em um expansor
    with st.expander("📦 Resumo do Estoque"):
        # Layout em colunas para as métricas
        col1, col2, col3 = st.columns(3)
        
        # Coluna 1: Informações básicas
        with col1:
            st.metric("Total de itens em estoque", f"{total_itens}")
            st.write(f"**Data do estoque:** {data_estoque}")
        
        # Coluna 2: Quantidade total
        with col2:
            st.metric("Quantidade total em estoque", f"{quantidade_total:,.0f}")
        
        # Coluna 3: Variação em relação ao estoque anterior
        with col3:
            if variacao_total is not None:
                delta_color = "normal" if variacao_total >= 0 else "inverse"
                st.metric(
                    "Variação em relação ao estoque anterior", 
                    f"{quantidade_total:,.0f}",
                    delta=f"{variacao_total:+,.0f} ({variacao_percentual:.1f}%)",
                    delta_color=delta_color
                )
            else:
                st.write("**Variação:** Não disponível")
        
        # Tabela detalhada do estoque
        st.subheader("Detalhes do Estoque")
        df_estoque = pd.DataFrame(list(mapa_estoque.items()), columns=['Caixa', 'Quantidade'])
        df_estoque = df_estoque.sort_values('Quantidade', ascending=False)
        st.dataframe(df_estoque, use_container_width=True)

# Processamento do arquivo principal
if uploaded_file:
    df_novo = processar_excel(uploaded_file, tipo="novo")
    
    # Extrair data do nome do arquivo
    filename = uploaded_file.name
    date_match = re.search(r'.*?(\d{2})_(\d{2})_(\d{4})', filename)
    
    if date_match:
        dia, mes, ano = date_match.groups()
        data_programa = pd.Timestamp(f"{ano}-{mes}-{dia}")
        st.success(f"✅ Data do programa: {data_programa.strftime('%d/%m/%Y')}")
    else:
        # Se não encontrar data no nome, usar data atual
        data_programa = pd.Timestamp.now().floor('D')
        st.warning(f"⚠️ Data não identificada no nome do programa. Usando data atual: {data_programa.strftime('%d/%m/%Y')}")
    
    # Programa Original em expansor
    with st.expander("📋 Programa Original (limpo)"):
        st.dataframe(df_novo,use_container_width=True)
        st.download_button("⬇️ Baixar Programa Original (CSV)", gerar_csv(df_novo), "programa_original.csv", mime="text/csv")

    # Expandir produção
    df_expandidos = pd.concat([expandir_producao(row) for _,row in df_novo.iterrows()], ignore_index=True)
    
    # Programa Expandido em expansor
    with st.expander("📋 Programa Expandido Completo"):
        if not df_expandidos.empty:
            df_expandidos['Dia Entrega'] = pd.to_datetime(df_expandidos['Dia Entrega'])
            df_expandidos['Dia Entrega Formatado'] = df_expandidos['Dia Entrega'].dt.strftime('%d/%m/%Y %H:%M')
            st.dataframe(
                df_expandidos[['Ordem / oper / split / Descrição','Item/descrição','Data Produção','Caixa','Fornecedor','Quantidade','Dia Entrega Formatado']],
                use_container_width=True
            )
            st.download_button("⬇️ Baixar Programa Expandido (CSV)", gerar_csv(df_expandidos), "programa_expandido.csv", mime="text/csv")
        else:
            st.warning("Nenhum dado para exibir.")
    
    # =========================
    # Dados por Fornecedor (NOVO)
    # =========================
    st.subheader("🏭 Dados por Fornecedor")
    if not df_expandidos.empty:
        # Obter lista única de fornecedores
        fornecedores = sorted(df_expandidos['Fornecedor'].unique())
        
        # Criar abas para cada fornecedor
        tabs = st.tabs([f"📊 {fornecedor}" for fornecedor in fornecedores])
        
        # Preencher cada aba com dados específicos do fornecedor
        for i, fornecedor in enumerate(fornecedores):
            with tabs[i]:
                # Filtrar dados apenas para este fornecedor
                df_forn = df_expandidos[df_expandidos['Fornecedor'] == fornecedor]

                # Filtrar dados do programa anterior para este fornecedor, se disponível
                df_forn_antigo = None
                if df_antigo_expandidos is not None:
                    df_forn_antigo = df_antigo_expandidos[df_antigo_expandidos['Fornecedor'] == fornecedor]

                # NOVO: mapeamento de datas por (Caixa, OrdemUnica) para o fornecedor
                mapeamento_datas = criar_mapeamento_datas_ordem_caixa(df_forn, df_forn_antigo) if df_forn_antigo is not None else {}

                # Total de caixas para o fornecedor
                total_forn = df_forn['Quantidade'].sum()
                
                # Mostrar totais comparativos se tiver programa anterior
                if df_forn_antigo is not None:
                    total_forn_antigo = df_forn_antigo['Quantidade'].sum()
                    variacao = total_forn - total_forn_antigo
                    
                    # Mostrar totais em formato de métricas
                    col1, col2 = st.columns(2)
                    with col1:
                        st.metric(
                            "Total de caixas (programa atual)", 
                            f"{total_forn:.0f}"
                        )
                    with col2:
                        delta_color = "normal" if variacao >= 0 else "inverse"
                        st.metric(
                            "Variação em relação ao programa anterior", 
                            f"{total_forn:.0f}",
                            delta=f"{variacao:+.0f}",
                            delta_color=delta_color
                        )
                else:
                    # Exibir o total normal sem comparativo
                    st.write(f"**Total de caixas: {total_forn:.0f}**")
                
                # Preparar dados para visualização semanal
                df_semana = df_forn.copy()
                
                # Adicionar coluna de semana e ano
                df_semana['Semana'] = df_semana['Dia Entrega'].dt.isocalendar().week
                df_semana['Ano'] = df_semana['Dia Entrega'].dt.isocalendar().year
                    
                # Criar semanas_unicas
                semanas_unicas = [f"{semana}/{ano}" for semana, ano in zip(df_semana['Semana'], df_semana['Ano'])]
                semanas_unicas = sorted(set(semanas_unicas))  # Remove duplicados e ordena

                # Criar abas para cada semana
                semana_tabs = st.tabs([f"📅 Semana {semana_str}" for semana_str in semanas_unicas])
                
                # Resetar o estoque consumido para cada fornecedor
                estoque_consumido_global = {}
                
                # Para cada semana, criar uma aba
                for sem_idx, semana_str in enumerate(semanas_unicas):
                    with semana_tabs[sem_idx]:
                        try:
                            semana_num, ano = map(int, semana_str.split("/"))
                            
                            # Filtrar dados da semana atual
                            df_semana_atual = df_forn[
                                (df_forn['Dia Entrega'].dt.isocalendar().week == semana_num) &
                                (df_forn['Dia Entrega'].dt.isocalendar().year == ano)
                            ]
                            
                            # Filtrar dados do programa anterior para esta semana, se disponível
                            df_semana_antiga = None
                            if df_forn_antigo is not None:
                                df_semana_antiga = df_forn_antigo[
                                    (df_forn_antigo['Dia Entrega'].dt.isocalendar().week == semana_num) &
                                    (df_forn_antigo['Dia Entrega'].dt.isocalendar().year == ano)
                                ]
                            
                            # Obter datas únicas na semana
                            datas_unicas = sorted(df_semana_atual['Dia Entrega'].dt.date.unique())
                            
                            # Filtrar datas para mostrar apenas as >= data_programa
                            if data_programa is not None:
                                datas_unicas = [data for data in datas_unicas 
                                              if data >= data_programa.date()]
                            
                            # Se houver dados do programa anterior, adicione suas datas também
                            datas_antigas_adicionais = []
                            if df_semana_antiga is not None and not df_semana_antiga.empty:
                                datas_antigas = sorted(df_semana_antiga['Dia Entrega'].dt.date.unique())
                                if data_programa is not None:
                                    datas_antigas = [data for data in datas_antigas if data >= data_programa.date()]
                                datas_antigas_adicionais = [data for data in datas_antigas if data not in datas_unicas]
                            
                            # Combine as datas e ordene
                            todas_datas = sorted(list(datas_unicas) + datas_antigas_adicionais)
                            
                            if len(todas_datas) > 0:
                                # Adicionar filtros para seleção de informações
                                with st.expander("🔍 Filtros de visualização", expanded=False):
                                    col1, col2 = st.columns(2)
                                    with col1:
                                        mostrar_com_estoque = st.checkbox("✅ Mostrar itens com estoque suficiente", value=True, key=f"est_ok_{fornecedor}_{semana_str}")
                                        mostrar_sem_estoque = st.checkbox("⚠️ Mostrar itens com estoque insuficiente", value=True, key=f"est_falta_{fornecedor}_{semana_str}")
                                    with col2:
                                        mostrar_novos = st.checkbox("🆕 Mostrar itens novos/alterados", value=True, key=f"novos_{fornecedor}_{semana_str}")
                                        mostrar_removidos = st.checkbox("❌ Mostrar itens removidos", value=True, key=f"removidos_{fornecedor}_{semana_str}")
                                
                                # Criar abas para cada dia dentro da semana
                                dias_tabs = st.tabs([f"📆 {data.strftime('%d/%m/%Y')} ({data.strftime('%a')})" for data in todas_datas])
                                
                                for idx, data in enumerate(todas_datas):
                                    # Em vez de usar colunas, usar abas para cada dia
                                    with dias_tabs[idx]:
                                        # Filtrar dados apenas para este dia
                                        df_dia = df_semana_atual[df_semana_atual['Dia Entrega'].dt.date == data]
                                        
                                        # Filtrar dados do programa anterior para este dia, se disponível
                                        df_dia_antigo = None
                                        if df_semana_antiga is not None:
                                            df_dia_antigo = df_semana_antiga[df_semana_antiga['Dia Entrega'].dt.date == data]

                                        # Calcular total do dia
                                        total_dia = df_dia['Quantidade'].sum()
                                        
                                        # Agrupar caixas do mesmo tipo e somar quantidades
                                        df_caixas_agrupadas = df_dia.groupby('Caixa')['Quantidade'].sum().reset_index()
                                        
                                        # Criar um dicionário com TODAS as caixas do programa anterior para este fornecedor
                                        # com informações sobre em que dias elas aparecem
                                        # Formato: {caixa: {ordem_unica: {datas}}}
                                        caixas_antigas_com_dias = {}
                                        if df_forn_antigo is not None and not df_forn_antigo.empty:
                                            tem_col_ordem_unica_ant = 'OrdemUnica' in df_forn_antigo.columns
                                            for _, r_ant in df_forn_antigo.iterrows():
                                                cx = r_ant['Caixa']
                                                data_ent = pd.to_datetime(r_ant['Dia Entrega']).date()
                                                ordem_u = (
                                                    r_ant['OrdemUnica']
                                                    if tem_col_ordem_unica_ant and pd.notna(r_ant['OrdemUnica'])
                                                    else extrair_ordem_unica(r_ant.get('Ordem / oper / split / Descrição', ''))
                                                )
                                                if not ordem_u:
                                                    continue
                                                caixas_antigas_com_dias.setdefault(cx, {}).setdefault(ordem_u, set()).add(data_ent)
                                        
                                        # Verificar se temos dados específicos para esta data no programa anterior
                                        caixas_antigas = {}
                                        total_dia_antigo = 0
                                        data_existe_no_programa_anterior = False
                                        
                                        if df_dia_antigo is not None and not df_dia_antigo.empty:
                                            # Se temos dados para esta data específica, usar eles
                                            df_caixas_antigas = df_dia_antigo.groupby('Caixa')['Quantidade'].sum().reset_index()
                                            caixas_antigas = dict(zip(df_caixas_antigas['Caixa'], df_caixas_antigas['Quantidade']))
                                            total_dia_antigo = df_dia_antigo['Quantidade'].sum()
                                            data_existe_no_programa_anterior = True
                                                                                # Inicializar lista (usada mais abaixo para exibir e também para o caso sem comparativo)
                                        removidos_msgs = []
                                        
                                        # Encontrar itens removidos (por OrdemUnica + Caixa) e mapear para novas datas
                                        if df_dia_antigo is not None and not df_dia_antigo.empty:
                                             # garantir coluna OrdemUnica no df_dia_antigo e df_dia
                                             if 'OrdemUnica' not in df_dia_antigo.columns:
                                                 df_dia_antigo = df_dia_antigo.copy()
                                                 df_dia_antigo['OrdemUnica'] = df_dia_antigo['Ordem / oper / split / Descrição'].apply(extrair_ordem_unica)
                                             if 'OrdemUnica' not in df_dia.columns:
                                                 df_dia = df_dia.copy()
                                                 df_dia['OrdemUnica'] = df_dia['Ordem / oper / split / Descrição'].apply(extrair_ordem_unica)
                                             # Pares (Caixa, OrdemUnica) no programa antigo deste dia
                                             pares_antigos = (
                                                 df_dia_antigo.groupby(['Caixa','OrdemUnica'], as_index=False)['Quantidade']
                                                 .sum()
                                             )

                                             for _, r in pares_antigos.iterrows():
                                                cx = r['Caixa']
                                                ou = str(r['OrdemUnica']).strip()
                                                qtd_ant = float(r['Quantidade']) if pd.notna(r['Quantidade']) else 0.0

                                                # SOLUÇÃO TEMPORÁRIA: ignorar caixas específicas que sabemos serem produzidas em múltiplas máquinas
                                                if cx == "11.000.00336":
                                                    continue  # Pular esta caixa na verificação de remoções

                                                # Verificação existente - se a caixa ainda existe na mesma data (em qualquer ordem)
                                                existe_no_atual_qualquer_ordem = not df_dia[df_dia['Caixa'] == cx].empty
                                                
                                                # Se a caixa ainda existe na mesma data, não é removida
                                                if existe_no_atual_qualquer_ordem:
                                                    continue

                                                # Verificar para onde foi movido este par usando o mapeamento (old -> new)
                                                datas_destino = []
                                                mapa = mapeamento_datas.get((cx, ou), {})
                                                for data_nova, data_antiga in mapa.items():
                                                    if data_antiga == data:
                                                        datas_destino.append(pd.to_datetime(data_nova).strftime('%d/%m'))
                                                datas_destino = sorted(set(datas_destino))

                                                # Estoque desta caixa
                                                estoque_inicial_removido = mapa_estoque.get(cx, 0)
                                                consumido_ate_agora_removido = estoque_consumido_global.get(cx, 0)
                                                estoque_disponivel_removido = estoque_inicial_removido - consumido_ate_agora_removido
                                                estoque_emoji = "✅" if estoque_disponivel_removido > 0 else "⚠️"

                                                # Descrições só deste par
                                                itens_removidos_dessa_caixa = df_dia_antigo[(df_dia_antigo['Caixa'] == cx) & (df_dia_antigo['OrdemUnica'] == ou)]['Item/descrição'].unique()
                                                descricoes_removidas_limpas = [limpar_descricao(desc) for desc in itens_removidos_dessa_caixa]
                                                descricoes_removidas = '; '.join(descricoes_removidas_limpas) if descricoes_removidas_limpas else "Informação indisponível"

                                                if datas_destino:
                                                    removidos_msgs.append(f"{estoque_emoji} ❌ **{cx}** | Removido (Antes: {qtd_ant:.0f}) | Movido para: {', '.join(datas_destino)} | Estoque: {max(0, estoque_disponivel_removido):.0f} | *{descricoes_removidas}*")
                                                else:
                                                    removidos_msgs.append(f"{estoque_emoji} ❌ **{cx}** | Removido (Antes: {qtd_ant:.0f}) | Estoque: {max(0, estoque_disponivel_removido):.0f} | *{descricoes_removidas}*")
                                             # Agregar por (Caixa, Conjunto de Datas Destino)
                                                agreg = {}  # {(cx, tuple_datas): {'qtd': float, 'descricoes': set()}}
                                                for _, r in pares_antigos.iterrows():
                                                    cx = r['Caixa']
                                                    ou = str(r['OrdemUnica']).strip()
                                                    qtd_ant = float(r['Quantidade']) if pd.notna(r['Quantidade']) else 0.0

                                                    # Se o mesmo par existe no dia atual, não é removido
                                                    existe_no_atual = not df_dia[(df_dia['Caixa'] == cx) & (df_dia['OrdemUnica'] == ou)].empty
                                                    if existe_no_atual:
                                                        continue

                                                    # Verificar para onde foi movido este par usando o mapeamento (old -> new)
                                                    datas_destino = []
                                                    
                                                    # 1. Primeiro procurar no mapeamento de datas
                                                    mapa = mapeamento_datas.get((cx, ou), {})
                                                    for data_nova, data_antiga in mapa.items():
                                                        if data_antiga == data:
                                                            datas_destino.append(pd.to_datetime(data_nova).strftime('%d/%m'))
                                                    
                                                    # 2. Se não encontrou, procurar por splits relacionados no programa novo
                                                    if not datas_destino:
                                                        splits_relacionados = encontrar_proximos_splits(ou, cx, df_forn)
                                                        if splits_relacionados:
                                                            datas_destino = splits_relacionados
                                                    
                                                    datas_destino = tuple(sorted(set(datas_destino)))  # chave estável para agrupar

                                                    # Descrições deste par
                                                    descs = df_dia_antigo[
                                                        (df_dia_antigo['Caixa'] == cx) & (df_dia_antigo['OrdemUnica'] == ou)
                                                    ]['Item/descrição'].dropna().astype(str).tolist()
                                                    descs_limpas = {limpar_descricao(d) for d in descs if d}

                                                    chave = (cx, datas_destino)
                                                    if chave not in agreg:
                                                        agreg[chave] = {'qtd': 0.0, 'descricoes': set()}
                                                    agreg[chave]['qtd'] += qtd_ant
                                                    agreg[chave]['descricoes'].update(descs_limpas)

                                            # Montar mensagens já agregada
                                                removidos_msgs = []
                                                for (cx, datas_destino), info in agreg.items():
                                                    # Se a caixa ainda existe na data atual em qualquer ordem, não é removida
                                                    existe_no_atual_qualquer_ordem = not df_dia[df_dia['Caixa'] == cx].empty
                                                    if existe_no_atual_qualquer_ordem:
                                                        continue
                                                    estoque_inicial_removido = mapa_estoque.get(cx, 0)
                                                    consumido_ate_agora_removido = estoque_consumido_global.get(cx, 0)
                                                    estoque_disponivel_removido = estoque_inicial_removido - consumido_ate_agora_removido
                                                    estoque_emoji = "✅" if estoque_disponivel_removido > 0 else "⚠️"
                                                    descricoes_removidas = '; '.join(sorted(info['descricoes'])) if info['descricoes'] else "Informação indisponível"
                                                    if datas_destino:
                                                        destino_str = ", ".join(datas_destino)
                                                        removidos_msgs.append(
                                                            f"{estoque_emoji} ❌ **{cx}** | Removido (Antes: {info['qtd']:.0f}) | Movido para: {destino_str} | Estoque: {max(0, estoque_disponivel_removido):.0f} | *{descricoes_removidas}*"
                                                        )
                                                    else:
                                                        removidos_msgs.append(
                                                            f"{estoque_emoji} ❌ **{cx}** | Removido (Antes: {info['qtd']:.0f}) | Estoque: {max(0, estoque_disponivel_removido):.0f} | *{descricoes_removidas}*"
                                                        )
                                        
                                        # Exibir bloco no layout
                                        st.markdown(f"**{data.strftime('%d/%m/%Y')} ({data.strftime('%a')})**")
                                        
                                        # Calcular variação em relação ao programa anterior para este dia
                                        if df_dia_antigo is not None and not df_dia_antigo.empty:
                                            total_dia_antigo = df_dia_antigo['Quantidade'].sum()
                                            variacao_dia = total_dia - total_dia_antigo
                                            delta_color = "normal" if variacao_dia >= 0 else "inverse"
                                            
                                            st.metric(
                                                label="Total de Caixas", 
                                                value=f"{total_dia:.0f}",
                                                delta=f"{variacao_dia:+.0f}",
                                                delta_color=delta_color
                                            )
                                        else:
                                            # Sem comparativo - todos os itens serão novos neste caso
                                            st.metric(
                                                label="Total de Caixas", 
                                                value=f"{total_dia:.0f}",
                                                delta=None
                                            )
                                            
                                            # Sem dados do programa anterior para esta data
                                            st.write("_Sem dados do programa anterior para esta data_")
                                        
                                        # Aqui é onde criamos a lista de itens com indicadores:
                                        itens_dia = []
                                        
                                        # Primeiro adicionar itens atuais
                                        for _, row in df_caixas_agrupadas.iterrows():
                                            caixa = row['Caixa']
                                            qtd_total = row['Quantidade']
                                            data_atual = pd.to_datetime(data)  # Converte para datetime
                                            
                                            # Itens (ordens únicas) desta caixa no dia atual
                                            itens_atuais_ord = set(
                                                df_dia.loc[df_dia['Caixa'] == caixa, 'OrdemUnica']
                                                   .dropna().astype(str).str.strip()
                                            )

                                            # NOVO: usar mapeamento para decidir "movido de"
                                            datas_mapeadas = set()
                                            houve_correspondencia_mesma_data = False
                                            for ou in itens_atuais_ord:
                                                mapa = mapeamento_datas.get((caixa, ou), {})
                                                antiga = mapa.get(data_atual.date())
                                                if antiga is None:
                                                    continue
                                                if antiga == data_atual.date():
                                                    houve_correspondencia_mesma_data = True
                                                else:
                                                    datas_mapeadas.add(antiga)

                                            # IMPORTANTE: Verificar se df_dia_antigo existe e tem dados
                                            status_alteracao = ""
                                            qtd_antiga = 0
                                            
                                            if df_dia_antigo is not None and not df_dia_antigo.empty:
                                                caixa_anterior = df_dia_antigo[df_dia_antigo['Caixa'] == caixa]
                                                
                                                if not caixa_anterior.empty:
                                                    qtd_antiga = caixa_anterior['Quantidade'].sum()
                                                    if qtd_total > qtd_antiga:
                                                        status_alteracao = "⬆️ "
                                                    elif qtd_total < qtd_antiga:
                                                        status_alteracao = "⬇️ "
                                                else:
                                                    # não havia essa caixa no dia anterior (para este dia específico)
                                                    pass

                                            # Aplicar rótulo de movido com base no mapeamento (independente de existir a mesma data no antigo)
                                            if datas_mapeadas:
                                                datas_fmt = sorted({pd.to_datetime(d).strftime('%d/%m') for d in datas_mapeadas})
                                                if len(datas_fmt) > 3:
                                                    datas_mostradas = f"{', '.join(datas_fmt[:3])}... +{len(datas_fmt)-3}"
                                                else:
                                                    datas_mostradas = ', '.join(datas_fmt)
                                                # prefixar eventual seta de quantidade
                                                status_alteracao = f"🆕 (Movido de: {datas_mostradas}) " + status_alteracao
                                            

                                            # Verificar estoque
                                            tem_estoque = False
                                            estoque_disponivel = 0
                                            quantidade_faltante = 0
                                            
                                            if caixa in mapa_estoque:
                                                estoque_inicial = mapa_estoque.get(caixa, 0)
                                                consumido_ate_agora = estoque_consumido_global.get(caixa, 0)
                                                estoque_disponivel = estoque_inicial - consumido_ate_agora
                                                

                                                if estoque_disponivel >= qtd_total:
                                                    # Há estoque suficiente
                                                    tem_estoque = True
                                                    estoque_consumido_global[caixa] = consumido_ate_agora + qtd_total
                                                    quantidade_faltante = 0
                                                else:
                                                    # Estoque insuficiente, mas vamos consumir o que tem
                                                    tem_estoque = False
                                                    # Consumir o estoque disponível
                                                    quantidade_consumida = max(0, estoque_disponivel)
                                                    estoque_consumido_global[caixa] = consumido_ate_agora + quantidade_consumida
                                                    # Calcular quantidade que faltará
                                                    quantidade_faltante = qtd_total - quantidade_consumida
                                            else:
                                                # Item não existe no estoque
                                                quantidade_faltante = qtd_total
                                            
                                            # Adicionar à lista de itens formatados
                                            estoque_emoji = "✅" if tem_estoque else "⚠️"
                                            
                                            # Mostrar informação de comparativo se disponível
                                            info_comparativo = ""
                                            if status_alteracao and status_alteracao != "🆕 " and qtd_antiga > 0:
                                                info_comparativo = f" (Antes: {qtd_antiga:.0f})"
                                            
                                            # NOVA FUNCIONALIDADE: Obter as descrições dos itens para esta caixa
                                            itens_dessa_caixa = df_dia[df_dia['Caixa'] == caixa]['Item/descrição'].unique()

                                            # Limpar as descrições removendo os códigos dos itens
                                            descricoes_limpas = [limpar_descricao(desc) for desc in itens_dessa_caixa]
                                            descricoes = '; '.join(descricoes_limpas)

                                            # Para itens com estoque suficiente
                                            if tem_estoque:
                                                itens_dia.append(f"{estoque_emoji} {status_alteracao}**{caixa}** | Qtd: {qtd_total:.0f}{info_comparativo} | Estoque: {max(0, estoque_disponivel):.0f} | *{descricoes}*")
                                            else:
                                                # Mostrar quanto falta quando não há estoque suficiente
                                                itens_dia.append(f"{estoque_emoji} {status_alteracao}**{caixa}** | Qtd: {qtd_total:.0f}{info_comparativo} | Estoque: {max(0, estoque_disponivel):.0f} | Faltam: {quantidade_faltante:.0f} | *{descricoes}*")
                                        
                                        # Depois adicionar itens removidos (mensagens já formatadas)
                                        for msg in removidos_msgs:
                                            itens_dia.append(msg)
                                        
                                        # Mostrar lista de itens
                                        if itens_dia:
                                            # Filtrar itens com base nos checkboxes selecionados
                                            itens_dia_filtrados = []
                                            for item in itens_dia:
                                                # Verificar se o item atende aos critérios de filtro
                                                mostrar_item = True
                                                
                                                # Filtrar por status de estoque
                                                if "✅" in item and not mostrar_com_estoque:
                                                    mostrar_item = False
                                                elif "⚠️" in item and not mostrar_sem_estoque:
                                                    mostrar_item = False
                                                

                                                # Filtrar por status de alteração
                                                if "❌" in item and not mostrar_removidos:
                                                    mostrar_item = False
                                                elif ("🆕" in item or "⬆️" in item or "⬇️" in item) and not mostrar_novos:
                                                    mostrar_item = False
                                                

                                                # Adicionar à lista filtrada se atender aos critérios
                                                if mostrar_item:
                                                    itens_dia_filtrados.append(item)

                                            # Mostrar lista de itens filtrados
                                            if itens_dia_filtrados:
                                                for item in itens_dia_filtrados:
                                                    st.markdown(item)
                                            else:
                                                if len(itens_dia) > 0:
                                                    st.info("Nenhum item corresponde aos filtros selecionados.")
                                                else:
                                                    st.info("Sem itens")
                                        else:
                                            st.info("Sem itens")
                                
                                # Adicionar legenda dos símbolos após os dias
                                st.markdown("---")
                                st.markdown("**Legenda:**")
                                col1, col2, col3, col4, col5 = st.columns(5)
                                with col1:
                                    st.markdown("✅ - Estoque suficiente")
                                with col2:
                                    st.markdown("⚠️ - Estoque insuficiente")
                                with col3:
                                    st.markdown("🆕 - Item novo")
                                with col4:
                                    st.markdown("⬆️/⬇️ - Alteração de quantidade")
                                with col5:
                                    st.markdown("❌ - Item removido")
                                    
                            else:
                                st.info("Sem dados para esta semana")
                        except Exception as e:
                            st.error(f"Erro ao processar semana {semana_str}: {str(e)}")
else:
    st.info("📂 Faça o upload do arquivo Excel principal para visualizar o cronograma.")

# =========================
# Adicionar comparativo com programa antigo (após visualização principal)
# =========================

if uploaded_file and not df_expandidos.empty and uploaded_old_file and df_antigo is not None:
    st.divider()
    st.subheader("🔄 Comparação com Programa Anterior")
    
    # Mostrar programa antigo em expansor
    with st.expander("📋 Programa Anterior (limpo)"):
        st.dataframe(df_antigo, use_container_width=True)
        st.download_button("⬇️ Baixar Programa Anterior (CSV)", 
                          gerar_csv(df_antigo), 
                          "programa_anterior.csv", 
                          mime="text/csv")

    # Criar campos para comparação
    df_novo['Ordem-split'] = df_novo['Ordem / oper / split / Descrição'].astype(str).str.strip()
    df_antigo['Ordem-split'] = df_antigo['Ordem / oper / split / Descrição'].astype(str).str.strip()

    # Agrupar por ordem-split (primeira ocorrência)
    df_novo_first = df_novo.groupby('Ordem-split', as_index=False).first()
    df_antigo_first = df_antigo.groupby('Ordem-split', as_index=False).first()

    # Criar três colunas para mostrar os comparativos
    col1, col2 = st.columns(2)
    
    # Coluna 1: Itens Novos
    with col1:
        st.markdown("### 🆕 Itens Novos")
        novos = df_novo_first[~df_novo_first['Ordem-split'].isin(df_antigo_first['Ordem-split'])]
        if not novos.empty:
            # Criar cópia para formatação
            novos_display = novos.copy()
            # Formatar a quantidade como inteiro
            novos_display['Quantidade'] = novos_display['Quantidade'].fillna(0).astype(int)
            
            st.dataframe(novos_display[['Ordem-split', 'Item/descrição', 'Inicio', 'Caixa', 'Quantidade']], 
                        use_container_width=True)
            st.download_button("⬇️ Baixar Itens Novos", 
                              gerar_csv(novos), 
                              "itens_novos.csv", 
                              mime="text/csv")
            st.info(f"Total de itens novos: {len(novos)}")
        else:
            st.info("Nenhum item novo detectado.")

    # Coluna 2: Itens Removidos
    with col2:
        st.markdown("### 🗑️ Itens Removidos")
        removidos = df_antigo_first[~df_antigo_first['Ordem-split'].isin(df_novo_first['Ordem-split'])]
        if not removidos.empty:
            # Criar cópia para formatação
            removidos_display = removidos.copy()
            # Formatar a quantidade como inteiro
            removidos_display['Quantidade'] = removidos_display['Quantidade'].fillna(0).astype(int)
            
            st.dataframe(removidos_display[['Ordem-split', 'Item/descrição', 'Inicio', 'Caixa', 'Quantidade']],
                        use_container_width=True)
            st.download_button("⬇️ Baixar Itens Removidos", 
                              gerar_csv(removidos), 
                              "itens_removidos.csv", 
                              mime="text/csv")
            st.info(f"Total de itens removidos: {len(removidos)}")
        else:
            st.info("Nenhum item foi removido.")

    # Itens com mudanças de data
    st.markdown("### ⏱️ Itens com Alterações de Data")
    
    # Juntar tabelas para comparar datas
    df_merge = pd.merge(
        df_novo_first[['Ordem-split', 'Item/descrição', 'Inicio', 'Termino', 'Quantidade']],
        df_antigo_first[['Ordem-split', 'Inicio', 'Termino', 'Quantidade']],
        on='Ordem-split',
        suffixes=('_novo', '_antigo')
    )
    
    # Filtrar apenas os que tiveram mudança de data
    alterados_data = df_merge[
        (df_merge['Inicio_novo'] != df_merge['Inicio_antigo']) | 
        (df_merge['Termino_novo'] != df_merge['Termino_antigo'])
    ]
    
    # Criar tabela de comparação
    if not alterados_data.empty:
        # Formatar para visualização
        df_alterados = alterados_data.copy()
        
        # Calcular diferenças em horas
        df_alterados['Dif_Inicio_Horas'] = (df_alterados['Inicio_novo'] - df_alterados['Inicio_antigo']).dt.total_seconds() / 3600
        
        # Converter diferença de horas para formato HH:MM
        def horas_para_hhmm(horas):
            # Preservar o sinal
            sinal = '-' if horas < 0 else ''
            horas_abs = abs(horas)
            horas_int = int(horas_abs)
            minutos = int((horas_abs - horas_int) * 60)
            return f"{sinal}{horas_int:02d}:{minutos:02d}"
        
        # Criar coluna formatada para exibição
        df_alterados['Diferença'] = df_alterados['Dif_Inicio_Horas'].apply(horas_para_hhmm)
        
        # ADICIONAR EXPLICITAMENTE a classificação das alterações
        df_alterados['Status'] = df_alterados.apply(
            lambda x: "Antecipado" if x['Dif_Inicio_Horas'] < -12 else 
                    ("Adiado" if x['Dif_Inicio_Horas'] > 12 else "Alteração Menor"),
            axis=1
        )
        
        # Formatar datas para visualização
        for col in ['Inicio_novo', 'Inicio_antigo']:
            df_alterados[col] = df_alterados[col].dt.strftime('%d/%m/%Y %H:%M')
        
        # Renomear colunas para nomes mais claros
        colunas_renomeadas = {
            'Ordem-split': 'Ordem',
            'Item/descrição': 'Descrição',
            'Inicio_antigo': 'Data Anterior',
            'Inicio_novo': 'Data Atual',
            'Diferença': 'Diferença (HH:MM)',
            'Status': 'Status'
        }
        
        # Criar abas para visualizar por tipo de alteração
        status_tabs = st.tabs(["Todas Alterações", "Antecipados", "Adiados"])
        
        with status_tabs[0]:
            st.dataframe(
                df_alterados[['Ordem-split', 'Item/descrição', 'Inicio_antigo', 'Inicio_novo', 
                             'Diferença', 'Status']].rename(columns=colunas_renomeadas),
                use_container_width=True
            )
            st.download_button("⬇️ Baixar Todas Alterações", 
                              gerar_csv(df_alterados), 
                              "todas_alteracoes.csv", 
                              mime="text/csv")
            st.info(f"Total de itens com alterações de data: {len(df_alterados)}")
        
        with status_tabs[1]:
            # Filtrar após garantir que a coluna existe
            antecipados = df_alterados[df_alterados['Status'] == 'Antecipado']
            if not antecipados.empty:
                st.dataframe(
                    antecipados[['Ordem-split', 'Item/descrição', 'Inicio_antigo', 'Inicio_novo', 
                                'Diferença']].rename(columns=colunas_renomeadas),
                    use_container_width=True
                )
                st.info(f"Itens antecipados: {len(antecipados)}")
            else:
                st.info("Nenhum item antecipado.")
        
        with status_tabs[2]:
            # Usar a coluna Status para filtrar
            adiados = df_alterados[df_alterados['Status'] == "Adiado"]
            if not adiados.empty:
                st.dataframe(
                    adiados[['Ordem-split', 'Item/descrição', 'Inicio_antigo', 'Inicio_novo', 
                            'Diferença']].rename(columns=colunas_renomeadas),
                    use_container_width=True
                )
                st.info(f"Itens adiados: {len(adiados)}")
            else:
                st.info("Nenhum item adiado.")

       # =========================
    # NOVA SEÇÃO: Relatórios e Análises Básicas
    # =========================

if uploaded_file and not df_expandidos.empty:
    st.divider()
    st.subheader("📊 Análise de Alterações por Fornecedor, Dia e Semana")

    # Calcular percentuais de alteração por fornecedor
    if df_antigo_expandidos is not None:
        df_expandidos['Fornecedor'] = df_expandidos['Fornecedor'].fillna('Desconhecido')
        df_antigo_expandidos['Fornecedor'] = df_antigo_expandidos['Fornecedor'].fillna('Desconhecido')

        # Agrupar por fornecedor no programa atual
        atual_por_fornecedor = df_expandidos.groupby('Fornecedor')['Quantidade'].sum().reset_index()
        atual_por_fornecedor.rename(columns={'Quantidade': 'Quantidade Atual'}, inplace=True)

        # Agrupar por fornecedor no programa antigo
        antigo_por_fornecedor = df_antigo_expandidos.groupby('Fornecedor')['Quantidade'].sum().reset_index()
        antigo_por_fornecedor.rename(columns={'Quantidade': 'Quantidade Anterior'}, inplace=True)

        # Combinar os dois dataframes
        comparativo_fornecedor = pd.merge(atual_por_fornecedor, antigo_por_fornecedor, on='Fornecedor', how='outer').fillna(0)
        comparativo_fornecedor['Variação Absoluta'] = comparativo_fornecedor['Quantidade Atual'] - comparativo_fornecedor['Quantidade Anterior']
        comparativo_fornecedor['Variação (%)'] = (comparativo_fornecedor['Variação Absoluta'] / comparativo_fornecedor['Quantidade Anterior'].replace(0, 1)) * 100
        
        # Formatação de valores numéricos
        comparativo_fornecedor['Quantidade Atual'] = comparativo_fornecedor['Quantidade Atual'].map('{:.0f}'.format)
        comparativo_fornecedor['Quantidade Anterior'] = comparativo_fornecedor['Quantidade Anterior'].map('{:.0f}'.format)
        comparativo_fornecedor['Variação Absoluta'] = comparativo_fornecedor['Variação Absoluta'].map('{:.0f}'.format)
        comparativo_fornecedor['Variação (%)'] = comparativo_fornecedor['Variação (%)'].map('{:.2f}%'.format)

        # Mostrar tabela de comparativo por fornecedor
        st.markdown("### 📦 Alterações por Fornecedor")
        st.dataframe(comparativo_fornecedor, use_container_width=True)

    # Calcular alterações por dia
    st.markdown("### 📅 Alterações por Dia")
    alteracoes_por_dia = df_expandidos.groupby('Dia Entrega')['Quantidade'].sum().reset_index()
    alteracoes_por_dia.rename(columns={'Quantidade': 'Quantidade Atual'}, inplace=True)

    if df_antigo_expandidos is not None:
        antigo_por_dia = df_antigo_expandidos.groupby('Dia Entrega')['Quantidade'].sum().reset_index()
        antigo_por_dia.rename(columns={'Quantidade': 'Quantidade Anterior'}, inplace=True)

        alteracoes_por_dia = pd.merge(alteracoes_por_dia, antigo_por_dia, on='Dia Entrega', how='outer').fillna(0)
        alteracoes_por_dia['Variação Absoluta'] = alteracoes_por_dia['Quantidade Atual'] - alteracoes_por_dia['Quantidade Anterior']
        alteracoes_por_dia['Variação (%)'] = (alteracoes_por_dia['Variação Absoluta'] / alteracoes_por_dia['Quantidade Anterior'].replace(0, 1)) * 100
        
        # Formatação de valores numéricos
        alteracoes_por_dia['Quantidade Atual'] = alteracoes_por_dia['Quantidade Atual'].map('{:.0f}'.format)
        alteracoes_por_dia['Quantidade Anterior'] = alteracoes_por_dia['Quantidade Anterior'].map('{:.0f}'.format)
        alteracoes_por_dia['Variação Absoluta'] = alteracoes_por_dia['Variação Absoluta'].map('{:.0f}'.format)
        alteracoes_por_dia['Variação (%)'] = alteracoes_por_dia['Variação (%)'].map('{:.2f}%'.format)
    else:
        # Se não houver dados anteriores, formatar apenas quantidade atual
        alteracoes_por_dia['Quantidade Atual'] = alteracoes_por_dia['Quantidade Atual'].map('{:.0f}'.format)
    st.dataframe(alteracoes_por_dia, use_container_width=True)

    # Calcular alterações por semana
    st.markdown("### 📅 Alterações por Semana")
    df_expandidos['Semana'] = df_expandidos['Dia Entrega'].dt.isocalendar().week
    alteracoes_por_semana = df_expandidos.groupby('Semana')['Quantidade'].sum().reset_index()
    alteracoes_por_semana.rename(columns={'Quantidade': 'Quantidade Atual'}, inplace=True)

    if df_antigo_expandidos is not None:
        df_antigo_expandidos['Semana'] = df_antigo_expandidos['Dia Entrega'].dt.isocalendar().week
        antigo_por_semana = df_antigo_expandidos.groupby('Semana')['Quantidade'].sum().reset_index()
        antigo_por_semana.rename(columns={'Quantidade': 'Quantidade Anterior'}, inplace=True)

        alteracoes_por_semana = pd.merge(alteracoes_por_semana, antigo_por_semana, on='Semana', how='outer').fillna(0)
        alteracoes_por_semana['Variação Absoluta'] = alteracoes_por_semana['Quantidade Atual'] - alteracoes_por_semana['Quantidade Anterior']
        alteracoes_por_semana['Variação (%)'] = (alteracoes_por_semana['Variação Absoluta'] / alteracoes_por_semana['Quantidade Anterior'].replace(0, 1)) * 100
        
        # Formatação de valores numéricos
        alteracoes_por_semana['Quantidade Atual'] = alteracoes_por_semana['Quantidade Atual'].map('{:.0f}'.format)
        alteracoes_por_semana['Quantidade Anterior'] = alteracoes_por_semana['Quantidade Anterior'].map('{:.0f}'.format)
        alteracoes_por_semana['Variação Absoluta'] = alteracoes_por_semana['Variação Absoluta'].map('{:.0f}'.format)
        alteracoes_por_semana['Variação (%)'] = alteracoes_por_semana['Variação (%)'].map('{:.2f}%'.format)
    else:
        # Se não houver dados anteriores, formatar apenas quantidade atual
        alteracoes_por_semana['Quantidade Atual'] = alteracoes_por_semana['Quantidade Atual'].map('{:.0f}'.format)
    st.dataframe(alteracoes_por_semana, use_container_width=True)

    # Gráficos de alterações
    st.markdown("### 📊 Gráficos de Alterações")
    
    # Para os gráficos, precisamos converter de volta para numérico, pois formatamos como strings
    # Crie cópias para os gráficos com valores numéricos
    alteracoes_por_dia_chart = alteracoes_por_dia.copy()
    alteracoes_por_semana_chart = alteracoes_por_semana.copy()
    
    # Converter strings para float para as colunas de quantidade
    for df in [alteracoes_por_dia_chart, alteracoes_por_semana_chart]:
        for col in ['Quantidade Atual', 'Quantidade Anterior']:
            if col in df.columns:
                try:
                    df[col] = pd.to_numeric(df[col].str.replace(',', '.'), errors='coerce')
                except:
                    # Se já for numérico ou ocorrer algum erro, continue
                    pass
    
    # Verificar se as colunas existem antes de tentar plotar
    colunas_dia = [col for col in ['Quantidade Atual', 'Quantidade Anterior'] if col in alteracoes_por_dia_chart.columns]
    if colunas_dia:
        st.line_chart(alteracoes_por_dia_chart.set_index('Dia Entrega')[colunas_dia])
    
    colunas_semana = [col for col in ['Quantidade Atual', 'Quantidade Anterior'] if col in alteracoes_por_semana_chart.columns]
    if colunas_semana:
        st.bar_chart(alteracoes_por_semana_chart.set_index('Semana')[colunas_semana])
        
    # =========================
    # Análise de Acuracidade de Entregas
    # =========================
    if dados_acuracidade is not None and not df_expandidos.empty and data_programa is not None:
        st.divider()
        st.subheader("🎯 Análise de Acuracidade de Entregas")
        st.markdown(f"Verificação do que foi recebido na data **{data_programa.strftime('%d/%m/%Y')}** e se estava programado no cronograma.")
        
        try:
            # Preparar os dados do programa para cruzamento
            df_programa_para_cruzar = df_expandidos.copy()
            df_programa_para_cruzar['DATA_PROGRAMA'] = df_programa_para_cruzar['Dia Entrega'].dt.strftime('%Y-%m-%d')
            df_programa_para_cruzar['SKU'] = df_programa_para_cruzar['Caixa'].astype(str).str.strip()
            
            # Preparar os dados do estoque (recebimentos)
            data_programa_str = data_programa.strftime('%Y-%m-%d')
            st.info(f"🔍 Analisando recebimentos na data: {data_programa.strftime('%d/%m/%Y')}")
            
            # Filtrar o estoque para incluir apenas os itens recebidos na data do programa
            df_acuracidade = dados_acuracidade[dados_acuracidade['DATA_STR'] == data_programa_str].copy()
            df_acuracidade = df_acuracidade[df_acuracidade['RECEBIDO'] > 0].copy()  # Apenas itens efetivamente recebidos
            
            if df_acuracidade.empty:
                st.warning(f"⚠️ Não foram encontrados recebimentos para a data {data_programa.strftime('%d/%m/%Y')} no estoque.")
                st.stop() # Interrompe a execução da seção
            
            if not df_acuracidade.empty:
                st.info("🔍 Analisando os recebimentos e verificando se estavam programados...")
                
                # Criar um DataFrame para análise de acuracidade cruzando os dados
                acuracidade_cruzada = []
                
                # Agrupar estoque por SKU para obter quantidades recebidas
                recebimentos_agrupados = df_acuracidade.groupby('SKU').agg({
                    'RECEBIDO': 'sum',
                    'ENTREGA_PROG': 'sum',
                    'FORNECEDOR': 'first'
                }).reset_index()
                
                # Para cada item recebido no estoque, buscar se estava programado
                for _, row in recebimentos_agrupados.iterrows():
                    sku = row['SKU']
                    quantidade_recebida = row['RECEBIDO']
                    quantidade_estoque_prog = row['ENTREGA_PROG']
                    fornecedor_estoque = row['FORNECEDOR']
                    
                    # Buscar no programa se havia programação para este SKU
                    registros_programa = df_programa_para_cruzar[
                        (df_programa_para_cruzar['SKU'] == sku) & 
                        (df_programa_para_cruzar['DATA_PROGRAMA'] == data_programa_str)
                    ]
                    
                    if not registros_programa.empty:
                        # Encontrou programação para este SKU e data
                        quantidade_programada = registros_programa['Quantidade'].sum()
                        fornecedor = registros_programa['Fornecedor'].iloc[0]  # Usar o fornecedor do programa
                    else:
                        # Não encontrou programação para este SKU e data
                        quantidade_programada = 0
                        fornecedor = fornecedor_estoque  # Usar o fornecedor do estoque
                    
                    # Calcular acuracidade - agora baseada no recebimento vs programado
                    diferenca = quantidade_recebida - quantidade_programada
                    
                    # Verificar estoque disponível desta caixa
                    estoque_disponivel = mapa_estoque.get(sku, 0)
                    
                    # Se havia programação, calcular acuracidade entre recebido e programado
                    if quantidade_programada > 0:
                        acuracidade = ((quantidade_recebida / quantidade_programada) * 100)
                        acuracidade = min(100, acuracidade) if acuracidade > 0 else acuracidade
                        status = "✓ Programado e Recebido"
                    else:
                        # Se não havia programação mas foi recebido, acuracidade é 0%
                        acuracidade = 0
                        status = "❌ Recebido sem Programação"
                    
                    # Calcular o estoque disponível real antes do recebimento
                    # Subtrair o que foi recebido para ter o valor real do estoque antes da entrega
                    estoque_antes_recebimento = estoque_disponivel - quantidade_recebida
                    
                    # Calcular necessidade para itens recebidos
                    if quantidade_programada > 0:
                        # Este item estava programado e foi recebido
                        if estoque_antes_recebimento >= quantidade_programada:
                            # Se já havia estoque suficiente mesmo antes do recebimento
                            # A programação não era necessária
                            necessidade = 0
                        else:
                            # Calcular o quanto da programação era realmente necessário
                            # Baseado no estoque disponível ANTES do recebimento
                            necessidade = 100 - ((estoque_antes_recebimento / quantidade_programada) * 100)
                            necessidade = max(0, necessidade)  # Garantir que não seja negativo
                    else:
                        # Se não estava programado mas foi recebido
                        necessidade = 0  # Recebido sem programação não era necessário programar
                    
                    # Adicionar ao resultado - converter valores para inteiros
                    acuracidade_cruzada.append({
                        'Data': data_programa.strftime('%d/%m/%Y'),
                        'SKU': sku,
                        'Fornecedor': fornecedor,
                        'Qtd Programada': int(quantidade_programada),
                        'Qtd Estoque Prog': int(quantidade_estoque_prog),
                        'Qtd Recebida': int(quantidade_recebida),
                        'Estoque Antes Recebimento': int(estoque_antes_recebimento),  # Estoque antes do recebimento
                        'Estoque Total': int(estoque_disponivel),  # Estoque total (inclui recebimento)
                        'Diferença': int(diferenca),
                        'Acuracidade (%)': acuracidade,
                        'Necessidade (%)': necessidade,  # Nova métrica
                        'Status': status
                    })
                
                # Agora incluir os itens que estavam programados mas não foram recebidos
                # Primeiro agrupar por SKU para somar as quantidades programadas
                programados_nao_recebidos = df_programa_para_cruzar[
                    (df_programa_para_cruzar['DATA_PROGRAMA'] == data_programa_str) & 
                    (~df_programa_para_cruzar['SKU'].isin(recebimentos_agrupados['SKU'].values))
                ].groupby(['SKU', 'Fornecedor'], as_index=False)['Quantidade'].sum()
                
                # Processar cada SKU agrupado
                for _, row in programados_nao_recebidos.iterrows():
                    sku = row['SKU']
                    quantidade_programada = row['Quantidade']
                    fornecedor = row['Fornecedor']
                    
                    # Verificar se existe este item no estoque (independente da data)
                    estoque_disponivel = 0
                    
                    # Verificar no mapa de estoque se a caixa existe
                    if sku in mapa_estoque:
                        estoque_disponivel = mapa_estoque.get(sku, 0)
                        
                        # Calcular acuracidade e diferença considerando o estoque
                        acuracidade = 0
                        if estoque_disponivel >= quantidade_programada:
                            # Se temos estoque suficiente, acuracidade é 100%
                            acuracidade = 100
                            diferenca = 0  # Não há diferença, pois o estoque cobre a programação
                            status = "🔵 Programado não Recebido (Estoque Suficiente)"
                        elif estoque_disponivel > 0:
                            # Se temos estoque parcial, calcular acuracidade proporcional
                            acuracidade = (estoque_disponivel / quantidade_programada) * 100
                            diferenca = int(estoque_disponivel - quantidade_programada)
                            status = "🟡 Programado não Recebido (Estoque Parcial)"
                        else:
                            # Sem estoque disponível
                            acuracidade = 0
                            diferenca = int(-quantidade_programada)
                            status = "🔴 Programado não Recebido (Sem Estoque)"
                    else:
                        # Item não cadastrado no estoque
                        acuracidade = 0
                        diferenca = int(-quantidade_programada)
                        status = "⚪ Programado não Recebido (Não Cadastrado)"
                        
                    # Calcular necessidade para itens programados e não recebidos
                    # Para todos os itens programados e não recebidos, agora consideramos necessidade como 100%,
                    # independentemente do estoque disponível
                    if status == "🔵 Programado não Recebido (Estoque Suficiente)":
                        # Mesmo com estoque suficiente, a programação era necessária (conforme solicitado)
                        necessidade = 100
                    else:
                        # Para os demais casos de programado e não recebido, também é 100%
                        necessidade = 100
                    
                    # Este item estava programado mas não foi recebido
                    estoque_disponivel_valor = 0 if estoque_disponivel is None else estoque_disponivel
                    acuracidade_cruzada.append({
                        'Data': data_programa.strftime('%d/%m/%Y'),
                        'SKU': sku,
                        'Fornecedor': fornecedor,
                        'Qtd Programada': int(quantidade_programada),  # Convertido para inteiro
                        'Qtd Estoque Prog': 0,  # Não recebido nesta data
                        'Qtd Recebida': 0,      # Não recebido nesta data
                        'Estoque Antes Recebimento': int(estoque_disponivel_valor),  # Para itens não recebidos, é igual ao estoque total
                        'Estoque Total': int(estoque_disponivel_valor),  # Estoque total (novo nome)
                        'Diferença': int(diferenca) if diferenca is not None else 0,  # Garantir que não seja None
                        'Acuracidade (%)': acuracidade,  # Pode ser 100% se estoque suficiente
                        'Necessidade (%)': necessidade,  # Nova métrica
                        'Status': status
                    })
                
                    # Converter lista para DataFrame
                df_acuracidade_cruzada = pd.DataFrame(acuracidade_cruzada)
                
                if not df_acuracidade_cruzada.empty:
                    # Adicionar coluna de relação estoque/programado
                    df_acuracidade_cruzada['Relação Estoque/Programado'] = df_acuracidade_cruzada.apply(
                        lambda row: (row['Estoque Total'] / row['Qtd Programada']) if row['Qtd Programada'] > 0 else float('inf'),
                        axis=1
                    )
                    
                    # Formatar a nova coluna
                    df_acuracidade_cruzada['Relação Estoque/Programado'] = df_acuracidade_cruzada['Relação Estoque/Programado'].apply(
                        lambda x: '∞' if x == float('inf') else '{:.2f}'.format(x)
                    )
                    
                    # Formatar as colunas de acuracidade e necessidade
                    # Garantir que mostre 100.00% quando for exatamente 100
                    df_acuracidade_cruzada['Acuracidade (%)'] = df_acuracidade_cruzada['Acuracidade (%)'].apply(
                        lambda x: '100.00%' if x == 100 else '{:.2f}%'.format(x)
                    )
                    
                    # Formatar a coluna de necessidade
                    df_acuracidade_cruzada['Necessidade (%)'] = df_acuracidade_cruzada['Necessidade (%)'].apply(
                        lambda x: '0.00%' if x == 0 else '{:.2f}%'.format(x)
                    )                    # Estatísticas gerais
                    total_programado = df_acuracidade_cruzada['Qtd Programada'].sum()
                    total_recebido = df_acuracidade_cruzada['Qtd Recebida'].sum()
                    
                    # Contagens por status
                    status_counts = df_acuracidade_cruzada['Status'].value_counts()
                    prog_recebido = status_counts.get("✓ Programado e Recebido", 0)
                    sem_prog = status_counts.get("❌ Recebido sem Programação", 0) 
                    
                    # Somar todos os tipos de "Programado não Recebido"
                    prog_nao_recebido_estoque_suf = status_counts.get("🔵 Programado não Recebido (Estoque Suficiente)", 0)
                    prog_nao_recebido_estoque_parcial = status_counts.get("🟡 Programado não Recebido (Estoque Parcial)", 0)
                    prog_nao_recebido_sem_estoque = status_counts.get("🔴 Programado não Recebido (Sem Estoque)", 0)
                    prog_nao_recebido_nao_cadastrado = status_counts.get("⚪ Programado não Recebido (Não Cadastrado)", 0)
                    
                    # Total de itens não recebidos
                    prog_nao_recebido = prog_nao_recebido_estoque_suf + prog_nao_recebido_estoque_parcial + prog_nao_recebido_sem_estoque + prog_nao_recebido_nao_cadastrado
                    
                    # Total de itens com acuracidade efetiva de 100%
                    itens_100_pct = prog_recebido + prog_nao_recebido_estoque_suf
                    
                    # Calcular acuracidade de programação
                    itens_recebidos_total = prog_recebido + sem_prog
                    taxa_programacao = (prog_recebido / itens_recebidos_total * 100) if itens_recebidos_total > 0 else 0
                    
                    # Calcular acuracidade considerando itens com estoque suficiente como "atendidos"
                    total_itens_programados = prog_recebido + prog_nao_recebido
                    itens_atendidos = prog_recebido + prog_nao_recebido_estoque_suf
                    taxa_atendimento = (itens_atendidos / total_itens_programados * 100) if total_itens_programados > 0 else 0
                    
                    # Calcular métrica de necessidade média
                    necessidade_media = df_acuracidade_cruzada['Necessidade (%)'].apply(
                        lambda x: float(x.replace('%', '')) if isinstance(x, str) else float(x)
                    ).mean()
                    
                    # Calcular aceitação da programação
                    # Consideramos aceitáveis as programações com necessidade > 50%
                    programacoes_necessarias = df_acuracidade_cruzada[
                        df_acuracidade_cruzada['Necessidade (%)'].apply(
                            lambda x: float(x.replace('%', '')) if isinstance(x, str) else float(x)
                        ) > 50
                    ]
                    taxa_aceitacao = (len(programacoes_necessarias) / len(df_acuracidade_cruzada) * 100) if len(df_acuracidade_cruzada) > 0 else 0
                    
                    # Calcular acuracidade de quantidade para todos os itens com acuracidade 100%
                    df_atendidos = df_acuracidade_cruzada[
                        (df_acuracidade_cruzada['Status'] == "✓ Programado e Recebido") |
                        (df_acuracidade_cruzada['Status'] == "🔵 Programado não Recebido (Estoque Suficiente)")
                    ]
                    
                    if not df_atendidos.empty:
                        prog_qtd = df_atendidos['Qtd Programada'].sum()
                        # Para itens recebidos, usar a qtd recebida + para itens com estoque suficiente, usar estoque total
                        qtd_atendida = df_atendidos.apply(
                            lambda x: x['Qtd Recebida'] if x['Status'] == "✓ Programado e Recebido" else x['Estoque Total'], 
                            axis=1
                        ).sum()
                        acuracidade_qtd = (qtd_atendida / prog_qtd * 100) if prog_qtd > 0 else 0
                    else:
                        acuracidade_qtd = 0
                    
                    # Mostrar métricas gerais
                    col1, col2 = st.columns(2)
                    col1.metric("Taxa de Programação", f"{taxa_programacao:.2f}%", 
                               help=f"Porcentagem de itens recebidos que estavam programados: {prog_recebido} de {itens_recebidos_total}")
                    col2.metric("Acuracidade com Estoque", f"{taxa_atendimento:.2f}%",
                               help=f"Considerando itens com estoque suficiente como atendidos: {itens_atendidos} de {total_itens_programados}")
                    
                    # Métricas relacionadas à necessidade de programação
                    col1, col2 = st.columns(2)
                    col1.metric("Necessidade Média", f"{necessidade_media:.2f}%",
                               help="Média da necessidade de programação. 0% significa que não era necessário (estoque suficiente), 100% significa que era totalmente necessário (sem estoque)")
                    col2.metric("Taxa de Aceitação da Programação", f"{taxa_aceitacao:.2f}%",
                               help="Porcentagem de itens cuja programação era realmente necessária (necessidade > 50%)")
                    
                    # Métricas de cobertura
                    col1, col2 = st.columns(2)
                    col1.metric("Itens sem Cobertura", f"{prog_nao_recebido_sem_estoque + prog_nao_recebido_nao_cadastrado}",
                               help="Quantidade de SKUs programados que não foram recebidos e não têm estoque suficiente")
                    col2.metric("Itens Desnecessários", f"{len(df_acuracidade_cruzada[df_acuracidade_cruzada['Necessidade (%)'] == '0.00%'])}",
                               help="Quantidade de itens com estoque suficiente (não era necessário programar)")
                    
                    # Exibir tabela cruzada
                    st.markdown("### 📊 Análise de Acuracidade de Entrega")
                    st.info("""
                    Esta análise identifica o que foi recebido e verifica se estava programado, destacando também os itens programados que não foram recebidos. 
                    
                    **Métricas importantes**:
                    - **Acuracidade**: Quando há estoque suficiente para cobrir a programação, a acuracidade é considerada 100%
                    - **Necessidade**: Avalia se a programação era realmente necessária, considerando o estoque disponível:
                      * 0% = Não necessário (estoque suficiente disponível)
                      * 100% = Totalmente necessário (sem estoque disponível)
                    - **Taxa de Aceitação**: Porcentagem de itens cuja programação era realmente necessária (necessidade > 50%)
                    """)
                    
                    st.warning("""
                    ⚠️ **Nota sobre estoque**: A coluna 'Estoque Total' mostra o estoque total disponível, que já inclui a quantidade recebida.
                    A coluna 'Estoque Antes Recebimento' mostra o estoque antes da entrega ser computada.
                    Quando o estoque antes do recebimento é maior ou igual à quantidade programada, isso indica que a programação pode não ter sido necessária.
                    """)
                    
                    # Adicionar legenda de status
                    st.markdown("""
                    **Legenda:**
                    - ✓ Programado e Recebido: Item estava programado e foi recebido
                    - ❌ Recebido sem Programação: Item foi recebido mas não estava programado
                    - 🔵 Programado não Recebido (Estoque Suficiente): Item não recebido formalmente, mas estoque disponível cobre 100% da programação
                    - 🟡 Programado não Recebido (Estoque Parcial): Item não recebido formalmente, estoque disponível cobre parcialmente a programação
                    - 🔴 Programado não Recebido (Sem Estoque): Item programado, não recebido e sem estoque disponível
                    - ⚪ Programado não Recebido (Não Cadastrado): Item programado mas não consta no cadastro de estoque
                    """)
                    
                    # Criar filtros para a tabela
                    status_options = ["Todos", "✓ Programado e Recebido", "❌ Recebido sem Programação", 
                                      "🔵 Programado não Recebido (Estoque Suficiente)", 
                                      "🟡 Programado não Recebido (Estoque Parcial)",
                                      "🔴 Programado não Recebido (Sem Estoque)",
                                      "⚪ Programado não Recebido (Não Cadastrado)"]
                    selected_status = st.selectbox("Filtrar por status:", status_options)
                    
                    # Opção para ver apenas itens programados e não recebidos (independente de estoque)
                    ver_todos_nao_recebidos = st.checkbox("Ver todos os itens programados e não recebidos", value=False)
                    
                    # Opções de filtros adicionais
                    col1, col2 = st.columns(2)
                    with col1:
                        ver_acuracidade_100 = st.checkbox("Ver itens com acuracidade 100% (com estoque suficiente)", value=False)
                    with col2:
                        ver_desnecessarios = st.checkbox("Ver itens desnecessários (necessidade = 0%)", value=False)
                    
                    # Aplicar filtros
                    if ver_desnecessarios:
                        # Mostrar itens com necessidade 0% (programação desnecessária)
                        filtered_df = df_acuracidade_cruzada[
                            df_acuracidade_cruzada['Necessidade (%)'] == '0.00%'
                        ]
                    elif ver_acuracidade_100:
                        # Mostrar todos os itens com acuracidade 100% (recebidos ou com estoque suficiente)
                        filtered_df = df_acuracidade_cruzada[
                            (df_acuracidade_cruzada['Acuracidade (%)'] == '100.00%') | 
                            (df_acuracidade_cruzada['Status'] == "🔵 Programado não Recebido (Estoque Suficiente)")
                        ]
                    elif ver_todos_nao_recebidos:
                        # Mostrar todos os itens não recebidos (todos os 4 status)
                        filtered_df = df_acuracidade_cruzada[
                            df_acuracidade_cruzada['Status'].str.contains("Programado não Recebido")
                        ]
                    elif selected_status != "Todos":
                        # Filtro por status específico
                        filtered_df = df_acuracidade_cruzada[df_acuracidade_cruzada['Status'] == selected_status]
                    else:
                        # Mostrar todos
                        filtered_df = df_acuracidade_cruzada
                    
                    # Exibir a tabela filtrada
                    st.dataframe(filtered_df, use_container_width=True)
                    
                    # Adicionar informação específica para os programados não recebidos
                    if ver_todos_nao_recebidos or "Programado não Recebido" in selected_status:
                        st.info("""
                        Para itens programados e não recebidos:
                        - 🔵 Estoque Suficiente: Acuracidade 100%, o estoque cobre toda a programação
                        - 🟡 Estoque Parcial: Acuracidade parcial, estoque cobre parte da programação
                        - 🔴 Sem Estoque: Acuracidade 0%, não há estoque disponível
                        - ⚪ Não Cadastrado: Item não encontrado no sistema de estoque
                        """)
                    
                    # Análise por fornecedor (agrupada)
                    st.markdown("### 📊 Acuracidade por Fornecedor")
                    # Converter para numérico para agrupamento
                    df_acuracidade_cruzada_num = df_acuracidade_cruzada.copy()
                    df_acuracidade_cruzada_num['Acuracidade (%)'] = pd.to_numeric(df_acuracidade_cruzada_num['Acuracidade (%)'].str.replace('%', ''), errors='coerce')
                    
                    acuracidade_fornecedor = df_acuracidade_cruzada.groupby('Fornecedor').agg({
                        'Qtd Programada': 'sum',
                        'Qtd Recebida': 'sum',
                        'Estoque Total': 'sum'  # Usando Estoque Total em vez de Estoque Disponível
                    }).reset_index()
                    
                    acuracidade_fornecedor['Acuracidade (%)'] = (acuracidade_fornecedor['Qtd Recebida'] / acuracidade_fornecedor['Qtd Programada'] * 100).fillna(0)
                    acuracidade_fornecedor['Acuracidade (%)'] = acuracidade_fornecedor['Acuracidade (%)'].apply(lambda x: min(100, x) if x > 0 else x)
                    acuracidade_fornecedor['Acuracidade (%)'] = acuracidade_fornecedor['Acuracidade (%)'].map('{:.2f}%'.format)
                    
                    # Calcular a cobertura potencial (Estoque + Recebido) / Programado
                    acuracidade_fornecedor['Cobertura Potencial'] = ((acuracidade_fornecedor['Estoque Total'] + acuracidade_fornecedor['Qtd Recebida']) / acuracidade_fornecedor['Qtd Programada'] * 100).fillna(0)
                    acuracidade_fornecedor['Cobertura Potencial'] = acuracidade_fornecedor['Cobertura Potencial'].apply(lambda x: min(100, x) if x > 0 else x)
                    acuracidade_fornecedor['Cobertura Potencial'] = acuracidade_fornecedor['Cobertura Potencial'].map('{:.2f}%'.format)
                    
                    st.dataframe(acuracidade_fornecedor, use_container_width=True)
                    
                    st.info("A coluna 'Cobertura Potencial' mostra a porcentagem de itens que poderiam ser atendidos considerando o estoque total disponível.")
                    
                    # Análise por data (agrupada)
                    st.markdown("### 📊 Acuracidade por Data")
                    acuracidade_data = df_acuracidade_cruzada.groupby('Data').agg({
                        'Qtd Programada': 'sum',
                        'Qtd Recebida': 'sum'
                    }).reset_index()
                    
                    acuracidade_data['Acuracidade (%)'] = (acuracidade_data['Qtd Recebida'] / acuracidade_data['Qtd Programada'] * 100).fillna(0)
                    acuracidade_data['Acuracidade (%)'] = acuracidade_data['Acuracidade (%)'].apply(lambda x: min(100, x) if x > 0 else x)
                    acuracidade_data['Acuracidade (%)'] = acuracidade_data['Acuracidade (%)'].map('{:.2f}%'.format)
                    
                    st.dataframe(acuracidade_data, use_container_width=True)
                    
                    # Gráficos
                    st.markdown("### 📈 Gráficos de Acuracidade")
                    
                    # Distribuição por status
                    st.markdown("#### Distribuição por Status")
                    
                    # Criar categorias mais específicas para o gráfico
                    df_acuracidade_cruzada_grafico = df_acuracidade_cruzada.copy()
                    df_acuracidade_cruzada_grafico['Status Simplificado'] = df_acuracidade_cruzada_grafico['Status'].apply(
                        lambda s: "✅ Recebido ou com Estoque 100%" if s in ["✓ Programado e Recebido", "🔵 Programado não Recebido (Estoque Suficiente)"]
                        else "🟡 Estoque Parcial" if "Estoque Parcial" in s
                        else "❌ Sem Cobertura" if "Sem Estoque" in s or "Não Cadastrado" in s
                        else "⚠️ Recebido sem Programação" if "Recebido sem Programação" in s
                        else s  # Caso padrão
                    )
                    
                    status_counts = df_acuracidade_cruzada_grafico['Status Simplificado'].value_counts().reset_index()
                    status_counts.columns = ['Status', 'Quantidade']
                    
                    # Usar pyplot para gráfico de pizza
                    import matplotlib.pyplot as plt
                    
                    fig, ax = plt.subplots(figsize=(10, 6))
                    ax.pie(status_counts['Quantidade'], labels=status_counts['Status'], autopct='%1.1f%%', 
                          startangle=90, shadow=True, explode=[0.05, 0.05, 0.05])
                    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
                    
                    st.pyplot(fig)
                    
                    # Gráfico por fornecedor
                    st.markdown("#### Por Fornecedor")
                    chart_fornecedor = df_acuracidade_cruzada_num.groupby('Fornecedor').agg({
                        'Qtd Programada': 'sum',
                        'Qtd Recebida': 'sum'
                    })
                    
                    fig2, ax2 = plt.subplots(figsize=(10, 6))
                    chart_fornecedor.plot(kind='bar', ax=ax2)
                    ax2.set_title('Comparação entre Quantidade Programada e Recebida por Fornecedor')
                    ax2.set_ylabel('Quantidade')
                    ax2.set_xlabel('Fornecedor')
                    ax2.legend(['Programado', 'Recebido'])
                    st.pyplot(fig2)
                    
                    # Tabela de status por fornecedor
                    st.markdown("#### Status por Fornecedor")
                    status_fornecedor = pd.crosstab(df_acuracidade_cruzada['Fornecedor'], 
                                                   df_acuracidade_cruzada['Status'])
                    st.dataframe(status_fornecedor, use_container_width=True)
                    
                    # Gráfico de distribuição de necessidade
                    st.markdown("#### Distribuição de Necessidade de Programação")
                    
                    # Converter necessidade de string para float para usar nos gráficos
                    df_necessidade = df_acuracidade_cruzada.copy()
                    df_necessidade['Necessidade (%)'] = df_necessidade['Necessidade (%)'].apply(
                        lambda x: float(x.replace('%', '')) if isinstance(x, str) else float(x)
                    )
                    
                    # Criar categorias de necessidade
                    bins = [0, 25, 50, 75, 100]
                    labels = ['Baixa (0-25%)', 'Média-Baixa (25-50%)', 'Média-Alta (50-75%)', 'Alta (75-100%)']
                    df_necessidade['Categoria Necessidade'] = pd.cut(df_necessidade['Necessidade (%)'], bins=bins, labels=labels)
                    
                    # Contar por categoria
                    necessidade_counts = df_necessidade['Categoria Necessidade'].value_counts().reset_index()
                    necessidade_counts.columns = ['Categoria', 'Quantidade']
                    
                    # Criar gráfico de barras para necessidade
                    fig, ax = plt.subplots(figsize=(10, 6))
                    colors = ['green', 'yellowgreen', 'orange', 'red']
                    bars = ax.bar(necessidade_counts['Categoria'], necessidade_counts['Quantidade'], color=colors)
                    
                    # Adicionar rótulos nas barras
                    for bar in bars:
                        height = bar.get_height()
                        ax.text(bar.get_x() + bar.get_width()/2., height + 0.1,
                                f'{height:.0f}', ha='center', va='bottom')
                    
                    ax.set_title('Distribuição de Necessidade de Programação')
                    ax.set_ylabel('Quantidade de Itens')
                    ax.set_xlabel('Nível de Necessidade')
                    
                    st.pyplot(fig)
                    
                    # Explicação do gráfico
                    st.info("""
                    **Interpretação do gráfico:**
                    - **Baixa (0-25%)**: Itens com grande estoque disponível, programação praticamente desnecessária
                    - **Média-Baixa (25-50%)**: Itens com estoque significativo, programação pouco necessária
                    - **Média-Alta (50-75%)**: Itens com estoque parcial, programação moderadamente necessária
                    - **Alta (75-100%)**: Itens com pouco ou nenhum estoque, programação muito necessária
                    """)
                    
                    # Adicionar coluna de data formatada para exibição nos gráficos
                    if 'DATA_FORMATADA' in df_acuracidade.columns:
                        df_acuracidade['DATA'] = df_acuracidade['DATA_FORMATADA'].dt.strftime('%d/%m/%Y')
                    
                    # Botão para baixar relatório de acuracidade
                    st.markdown("### 📥 Exportar Relatório de Acuracidade")
                    
                    # Adicionar data ao nome do arquivo
                    data_arquivo = data_programa.strftime('%d-%m-%Y')
                    
                    # Botão para baixar o relatório completo
                    csv = gerar_csv(df_acuracidade_cruzada)
                    st.download_button(
                        label="⬇️ Baixar Relatório Completo de Acuracidade",
                        data=csv,
                        file_name=f"acuracidade_relatorio_{data_arquivo}.csv",
                        mime="text/csv"
                    )
                    
                    # Botões específicos para cada status
                    col1, col2, col3 = st.columns(3)
                    
                    with col1:
                        programados = df_acuracidade_cruzada[df_acuracidade_cruzada['Status'] == "✓ Programado e Recebido"]
                        if not programados.empty:
                            csv_prog = gerar_csv(programados)
                            st.download_button(
                                label="⬇️ Itens Programados e Recebidos",
                                data=csv_prog,
                                file_name=f"acuracidade_programados_{data_arquivo}.csv",
                                mime="text/csv"
                            )
                            
                    with col2:
                        sem_programacao = df_acuracidade_cruzada[df_acuracidade_cruzada['Status'] == "❌ Recebido sem Programação"]
                        if not sem_programacao.empty:
                            csv_sem_prog = gerar_csv(sem_programacao)
                            st.download_button(
                                label="⬇️ Recebidos sem Programação",
                                data=csv_sem_prog,
                                file_name=f"acuracidade_sem_programacao_{data_arquivo}.csv",
                                mime="text/csv"
                            )
                            
                    with col3:
                        # Agrupar todos os tipos de "programado não recebido"
                        nao_recebidos = df_acuracidade_cruzada[
                            df_acuracidade_cruzada['Status'].str.contains("Programado não Recebido")
                        ]
                        if not nao_recebidos.empty:
                            csv_nao_rec = gerar_csv(nao_recebidos)
                            st.download_button(
                                label="⬇️ Programados não Recebidos",
                                data=csv_nao_rec,
                                file_name=f"acuracidade_nao_recebidos_{data_arquivo}.csv",
                                mime="text/csv"
                            )
                else:
                    st.warning("⚠️ Não foi possível encontrar correspondência entre os itens do programa e os registros de estoque.")
                    st.info("Verifique se os códigos SKU estão consistentes entre o programa e o arquivo de estoque.")
                
                # Mostrar os dados originais do estoque (opção expandida)
                with st.expander("📋 Ver dados originais do estoque"):
                    # Preparar dados para exibição
                    df_display = df_acuracidade.copy()
                    df_display['ACURACIDADE (%)'] = df_display['ACURACIDADE'].map('{:.2f}%'.format)
                    
                    # Renomear colunas para exibição
                    colunas_exibir = ['SKU', 'FORNECEDOR', 'DATA', 'ENTREGA_PROG', 'RECEBIDO', 'DIFERENCA', 'ACURACIDADE (%)']
                    colunas_disponiveis = [col for col in colunas_exibir if col in df_display.columns]
                    
                    df_display = df_display[colunas_disponiveis].copy()
                    df_display.columns = [col.title().replace('_', ' ') for col in df_display.columns]
                    
                    # Mostrar tabela detalhada
                    st.markdown("### 📋 Dados originais do estoque")
                    st.dataframe(df_display, use_container_width=True)
            else:
                st.info("Não há dados suficientes para análise de acuracidade. Verifique se existem valores nas colunas de programação e recebimento.")
        except Exception as e:
            st.error(f"Erro ao processar dados de acuracidade: {str(e)}")
            st.write("Verifique o formato dos dados nas colunas ENTREGA_PROG e RECEBIDO.")

# O código para formatação das colunas de variação percentual já está na seção principal de análise

