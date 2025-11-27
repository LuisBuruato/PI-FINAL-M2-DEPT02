--1.-  ¿Cuáles son los productos más vendidos por categoría en los últimos 6 meses?

SELECT 
    c.Nombre AS Categoria,
    p.Nombre AS Producto,
    SUM(d.Cantidad) AS UnidadesVendidas
FROM dbo.DetalleOrdenes d
INNER JOIN dbo.Productos p 
    ON d.ProductoID = p.ProductoID
INNER JOIN dbo.Categorias c 
    ON p.CategoriaID = c.CategoriaID
INNER JOIN dbo.Ordenes o 
    ON d.OrdenID = o.OrdenID
WHERE o.FechaOrden >= DATEADD(MONTH, -6, GETDATE())
GROUP BY 
    c.Nombre,
    p.Nombre
ORDER BY 
    UnidadesVendidas DESC;

	-------------------------------------------------------------------------------------
	--2.-¿Qué clientes realizaron más compras y cuánto gastaron en promedio por orden?

	SELECT 
    u.UsuarioID,
    u.Nombre AS Cliente,
    COUNT(o.OrdenID) AS TotalCompras,
    AVG(o.Total) AS PromedioPorOrden
FROM dbo.Usuarios u
INNER JOIN dbo.Ordenes o 
    ON u.UsuarioID = o.UsuarioID
GROUP BY 
    u.UsuarioID,
    u.Nombre
ORDER BY 
    TotalCompras DESC;


----------------------------------------------------------------------------
--3.-¿Qué porcentaje de los clientes son recurrentes vs. nuevos cada mes?

WITH PrimerasCompras AS (
    SELECT
        UsuarioID,
        MIN(CAST(FechaOrden AS date)) AS FechaPrimeraCompra
    FROM dbo.Ordenes
    GROUP BY UsuarioID
),
ComprasMensuales AS (
    SELECT
        UsuarioID,
        DATEFROMPARTS(YEAR(FechaOrden), MONTH(FechaOrden), 1) AS Mes
    FROM dbo.Ordenes
),
Clasificacion AS (
    SELECT
        c.Mes,
        c.UsuarioID,
        CASE 
            WHEN pc.FechaPrimeraCompra >= c.Mes 
                THEN 'Nuevo'
            ELSE 'Recurrente'
        END AS TipoCliente
    FROM ComprasMensuales c
    INNER JOIN PrimerasCompras pc
        ON c.UsuarioID = pc.UsuarioID
)
SELECT 
    Mes,
    TipoCliente,
    COUNT(DISTINCT UsuarioID) AS CantidadClientes,
    CAST(
        100.0 * COUNT(DISTINCT UsuarioID) 
        / SUM(COUNT(DISTINCT UsuarioID)) OVER (PARTITION BY Mes)
        AS DECIMAL(10,2)
    ) AS Porcentaje
FROM Clasificacion
GROUP BY 
    Mes, TipoCliente
ORDER BY 
    Mes, TipoCliente;

	-----------------------------------------------------------------------

