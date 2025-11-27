import os
import streamlit as st
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt
import seaborn as sns
from etl.extract import get_engine

# -----------------------------------
# Configuración
# -----------------------------------
st.set_page_config(page_title="Dashboard de Ventas", layout="wide")
sns.set(style="whitegrid")
plt.rcParams['figure.figsize'] = (10,6)

# Carpeta donde se guardarán los gráficos
output_dir = "output_charts"
os.makedirs(output_dir, exist_ok=True)

# -----------------------------------
# Conexión a la base de datos
# -----------------------------------
try:
    engine = get_engine()
except Exception as e:
    st.error(f"Error al conectar a la base de datos: {e}")
    st.stop()

# -----------------------------------
# 1️⃣ Top 10 productos por categoría últimos 6 meses
# -----------------------------------
st.header("📊 Top 10 Productos por Categoría — Últimos 6 meses")
try:
    query_top_productos = """
    SELECT 
        c.Nombre AS Categoria,
        p.Nombre AS Producto,
        SUM(d.Cantidad) AS UnidadesVendidas
    FROM dbo.DetalleOrdenes d
    INNER JOIN dbo.Productos p ON d.ProductoID = p.ProductoID
    INNER JOIN dbo.Categorias c ON p.CategoriaID = c.CategoriaID
    INNER JOIN dbo.Ordenes o ON d.OrdenID = o.OrdenID
    WHERE o.FechaOrden >= DATEADD(MONTH, -6, GETDATE())
    GROUP BY c.Nombre, p.Nombre
    ORDER BY UnidadesVendidas DESC;
    """
    df_top_productos = pd.read_sql(query_top_productos, engine)
    df_top10 = df_top_productos.groupby('Categoria').head(10)

    # Streamlit chart
    chart_top_productos = alt.Chart(df_top10).mark_bar().encode(
        x=alt.X('UnidadesVendidas:Q', title='Unidades Vendidas'),
        y=alt.Y('Producto:N', sort='-x'),
        color='Categoria:N',
        tooltip=['Producto', 'Categoria', 'UnidadesVendidas']
    )
    st.altair_chart(chart_top_productos, use_container_width=True)

    # Guardar como PNG
    plt.figure()
    sns.barplot(data=df_top10, x='UnidadesVendidas', y='Producto', hue='Categoria', dodge=False)
    plt.title("Top 10 Productos por Categoría — Últimos 6 meses")
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "top10_productos.png"))
    plt.close()
except Exception as e:
    st.error(f"Error al consultar la base de datos: {e}")

# -----------------------------------
# 2️⃣ Clientes con más compras y promedio por orden
# -----------------------------------
st.header("📊 Clientes más activos y promedio de gasto por orden")
try:
    query_clientes = """
    SELECT 
        u.UsuarioID,
        u.Nombre AS Cliente,
        COUNT(o.OrdenID) AS TotalCompras,
        AVG(o.Total) AS PromedioPorOrden
    FROM dbo.Usuarios u
    INNER JOIN dbo.Ordenes o ON u.UsuarioID = o.UsuarioID
    GROUP BY u.UsuarioID, u.Nombre
    ORDER BY TotalCompras DESC;
    """
    df_clientes = pd.read_sql(query_clientes, engine)
    df_clientes_top10 = df_clientes.head(10)

    chart_clientes = alt.Chart(df_clientes_top10).mark_bar().encode(
        x=alt.X('TotalCompras:Q', title='Total Compras'),
        y=alt.Y('Cliente:N', sort='-x'),
        color='PromedioPorOrden:Q',
        tooltip=['Cliente', 'TotalCompras', 'PromedioPorOrden']
    )
    st.altair_chart(chart_clientes, use_container_width=True)

    # Guardar como PNG
    plt.figure()
    sns.barplot(data=df_clientes_top10, x='TotalCompras', y='Cliente', palette="viridis")
    plt.title("Clientes más activos y promedio de gasto por orden")
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "clientes_top10.png"))
    plt.close()
