select
    UsuarioID as cliente_id,
    Nombre,
    Apellido,
    DNI,
    Email,
    Contraseña,
    FechaRegistro,
    getdate() as fecha_creacion,
    null as fecha_fin
from dbo.Usuarios