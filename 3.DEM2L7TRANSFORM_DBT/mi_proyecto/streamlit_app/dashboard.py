import sys
import os

# ---------------------------
# Agregar la carpeta raíz al PYTHONPATH
# ---------------------------
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(ROOT_DIR)

# Ahora sí podemos importar tus módulos ETL
from etl.extract import get_engine
import pandas as pd
import streamlit as st

# ---------- Conexión al warehouse ----------
engine = get_engine()

st.set_page_config(page_title="Ecommerce Dashboard", layout="wide")
st.title("📊 Ecommerce Analytics Dashboard")

# ---------- 1️⃣ Productos más vendidos por categoría ----------
st.header("1️⃣ Productos más vendidos por categoría (últimos 6 meses)")
query_1 = """
SELECT p.categoria, p.nombre_producto, SUM(d.cantidad) AS total_vendido
FROM fact_detalle_ordenes d
JOIN dim_productos p ON d.producto_id = p.producto_id
WHERE d.fecha_orden >= DATEADD(MONTH, -6, GETDATE())
GROUP BY p.categoria, p.nombre_producto
ORDER BY p.categoria, total_vendido DESC
"""
df_prod_vendidos = pd.read_sql(query_1, engine)
st.dataframe(df_prod_vendidos)
st.bar_chart(df_prod_vendidos.groupby('categoria')['total_vendido'].sum())

# ---------- 2️⃣ Clientes top y gasto promedio ----------
st.header("2️⃣ Clientes con más compras y gasto promedio")
query_2 = """
SELECT u.cliente_id, u.nombre_usuario, COUNT(o.orden_id) AS total_compras,
       AVG(o.total_orden) AS gasto_promedio
FROM fact_ordenes o
JOIN dim_usuarios u ON o.cliente_id = u.cliente_id
GROUP BY u.cliente_id, u.nombre_usuario
ORDER BY total_compras DESC
"""
df_clientes = pd.read_sql(query_2, engine)
st.dataframe(df_clientes.head(10))

# ---------- 3️⃣ Clientes recurrentes vs nuevos ----------
st.header("3️⃣ Clientes recurrentes vs nuevos por mes")
query_3 = """
WITH ordenes_cliente AS (
    SELECT cliente_id, MIN(fecha_orden) AS primer_orden, fecha_orden
    FROM fact_ordenes
    GROUP BY cliente_id, fecha_orden
)
SELECT YEAR(fecha_orden) AS año, MONTH(fecha_orden) AS mes,
       SUM(CASE WHEN fecha_orden = primer_orden THEN 1 ELSE 0 END) AS nuevos,
       SUM(CASE WHEN fecha_orden > primer_orden THEN 1 ELSE 0 END) AS recurrentes
FROM ordenes_cliente
GROUP BY YEAR(fecha_orden), MONTH(fecha_orden)
ORDER BY año, mes
"""
df_clientes_rec = pd.read_sql(query_3, engine)
st.line_chart(df_clientes_rec.set_index(['año','mes']))

# ---------- 4️⃣ Productos mayor y menor rotación ----------
st.header("4️⃣ Productos con mayor y menor rotación")
query_4 = """
SELECT p.nombre_producto, SUM(d.cantidad) AS total_vendido
FROM fact_detalle_ordenes d
JOIN dim_productos p ON d.producto_id = p.producto_id
GROUP BY p.nombre_producto
ORDER BY total_vendido DESC
"""
df_rotacion = pd.read_sql(query_4, engine)
st.dataframe(df_rotacion.head(10))  # mayor rotación
st.dataframe(df_rotacion.tail(10))  # menor rotación

# ---------- 5️⃣ Regiones con más demoras ----------
st.header("5️⃣ Regiones con mayor demora en entrega")
query_5 = """
SELECT u.region, AVG(DATEDIFF(DAY, o.fecha_envio, o.fecha_entrega)) AS dias_entrega
FROM fact_ordenes o
JOIN dim_usuarios u ON o.cliente_id = u.cliente_id
GROUP BY u.region
ORDER BY dias_entrega DESC
"""
df_demoras = pd.read_sql(query_5, engine)
st.bar_chart(df_demoras.set_index('region'))

# ---------- 6️⃣ Campañas con mayor impacto ----------
st.header("6️⃣ Campañas de marketing más efectivas")
query_6 = """
SELECT c.campaña, SUM(o.total_orden) AS ventas
FROM fact_ordenes o
JOIN dim_campañas c ON o.campaña_id = c.campaña_id
GROUP BY c.campaña
ORDER BY ventas DESC
"""
try:
    df_campañas = pd.read_sql(query_6, engine)
    st.bar_chart(df_campañas.set_index('campaña'))
except:
    st.info("No hay datos de campañas configuradas.")

# ---------- 7️⃣ Ticket promedio por canal ----------
st.header("7️⃣ Ticket promedio por canal de venta")
query_7 = """
SELECT canal_venta, AVG(total_orden) AS ticket_promedio
FROM fact_ordenes
GROUP BY canal_venta
"""
df_ticket = pd.read_sql(query_7, engine)
st.bar_chart(df_ticket.set_index('canal_venta'))

# ---------- 8️⃣ Evolución mensual ingreso bruto ----------
st.header("8️⃣ Evolución mensual del ingreso bruto")
query_8 = """
SELECT YEAR(fecha_orden) AS año, MONTH(fecha_orden) AS mes, SUM(total_orden) AS ingreso
FROM fact_ordenes
GROUP BY YEAR(fecha_orden), MONTH(fecha_orden)
ORDER BY año, mes
"""
df_ingreso = pd.read_sql(query_8, engine)
st.line_chart(df_ingreso.set_index(['año','mes']))

# ---------- 9️⃣ Categorías con mayor margen ----------
st.header("9️⃣ Categorías con mayor margen de ganancia")
query_9 = """
SELECT p.categoria, SUM((d.precio_unitario - p.costo_unitario) * d.cantidad) AS margen
FROM fact_detalle_ordenes d
JOIN dim_productos p ON d.producto_id = p.producto_id
GROUP BY p.categoria
ORDER BY margen DESC
"""
df_margen = pd.read_sql(query_9, engine)
st.bar_chart(df_margen.set_index('categoria'))

# ---------- 🔟 Provincias con más clientes ----------
st.header("🔟 Provincias con más clientes")
query_10 = """
SELECT provincia, COUNT(cliente_id) AS total_clientes
FROM dim_usuarios
GROUP BY provincia
ORDER BY total_clientes DESC
"""
df_provincias = pd.read_sql(query_10, engine)
st.bar_chart(df_provincias.set_index('provincia'))