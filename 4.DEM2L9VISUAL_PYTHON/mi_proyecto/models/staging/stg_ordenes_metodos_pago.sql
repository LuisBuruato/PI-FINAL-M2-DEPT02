-- models/staging/stg_ordenes_metodos_pago.sql
select
    OrdenID as id_orden,
    MetodoPagoID as id_metodo_pago
from dbo.OrdenesMetodosPago;


