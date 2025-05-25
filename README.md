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

Cualquier persona que quiera aprender jugando.# 🎮 Alma Gemela Virtual - Juego de Emparejamiento con IA

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python&logoColor=white)](#)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](#)

<div align="center">
  <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcG9uZ2FjY2VtYW5pY2NpZ2VvYjJtY3VrMWw1Y2VjZ2VtZ3B5dCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o7TKrQlfBvV6Xgd2w/giphy.gif" width="300">
</div>

## 🌟 Características Principales

- **Tecnología de punta**: Utiliza algoritmos de aprendizaje no supervisado (K-Means) para encontrar patrones ocultos en los datos.
- **Interfaz intuitiva**: Diseño amigable y fácil de usar con Streamlit.
- **Personalizable**: Configura el número de jugadores (de 2 a 26, siempre pares).
- **Visualización interactiva**: Gráficos que muestran cómo se agrupan los participantes.
- **Explicaciones detalladas**: Descubre por qué se formaron las parejas basado en sus similitudes.

## 🚀 Cómo Funciona

1. **Configuración**: Elige cuántas personas participarán.
2. **Recolección de datos**: Cada jugador responde preguntas sobre sus preferencias.
3. **Análisis IA**: Nuestro sistema agrupa a los participantes usando K-Means.
4. **Resultados**: Descubre tu "alma gemela virtual" y por qué hicieron match.

## 🛠️ Requisitos Técnicos

- Python 3.8 o superior
- Bibliotecas principales:
  - Streamlit
  - Scikit-learn
  - Pandas
  - NumPy
  - Matplotlib

## 🚀 Instalación

1. Clona el repositorio:
   ```bash
   git clone [https://github.com/tuusuario/alma-gemela-virtual.git](https://github.com/tuusuario/alma-gemela-virtual.git)
   cd alma-gemela-virtual
2. Crea y activa un entorno virtual (recomendado):
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    ```
    O en Windows:
    ```bash
    .venv\Scripts\activate
    ```
3. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```
4. Ejecuta la aplicación:
    ```bash
    streamlit run app.py
    ```

## 🎯 Aprendizaje No Supervisado en Acción
Este proyecto demuestra cómo el aprendizaje no supervisado puede descubrir patrones ocultos en datos no etiquetados. El algoritmo K-Means agrupa a los participantes basándose en sus respuestas, permitiendo emparejamientos basados en similitudes reales.

## 📊 Métricas Clave
- Precisión del agrupamiento: Mide cuán similares son los miembros dentro de cada grupo.
- Distancia entre clusters: Evalúa qué tan diferentes son los grupos entre sí.
- Coeficiente de silueta: Calidad general de los clusters formados.

## 🌈 Posibles Mejoras
- [ ] Añadir más preguntas personalizables
- [ ] Integrar con redes sociales
- [ ] Guardar resultados históricos
- [ ] Añadir modo competencia
- [ ] Versión multijugador en tiempo real