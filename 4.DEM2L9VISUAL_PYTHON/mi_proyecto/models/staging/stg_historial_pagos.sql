-- Modelo staging de historial de pagos
select
    PagoID as id_pago,
    OrdenID as id_orden,
    MetodoPagoID as id_metodo_pago,
    Monto as monto,
    FechaPago as fecha_pago
from dbo.HistorialPagos;