except Exception as e:
    st.error(f"Error al consultar la base de datos: {e}")

# -----------------------------------
# 3️⃣ Productos con mayor rotación
# -----------------------------------
st.header("📊 Productos con mayor y menor rotación")
try:
    query_rotacion = """
    SELECT TOP 10
        p.Nombre AS Producto,
        SUM(d.Cantidad) AS TotalVendido
    FROM dbo.DetalleOrdenes d
    INNER JOIN dbo.Productos p ON d.ProductoID = p.ProductoID
    GROUP BY p.Nombre
    ORDER BY TotalVendido DESC;
    """
    df_rotacion = pd.read_sql(query_rotacion, engine)

    chart_rotacion = alt.Chart(df_rotacion).mark_bar().encode(
        x='TotalVendido:Q',
        y=alt.Y('Producto:N', sort='-x'),
        tooltip=['Producto', 'TotalVendido']
    )
    st.altair_chart(chart_rotacion, use_container_width=True)

    plt.figure()
    sns.barplot(data=df_rotacion, x='TotalVendido', y='Producto', palette="coolwarm")
    plt.title("Productos con mayor rotación")
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "productos_rotacion.png"))
    plt.close()
except Exception as e:
    st.error(f"Error al consultar la base de datos: {e}")

# -----------------------------------
# 4️⃣ Evolución mensual del ingreso bruto
# -----------------------------------
st.header("📊 Evolución mensual del ingreso bruto")
try:
    query_ingreso = """
    SELECT 
        FORMAT(o.FechaOrden, 'yyyy-MM') AS Mes,
        SUM(d.PrecioUnitario * d.Cantidad) AS IngresoBruto
    FROM dbo.Ordenes o
    INNER JOIN dbo.DetalleOrdenes d ON o.OrdenID = d.OrdenID
    GROUP BY FORMAT(o.FechaOrden, 'yyyy-MM')
    ORDER BY Mes;
    """
    df_ingreso = pd.read_sql(query_ingreso, engine)

    chart_ingreso = alt.Chart(df_ingreso).mark_line(point=True).encode(
        x='Mes:T',
        y='IngresoBruto:Q',
        tooltip=['Mes', 'IngresoBruto']
    )
    st.altair_chart(chart_ingreso, use_container_width=True)

    plt.figure()
    sns.lineplot(data=df_ingreso, x='Mes', y='IngresoBruto', marker="o")
    plt.title("Evolución mensual del ingreso bruto")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "ingreso_mensual.png"))
    plt.close()
except Exception as e:
    st.error(f"Error al consultar la base de datos: {e}")

# -----------------------------------
# 5️⃣ Margen aproximado por categoría
# -----------------------------------
st.header("📊 Margen aproximado por categoría")
try:
    query_margen = """
    SELECT 
        c.Nombre AS Categoria,
        SUM(d.PrecioUnitario * d.Cantidad) AS MargenAprox
    FROM dbo.DetalleOrdenes d
    INNER JOIN dbo.Productos p ON d.ProductoID = p.ProductoID
    INNER JOIN dbo.Categorias c ON p.CategoriaID = c.CategoriaID
    GROUP BY c.Nombre
    ORDER BY MargenAprox DESC;
    """
    df_margen = pd.read_sql(query_margen, engine)

    chart_margen = alt.Chart(df_margen).mark_bar().encode(
        x='MargenAprox:Q',
        y=alt.Y('Categoria:N', sort='-x'),
        tooltip=['Categoria', 'MargenAprox']
    )
    st.altair_chart(chart_margen, use_container_width=True)

    plt.figure()
    sns.barplot(data=df_margen, x='MargenAprox', y='Categoria', palette="magma")
    plt.title("Margen aproximado por categoría")
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "margen_categoria.png"))
    plt.close()
except Exception as e:
    st.error(f"Error al consultar la base de datos: {e}")





























