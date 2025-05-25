import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

st.set_page_config(page_title="Juego de Emparejamiento", layout="wide")

st.title("🎮 ¡Encuentra tu Alma Gemela Virtual!")
st.write("""💜 ¡Bienvenido al juego más divertido de emparejamiento! 💜
Reuniremos a varias personas y usaremos magia tecnológica ✨ (bueno, Inteligencia Artificial 🤖) 
para encontrar las parejas más compatibles. ¿Quién será tu alma gemela virtual? 🧐‍✨""")

# Estado inicial
if 'num_players' not in st.session_state:
    st.session_state.num_players = 0
    st.session_state.current_person = 0
    st.session_state.data = []
    st.session_state.analysis_complete = False
    st.session_state.setup_complete = False

# Configuración del juego
if not st.session_state.setup_complete:
    st.subheader("🎮 Configuración del Juego")
    num_players = st.number_input("👥 ¿Cuántas personas van a jugar?",
                                  min_value=2, max_value=26, value=10, step=2)

    if st.button("✨ ¡Comenzar el Juego!"):
        if num_players % 2 == 0:
            st.session_state.num_players = num_players
            st.session_state.setup_complete = True
            st.rerun()

        else:
            st.error("❌ El número debe ser par para emparejar.")

# Formulario de ingreso de datos
if st.session_state.setup_complete and st.session_state.current_person < st.session_state.num_players and not st.session_state.analysis_complete:
    st.subheader(f"🧐 Jugador {st.session_state.current_person + 1} de {st.session_state.num_players}")
    progress = st.progress(st.session_state.current_person / st.session_state.num_players)

    with st.form(key=f"person_{st.session_state.current_person}"):
        nombre = st.text_input("Tu nombre o apodo")
        gusto_aventura = st.slider("¿Qué tanto te gustan las aventuras? 🎢", 1, 10, 5)
        nivel_creatividad = st.slider("¿Qué tan creativ@ te consideras? 🎨", 1, 10, 5)
        comida_picante = st.slider("¿Cuánto te gusta la comida picante? 🌶️", 1, 10, 5)
        musica_diaria = st.slider("¿Cuántas horas de música escuchas al día? 🎵", 0, 12, 3)
        mascota_ideal = st.selectbox("Mascota ideal", ["🐶 Perro", "😺 Gato", "🦜 Pájaro", "🐠 Pez", "🦎 Reptil"])
        clima_favorito = st.selectbox("Clima favorito", ["☀️ Soleado", "🌧️ Lluvioso", "⛅ Nublado", "❄️ Nevado"])
        hora_despertar = st.slider("¿A qué hora prefieres despertar? 🌅", 5, 12, 7)
        tipo_pelicula = st.selectbox("Género de película favorito", ["🎭 Drama", "😂 Comedia", "🦸 Acción", "👻 Terror", "❤️ Romance"])

        submitted = st.form_submit_button("Siguiente persona")
        if submitted:
            if not nombre.strip():
                st.error("Por favor ingresa un nombre o apodo.")
            else:
                st.session_state.data.append({
                    'nombre': nombre.strip(),
                    'gusto_aventura': gusto_aventura,
                    'nivel_creatividad': nivel_creatividad,
                    'comida_picante': comida_picante,
                    'musica_diaria': musica_diaria,
                    'mascota_ideal': mascota_ideal,
                    'clima_favorito': clima_favorito,
                    'hora_despertar': hora_despertar,
                    'tipo_pelicula': tipo_pelicula
                })
                st.session_state.current_person += 1
                st.rerun()


