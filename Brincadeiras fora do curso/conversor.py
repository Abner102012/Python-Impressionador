import streamlit as st
import requests

# 1. CONFIGURAÇÃO DA PÁGINA (Sempre deve ser a primeira linha de comando Streamlit)
st.set_page_config(page_title="Conversor Pro", page_icon="💰", layout="centered")

# 2. ESTILO VISUAL (CSS Customizado)
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to right, #1e3c72, #2a5298);
        color: white;
    }
    .stNumberInput, .stSelectbox {
        background-color: rgba(255, 255, 255, 0.1);
        border-radius: 10px;
        padding: 5px;
    }
    .stButton>button {
        width: 100%;
        background-color: #ff4b4b;
        color: white;
        font-weight: bold;
        border-radius: 20px;
        height: 3em;
        transition: 0.3s;
        border: none;
    }
    .stButton>button:hover {
        background-color: #ff7575;
        transform: scale(1.02);
    }
    /* Estiliza textos dos labels para branco */
    label { color: white !important; }
    </style>
    """, unsafe_allow_html=True)

# 3. FUNÇÃO DE BUSCA DE DADOS
def get_rates(base):
    try:
        url = f"https://open.er-api.com/v6/latest/{base}"
        response = requests.get(url)
        return response.json()
    except:
        return None

# 4. INTERFACE DO USUÁRIO
st.title("💸 Conversor de Moedas VIP")
st.write("Taxas de câmbio globais atualizadas em tempo real.")

with st.container():
    valor = st.number_input("Quanto deseja converter?", min_value=0.0, value=100.0, step=1.0)
    
    moedas = ["BRL", "USD", "EUR", "GBP", "JPY", "CAD", "ARS", "CHY"]
    
    col1, col2 = st.columns(2)
    with col1:
        # Adicionei 'key' únicas para evitar o erro de duplicata
        origem = st.selectbox("De:", moedas, index=0, key="moeda_de")
    with col2:
        destino = st.selectbox("Para:", moedas, index=1, key="moeda_para")

    st.markdown("<br>", unsafe_allow_html=True)
    
    if st.button("CALCULAR AGORA"):
        with st.spinner('Consultando mercado financeiro...'):
            dados = get_rates(origem)
            
            if dados and dados.get("result") == "success":
                taxa = dados["rates"][destino]
                resultado = valor * taxa
                atualizacao = dados["time_last_update_utc"]
                
                # Resultado Estilizado
                st.markdown(f"""
                    <div style="background-color: rgba(255,255,255,0.2); padding: 25px; border-radius: 15px; text-align: center; border: 1px solid rgba(255,255,255,0.3);">
                        <h2 style="margin:0; font-weight: 300;">{valor:,.2f} {origem} equivale a</h2>
                        <h1 style="color: #00ffcc; margin: 10px 0; font-size: 3em;">{resultado:,.2f} {destino}</h1>
                        <p style="margin:0; opacity: 0.7;">Taxa: 1 {origem} = {taxa:.4f} {destino}</p>
                        <p style="font-size: 0.8em; opacity: 0.5;">Atualizado em: {atualizacao}</p>
                    </div>
                """, unsafe_allow_html=True)
            else:
                st.error("Erro ao conectar com o serviço de câmbio. Verifique sua internet.")

# 5. RODAPÉ
st.markdown("---")
st.caption("🚀 Desenvolvido com Python e Streamlit | Dados: ExchangeRate-API")