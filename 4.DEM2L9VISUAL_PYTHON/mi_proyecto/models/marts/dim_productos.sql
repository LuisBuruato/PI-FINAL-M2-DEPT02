{{ config(
    materialized='table'
) }}

select
    id_producto,
    nombre,
    categoria,
    precio
from {{ ref('stg_productos') }};
