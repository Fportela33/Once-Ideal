import streamlit as st

# Diccionario del once ideal
once_ideal = {
    "Portero": "Kobel",
    "Defensa Central 1": "Saliba",
    "Defensa Central 2": "Bastoni",
    "Lateral Izquierdo": "Guardiol",
    "Lateral Derecho": "Alexander",
    "Mediocampista 1": "Rodri",
    "Mediocampista 2": "Valverde",
    "Mediocampista 3": "Bellingham",
    "Extremo Izquierdo": "Vinicius",
    "Extremo Derecho": "Yamal",
    "Delantero Centro": "Haaland"
}

st.set_page_config(page_title="Once Ideal", layout="centered")
st.title("⚽ ¿Puedes adivinar el Once Ideal?")

st.markdown("Escribe el nombre de cada jugador según su posición. Al final, presiona **Verificar**.")

# Crear campos de entrada
respuestas = {}
with st.form("form_once"):
    for posicion in once_ideal:
        respuestas[posicion] = st.text_input(posicion)
    submit = st.form_submit_button("Verificar")

# Verificar respuestas
if submit:
    aciertos = 0
    st.subheader("✅ Resultados")
    for posicion, nombre_correcto in once_ideal.items():
        respuesta = respuestas[posicion].strip()
        if respuesta.lower() == nombre_correcto.lower():
            st.success(f"{posicion}: ¡Correcto! ✅")
            aciertos += 1
        else:
            st.error(f"{posicion}: ❌ Era **{nombre_correcto}**, tú escribiste: {respuesta}")
    st.markdown(f"### 🎯 Tuviste **{aciertos} de 11 aciertos**")

