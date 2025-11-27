select
    DetalleID      as id_detalle,
    OrdenID        as id_orden,
    ProductoID     as id_producto,
    Cantidad       as cantidad,
    PrecioUnitario as precio_unitario,
    Cantidad * PrecioUnitario as total_venta
from {{ ref('stg_ventas') }}














