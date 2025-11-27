--1.-¿Qué campañas de marketing tuvieron mayor impacto en ventas?

SELECT 
    p.ProductoID,
    p.Nombre AS Producto,
    
    -- Ventas totales
    SUM(do.Cantidad) AS TotalVendidas,

    -- Clientes que compraron (aprox. impacto comercial)
    COUNT(DISTINCT o.UsuarioID) AS ClientesUnicos,

    -- Métricas de reseñas
    COUNT(r.UsuarioID) AS TotalReseñas,
    AVG(r.Calificacion) AS PromedioCalificacion,

    -- Índice compuesto de "Impacto"
    (SUM(do.Cantidad) * 0.5) +
    (COUNT(r.UsuarioID) * 0.3) +
    (AVG(r.Calificacion) * 0.2) AS ImpactoMarketing
FROM dbo.Productos p
LEFT JOIN dbo.DetalleOrdenes do
    ON p.ProductoID = do.ProductoID
LEFT JOIN dbo.Ordenes o
    ON do.OrdenID = o.OrdenID
LEFT JOIN dbo.ReseñasProductos r
    ON p.ProductoID = r.ProductoID
GROUP BY 
    p.ProductoID,
    p.Nombre
ORDER BY 
    ImpactoMarketing DESC;

	--------------------------------------------------------------------------
	--2.-¿Cuál es el ticket promedio por canal de venta?

	SELECT 
    mp.Nombre AS CanalVenta,
    AVG(omp.MontoPagado) AS TicketPromedio
FROM dbo.OrdenesMetodosPago omp
JOIN dbo.MetodosPago mp 
    ON omp.MetodoPagoID = mp.MetodoPagoID
GROUP BY 
    mp.Nombre
ORDER BY 
    TicketPromedio DESC;


