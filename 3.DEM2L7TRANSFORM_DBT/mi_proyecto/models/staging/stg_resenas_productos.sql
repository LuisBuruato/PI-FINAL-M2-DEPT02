-- models/staging/stg_resenas_productos.sql
select
    [ReseñaID] as id_resena,
    [UsuarioID] as id_usuario,
    [ProductoID] as id_producto,
    [Calificacion] as calificacion,
    [Comentario] as comentario,
    [Fecha] as fecha_resena
from dbo.ReseñasProductos;







