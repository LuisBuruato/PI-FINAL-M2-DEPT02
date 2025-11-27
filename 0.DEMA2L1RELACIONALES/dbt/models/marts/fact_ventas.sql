{{ config(materialized='table') }}
select
  md5(detalle_id::text) as sale_id,
  orden_id,
  producto_id,
  usuario_id,
  fecha_orden::date as date,
  cantidad,
  precio_unitario,
  (cantidad * precio_unitario - coalesce(descuento,0)) as total_amount
from {{ ref('int_ordenes_detalle') }}
