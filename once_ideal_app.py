
import streamlit as st

# Once ideal real (según Transfermarkt)
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

# Lista de posibles jugadores para desplegar (puedes ampliarla)
opciones_jugadores = sorted([
    "Kobel", "Courtois", "Alisson",
    "Saliba", "Rüdiger", "Van Dijk", "Bastoni",
    "Guardiol", "Davies",
    "Alexander", "Hakimi",
    "Rodri", "Valverde", "Modric", "De Bruyne", "Tchouameni",
    "Bellingham", "Pedri",
    "Vinicius", "Mbappé", "Martinelli",
    "Yamal", "Messi", "Saka",
    "Haaland", "Lewandowski", "Kane"
])

st.set_page_config(page_title="Once Ideal", layout="centered")
st.title("⚽ ¿Puedes adivinar el Once Ideal más valioso según Transfermarkt?")

st.markdown("Selecciona un jugador para cada posición y presiona **Verificar** para ver cuántos aciertos logras.")

# Formulario con selectboxes
respuestas = {}
with st.form("form_once"):
    for posicion in once_ideal:
        respuestas[posicion] = st.selectbox(f"{posicion}:", opciones_jugadores, key=posicion)
    submit = st.form_submit_button("Verificar")

# Verificación
if submit:
    aciertos = 0
    st.subheader("✅ Resultados")
    for posicion, correcto in once_ideal.items():
        elegido = respuestas[posicion]
        if elegido == correcto:
            st.success(f"{posicion}: ¡Correcto! ✅ ({elegido})")
            aciertos += 1
        else:
            st.error(f"{posicion}: ❌ Era **{correcto}**, tú seleccionaste: {elegido}")
    st.markdown(f"### 🎯 Tuviste **{aciertos} de 11 aciertos**")
