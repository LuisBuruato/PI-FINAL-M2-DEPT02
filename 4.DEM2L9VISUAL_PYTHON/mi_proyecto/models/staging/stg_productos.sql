-- Modelo staging de productos
-- models/staging/stg_productos.sql
select
    ProductoID as id_producto,
    Nombre as nombre_producto,
    Descripcion as descripcion,
    Precio as precio,
    Stock as stock,
    CategoriaID as categoria_id
from dbo.Productos;

