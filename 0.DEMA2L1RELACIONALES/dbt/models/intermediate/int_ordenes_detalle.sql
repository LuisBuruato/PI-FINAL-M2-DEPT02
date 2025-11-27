{{ config(materialized='view') }}
with o as (select * from {{ ref('stg_ordenes') }}),
     d as (select * from {{ ref('stg_detalle_ordenes') }})
select
  d.detalle_id,
  d.orden_id,
  d.producto_id,
  d.cantidad,
  d.precio_unitario,
  d.descuento,
  o.usuario_id,
  o.fecha_orden
from d
join o using (orden_id)
