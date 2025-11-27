-- models/staging/stg_ordenes.sql
select
    OrdenID as id_orden,
    UsuarioID as id_usuario,
    FechaOrden as fecha_orden,
    Total as total_orden,
    Estado as estado_orden
from dbo.Ordenes;






