import pandas as pd
import streamlit as st
import plotly.express as px
if 'dataframe_inicial' not in st.session_state:
    st.error("DataFrame não encontrado na sessão. Carregue os dados primeiro.")
    st.info(
        "Por favor, vá para a página 🐼 Pandas primeiro para inicializar o dataframe."
    )
    # Link para a página principal
    st.page_link(
        "pages/2_🐼Pandas.py",
        label="Ir para a página da biblioteca Pandas",
        icon="🐼",
    )
else:
    df_original = st.session_state.dataframe_inicial
    # Título da Página
    st.title("Visualização dos Gráficos Não-Interativos")

    # Menu na barra lateral:
    st.sidebar.header("Menu de Gráficos")
    escolha_grafico = st.sidebar.radio(
        "Selecione o gráfico que deseja visualizar:",
        ("Distribuição da popularidade dos artistas (Histograma)",
         "Relação Entre Seguidores e Popularidade (Dispersão)",
         "Os 20 Maiores Artistas do Spotify (Barras Horizontais)",
         "Os 10 Artistas com mais seguidores no Spotify (Barras Verticais)"
         )
    )

    st.header(f"Visualizando: {escolha_grafico}")

    if escolha_grafico == "Distribuição da popularidade dos artistas (Histograma)":
        st.subheader("Distribuição da popularidade")
        # Para um histograma mais útil, vamos ignorar os artistas com popularidade 0
        df_com_popularidade = df_original[df_original['popularity'] > 10]

        if not df_com_popularidade.empty:
            # Código do histograma
            fig_hist = px.histogram(
                df_com_popularidade,
                x='popularity',
                title='Distribuição da Popularidade dos Artistas',
                labels={'popularity': 'Nível de Popularidade'},
                nbins=50,  # Aumentar o número de "caixas" para mais detalhes
                color='popularity',
                category_orders={"Categoria": ["C", "B", "A"]}
            )
            fig_hist.update_layout(height=800)
            st.plotly_chart(fig_hist, use_container_width=True)
        else:
            st.error(
                "DataFrame não encontrado na sessão. Carregue os dados primeiro.")
            st.info(
                "Por favor, vá para a página 🐼 Pandas primeiro para inicializar o dataframe."
            )
            # Link para a página principal
            st.page_link(
                "pages/2_🐼Pandas.py",
                label="Ir para a página da biblioteca Pandas",
                icon="🐼",
            )
    elif escolha_grafico == "Relação Entre Seguidores e Popularidade (Dispersão)":
        st.subheader(
            "Relação Entre Seguidores e Popularidade")
        # Vamos focar em artistas que têm pelo menos alguns seguidores e popularidade
        df_filtrado = df_original[(
            df_original['popularity'] > 25) & (df_original['followers'] > 100)]
        if not df_filtrado.empty:
            # Gráfico de dispersão
            fig_scatter = px.scatter(
                df_filtrado,
                x='followers',
                y='popularity',
                title='Relação entre Seguidores e Popularidade',
                labels={'followers': 'Número de Seguidores',
                        'popularity': 'Popularidade (0-100)'},
                hover_name='name',  # Mostra o nome do artista ao passar o mouse
                color="popularity",
                color_discrete_sequence=px.colors.qualitative.Pastel
            )
            fig_scatter.update_layout(xaxis_type='log', yaxis_type='log',
                                      height=1000)
            st.plotly_chart(fig_scatter, use_container_width=True)
        else:
            st.error(
                "DataFrame não encontrado na sessão. Carregue os dados primeiro.")
            st.info(
                "Por favor, vá para a página 🐼 Pandas primeiro para inicializar o dataframe."
            )
            # Link para a página principal
            st.page_link(
                "pages/2_🐼Pandas.py",
                label="Ir para a página da biblioteca Pandas",
                icon="🐼",
            )
    elif escolha_grafico == "Os 20 Maiores Artistas do Spotify (Barras Horizontais)":
        st.subheader(
            "Top 20 Maiores Artistas do Spotify (por popularidade)"
        )
        # Ordenar o DataFrame e pegar os 20 primeiros
        df_filtrado = top_20_populares = df_original.sort_values(
            by='popularity', ascending=False).head(20)
        if not top_20_populares.empty:
            # Gráfico de barras horizontal
            fig_bar_top20 = px.bar(
                top_20_populares,
                x='popularity',
                y='name',  # Note que 'name' está no eixo Y
                orientation='h',  # Define a orientação como horizontal
                title='Top 20 Artistas (por popularidade)',
                labels={'name': 'Artista',
                        'popularity': 'Nível de Popularidade'},
                color="name"
            )
            # Inverter o eixo Y para que o artista mais popular fique no topo
            fig_bar_top20.update_layout(yaxis={'categoryorder': 'total ascending'},
                                        height=1000)
            st.plotly_chart(fig_bar_top20, use_container_width=True)
        else:
            st.error(
                "DataFrame não encontrado na sessão. Carregue os dados primeiro.")
            st.info(
                "Por favor, vá para a página 🐼 Pandas primeiro para inicializar o dataframe."
            )
            # Link para a página principal
            st.page_link(
                "pages/2_🐼Pandas.py",
                label="Ir para a página da biblioteca Pandas",
                icon="🐼",
            )
    elif escolha_grafico == "Os 10 Artistas com mais seguidores no Spotify (Barras Verticais)":
        st.subheader(
            "Top 10 Artistas com mais seguidores no Spotify (Por Seguidores)"
        )
        top_10_followers = df_original.sort_values(
            by='followers', ascending=False).head(10)
        if not top_10_followers.empty:
            fig_barras_top10 = px.bar(
                data_frame=top_10_followers,
                x='name',        # As categorias (nomes dos artistas) no eixo X
                y='followers',   # Os valores (número de seguidores) no eixo Y
                title='Top 10 Artistas por Número de Seguidores',
                labels={'name': 'Artista',
                        'followers': 'Número de Seguidores'},
                text_auto=True,  # Adiciona o valor exato no topo de cada barra
                color='name'
            )
            # Rotação do eixo X em 45 graus.
            fig_barras_top10.update_layout(
                xaxis_tickangle=-45,
                height=600
            )
            st.plotly_chart(fig_barras_top10, use_container_width=True)
        else:
            st.error(
                "DataFrame não encontrado na sessão. Carregue os dados primeiro.")
            st.info(
                "Por favor, vá para a página 🐼 Pandas primeiro para inicializar o dataframe."
            )
            # Link para a página principal
            st.page_link(
                "pages/2_🐼Pandas.py",
                label="Ir para a página da biblioteca Pandas",
                icon="🐼",
            )
