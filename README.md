
🛒 Ecommerce Data Project

Proyecto integrador que incluye scripts ETL (Extract, Transform, Load), definiciones SQL y modelos DBT, formando un pipeline completo de procesamiento y modelado de datos para un escenario de comercio electrónico.


📁 Estructura del Proyecto

data/: Ubicación de CSVs y archivos procesados.

notebooks/: Notebook explicativo del análisis y el proceso.

dbt/: Modelos y configuraciones del proyecto DBT.

scripts/: Scripts ETL (extract.py, transform.py, load.py).

SQL/: Definiciones de tablas y consultas utilizadas.

tests/: Notas, pruebas y validaciones adicionales.


⚙️ Proyecto DBT
1️⃣ Objetivo del Proyecto

El proyecto tiene como objetivo implementar un pipeline de transformación de datos para un escenario real de ventas, utilizando DBT sobre SQL Server.
Incluye:

Limpieza y normalización de datos

Construcción de tablas de staging

Modelado de dimensiones y hechos

Implementación de Slowly Changing Dimensions (SCD Tipo 2) para el seguimiento histórico de usuarios.

2️⃣ Estructura de Carpetas y Modelos
staging/

Modelos que cargan y limpian los datos crudos.

stg_usuarios.sql: Normalización de datos de usuarios.

stg_ventas.sql: Normalización de ventas.

marts/

Modelos finales orientados al negocio.

dim_usuarios.sql: Dimensión de usuarios (SCD Tipo 2).

fact_ventas.sql: Tabla de hechos de ventas.

snapshots/

Implementaciones SCD basadas en snapshots.

snapshot_cliente.sql: Seguimiento histórico de usuarios.

3️⃣ Modelos y Transformaciones

Staging: Limpieza, cast de tipos, normalización y estandarización.

Dimensiones (SCD Tipo 2):
dim_usuarios conserva la historia de cambios utilizando campos:

dbt_scd_id

dbt_updated_at

dbt_valid_from

dbt_valid_to

Tabla de Hechos:
fact_ventas incluye el cálculo derivado:

Total = Cantidad * PrecioUnitario

Snapshots:
snapshot_cliente captura cambios históricos para alimentar la dimensión.

4️⃣ Relaciones y Constraints

Llaves foráneas entre hechos y dimensiones para asegurar integridad.

Índices en columnas consultadas frecuentemente:

email_usuario en dim_usuarios

OrdenID en fact_ventas.


5️⃣ Pasos Ejecutados con DBT

dbt run --models stg_usuarios

dbt run --models stg_ventas

dbt run --models fact_ventas

dbt snapshot para crear el snapshot histórico snapshot_cliente.


6️⃣ Consideraciones

Corrección de errores por columnas inexistentes.

Manejo de identities en snapshots.

Verificación de creación de tablas finales.

Configuración completa para uso con SQL Server.

        ┌───────────────┐
        │ stg_usuarios  │  ← Datos maestros de usuarios
        └───────┬───────┘
                │
                │ ref('stg_usuarios')
                ▼
        ┌───────────────┐
        │ dim_usuarios  │  ← Dimensión con SCD Tipo 2
        │ dbt_scd_id PK │
        └───────┬───────┘
                │
        ┌───────┴─────────┐
        │                 │
        ▼                 ▼
┌───────────────┐   ┌───────────────┐
│ snapshot_cliente│  │ fact_ventas    │  ← Tabla de hechos
│ (SCD Historico) │  │ DetalleID PK   │
└───────────────┘   │ FK → dim_usuarios
                    └───────────────┘

        ┌───────────────┐
        │ stg_ventas    │  ← Datos de ventas crudos
        └───────┬───────┘
                │
                ▼
              fact_ventas


📊 Insights y Visualizaciones (Análisis Final)

Este proyecto incluye un módulo de análisis exploratorio y visualización donde se identificaron:

🔹 Ingreso mensual

🔹 Margen por categoría

🔹 Rotación de productos

🔹 Top 10 productos

🔹 Top 10 clientes

