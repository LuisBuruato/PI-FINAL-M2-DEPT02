{{ config(materialized='table') }}
select
  usuario_id as client_id,
  nombre,
  email,
  fecha_registro::date,
  ciudad,
  provincia
from {{ ref('stg_usuarios') }}
