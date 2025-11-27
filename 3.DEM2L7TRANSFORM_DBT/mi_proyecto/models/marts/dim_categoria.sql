select
    CategoriaID as categoria_id,
    Nombre as categoria_nombre,
    getdate() as fecha_creacion,
    null as fecha_fin
from dbo.Categorias