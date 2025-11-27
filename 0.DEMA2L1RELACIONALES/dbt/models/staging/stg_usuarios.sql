{{ config(materialized='view') }}

select
  usuario_id,
  nombre,
  email,
  telefono,
  fecha_registro::timestamp as fecha_registro,
  ciudad,
  provincia
from {{ source('raw','usuarios') }}
