with pagos as (
    select
        h.PagoID,
        h.OrdenID,
        h.MetodoPagoID,
        h.Monto,
        h.FechaPago
    from dbo.HistorialPagos h
)
select
    p.PagoID,
    p.OrdenID,
    m.Nombre as metodo_pago,
    p.Monto,
    p.FechaPago
from pagos p
join dbo.MetodosPago m on p.MetodoPagoID = m.MetodoPagoID