--1.-¿Cuáles son los productos con mayor y menor rotación?

--PRODUCTOS DE MAYOR ROTACION.
SELECT TOP 10
    p.ProductoID,
    p.Nombre AS Producto,
    SUM(d.Cantidad) AS UnidadesVendidas
FROM dbo.DetalleOrdenes d
INNER JOIN dbo.Productos p 
    ON d.ProductoID = p.ProductoID
INNER JOIN dbo.Ordenes o 
    ON d.OrdenID = o.OrdenID
WHERE o.FechaOrden >= DATEADD(MONTH, -6, GETDATE())  -- últimos 6 meses
GROUP BY 
    p.ProductoID,
    p.Nombre
ORDER BY UnidadesVendidas DESC;

--PRODUCTOS CON MENOR ROTACION.
SELECT TOP 10
    p.ProductoID,
    p.Nombre AS Producto,
    SUM(d.Cantidad) AS UnidadesVendidas
FROM dbo.DetalleOrdenes d
INNER JOIN dbo.Productos p 
    ON d.ProductoID = p.ProductoID
INNER JOIN dbo.Ordenes o 
    ON d.OrdenID = o.OrdenID
WHERE o.FechaOrden >= DATEADD(MONTH, -6, GETDATE())
GROUP BY 
    p.ProductoID,
    p.Nombre
ORDER BY UnidadesVendidas ASC;











------------------------------------------------------------------------------

--2.-¿Qué regiones presentan más demoras en la entrega?

SELECT 
    de.Provincia,
    COUNT(DISTINCT u.UsuarioID) AS NumeroClientes
FROM dbo.Usuarios u
JOIN dbo.DireccionesEnvio de 
    ON u.UsuarioID = de.UsuarioID
GROUP BY 
    de.Provincia
ORDER BY 
    NumeroClientes DESC;


