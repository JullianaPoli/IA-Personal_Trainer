import streamlit as st # type: ignore

# Função para classificar o biotipo
def classificar_biotipo(altura, peso, caracteristicas):
    if "alta" in caracteristicas and ("barriga" in caracteristicas or "largos" in caracteristicas):
        return "Endomorfo"
    elif "alta" in caracteristicas and "magro" in caracteristicas:
        return "Ectomorfo"
    elif "musculoso" in caracteristicas or "atleta" in caracteristicas:
        return "Mesomorfo"
    else:
        return "Não identificado"

# Função para classificar o treino
def classificar_treino(dias_disponiveis):
    if dias_disponiveis == "1 dia" or dias_disponiveis == "2 dias":
        return "Treino Full Body"
    elif dias_disponiveis == "3 dias" or dias_disponiveis == "4 dias":
        return "Treino Soft"
    elif dias_disponiveis == "5 dias" or dias_disponiveis == "6 dias":
        return "Treino Full Power"
    else:
        return "Não definido"

# Função para classificar o tipo de treino
def classificar_tipo_treino(biotipo):
    if "Endomorfo" in biotipo:
        return "HIIT ou Cardio"
    elif "Ectomorfo" in biotipo:
        return "Peso Livre"
    elif "Mesomorfo" in biotipo:
        return "Funcional ou Maquinário"
    else:
        return "Tipo de treino não definido"

# Layout do Streamlit
st.title("Personal Trainer IA")
st.write("Preencha os dados abaixo para obter uma recomendação de treino personalizada.")

# Campos de entrada
altura = st.number_input("Sua altura (cm):", min_value=100, max_value=250, value=170)
peso = st.number_input("Seu peso (kg):", min_value=30, max_value=200, value=70)
caracteristicas = st.text_input("Características do corpo (Ex: alta com barriga e braços largos):")
dias_disponiveis = st.selectbox("Dias disponíveis para treino:", ["1 dia", "2 dias", "3 dias", "4 dias", "5 dias", "6 dias"])

# Botão de confirmação
if st.button("Confirmar"):
    biotipo = classificar_biotipo(altura, peso, caracteristicas)
    treino = classificar_treino(dias_disponiveis)
    tipo_treino = classificar_tipo_treino(biotipo)

    st.write(f"Seu biotipo corporal é: {biotipo}")
    st.write(f"Tipo de treino recomendado: {treino}")
    st.write(f"Tipo de treino adicional recomendado: {tipo_treino}")