Estos visuales permiten entender:

Tendencias de ventas

Rentabilidad por categoría

Productos con mayor rotación

Clientes más valiosos

Comportamiento general del e-commerce
































# Ecommerce Data Project

Proyecto integrador con scripts ETL (extract, transform, load), definiciones SQL y modelos DBT.

Estructura:
- data/: ubicación de CSVs y archivos procesados
- notebooks/: notebook explicativo
- dbt/: modelos DBT (plantillas)
- scripts/: ETL scripts (extract.py, transform.py, load.py)
- SQL/: definiciones de tablas y consultas
- tests/: notas y tests

- 

# Proyecto DBT
1.	Objetivo del Proyecto El proyecto tiene como objetivo implementar un pipeline de transformación de datos para un escenario de ventas, utilizando DBT sobre SQL Server. Se incluye la limpieza y normalización de datos, la construcción de tablas de staging, dimensiones, hechos, y la implementación de Slowly Changing Dimensions (SCD) para el seguimiento histórico de usuarios.
2.	Estructura de Carpetas y Modelos
•	staging/: Contiene modelos de staging que cargan los datos crudos.
o	stg_usuarios.sql: Normalización de datos de usuarios.
o	stg_ventas.sql: Normalización de datos de ventas.
•	marts/: Contiene modelos finales o de negocio (tablas de hechos y dimensiones).
o	dim_usuarios.sql: Tabla de dimensión de usuarios (SCD Tipo 2).
o	fact_ventas.sql: Tabla de hechos de ventas.
•	snapshots/: Contiene snapshots para implementar SCD.
o	snapshot_cliente.sql: Snapshot de usuarios para rastrear cambios históricos.
3.	Modelos y Transformaciones
•	Staging: Se cargaron los datos crudos de ventas y usuarios, normalizando columnas y tipos de datos.
•	Dimensiones (SCD Tipo 2): dim_usuarios almacena la historia de cambios de los usuarios, incluyendo campos dbt_scd_id, dbt_updated_at, dbt_valid_from y dbt_valid_to.
•	Tabla de Hechos: fact_ventas contiene las ventas con el cálculo de Total = Cantidad * PrecioUnitario.
•	Snapshots: snapshot_cliente captura el estado histórico de los usuarios, utilizado para mantener el SCD Tipo 2.
4.	Relaciones y Constraints
•	Llaves foráneas entre hechos y dimensiones para asegurar integridad referencial.
•	Índices sobre columnas frecuentemente consultadas (ej. email_usuario en dim_usuarios, OrdenID en fact_ventas).
5.	Pasos Ejecutados con DBT
•	dbt run --models stg_usuarios y dbt run --models stg_ventas: Creación de vistas de staging.
•	dbt run --models fact_ventas: Creación de tabla de hechos.
•	dbt snapshot: Creación de snapshot snapshot_cliente para SCD Tipo 2.
6.	Consideraciones
•	Se resolvieron errores de columnas inexistentes y de identidad en snapshots.
•	Se verificó la correcta ejecución y creación de todas las tablas y snapshots.
•	Se utilizó SQL Server como motor de base de datos y se configuró DBT para manejar SCD y relaciones entre modelos.


        ┌───────────────┐
        │ stg_usuarios  │  ← Datos maestros de usuarios
        └───────┬───────┘
                │
                │ ref('stg_usuarios')
                ▼
        ┌───────────────┐
        │ dim_usuarios  │  ← Dimensión con SCD Tipo 2
        │ dbt_scd_id PK │
        └───────┬───────┘
                │
        ┌───────┴─────────┐
        │                 │
        ▼                 ▼
┌───────────────┐   ┌───────────────┐
│ snapshot_cliente│  │ fact_ventas    │  ← Tabla de hechos
│ (SCD Historico) │  │ DetalleID PK   │
└───────────────┘   │ FK → dim_usuarios
                    └───────────────┘

        ┌───────────────┐
        │ stg_ventas    │  ← Datos de ventas crudos
        └───────┬───────┘
                │
                ▼
fact_ventas