# Análisis de compatibilidad
if st.session_state.current_person == st.session_state.num_players and not st.session_state.analysis_complete:
    if not st.session_state.data or 'mascota_ideal' not in st.session_state.data[0]:
        st.warning("⚠️ No hay suficientes datos para realizar el análisis. Asegúrate de haber ingresado todos los jugadores.")
    else:
        st.subheader("✨ ¡Hora de la magia! 🤖")
        
        df = pd.DataFrame(st.session_state.data)

        # Mapeos para convertir variables categóricas a numéricas
        mascota_map = {"🐶 Perro": 0, "😺 Gato": 1, "🦜 Pájaro": 2, "🐠 Pez": 3, "🦎 Reptil": 4}
        clima_map = {"☀️ Soleado": 0, "🌧️ Lluvioso": 1, "⛅ Nublado": 2, "❄️ Nevado": 3}
        pelicula_map = {"🎭 Drama": 0, "😂 Comedia": 1, "🦸 Acción": 2, "👻 Terror": 3, "❤️ Romance": 4}

        df['mascota_num'] = df['mascota_ideal'].map(mascota_map)
        df['clima_num'] = df['clima_favorito'].map(clima_map)
        df['pelicula_num'] = df['tipo_pelicula'].map(pelicula_map)

        features = [
            'gusto_aventura', 'nivel_creatividad', 'comida_picante', 'musica_diaria', 'hora_despertar',
            'mascota_num', 'clima_num', 'pelicula_num'
        ]
        X = df[features]

        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)

        n_clusters = st.session_state.num_players // 2
        kmeans = KMeans(n_clusters=n_clusters, random_state=42)
        df['cluster'] = kmeans.fit_predict(X_scaled)

        # Emparejamiento
        parejas = []
        disponibles = set(range(st.session_state.num_players))

        while len(disponibles) >= 2:
            p1 = disponibles.pop()
            mejor_pareja = None
            mejor_distancia = float('inf')

            for p2 in disponibles:
                if df.iloc[p1]['cluster'] == df.iloc[p2]['cluster']:
                    dist = np.linalg.norm(X_scaled[p1] - X_scaled[p2])
                    if dist < mejor_distancia:
                        mejor_distancia = dist
                        mejor_pareja = p2

            if mejor_pareja is not None:
                disponibles.remove(mejor_pareja)
                parejas.append((p1, mejor_pareja))
            else:
                # En caso de que no encuentre en mismo cluster, empareja por menor distancia en general
                for p2 in disponibles:
                    dist = np.linalg.norm(X_scaled[p1] - X_scaled[p2])
                    if dist < mejor_distancia:
                        mejor_distancia = dist
                        mejor_pareja = p2
                if mejor_pareja:
                    disponibles.remove(mejor_pareja)
                    parejas.append((p1, mejor_pareja))

        # Mostrar parejas con explicación detallada
        # Cambia esta parte justo donde muestras las parejas

        st.subheader("💜 ¡Las Almas Gemelas Virtuales son... 💜")
        for i, (p1, p2) in enumerate(parejas, 1):
            nombre1 = df.iloc[p1]['nombre']
            nombre2 = df.iloc[p2]['nombre']
            st.write(f"**Pareja {i}:** {nombre1} ❤️ {nombre2}")

            distancia = np.linalg.norm(X_scaled[p1] - X_scaled[p2])

            if distancia < 2.5:  # Umbral de similitud alta
                st.markdown("**¿Por qué se eligieron como pareja?**")
                st.write("Ambos están en el mismo grupo de compatibilidad según sus respuestas.")
                st.write("Sus gustos y hábitos son muy similares, lo que hace que sean compatibles. Por ejemplo:")

                def mostrar_dif(campo, etiqueta, emoji=None):
                    val1 = df.iloc[p1][campo]
                    val2 = df.iloc[p2][campo]
                    if isinstance(val1, (int, float)) and isinstance(val2, (int, float)):
                        st.write(f"{etiqueta}: {val1} vs {val2}")
                    else:
                        st.write(f"{etiqueta}: {val1} y {val2}")

                mostrar_dif('gusto_aventura', "Aventura")
                mostrar_dif('nivel_creatividad', "Creatividad")
                mostrar_dif('comida_picante', "Gusto por comida picante")
                mostrar_dif('musica_diaria', "Horas escuchando música")
                mostrar_dif('mascota_ideal', "Mascota favorita")
                mostrar_dif('clima_favorito', "Clima favorito")
                mostrar_dif('hora_despertar', "Hora para despertar")
                mostrar_dif('tipo_pelicula', "Género de película favorito")

                comentarios = [
                    "💖 ¡Son el match perfecto!",
                    "✨ ¡Las estrellas los han unido!",
                    "🌈 ¡El destino ha hablado!",
                    "🤩 ¡Qué pareja más increíble!",
                    "💜 ¡La IA cupido ha acertado!"
                ]
                st.write(f"🔮 {np.random.choice(comentarios)}")
            else:
                st.write("🤔 Aunque están emparejados por cercanía, no son tan parecidos. ¡Tal vez los opuestos se atraen!")


        # Visualización del clustering
        fig, ax = plt.subplots(figsize=(8, 6))
        scatter = ax.scatter(X_scaled[:, 0], X_scaled[:, 1], c=df['cluster'], cmap='viridis')
        ax.set_title("Visualización de Clustering (2D)")
        ax.set_xlabel("Componente 1 (escalada)")
        ax.set_ylabel("Componente 2 (escalada)")
        st.pyplot(fig)

        st.session_state.analysis_complete = True

# Reinicio
if st.session_state.analysis_complete:
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔄 Jugar de nuevo"):
            st.session_state.current_person = 0
            st.session_state.data = []
            st.session_state.analysis_complete = False
            st.rerun()

    with col2:
        if st.button("🛠️ Nuevo juego"):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()

