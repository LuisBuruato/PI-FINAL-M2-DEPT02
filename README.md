
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


