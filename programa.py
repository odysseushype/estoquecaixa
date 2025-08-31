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
col_prog, col_estoque = st.columns([1, 1])

with col_prog:
    uploaded_file = st.file_uploader("Selecione o arquivo Excel principal", type=["xlsx"])

with col_estoque:
    uploaded_stock_file = st.file_uploader("📦 Arquivo de Estoque", type=["xlsx", "csv"])

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
    
    # REMOVER ESTE BLOCO: Não extrair data do nome do arquivo 
    # data_estoque = None
    # nome_arquivo = uploaded_stock_file.name
    # date_match = re.search(r'.*?(\d{2})[-_](\d{2})[-_](\d{4})', nome_arquivo)
    # if date_match:
    #     dia, mes, ano = date_match.groups()
    #     data_estoque = f"{dia}/{mes}/{ano}"
    # else:
    #     data_estoque = "Data não identificada"
    
    # REMOVER ESTE BLOCO: Não recalcular variação usando histórico de sessão
    # variacao_total = None
    # if st.session_state.historico_estoque:
    #     estoque_anterior = st.session_state.historico_estoque[-1]
    #     qtd_anterior = sum(estoque_anterior.values())
    #     variacao_total = quantidade_total - qtd_anterior
    #     variacao_percentual = (variacao_total / qtd_anterior) * 100 if qtd_anterior > 0 else 0
    
    # Salvar no histórico apenas se for útil para outras funções
    # (pode ser removido se não for necessário)
    if data_estoque and data_estoque not in st.session_state.datas_estoque:
        st.session_state.historico_estoque.append(mapa_estoque.copy())
        st.session_state.datas_estoque.append(data_estoque)
    
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
                
                # Total de caixas para o fornecedor
                total_forn = df_forn['Quantidade'].sum()
                
                # Exibir o total
                st.write(f"**Total de caixas: {total_forn:.2f}**")
                
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
                            
                            # Obter datas únicas na semana
                            datas_unicas = sorted(df_semana_atual['Dia Entrega'].dt.date.unique())
                            
                            # Filtrar datas para mostrar apenas as >= data_programa
                            if data_programa is not None:
                                datas_unicas = [data for data in datas_unicas 
                                              if data >= data_programa.date()]
                            
                            if len(datas_unicas) > 0:
                                # Criar colunas lado a lado para cada dia
                                cols = st.columns(min(len(datas_unicas), 5))  # Máximo de 5 colunas por linha
                                
                                for idx, data in enumerate(datas_unicas):
                                    # Definir em qual coluna este dia será exibido
                                    col_idx = idx % len(cols)
                                    
                                    # Filtrar dados apenas para este dia
                                    df_dia = df_semana_atual[df_semana_atual['Dia Entrega'].dt.date == data]
                                    
                                    # Calcular total do dia
                                    total_dia = df_dia['Quantidade'].sum()
                                    
                                    # Agrupar caixas do mesmo tipo e somar quantidades
                                    df_caixas_agrupadas = df_dia.groupby('Caixa')['Quantidade'].sum().reset_index()
                                    
                                    # Listar itens do dia com verificação de estoque
                                    itens_dia = []
                                    for _, row in df_caixas_agrupadas.iterrows():
                                        caixa = row['Caixa']
                                        qtd_total = row['Quantidade']
                                        
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
                                        
                                        if tem_estoque:
                                            itens_dia.append(f"{estoque_emoji} **{caixa}** | Qtd: {qtd_total:.0f} | Estoque: {max(0, estoque_disponivel):.0f}")
                                        else:
                                            # Mostrar quanto falta quando não há estoque suficiente
                                            itens_dia.append(f"{estoque_emoji} **{caixa}** | Qtd: {qtd_total:.0f} | Estoque: {max(0, estoque_disponivel):.0f} | **Falta: {quantidade_faltante:.0f}**")
                                    
                                    # Exibir bloco no layout
                                    with cols[col_idx]:
                                        st.markdown(f"**{data.strftime('%d/%m/%Y')} ({data.strftime('%a')})**")
                                        st.metric(
                                            label="Total de Caixas", 
                                            value=f"{total_dia:.0f}",
                                            delta=None
                                        )
                                        
                                        # Mostrar lista de itens
                                        if itens_dia:
                                            for item in itens_dia:
                                                st.markdown(item)
                                        else:
                                            st.info("Sem itens")
                            else:
                                st.info("Sem dados para esta semana")
                        except Exception as e:
                            st.error(f"Erro ao processar semana {semana_str}: {str(e)}")
else:
    st.info("📂 Faça o upload do arquivo Excel principal para visualizar o cronograma.")
