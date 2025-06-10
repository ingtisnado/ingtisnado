
"""
===========================================================
          CÁLCULO SUPER DETALLADO DE POZO SÉPTICO
===========================================================

Este script realiza un cálculo completo y detallado para el diseño
hidráulico de un pozo séptico doméstico, incluyendo:

✔ Cálculo de volumen útil
✔ Diseño geométrico del tanque
✔ Campo de infiltración
✔ Costos estimados
✔ Mantenimiento
✔ Visualización gráfica

Basado en recomendaciones de la OMS, normas técnicas locales y prácticas comunes
de ingeniería sanitaria.
"""

import math
import matplotlib.pyplot as plt

# ----------------------
# PARÁMETROS DE ENTRADA
# ----------------------
personas = 5                             # Cantidad de habitantes
consumo_diario = 150                     # L/persona/día (OMS: 100-200 L)
tiempo_retencion = 2                    # Días (mínimo recomendado: 1.5-2 días)
profundidad_tanque = 1.5                 # m
tasa_infiltracion = 30                   # L/m²/día (suelos arenosos)

# ----------------------
# CÁLCULOS HIDRÁULICOS
# ----------------------
volumen_diario = personas * consumo_diario
volumen_total_litros = volumen_diario * tiempo_retencion
volumen_total_m3 = volumen_total_litros / 1000

# ----------------------
# DISEÑO DEL TANQUE
# ----------------------
area_tanque_m2 = volumen_total_m3 / profundidad_tanque
lado_tanque_m = math.sqrt(area_tanque_m2)
volumen_con_margen = volumen_total_m3 * 1.2  # +20% por lodos

# ----------------------
# CAMPO DE INFILTRACIÓN
# ----------------------
area_infiltracion_m2 = volumen_diario / tasa_infiltracion
longitud_tuberia = area_infiltracion_m2 / 0.6  # 0.6m de ancho de zanja
zanjas_necesarias = math.ceil(longitud_tuberia / 10)

# ----------------------
# COSTOS ESTIMADOS
# ----------------------
costo_excavacion_m3 = 25
costo_materiales_m2 = 120
costo_total = costo_excavacion_m3 * volumen_total_m3 + costo_materiales_m2 * area_tanque_m2

# ----------------------
# MANTENIMIENTO
# ----------------------
frecuencia_limpieza = 2
lodos_anuales_m3 = personas * 0.04
costo_limpieza = 80
costo_anual_operacion = costo_limpieza / frecuencia_limpieza

# ----------------------
# RESULTADOS
# ----------------------
print("\n=== CÁLCULO DETALLADO DE POZO SÉPTICO ===\n")
print(f"🔹 Número de Personas: {personas}")
print(f"🔹 Consumo Diario Total: {volumen_diario} L/día")
print(f"🔹 Volumen Total Requerido: {volumen_total_litros} L ({volumen_total_m3:.2f} m³)")
print(f"🔹 Área del Tanque: {area_tanque_m2:.2f} m²")
print(f"🔹 Lado del Tanque: {lado_tanque_m:.2f} m (cuadrado)")
print(f"🔹 Volumen con margen: {volumen_con_margen:.2f} m³")
print(f"🔹 Área Campo Infiltración: {area_infiltracion_m2:.2f} m²")
print(f"🔹 Longitud Total de Tubería: {longitud_tuberia:.2f} m")
print(f"🔹 Zanjas necesarias de 10m: {zanjas_necesarias}")
print(f"🔹 Costo estimado total: ${costo_total:.2f}")
print(f"🔹 Costo anual de operación: ${costo_anual_operacion:.2f}")

# ----------------------
# VISUALIZACIÓN DEL TANQUE
# ----------------------
plt.figure(figsize=(6, 4))
plt.gca().set_aspect('equal')
plt.title("Vista Lateral del Tanque Séptico")
plt.xlabel("Lado (m)")
plt.ylabel("Profundidad (m)")
plt.xlim(0, lado_tanque_m + 0.5)
plt.ylim(0, profundidad_tanque + 0.5)
plt.grid(True)

rect = plt.Rectangle((0, 0), lado_tanque_m, profundidad_tanque, fill=None, edgecolor='blue', linewidth=2)
plt.gca().add_patch(rect)
plt.text(lado_tanque_m/2 - 0.4, profundidad_tanque/2, f"{volumen_total_m3:.1f} m³", fontsize=10)

plt.tight_layout()
plt.show()
