{{ config(
    materialized='view'
) }}

select
    id_venta,
    id_usuario,
    id_producto,
    cantidad,
    precio_unitario,
    fecha_venta
from {{ source('raw', 'ventas') }};




