{{ config(
    materialized='view'
) }}

select
    v.*,
    p.nombre as producto_nombre,
    p.categoria
from {{ ref('stg_ventas') }} v
left join {{ ref('stg_productos') }} p
    on v.id_producto = p.id_producto;
