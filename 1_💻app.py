import pandas as pd
import streamlit as st
import plotly.express as px

# --- Configuração da Página ---
# Ajustado para refletir o tema do dashboard
st.set_page_config(
    page_title="Dashboard Spotify | Análise de Artistas",
    page_icon="🎵",
    layout="wide"
)

# --- Título Principal ---
st.title("🎵 Artistas Spotify: Análise dos números da indústria musical")

# --- Carregamento dos Dados ---
try:
    df = pd.read_csv('artists.csv')
except FileNotFoundError:
    st.error("Erro: O arquivo 'artists.csv' não foi encontrado. Certifique-se de que ele está na mesma pasta que o seu script.")
    st.stop()  # Interrompe a execução do app se o arquivo não existir

# --- Documentação do Projeto ---
st.markdown(f"""
Bem-vindo(a) ao **Dashboard de Análise de Artistas do Spotify**!

Este aplicativo interativo foi desenvolvido para explorar o vasto universo de artistas na maior plataforma de streaming de música do mundo. Utilizando um conjunto de dados detalhado, buscamos responder a perguntas-chave sobre o cenário musical atual:

* **Quem são os artistas que dominam os rankings de popularidade e seguidores?**
* **Quais são os gêneros musicais mais predominantes e quais estão em ascensão?**
* **Existe uma correlação entre o número de seguidores de um artista e sua popularidade na plataforma?**

Nosso objetivo é fornecer uma ferramenta visual e intuitiva para que fãs de música, analistas de dados e curiosos possam descobrir tendências e obter insights sobre seus artistas e gêneros favoritos.

---

### Como Navegar:

Utilize o menu na **barra lateral (esquerda)** para explorar as diferentes seções do dashboard:

* **🏆 Rankings:** Visualize os top artistas por popularidade e número de seguidores.
* **🎶 Análise por Gênero:** Mergulhe na distribuição de gêneros e suas características.
* **📈 Exploração de Dados:** Analise as relações entre as métricas com gráficos de dispersão e outras visualizações.
""")

st.markdown(f"""
O conjunto de dados analisado possui as seguintes dimensões:
- **Linhas (Artistas):** `{df.shape[0]}`
- **Colunas (Atributos):** `{df.shape[1]}`
""")

# --- Amostra dos Dados ---
st.header("Amostra dos Dados")
st.dataframe(df.head())  # preview dos dados

st.markdown("""
---
### Como Usar os Filtros

Em cada página de análise, você encontrará filtros interativos (como menus e sliders) na barra lateral. Esses filtros são a chave para explorar os dados:

**Qualquer alteração nos filtros atualizará todos os gráficos da página instantaneamente!** Isso permite que você investigue os dados da maneira que preferir, focando em gêneros específicos ou em artistas com um determinado nível de popularidade.

**Contamos também com os filtros não-interativos, montados afim de demonstrar alguns dados do DataFrame previamente tratados e condicionados para uma melhor visualização.**
            """)

# --- Barra Lateral ---
st.sidebar.header("Navegação")
st.sidebar.info(
    "Selecione uma das análises no menu acima para começar a explorar!")
