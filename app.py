import streamlit as st
import pandas as pd
import sqlite3
import math
import matplotlib.pyplot as plt

# =====================================================
# CONFIGURACION
# =====================================================

st.set_page_config(
    page_title="Sistema Energético Inteligente",
    page_icon="⚡",
    layout="wide"
)

# =====================================================
# ESTILOS
# =====================================================

st.markdown("""

<style>

.main {
    background-color: #0E1117;
}

h1, h2, h3 {
    color: #00D4FF;
}

.stMetric {
    background-color: #1C1F26;
    padding: 15px;
    border-radius: 15px;
}

</style>

""", unsafe_allow_html=True)

# =====================================================
# BASE DE DATOS
# =====================================================

conexion = sqlite3.connect(
    "energia.db",
    check_same_thread=False
)

cursor = conexion.cursor()

cursor.execute("""

CREATE TABLE IF NOT EXISTS encuestas(

id INTEGER PRIMARY KEY AUTOINCREMENT,

torre TEXT,
habitacion TEXT,

aire TEXT,
cantidad_aires INTEGER,
tipo_aire TEXT,
btu_aire TEXT,
voltaje_aire TEXT,
horas_aire REAL,

ventiladores INTEGER,
horas_vent REAL,

refrigerador TEXT,
potencia_refri REAL,
voltaje_refri TEXT,
corriente_refri REAL,
horas_refri REAL,

bombillos INTEGER,
tipo_iluminacion TEXT,
potencia_bombillos REAL,
horas_bombillos REAL,

tv TEXT,
horas_tv REAL,

lavadora TEXT,
horas_lavadora REAL,

microondas TEXT,
horas_micro REAL,

pc TEXT,
horas_pc REAL,

consumo_percibido TEXT,
problemas TEXT,

potencia REAL,
corriente REAL,
energia REAL,

joule REAL,
campo REAL,
densidad REAL,

factor_potencia REAL,
caida_voltaje REAL,
eficiencia TEXT,

riesgo TEXT

)

""")

conexion.commit()

# =====================================================
# TITULO
# =====================================================

st.title("⚡ Sistema Inteligente de Análisis Energético")

st.markdown("---")

# =====================================================
# COLUMNAS
# =====================================================

col1, col2 = st.columns(2)

# =====================================================
# COLUMNA 1
# =====================================================

with col1:

    st.subheader("🏢 Información General")

    torre = st.selectbox(
        "Torre",
        [
            "Torre A",
            "Torre B",
            "Torre C",
            "Torre D"
        ]
    )

    habitacion = st.selectbox(
        "¿Habita permanentemente?",
        [
            "Sí",
            "No"
        ]
    )

    st.subheader("❄ Aire Acondicionado")

    aire = st.selectbox(
        "¿Tiene aire acondicionado?",
        [
            "Sí",
            "No"
        ]
    )

    cantidad_aires = st.number_input(
        "Cantidad de aires",
        min_value=0,
        max_value=20,
        value=1
    )

    tipo_aire = st.selectbox(
        "Tipo de aire",
        [
            "Mini Split",
            "Ventana",
            "Inverter",
            "Portátil"
        ]
    )

    btu_aire = st.selectbox(
        "BTU del aire",
        [
            "9000",
            "12000",
            "18000",
            "24000"
        ]
    )

    voltaje_aire = st.selectbox(
        "Voltaje aire",
        [
            "110",
            "220"
        ]
    )

    horas_aire = st.slider(
        "Horas uso aire",
        0,
        24,
        8
    )

    st.subheader("🌀 Ventiladores")

    ventiladores = st.number_input(
        "Cantidad ventiladores",
        min_value=0,
        max_value=20,
        value=1
    )

    horas_vent = st.slider(
        "Horas ventiladores",
        0,
        24,
        6
    )

# =====================================================
# COLUMNA 2
# =====================================================

