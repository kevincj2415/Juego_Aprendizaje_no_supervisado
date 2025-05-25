🎮 Juego de Emparejamiento con IA
💡 ¿Qué es esto?
Este es un juego interactivo de emparejamiento desarrollado con Streamlit, que utiliza técnicas de aprendizaje no supervisado para encontrar las parejas más compatibles entre un grupo de personas. Ideal para clases, demostraciones o simplemente para divertirse aprendiendo sobre inteligencia artificial.

🧠 ¿Qué es el Aprendizaje No Supervisado?
El aprendizaje no supervisado es una rama del aprendizaje automático donde el modelo no recibe etiquetas ni respuestas correctas. En cambio, intenta descubrir patrones o estructuras ocultas en los datos por sí mismo. Uno de los métodos más comunes es el clustering (agrupamiento), como el algoritmo K-Means, que se usa en este juego.

🧪 ¿Qué hace este programa?
Recoge respuestas de varias personas sobre gustos y hábitos.

Convierte esas respuestas a valores numéricos y las normaliza.

Aplica K-Means Clustering para agrupar personas según similitud.

Empareja a las personas más similares dentro del mismo grupo.

Muestra los resultados de forma visual y explica por qué fueron emparejados (si son lo suficientemente compatibles).

🧭 ¿Por qué es una herramienta educativa?
Este juego:

📊 Muestra en la práctica cómo se pueden agrupar datos similares sin etiquetas previas.

🤖 Utiliza un algoritmo real de IA para tomar decisiones.

🔍 Visualiza los grupos en un gráfico interactivo (scatter plot).

💬 Explica los emparejamientos según las similitudes reales en los datos.

🧠 Sirve como introducción divertida y comprensible a conceptos como:

Vectores de características

Escalamiento de datos

Agrupamiento por proximidad

Interpretación de distancia en espacios multidimensionales

🚀 ¿Cómo usarlo?
Instala las dependencias:

bash
Copiar
Editar
pip install streamlit scikit-learn pandas matplotlib
Ejecuta la app:

bash
Copiar
Editar
streamlit run app.py
Ingresa los datos de varios jugadores y deja que la IA haga su magia.

🧩 Tecnologías usadas
Python 🐍

Streamlit 🎈

Scikit-Learn 🤖

Pandas 📊

Matplotlib 📉

🎓 Ideal para:
Profesores que enseñan IA o ciencia de datos.

Estudiantes que quieren ver cómo funciona el clustering.

Cualquier persona que quiera aprender jugando.