select
    DireccionID as direccion_id,
    UsuarioID as cliente_id,
    Calle,
    Ciudad,
    Estado,
    CodigoPostal,
    Pais,
    getdate() as fecha_creacion,
    null as fecha_fin
from dbo.DireccionesEnvio