with col2:

    st.subheader("🧊 Refrigerador")

    refrigerador = st.selectbox(
        "¿Tiene refrigerador?",
        [
            "Sí",
            "No"
        ]
    )

    potencia_refri = st.number_input(
        "Potencia refrigerador (W)",
        min_value=0.0,
        value=180.0
    )

    voltaje_refri = st.selectbox(
        "Voltaje refrigerador",
        [
            "110",
            "220"
        ]
    )

    corriente_refri = st.number_input(
        "Corriente refrigerador (A)",
        min_value=0.0,
        value=1.8
    )

    horas_refri = st.slider(
        "Horas refrigerador",
        0,
        24,
        24
    )

    st.subheader("💡 Iluminación")

    bombillos = st.number_input(
        "Cantidad bombillos",
        min_value=0,
        max_value=50,
        value=4
    )

    tipo_iluminacion = st.selectbox(
        "Tipo iluminación",
        [
            "LED",
            "Ahorrador",
            "Incandescente"
        ]
    )

    potencia_bombillos = st.number_input(
        "Potencia bombillos (W)",
        min_value=0.0,
        value=15.0
    )

    horas_bombillos = st.slider(
        "Horas bombillos",
        0,
        24,
        6
    )

    st.subheader("📺 Otros Equipos")

    tv = st.selectbox(
        "¿Tiene TV?",
        [
            "Sí",
            "No"
        ]
    )

    horas_tv = st.slider(
        "Horas TV",
        0,
        24,
        4
    )

    lavadora = st.selectbox(
        "¿Tiene lavadora?",
        [
            "Sí",
            "No"
        ]
    )

    horas_lavadora = st.slider(
        "Horas lavadora",
        0,
        24,
        1
    )

    microondas = st.selectbox(
        "¿Tiene microondas?",
        [
            "Sí",
            "No"
        ]
    )

    horas_micro = st.slider(
        "Horas microondas",
        0,
        24,
        1
    )

    pc = st.selectbox(
        "¿Tiene computador?",
        [
            "Sí",
            "No"
        ]
    )

    horas_pc = st.slider(
        "Horas computador",
        0,
        24,
        5
    )

    st.subheader("📊 Comportamiento")

    consumo_percibido = st.selectbox(
        "Percepción consumo",
        [
            "Bajo",
            "Medio",
            "Alto"
        ]
    )

    problemas = st.selectbox(
        "Problemas eléctricos",
        [
            "No",
            "Sí, a veces",
            "Frecuentes"
        ]
    )

# =====================================================
# BOTON
# =====================================================

analizar = st.button("⚡ ANALIZAR")

# =====================================================
# ANALISIS
# =====================================================

