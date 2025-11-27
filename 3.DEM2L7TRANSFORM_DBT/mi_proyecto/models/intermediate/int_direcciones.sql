with direcciones as (
    select
        d.DireccionID,
        d.UsuarioID,
        d.Calle,
        d.Ciudad,
        d.Estado,
        d.CodigoPostal,
        d.Pais
    from dbo.DireccionesEnvio d
)
select
    o.OrdenID,
    d.DireccionID,
    d.Calle,
    d.Ciudad,
    d.Estado,
    d.CodigoPostal,
    d.Pais
from dbo.Ordenes o
join direcciones d on o.UsuarioID = d.UsuarioID