--1.-¿Cuál ha sido la evolución mensual del ingreso bruto?

SELECT 
    FORMAT(FechaOrden, 'yyyy-MM') AS Mes,
    SUM(Total) AS IngresoBrutoMensual
FROM dbo.Ordenes
GROUP BY 
    FORMAT(FechaOrden, 'yyyy-MM')
ORDER BY 
    Mes;

	----------------------------------------------------------------------------
	--2.-¿Qué categorías aportan el mayor margen de ganancia?

	WITH Ventas AS (
    SELECT 
        p.CategoriaID,
        d.Cantidad,
        d.PrecioUnitario,
        -- Margen estimado (35% de costo)
        (d.PrecioUnitario * 0.65) AS MargenPorUnidad
    FROM dbo.DetalleOrdenes d
    JOIN dbo.Productos p ON d.ProductoID = p.ProductoID
)
SELECT 
    c.CategoriaID,
    c.Nombre AS Categoria,
    SUM(v.Cantidad * v.MargenPorUnidad) AS MargenTotalEstimado
FROM Ventas v
JOIN dbo.Categorias c ON v.CategoriaID = c.CategoriaID
GROUP BY 
    c.CategoriaID, c.Nombre
ORDER BY 
    MargenTotalEstimado DESC;

	--------------------------------------------------------------------
	