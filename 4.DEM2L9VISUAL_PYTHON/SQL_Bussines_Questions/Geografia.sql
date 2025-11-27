--1.-¿En qué provincias hay mayor concentración de clientes y cuáles están desatendidas?

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
