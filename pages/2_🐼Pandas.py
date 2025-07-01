import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Artistas Spotify - Pandas",
    page_icon="🎤",
    layout="wide"
)

st.title("Artistas Spotify: uso da biblioteca Pandas")

if 'dataframe_inicial' not in st.session_state:
    inicial = pd.read_csv('artists.csv')
    st.session_state.dataframe_inicial = inicial
    st.success("DataFrame inicial 'artists.csv' carregado com sucesso!")
else:
    st.info('O DataFrame já fora carregado anteriormente.')


def limpeza_dados():
    df = st.session_state.dataframe_inicial.copy()
    st.info("Iniciando limpeza de dados...")
    df = df[df['genres'] != '[]']
    df['genres'] = df['genres'].str.replace('[', '')\
        .str.replace(']', '')\
        .str.replace("'", '')\
        .str.replace('"', '')\
        .str.strip()
    if 'id' in df.columns:
        df = df.drop('id', axis=1, inplace=False).reset_index()
        st.success("Limpeza de dados concluída!")
    else:
        st.warning("Limpeza refeita, mas nada alterado.")
    return df


st.markdown(f"""
Bem-vindo(a) a breve explicação do uso do **Pandas**!

Nesta página, vamos manipular o DataFrame para que mostre somente o conteúdo releventa para nós.
* **Para conseguir armazenar a limpeza do DataFrame na página, mas sem modificar o original, vamos utilizar a ferramenta st.session.state.**

    *A ferramenta st.session_state ajuda a resolver um problema central nos script, a reexecução deles, pois o Streamlit reexecuta o script do zero quando há uma interação do usuário com qualquer widget do código, ou um salvamento.*

    *Basicamente, st.session_state é como um dicionário Python que persiste entre as reexecuções do script. Ele permite que você armazene e recupere informações ao longo da sessão de um usuário.*
            
* **Criar uma função em Python para automatizar a limpeza do DataFrame**

    * *Removendo os registros que não tenham um gênero musical definido:*   
    * *Excluir a coluna "id", pois esta informação não é necessária para nós.*  
    * *Por fim, retornar na função os valores copiados de st.session_state.dataframe_inicial, porém já tratados.*
            
* **O processo descrito acima foi feito com os seguinte trecho de código:**
    
        if 'dataframe_inicial' not in st.session_state:
            inicial = pd.read_csv('artists.csv')
            st.session_state.dataframe_inicial = inicial
            st.success("DataFrame inicial 'artists.csv' carregado com sucesso!")

        def limpeza_dados():
            df = st.session_state.dataframe_inicial.copy()
            st.info("Iniciando limpeza de dados...")
            df = df[df['genres'] != '[]']
            df = df.drop('id', axis=1, inplace=False)
            st.success("Limpeza de dados concluída!")
            return df

Ao final desse processo, o DataFrame está pronto para o uso na criação de gráficos.
            
Interessante verificar o código do botão:
        
        if st.button("Clique aqui para executar a limpeza de dados"):
            df_limpo = limpeza_dados()

            st.session_state.dataframe_inicial = df_limpo
            st.success("DataFrame limpo salvo no estado da sessão!")

**Vale lembrar que o "st.session_state" só será reiniciado quando a página for fechada, recarregada ou o servidor for reiniciado, se não, manterá salvo os dados mesmo quando navegarmos por diferentes páginas, pois o que determina a permanência dos dados é a sessão do usuário no navegador.**
""")

if st.button("Clique aqui para executar a limpeza de dados"):
    df_limpo = limpeza_dados()

    st.session_state.dataframe_inicial = df_limpo
    st.success("DataFrame limpo salvo no estado da sessão!")

st.subheader("Visão Geral sobre os Dados")
st.dataframe(st.session_state.dataframe_inicial)
