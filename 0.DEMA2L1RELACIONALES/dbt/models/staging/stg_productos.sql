{{ config(materialized='view') }}
select
  producto_id,
  nombre_producto,
  categoria_id,
  cast(precio as numeric) as precio,
  cast(costo as numeric) as costo,
  cast(stock as integer) as stock,
  cast(activo as boolean) as activo
from {{ source('raw','productos') }}