if analizar:

    # =================================================
    # BTU Y POTENCIA
    # =================================================

    mapa_btu = {

        "9000": 800,
        "12000": 1200,
        "18000": 1800,
        "24000": 2500

    }

    potencia_base_aire = mapa_btu[btu_aire]

    # =================================================
    # EFICIENCIA AIRE
    # =================================================

    if tipo_aire == "Inverter":

        potencia_base_aire *= 0.70

    elif tipo_aire == "Mini Split":

        potencia_base_aire *= 0.85

    elif tipo_aire == "Ventana":

        potencia_base_aire *= 1.25

    elif tipo_aire == "Portátil":

        potencia_base_aire *= 1.15

    # =================================================
    # POTENCIAS
    # =================================================

    potencia_aires = (
        cantidad_aires
        * potencia_base_aire
        * (horas_aire / 24)
    )

    potencia_vent = (
        ventiladores
        * 80
        * (horas_vent / 24)
    )

    potencia_refrigerador = (
        (1 if refrigerador == "Sí" else 0)
        * potencia_refri
        * (horas_refri / 24)
        * 0.45
    )

    if tipo_iluminacion == "LED":

        eficiencia_luz = 1

    elif tipo_iluminacion == "Ahorrador":

        eficiencia_luz = 1.3

    else:

        eficiencia_luz = 4

    potencia_luces = (
        bombillos
        * potencia_bombillos
        * eficiencia_luz
        * (horas_bombillos / 24)
    )

    potencia_tv = (
        (1 if tv == "Sí" else 0)
        * 90
        * (horas_tv / 24)
    )

    potencia_lavadora = (
        (1 if lavadora == "Sí" else 0)
        * 500
        * (horas_lavadora / 24)
    )

    potencia_micro = (
        (1 if microondas == "Sí" else 0)
        * 800
        * (horas_micro / 24)
    )

    potencia_pc = (
        (1 if pc == "Sí" else 0)
        * 300
        * (horas_pc / 24)
    )

    # =================================================
    # POTENCIA TOTAL
    # =================================================

    potencia = (

        potencia_aires +
        potencia_vent +
        potencia_refrigerador +
        potencia_luces +
        potencia_tv +
        potencia_lavadora +
        potencia_micro +
        potencia_pc

    )

    # =================================================
    # FACTOR SIMULTANEIDAD
    # =================================================

    potencia *= 0.80

    # =================================================
    # FACTOR POTENCIA
    # =================================================

    factor_potencia = 0.92

    # =================================================
    # LEY DE OHM
    # =================================================

    voltaje = float(voltaje_aire)

    corriente = (
        potencia /
        (voltaje * factor_potencia)
    )

    # =================================================
    # ENERGIA
    # =================================================

    energia = (
        potencia * 30
    ) / 1000

    # =================================================
    # EFICIENCIA
    # =================================================

    if energia < 150:

        eficiencia = "ALTA"

    elif energia < 300:

        eficiencia = "MEDIA"

    else:

        eficiencia = "BAJA"

    # =================================================
    # EFECTO JOULE
    # =================================================

    resistencia = 0.15

    joule = (
        corriente ** 2
    ) * resistencia

    # =================================================
    # CAIDA DE VOLTAJE
    # =================================================

    resistencia_linea = 0.08

    caida_voltaje = (
        corriente *
        resistencia_linea
    )

    # =================================================
    # CAMPO MAGNETICO
    # =================================================

    mu0 = 4 * math.pi * (10 ** -7)

    distancia = 0.10

    campo = (
        mu0 * corriente
    ) / (
        2 * math.pi * distancia
    )

    # =================================================
    # DENSIDAD CORRIENTE
    # =================================================

    area_cable = 3.31e-6

    densidad = (
        corriente / area_cable
    )

    # =================================================
    # RIESGO
    # =================================================

    if corriente > 30:

        riesgo = "MUY ALTO"

    elif corriente > 20:

        riesgo = "ALTO"

    elif corriente > 10:

        riesgo = "MEDIO"

    else:

        riesgo = "BAJO"

    # =================================================
    # INSERTAR DATOS
    # =================================================

    cursor.execute("""

    INSERT INTO encuestas(

    torre,
    habitacion,

    aire,
    cantidad_aires,
    tipo_aire,
    btu_aire,
    voltaje_aire,
    horas_aire,

    ventiladores,
    horas_vent,

    refrigerador,
    potencia_refri,
    voltaje_refri,
    corriente_refri,
    horas_refri,

    bombillos,
    tipo_iluminacion,
    potencia_bombillos,
    horas_bombillos,

    tv,
    horas_tv,

    lavadora,
    horas_lavadora,

    microondas,
    horas_micro,

    pc,
    horas_pc,

    consumo_percibido,
    problemas,

    potencia,
    corriente,
    energia,

    joule,
    campo,
    densidad,

    factor_potencia,
    caida_voltaje,
    eficiencia,

    riesgo

    )

    VALUES(

?,?,?,?,?,?,?,?,?,?,
?,?,?,?,?,?,?,?,?,?,
?,?,?,?,?,?,?,?,?,?,
?,?,?,?,?,?,?,?,?

)

    """, (

        torre,
        habitacion,

        aire,
        cantidad_aires,
        tipo_aire,
        btu_aire,
        voltaje_aire,
        horas_aire,

        ventiladores,
        horas_vent,

        refrigerador,
        potencia_refri,
        voltaje_refri,
        corriente_refri,
        horas_refri,

        bombillos,
        tipo_iluminacion,
        potencia_bombillos,
        horas_bombillos,

        tv,
        horas_tv,

        lavadora,
        horas_lavadora,

        microondas,
        horas_micro,

        pc,
        horas_pc,

        consumo_percibido,
        problemas,

        potencia,
        corriente,
        energia,

        joule,
        campo,
        densidad,

        factor_potencia,
        caida_voltaje,
        eficiencia,

        riesgo

    ))

    conexion.commit()

    # =================================================
    # RESULTADOS
    # =================================================

    st.success("✅ Encuesta registrada")

    st.markdown("---")

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "⚡ Potencia Total",
        f"{potencia:.2f} W"
    )

    c2.metric(
        "🔌 Corriente",
        f"{corriente:.2f} A"
    )

    c3.metric(
        "⚠ Riesgo",
        riesgo
    )

    c4, c5, c6 = st.columns(3)

    c4.metric(
        "🔥 Efecto Joule",
        f"{joule:.2f} W"
    )

    c5.metric(
        "🧲 Campo Magnético",
        f"{campo:.10f} T"
    )

    c6.metric(
        "⚡ Energía Mensual",
        f"{energia:.2f} kWh"
    )

    c7, c8, c9 = st.columns(3)

    c7.metric(
        "⚡ Factor Potencia",
        f"{factor_potencia:.2f}"
    )

    c8.metric(
        "🔻 Caída Voltaje",
        f"{caida_voltaje:.2f} V"
    )

    c9.metric(
        "🏠 Eficiencia",
        eficiencia
    )

    # =================================================
    # GRAFICAS
    # =================================================

    st.markdown("---")

    st.subheader("📊 Distribución de Consumo")

    equipos = [
        "Aires",
        "Vent",
        "Refri",
        "Luces",
        "TV",
        "Lavadora",
        "Micro",
        "PC"
    ]

    consumos = [

        potencia_aires,
        potencia_vent,
        potencia_refrigerador,
        potencia_luces,
        potencia_tv,
        potencia_lavadora,
        potencia_micro,
        potencia_pc

    ]

    fig, ax = plt.subplots(figsize=(10,5))

    ax.bar(
        equipos,
        consumos
    )

    plt.xticks(rotation=20)

    st.pyplot(fig)

    # =================================================
    # GRAFICA CIRCULAR
    # =================================================

    fig2, ax2 = plt.subplots(figsize=(7,7))

    ax2.pie(
        consumos,
        labels=equipos,
        autopct='%1.1f%%'
    )

    st.pyplot(fig2)

# =====================================================
# HISTORIAL
# =====================================================

st.markdown("---")

st.subheader("📁 Historial")

datos = pd.read_sql_query(
    "SELECT * FROM encuestas",
    conexion
)

st.dataframe(datos)

# =====================================================
# EXPORTAR EXCEL
# =====================================================

if st.button("📥 GENERAR EXCEL"):

    datos.to_excel(
        "ReporteEnergetico.xlsx",
        index=False
    )

    st.success("✅ Excel generado")