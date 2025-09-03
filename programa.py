import pandas as pd
import streamlit as st
from datetime import timedelta
import re

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
            linhas.append({
                'Ordem / oper / split / Descrição': str(row.get('Ordem / oper / split / Descrição', '')).strip(),
                'Item/descrição': str(row.get('Item/descrição', '')).strip(),
                'Data Produção': dia.strftime('%d/%m/%Y'),
                'Caixa': caixa,
                'Fornecedor': fornecedor,
                'Quantidade': qtd_por_dia,
                'Dia Entrega': dia_entrega
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
            return {}, None, None, None
        
        # Identificar tipo de arquivo e ler adequadamente
        nome_arquivo = uploaded_stock_file.name.lower()
        if nome_arquivo.endswith('.csv'):
            df = pd.read_csv(uploaded_stock_file, sep=None, engine='python')
        else:  # Excel
            df = pd.read_excel(uploaded_stock_file)
        
        # Normalizar nomes das colunas
        df.columns = [str(col).strip().upper() for col in df.columns]
        
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
        
        return mapa_estoque, data_atual_str, variacao, variacao_percentual
    
    except Exception as e:
        st.error(f"Erro ao processar o arquivo de estoque: {str(e)}")
        return {}, None, None, None

# =========================
# Configuração Streamlit
# =========================
st.set_page_config(page_title="Cronograma de Produção", layout="wide")
st.title("📅 Cronograma de Produção - Detalhado por Dia")

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
if 'historico_estoque' not in st.session_state:
    st.session_state.historico_estoque = []
    st.session_state.datas_estoque = []

if uploaded_stock_file:
    # Processar o estoque atual - retorna os valores corretos
    mapa_estoque, data_estoque, variacao_total, variacao_percentual = processar_estoque(uploaded_stock_file)
    
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
                                # Criar colunas lado a lado para cada dia
                                cols = st.columns(min(len(todas_datas), 5))  # Máximo de 5 colunas por linha
                                
                                for idx, data in enumerate(todas_datas):
                                    # Definir em qual coluna este dia será exibido
                                    col_idx = idx % len(cols)
                                    
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
                                    caixas_antigas_geral = {}
                                    if df_forn_antigo is not None and not df_forn_antigo.empty:
                                        df_caixas_antigas_geral = df_forn_antigo.groupby('Caixa')['Quantidade'].sum().reset_index()
                                        caixas_antigas_geral = dict(zip(df_caixas_antigas_geral['Caixa'], df_caixas_antigas_geral['Quantidade']))
                                    
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
                                    
                                    # Encontrar caixas que foram removidas do programa anterior para este dia
                                    caixas_removidas = {}
                                    if df_dia_antigo is not None and not df_dia_antigo.empty:
                                        caixas_atuais = set(df_caixas_agrupadas['Caixa'])
                                        caixas_antigas_set = set(df_caixas_antigas['Caixa'])
                                        caixas_removidas_set = caixas_antigas_set - caixas_atuais
                                        
                                        for caixa in caixas_removidas_set:
                                            qtd = caixas_antigas.get(caixa, 0)
                                            caixas_removidas[caixa] = qtd
                                    
                                    # Exibir bloco no layout
                                    with cols[col_idx]:
                                        # Cabeçalho com data
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
                                            
                                            # Apenas mostrar que não há dados anteriores se houver
                                            # apenas caixas atuais (sem caixas removidas)
                                            if len(caixas_removidas) == 0:
                                                st.write("_Sem dados do programa anterior para esta data_")
                                        
                                        # Aqui é onde criamos a lista de itens com indicadores:
                                        itens_dia = []
                                        
                                        # Primeiro adicionar itens atuais
                                        for _, row in df_caixas_agrupadas.iterrows():
                                            caixa = row['Caixa']
                                            qtd_total = row['Quantidade']
                                            
                                            # CORRIGIR A COMPARAÇÃO
                                            status_alteracao = ""
                                            qtd_antiga = 0
                                            
                                            # IMPORTANTE: Verificar se df_dia_antigo existe e tem dados
                                            if df_dia_antigo is not None and not df_dia_antigo.empty:
                                                # Verificar diretamente no DataFrame original, não só no dicionário
                                                caixa_anterior = df_dia_antigo[df_dia_antigo['Caixa'] == caixa]
                                                
                                                if not caixa_anterior.empty:
                                                    qtd_antiga = caixa_anterior['Quantidade'].sum()
                                                    if qtd_total > qtd_antiga:
                                                        status_alteracao = "⬆️ "  # Aumentou
                                                    elif qtd_total < qtd_antiga:
                                                        status_alteracao = "⬇️ "  # Diminuiu
                                                else:
                                                    status_alteracao = "🆕 "  # Novo item
                                            else:
                                                # Se não há dados do programa anterior para este dia, 
                                                # não marcar como novo (pois não temos como comparar)
                                                status_alteracao = ""
                                            
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
                                            
                                            if tem_estoque:
                                                itens_dia.append(f"{estoque_emoji} {status_alteracao}**{caixa}** | Qtd: {qtd_total:.0f}{info_comparativo} | Estoque: {max(0, estoque_disponivel):.0f}")
                                            else:
                                                # Mostrar quanto falta quando não há estoque suficiente
                                                itens_dia.append(f"{estoque_emoji} {status_alteracao}**{caixa}** | Qtd: {qtd_total:.0f}{info_comparativo} | Estoque: {max(0, estoque_disponivel):.0f} | Faltam: {quantidade_faltante:.0f}")
                                        
                                        # Depois adicionar itens removidos
                                        for caixa, qtd_removida in caixas_removidas.items():
                                            # Verificar estoque para itens removidos
                                            estoque_inicial_removido = mapa_estoque.get(caixa, 0)
                                            consumido_ate_agora_removido = estoque_consumido_global.get(caixa, 0)
                                            estoque_disponivel_removido = estoque_inicial_removido - consumido_ate_agora_removido
                                            estoque_emoji = "✅" if estoque_disponivel_removido > 0 else "⚠️"
                                            
                                            # Adicionar item removido à lista com marcador especial
                                            itens_dia.append(f"{estoque_emoji} ❌ **{caixa}** | Removido (Antes: {qtd_removida:.0f}) | Estoque: {max(0, estoque_disponivel_removido):.0f}")

                                        # Mostrar lista de itens
                                        if itens_dia:
                                            for item in itens_dia:
                                                st.markdown(item)
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
    # NOVA SEÇÃO: Relatórios e Análises Avançadas
    # =========================
    st.divider()
    st.header("📊 Relatórios e Análises Avançadas")
    
    # Gerar todos os relatórios analíticos
    with st.spinner("Gerando relatórios de análise..."):
        relatorios_analise = gerar_relatorio_analise(df_expandidos, df_antigo_expandidos, df_novo, df_antigo)
        graficos_analise = gerar_visualizacoes(relatorios_analise)
    
    # Mostrar os relatórios apenas se forem gerados com sucesso
    if relatorios_analise:
        # 1. Resumo das principais alterações
        st.subheader("📑 Resumo das Alterações")
        
        resumo_tabs = st.tabs(["Alterações por Fornecedor", "Alterações de Data", "Entregas Diárias"])
        
        # Tab 1: Alterações por Fornecedor
        with resumo_tabs[0]:
            if 'analise_fornecedor' in relatorios_analise:
                col1, col2 = st.columns(2)
                
                with col1:
                    if 'variacao_fornecedor' in graficos_analise:
                        st.plotly_chart(graficos_analise['variacao_fornecedor'], use_container_width=True)
                
                with col2:
                    if 'add_rem_fornecedor' in graficos_analise:
                        st.plotly_chart(graficos_analise['add_rem_fornecedor'], use_container_width=True)
                
                # Tabela detalhada de alterações por fornecedor
                st.subheader("Detalhes por Fornecedor")
                st.dataframe(relatorios_analise['analise_fornecedor'], use_container_width=True)
                
                # Botão para download do relatório
                st.download_button(
                    "⬇️ Baixar Relatório de Alterações por Fornecedor (CSV)",
                    gerar_csv(relatorios_analise['analise_fornecedor']),
                    "alteracoes_fornecedor.csv",
                    mime="text/csv"
                )
        
        # Tab 2: Alterações de Data
        with resumo_tabs[1]:
            col1, col2 = st.columns(2)
            
            with col1:
                if 'alteracoes_data' in graficos_analise:
                    st.plotly_chart(graficos_analise['alteracoes_data'], use_container_width=True)
            
            with col2:
                if 'alteracoes_fornecedor' in graficos_analise:
                    st.plotly_chart(graficos_analise['alteracoes_fornecedor'], use_container_width=True)
            
            # Estatísticas de alterações de data
            if 'analise_alteracoes' in relatorios_analise:
                st.subheader("Resumo de Alterações de Data")
                df_alteracoes = relatorios_analise['analise_alteracoes']
                
                # Mostrar estatísticas em colunas
                col1, col2, col3 = st.columns(3)
                total_alteracoes = df_alteracoes['Quantidade'].sum()
                
                with col1:
                    antecipacoes = df_alteracoes[df_alteracoes['Tipo de Alteração'] == 'Antecipado']['Quantidade'].sum() if 'Antecipado' in df_alteracoes['Tipo de Alteração'].values else 0
                    st.metric("Antecipações", f"{antecipacoes}", f"{antecipacoes/total_alteracoes*100:.1f}%" if total_alteracoes > 0 else "0%")
                
                with col2:
                    adiamentos = df_alteracoes[df_alteracoes['Tipo de Alteração'] == 'Adiado']['Quantidade'].sum() if 'Adiado' in df_alteracoes['Tipo de Alteração'].values else 0
                    st.metric("Adiamentos", f"{adiamentos}", f"{adiamentos/total_alteracoes*100:.1f}%" if total_alteracoes > 0 else "0%")
                
                with col3:
                    alteracoes_menores = df_alteracoes[df_alteracoes['Tipo de Alteração'] == 'Alteração Menor']['Quantidade'].sum() if 'Alteração Menor' in df_alteracoes['Tipo de Alteração'].values else 0
                    st.metric("Alterações Menores", f"{alteracoes_menores}", f"{alteracoes_menores/total_alteracoes*100:.1f}%" if total_alteracoes > 0 else "0%")
                
                # Mostrar tabela completa de alterações
                if 'alterados_data_completo' in relatorios_analise:
                    with st.expander("Ver todos os itens com alteração de data"):
                        df_alterados_completo = relatorios_analise['alterados_data_completo']
                        
                        # Formatar colunas para visualização
                        df_display = df_alterados_completo.copy()
                        if 'Inicio_novo' in df_display.columns and 'Inicio_antigo' in df_display.columns:
                            for col in ['Inicio_novo', 'Inicio_antigo', 'Termino_novo', 'Termino_antigo']:
                                if isinstance(df_display[col].iloc[0], pd.Timestamp):
                                    df_display[col] = df_display[col].dt.strftime('%d/%m/%Y %H:%M')
                        
                        # Selecionar colunas relevantes
                        cols_to_display = ['Ordem-split', 'Item/descrição', 'Fornecedor', 
                                          'Inicio_antigo', 'Inicio_novo', 'Status', 'Dif_Inicio_Horas']
                        
                        st.dataframe(df_display[cols_to_display], use_container_width=True)
                        
                        # Botão para download
                        st.download_button(
                            "⬇️ Baixar Relatório Completo de Alterações de Data (CSV)",
                            gerar_csv(df_alterados_completo),
                            "alteracoes_data_completo.csv",
                            mime="text/csv"
                        )
        
        # Tab 3: Entregas Diárias
        with resumo_tabs[2]:
            if 'entregas_diarias' in graficos_analise:
                st.plotly_chart(graficos_analise['entregas_diarias'], use_container_width=True)
            
            if 'entregas_comparativo' in relatorios_analise:
                with st.expander("Ver dados completos de entregas por dia"):
                    df_entregas = relatorios_analise['entregas_comparativo']
                    st.dataframe(df_entregas, use_container_width=True)
                    
                    # Botão para download
                    st.download_button(
                        "⬇️ Baixar Relatório de Entregas por Dia (CSV)",
                        gerar_csv(df_entregas),
                        "entregas_diarias.csv",
                        mime="text/csv"
                    )
        
        # 2. Análise de Adições e Remoções
        st.subheader("🔄 Análise de Adições e Remoções")
        
        add_rem_tabs = st.tabs(["Resumo de Adições/Remoções", "Itens Adicionados", "Itens Removidos"])
        
        # Tab 1: Resumo
        with add_rem_tabs[0]:
            # Gráfico de barras para novos vs. removidos
            if 'novos_removidos' in graficos_analise:
                st.plotly_chart(graficos_analise['novos_removidos'], use_container_width=True)
            
            # Resumo em números
            col1, col2, col3 = st.columns(3)
            
            total_novos = len(relatorios_analise.get('novos_itens_completo', pd.DataFrame())) if 'novos_itens_completo' in relatorios_analise else 0
            total_removidos = len(relatorios_analise.get('removidos_itens_completo', pd.DataFrame())) if 'removidos_itens_completo' in relatorios_analise else 0
            balanco = total_novos - total_removidos
            
            with col1:
                st.metric("Total de Itens Adicionados", f"{total_novos}")
            
            with col2:
                st.metric("Total de Itens Removidos", f"{total_removidos}")
            
            with col3:
                delta_color = "normal" if balanco >= 0 else "inverse"
                st.metric("Balanço (Adições - Remoções)", f"{balanco}", delta=f"{balanco:+d}", delta_color=delta_color)
        
        # Tab 2: Itens Adicionados
        with add_rem_tabs[1]:
            if 'novos_itens_completo' in relatorios_analise and not relatorios_analise['novos_itens_completo'].empty:
                df_novos = relatorios_analise['novos_itens_completo']
                
                # Agrupar por fornecedor para mostrar resumo
                resumo_novos = df_novos.groupby('Fornecedor').agg({
                    'Quantidade': ['sum', 'count']
                }).reset_index()
                
                resumo_novos.columns = ['Fornecedor', 'Volume Total', 'Quantidade de Itens']
                
                st.subheader("Resumo de Itens Adicionados por Fornecedor")
                st.dataframe(resumo_novos, use_container_width=True)
                
                # Mostrar lista completa em expansor
                with st.expander("Ver todos os itens adicionados"):
                    # Formatar para visualização
                    df_novos_display = df_novos.copy()
                    if 'Inicio' in df_novos_display.columns and isinstance(df_novos_display['Inicio'].iloc[0], pd.Timestamp):
                        df_novos_display['Inicio'] = df_novos_display['Inicio'].dt.strftime('%d/%m/%Y %H:%M')
                    
                    # Selecionar colunas relevantes
                    cols_to_display = ['Ordem-split', 'Item/descrição', 'Fornecedor', 'Inicio', 'Caixa', 'Quantidade']
                    
                    st.dataframe(df_novos_display[cols_to_display], use_container_width=True)
                    
                    # Botão para download
                    st.download_button(
                        "⬇️ Baixar Relatório de Itens Adicionados (CSV)",
                        gerar_csv(df_novos),
                        "itens_adicionados.csv",
                        mime="text/csv"
                    )
            else:
                st.info("Nenhum item adicionado identificado.")
        
        # Tab 3: Itens Removidos
        with add_rem_tabs[2]:
            if 'removidos_itens_completo' in relatorios_analise and not relatorios_analise['removidos_itens_completo'].empty:
                df_removidos = relatorios_analise['removidos_itens_completo']
                
                # Agrupar por fornecedor para mostrar resumo
                resumo_removidos = df_removidos.groupby('Fornecedor').agg({
                    'Quantidade': ['sum', 'count']
                }).reset_index()
                
                resumo_removidos.columns = ['Fornecedor', 'Volume Total', 'Quantidade de Itens']
                
                st.subheader("Resumo de Itens Removidos por Fornecedor")
                st.dataframe(resumo_removidos, use_container_width=True)
                
                # Mostrar lista completa em expansor
                with st.expander("Ver todos os itens removidos"):
                    # Formatar para visualização
                    df_removidos_display = df_removidos.copy()
                    if 'Inicio' in df_removidos_display.columns and isinstance(df_removidos_display['Inicio'].iloc[0], pd.Timestamp):
                        df_removidos_display['Inicio'] = df_removidos_display['Inicio'].dt.strftime('%d/%m/%Y %H:%M')
                    
                    # Selecionar colunas relevantes
                    cols_to_display = ['Ordem-split', 'Item/descrição', 'Fornecedor', 'Inicio', 'Caixa', 'Quantidade']
                    
                    st.dataframe(df_removidos_display[cols_to_display], use_container_width=True)
                    
                    # Botão para download
                    st.download_button(
                        "⬇️ Baixar Relatório de Itens Removidos (CSV)",
                        gerar_csv(df_removidos),
                        "itens_removidos.csv",
                        mime="text/csv"
                    )
            else:
                st.info("Nenhum item removido identificado.")
        
        # 3. Relatório de Impacto no Estoque
        if mapa_estoque:
            st.subheader("📦 Relatório de Impacto no Estoque")
            
            # Criar análise de impacto no estoque
            impact_tabs = st.tabs(["Visão Geral", "Itens sem Estoque", "Itens Removidos com Estoque"])
            
            # Tab 1: Visão Geral
            with impact_tabs[0]:
                # Analisar impacto no estoque das caixas atuais
                caixas_programa_atual = df_expandidos.groupby('Caixa')['Quantidade'].sum().reset_index()
                caixas_programa_atual['Em Estoque'] = caixas_programa_atual['Caixa'].map(lambda x: mapa_estoque.get(x, 0))
                caixas_programa_atual['Diferença'] = caixas_programa_atual['Em Estoque'] - caixas_programa_atual['Quantidade']
                caixas_programa_atual['Status'] = caixas_programa_atual['Diferença'].apply(
                    lambda x: "Suficiente" if x >= 0 else "Insuficiente"
                )
                caixas_programa_atual['Fornecedor'] = caixas_programa_atual['Caixa'].map(mapa_fornecedor)
                
                # Estatísticas gerais
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    total_necessario = caixas_programa_atual['Quantidade'].sum()
                    total_disponivel = caixas_programa_atual['Em Estoque'].sum()
                    st.metric(
                        "Total Necessário vs. Disponível", 
                        f"{total_necessario:.0f}",
                        f"Estoque: {total_disponivel:.0f} ({(total_disponivel/total_necessario*100):.1f}%)" if total_necessario > 0 else "N/A"
                    )
                
                with col2:
                    caixas_com_estoque_suficiente = len(caixas_programa_atual[caixas_programa_atual['Status'] == 'Suficiente'])
                    percentual_suficiente = (caixas_com_estoque_suficiente / len(caixas_programa_atual) * 100) if len(caixas_programa_atual) > 0 else 0
                    st.metric(
                        "Caixas com Estoque Suficiente", 
                        f"{caixas_com_estoque_suficiente}/{len(caixas_programa_atual)}",
                        f"{percentual_suficiente:.1f}%"
                    )
                
                with col3:
                    caixas_sem_estoque = len(caixas_programa_atual[caixas_programa_atual['Status'] == 'Insuficiente'])
                    percentual_insuficiente = (caixas_sem_estoque / len(caixas_programa_atual) * 100) if len(caixas_programa_atual) > 0 else 0
                    st.metric(
                        "Caixas com Estoque Insuficiente", 
                        f"{caixas_sem_estoque}/{len(caixas_programa_atual)}",
                        f"{percentual_insuficiente:.1f}%",
                        delta_color="inverse"
                    )
                
                # Gráfico de barras empilhadas para mostrar a situação por fornecedor
                resumo_estoque_fornecedor = caixas_programa_atual.groupby(['Fornecedor', 'Status']).size().reset_index()
                resumo_estoque_fornecedor.columns = ['Fornecedor', 'Status', 'Quantidade']
                
                fig_estoque_status = px.bar(
                    resumo_estoque_fornecedor,
                    x='Fornecedor',
                    y='Quantidade',
                    color='Status',
                    title='Status de Estoque por Fornecedor',
                    color_discrete_map={'Suficiente': 'green', 'Insuficiente': 'red'}
                )
                st.plotly_chart(fig_estoque_status, use_container_width=True)
            
            # Tab 2: Itens sem Estoque
            with impact_tabs[1]:
                caixas_sem_estoque_df = caixas_programa_atual[caixas_programa_atual['Status'] == 'Insuficiente'].sort_values('Diferença')
                
                if not caixas_sem_estoque_df.empty:
                    st.subheader("Itens com Estoque Insuficiente")
                    
                    # Adicionar coluna de prioridade
                    caixas_sem_estoque_df['Prioridade'] = caixas_sem_estoque_df['Diferença'].apply(
                        lambda x: "Alta" if x <= -100 else ("Média" if x <= -50 else "Baixa")
                    )
                    
                    # Agrupar por fornecedor e prioridade
                    resumo_prioridade = caixas_sem_estoque_df.groupby(['Fornecedor', 'Prioridade']).size().reset_index()
                    resumo_prioridade.columns = ['Fornecedor', 'Prioridade', 'Quantidade']
                    
                    # Gráfico de barras para prioridades
                    fig_prioridade = px.bar(
                        resumo_prioridade,
                        x='Fornecedor',
                        y='Quantidade',
                        color='Prioridade',
                        title='Itens sem Estoque Suficiente por Prioridade',
                        color_discrete_map={'Alta': 'red', 'Média': 'orange', 'Baixa': 'yellow'}
                    )
                    st.plotly_chart(fig_prioridade, use_container_width=True)
                    
                    # Mostrar tabela detalhada
                    st.dataframe(caixas_sem_estoque_df[[
                        'Caixa', 'Fornecedor', 'Quantidade', 'Em Estoque', 'Diferença', 'Prioridade'
                    ]].sort_values(['Fornecedor', 'Prioridade']), use_container_width=True)
                    
                    # Botão para download
                    st.download_button(
                        "⬇️ Baixar Relatório de Itens sem Estoque Suficiente (CSV)",
                        gerar_csv(caixas_sem_estoque_df),
                        "itens_sem_estoque.csv",
                        mime="text/csv"
                    )
                else:
                    st.success("Todos os itens do programa possuem estoque suficiente!")
            
            # Tab 3: Itens Removidos com Estoque
            with impact_tabs[2]:
                if 'removidos_itens_completo' in relatorios_analise and not relatorios_analise['removidos_itens_completo'].empty:
                    df_removidos = relatorios_analise['removidos_itens_completo']
                    df_removidos['Em Estoque'] = df_removidos['Caixa'].map(lambda x: mapa_estoque.get(x, 0))
                    df_removidos_com_estoque = df_removidos[df_removidos['Em Estoque'] > 0]
                    
                    if not df_removidos_com_estoque.empty:
                        st.subheader("Itens Removidos que ainda possuem Estoque")
                        
                        # Agrupar por fornecedor
                        resumo_removidos_estoque = df_removidos_com_estoque.groupby('Fornecedor').agg({
                            'Quantidade': 'count',
                            'Em Estoque': 'sum'
                        }).reset_index()
                        
                        resumo_removidos_estoque.columns = ['Fornecedor', 'Quantidade de Itens', 'Volume em Estoque']
                        
                        # Mostrar resumo
                        st.dataframe(resumo_removidos_estoque, use_container_width=True)
                        
                        # Gráfico de barras para itens removidos com estoque
                        fig_removidos_estoque = px.bar(
                            resumo_removidos_estoque,
                            x='Fornecedor',
                            y='Volume em Estoque',
                            title='Estoque Disponível de Itens Removidos',
                            color='Fornecedor'
                        )
                        st.plotly_chart(fig_removidos_estoque, use_container_width=True)
                        
                        # Mostrar tabela detalhada
                        with st.expander("Ver detalhes dos itens removidos com estoque"):
                            # Formatar para visualização
                            df_removidos_display = df_removidos_com_estoque.copy()
                            if 'Inicio' in df_removidos_display.columns and isinstance(df_removidos_display['Inicio'].iloc[0], pd.Timestamp):
                                df_removidos_display['Inicio'] = df_removidos_display['Inicio'].dt.strftime('%d/%m/%Y %H:%M')
                            
                            st.dataframe(df_removidos_display[[
                                'Caixa', 'Fornecedor', 'Em Estoque', 'Item/descrição'
                            ]], use_container_width=True)
                            
                            # Botão para download
                            st.download_button(
                                "⬇️ Baixar Relatório de Itens Removidos com Estoque (CSV)",
                                gerar_csv(df_removidos_com_estoque),
                                "itens_removidos_com_estoque.csv",
                                mime="text/csv"
                            )
                    else:
                        st.info("Nenhum item removido possui estoque disponível.")
                else:
                    st.info("Não há itens removidos para analisar.")
        
        # 4. Relatório completo para download
        st.subheader("📄 Gerar Relatório Completo")
        
        # Criar buffer para escrever o Excel
        if st.button("📊 Gerar Relatório Completo (Excel)"):
            with st.spinner("Gerando relatório completo..."):
                try:
                    # Criar buffer de memória para o arquivo Excel
                    output = io.BytesIO()
                    
                    # Criar escritor Excel com Pandas
                    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
                        # 1. Resumo por Fornecedor
                        if 'analise_fornecedor' in relatorios_analise:
                            relatorios_analise['analise_fornecedor'].to_excel(writer, sheet_name='Resumo_Fornecedor', index=False)
                        
                        # 2. Alterações de Data
                        if 'alterados_data_completo' in relatorios_analise:
                            # Formatar colunas de data
                            df_alterados = relatorios_analise['alterados_data_completo'].copy()
                            for col in ['Inicio_novo', 'Inicio_antigo', 'Termino_novo', 'Termino_antigo']:
                                if isinstance(df_alterados[col].iloc[0], pd.Timestamp):
                                    df_alterados[col] = df_alterados[col].dt.strftime('%d/%m/%Y %H:%M')
                            
                            df_alterados.to_excel(writer, sheet_name='Alterações_Data', index=False)
                        
                        # 3. Itens Adicionados
                        if 'novos_itens_completo' in relatorios_analise:
                            # Formatar colunas de data
                            df_novos = relatorios_analise['novos_itens_completo'].copy()
                            if 'Inicio' in df_novos.columns and isinstance(df_novos['Inicio'].iloc[0], pd.Timestamp):
                                df_novos['Inicio'] = df_novos['Inicio'].dt.strftime('%d/%m/%Y %H:%M')
                            
                            df_novos.to_excel(writer, sheet_name='Itens_Adicionados', index=False)
                        
                        # 4. Itens Removidos
                        if 'removidos_itens_completo' in relatorios_analise:
                            # Formatar colunas de data
                            df_removidos = relatorios_analise['removidos_itens_completo'].copy()
                            if 'Inicio' in df_removidos.columns and isinstance(df_removidos['Inicio'].iloc[0], pd.Timestamp):
                                df_removidos['Inicio'] = df_removidos['Inicio'].dt.strftime('%d/%m/%Y %H:%M')
                            
                            df_removidos.to_excel(writer, sheet_name='Itens_Removidos', index=False)
                        
                        # 5. Entregas Diárias
                        if 'entregas_comparativo' in relatorios_analise:
                            df_entregas = relatorios_analise['entregas_comparativo'].copy()
                            # Converter data para string se for datetime
                            if isinstance(df_entregas['Data'].iloc[0], pd.Timestamp):
                                df_entregas['Data'] = df_entregas['Data'].dt.strftime('%d/%m/%Y')
                            
                            df_entregas.to_excel(writer, sheet_name='Entregas_Diárias', index=False)
                        
                        # 6. Análise de Estoque
                        if mapa_estoque:
                            # Criar análise de estoque
                            caixas_programa_atual = df_expandidos.groupby('Caixa')['Quantidade'].sum().reset_index()
                            caixas_programa_atual['Em Estoque'] = caixas_programa_atual['Caixa'].map(lambda x: mapa_estoque.get(x, 0))
                            caixas_programa_atual['Diferença'] = caixas_programa_atual['Em Estoque'] - caixas_programa_atual['Quantidade']
                            caixas_programa_atual['Status'] = caixas_programa_atual['Diferença'].apply(
                                lambda x: "Suficiente" if x >= 0 else "Insuficiente"
                            )
                            caixas_programa_atual['Fornecedor'] = caixas_programa_atual['Caixa'].map(mapa_fornecedor)
                            
                            caixas_programa_atual.to_excel(writer, sheet_name='Análise_Estoque', index=False)
                    
                    # Reset pointer do BytesIO para o início
                    output.seek(0)
                    
                    # Obter timestamp para nome do arquivo
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    
                    # Mostrar botão de download
                    st.download_button(
                        label="⬇️ Baixar Relatório Completo (Excel)",
                        data=output,
                        file_name=f"relatorio_completo_{timestamp}.xlsx",
                        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                    )
                    
                    st.success("Relatório completo gerado com sucesso!")
                    
                except Exception as e:
                    st.error(f"Erro ao gerar relatório completo: {str(e)}")
    else:
        st.warning("Não foi possível gerar relatórios de análise. Certifique-se de que os arquivos do programa atual e anterior foram carregados corretamente.")
