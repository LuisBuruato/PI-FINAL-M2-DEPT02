select
    MetodoPagoID as metodo_pago_id,
    Nombre as metodo_pago_nombre,
    getdate() as fecha_creacion,
    null as fecha_fin
from dbo.MetodosPago