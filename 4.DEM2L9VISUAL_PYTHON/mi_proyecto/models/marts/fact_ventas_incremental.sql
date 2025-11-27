{{ config(
    materialized='incremental',
    unique_key='id_venta'
) }}

select
    id_venta,
    id_usuario,
    id_producto,
    cantidad,
    precio_unitario,
    fecha_venta
from {{ ref('stg_ventas') }}

{% if is_incremental() %}
where fecha_venta > (select max(fecha_venta) from {{ this }})
{% endif %}
