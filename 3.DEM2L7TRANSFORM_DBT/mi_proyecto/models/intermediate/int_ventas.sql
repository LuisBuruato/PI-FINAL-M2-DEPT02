with detalle as (
    select
        d.DetalleID,
        d.OrdenID,
        d.ProductoID,
        d.Cantidad,
        d.PrecioUnitario,
        d.Cantidad * d.PrecioUnitario as subtotal
    from dbo.DetalleOrdenes d
),
ordenes as (
    select
        o.OrdenID,
        o.UsuarioID,
        o.FechaOrden,
        o.Total as total_orden
    from dbo.Ordenes o
),
productos as (
    select
        p.ProductoID,
        p.Nombre as producto_nombre,
        p.CategoriaID
    from dbo.Productos p
),
clientes as (
    select
        u.UsuarioID,
        u.Nombre,
        u.Apellido,
        u.DNI
    from dbo.Usuarios u
)
select
    d.DetalleID,
    o.OrdenID,
    o.UsuarioID as cliente_id,
    c.Nombre as cliente_nombre,
    c.Apellido as cliente_apellido,
    d.ProductoID,
    p.producto_nombre,
    p.CategoriaID as categoria_id,
    d.Cantidad,
    d.PrecioUnitario,
    d.subtotal,
    o.FechaOrden
from detalle d
join ordenes o on d.OrdenID = o.OrdenID
join productos p on d.ProductoID = p.ProductoID
join clientes c on o.UsuarioID = c.UsuarioID