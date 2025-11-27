with raw_ventas as (
    select *
    from (values
        (1, 833, 33, 1, 425.26, 101, 201, 1, '2025-11-25'),
        (2, 657, 21, 4, 307.13, 102, 202, 2, '2025-11-26'),
        (3, 911, 15, 4, 444.75, 103, 203, 1, '2025-11-27')
        -- agrega más filas según necesites
    ) as t(
        DetalleID, OrdenID, ProductoID, Cantidad, PrecioUnitario,
        ClienteID, DireccionID, MetodoPagoID, FechaVenta
    )
)
select *
from raw_ventas;



