{{ config(
    materialized='table'
) }}

select
    id_usuario,
    nombre,
    apellido,
    email,
    estado,
    fecha_creacion
from {{ ref('stg_usuarios') }};
