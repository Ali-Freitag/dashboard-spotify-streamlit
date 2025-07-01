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
    st.title("Visualização dos Gráficos Interativos")

    # Menu na barra lateral:
    st.sidebar.header("Menu de Gráficos")
    escolha_grafico = st.sidebar.radio(
        "Selecione o gráfico que deseja visualizar:",
        ("Popularidade dos Artistas (Linhas)", "Contagem por Gênero (Barras)"),
    )

    st.header(f"Visualizando: {escolha_grafico}")

    if escolha_grafico == "Popularidade dos Artistas (Linhas)":
        # Criamos um slider que vai de 0 a 100, com o valor padrão em 80.
        # O valor escolhido pelo usuário é salvo na variável 'popularidade_selecionada'.
        st.subheader("Filtro por popularidade")
        popularidade_selecionada = st.slider(
            label="Selecione o nível mínimo de popularidade:",
            min_value=0,
            max_value=100,
            value=80,  # Valor inicial
        )

        # Verifica se o dataframe existe no estado da sessão
        if "dataframe_inicial" in st.session_state:
            df_filtrado = df_original[df_original["popularity"]
                                      >= popularidade_selecionada]

            # Criando o gráfico de linhas
            st.subheader(
                f"Gráfico de Popularidade dos Artistas no Spotify >= {popularidade_selecionada}"
            )
            if not df_filtrado.empty:
                fig_linha = px.line(
                    df_filtrado.sort_values(
                        "popularity", ascending=False
                    ),  # Ordenar pode melhorar a visualização
                    x="name",
                    y="popularity",
                    title=f"Artistas com Popularidade a partir de {popularidade_selecionada}",
                    labels={
                        "name": "Nome do Artista",
                        "popularity": "Popularidade (0-100)",
                    },
                    markers=True,  # Adiciona marcadores nos pontos para melhor visualização
                )
                st.plotly_chart(fig_linha, use_container_width=True)
            else:
                st.warning(
                    f"Nenhum artista encontrado com o filtro selecionados: {popularidade_selecionada}."
                )
        else:
            st.error(
                "DataFrame não encontrado na sessão. Carregue os dados primeiro.")
            st.info(
                "Por favor, vá para a página 🐼 Pandas primeiro para inicializar o dataframe."
            )
            # Você pode até colocar um link para a página principal
            st.page_link(
                "pages/2_🐼Pandas.py",
                label="Ir para a página da biblioteca Pandas",
                icon="🐼",
            )
    elif escolha_grafico == "Contagem por Gênero (Barras)":
        st.subheader(
            "Gráfico de barras mostrando quantos artistas há por gênero musical.")
        # Cria a lista de opções a partir da coluna do DataFrame, com 'Todos' adicionado para permitir a visualização completa
        st.subheader("Filtro com `st.selectbox`")
        opcoes_genero = ["Todos"] + list(df_original["genres"].unique())
        generos_selecionados = st.multiselect(
            "Selecione um ou mais gêneros:",
            options=opcoes_genero,
            default=['kuduro', 'grunge pop']
        )

        df_filtrado_pela_selecao = df_original[df_original['genres'].isin(
            generos_selecionados)]

        if not df_filtrado_pela_selecao.empty:
            df_contagem = df_filtrado_pela_selecao['genres'].value_counts(
            ).reset_index()
            df_contagem.columns = ['genres', 'count']  # Renomear colunas
            fig_barras = px.bar(
                df_contagem,
                x='genres',
                y='count',
                title='Proporção de Gêneros Musicais na Lista de Artistas',
                labels={'genres': 'Gênero Musical',
                        'count': 'Número de Artistas'}
            )
            fig_barras.update_layout(
                xaxis_tickangle=-45  # Rotacionar rótulos do eixo X
            )
            st.plotly_chart(fig_barras, use_container_width=True)
        else:
            st.warning(
                "Nenhum gênero selecionado ou nenhum dado encontrado para a seleção.")
