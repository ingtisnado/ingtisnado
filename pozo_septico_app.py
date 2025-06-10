
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Cálculo Pozo Séptico", layout="centered")

st.title("🧱 Cálculo de Pozo Séptico")
st.markdown("Esta aplicación calcula el volumen y dimensiones de un pozo séptico basado en entradas básicas de diseño.")

# Entradas del usuario
personas = st.number_input("Número de Personas", min_value=1, value=5)
consumo = st.number_input("Consumo Diario por Persona (L)", min_value=50, value=150)
retencion = st.number_input("Tiempo de Retención (días)", min_value=1.0, value=2.0)
profundidad = st.number_input("Profundidad del Tanque (m)", min_value=1.0, value=1.5)
infiltracion = st.number_input("Tasa de Infiltración (L/m²/día)", min_value=10.0, value=30.0)

# Cálculos
vol_litros = personas * consumo * retencion
vol_m3 = vol_litros / 1000
area_tanque = vol_m3 / profundidad
lado_tanque = np.sqrt(area_tanque)
area_infiltracion = (personas * consumo) / infiltracion

# Mostrar resultados
st.subheader("📊 Resultados")
st.write(f"**Volumen Total Requerido:** {vol_litros:.1f} litros ({vol_m3:.2f} m³)")
st.write(f"**Área del Tanque:** {area_tanque:.2f} m²")
st.write(f"**Lado Estimado del Tanque (cuadrado):** {lado_tanque:.2f} m")
st.write(f"**Área Campo de Infiltración:** {area_infiltracion:.2f} m²")

# Gráfico ilustrativo
st.subheader("📈 Ilustración del Tanque")
fig, ax = plt.subplots()
ax.set_aspect('equal')
rectangle = plt.Rectangle((0, 0), lado_tanque, profundidad, fill=None, edgecolor='blue', linewidth=2)
ax.add_patch(rectangle)
plt.xlim(0, max(2, lado_tanque + 0.5))
plt.ylim(0, max(2, profundidad + 0.5))
plt.title("Vista Lateral del Pozo Séptico")
plt.xlabel("Lado (m)")
plt.ylabel("Profundidad (m)")
st.pyplot(fig)

st.markdown("---")
st.markdown("Desarrollado con ❤️ por DeepSeek para cálculos sanitarios.")
