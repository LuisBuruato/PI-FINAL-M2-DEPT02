select
    ProductoID as producto_id,
    Nombre as producto_nombre,
    CategoriaID as categoria_id,
    Precio,
    getdate() as fecha_creacion,
    null as fecha_fin
from dbo.Productos