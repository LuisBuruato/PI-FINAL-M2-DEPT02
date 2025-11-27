-- models/staging/stg_usuarios.sql
select
    UsuarioID as id_usuario,
    Nombre as nombre_usuario,
    Email as email_usuario,
    FechaRegistro as fecha_registro
from dbo.Usuarios;



