{{ config(
    materialized='view'
) }}

select
    id_usuario,
    nombre,
    apellido,
    email,
    fecha_creacion,
    estado
from {{ source('raw', 'usuarios') }};




