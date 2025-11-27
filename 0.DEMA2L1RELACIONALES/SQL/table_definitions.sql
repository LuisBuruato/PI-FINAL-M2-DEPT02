-- Table definitions for Postgres
-- Raw schema (CSV imported)
CREATE SCHEMA IF NOT EXISTS raw;
CREATE SCHEMA IF NOT EXISTS staging;
CREATE SCHEMA IF NOT EXISTS marts;

-- raw tables (simple)
CREATE TABLE IF NOT EXISTS raw.usuarios (
  usuario_id TEXT,
  nombre TEXT,
  email TEXT,
  telefono TEXT,
  fecha_registro DATE,
  provincia TEXT,
  ciudad TEXT
);

CREATE TABLE IF NOT EXISTS raw.categorias (
  categoria_id TEXT,
  nombre TEXT
);

CREATE TABLE IF NOT EXISTS raw.productos (
  producto_id TEXT,
  nombre_producto TEXT,
  categoria_id TEXT,
  precio NUMERIC,
  costo NUMERIC,
  stock INTEGER,
  activo BOOLEAN
);

CREATE TABLE IF NOT EXISTS raw.ordenes (
  orden_id TEXT,
  usuario_id TEXT,
  fecha_orden TIMESTAMP,
  direccion_envio_id TEXT,
  estado TEXT,
  total NUMERIC
);

CREATE TABLE IF NOT EXISTS raw.detalle_ordenes (
  detalle_id TEXT,
  orden_id TEXT,
  producto_id TEXT,
  cantidad INTEGER,
  precio_unitario NUMERIC,
  descuento NUMERIC
);

CREATE TABLE IF NOT EXISTS raw.direcciones_envio (
  direccion_id TEXT,
  usuario_id TEXT,
  calle TEXT,
  ciudad TEXT,
  provincia TEXT,
  codigo_postal TEXT
);

CREATE TABLE IF NOT EXISTS raw.carrito (
  carrito_id TEXT,
  usuario_id TEXT,
  producto_id TEXT,
  fecha_agregado TIMESTAMP,
  cantidad INTEGER
);

CREATE TABLE IF NOT EXISTS raw.metodos_pago (
  metodo_id TEXT,
  nombre_metodo TEXT
);

CREATE TABLE IF NOT EXISTS raw.ordenes_metodospago (
  orden_id TEXT,
  metodo_id TEXT,
  monto NUMERIC
);

CREATE TABLE IF NOT EXISTS raw.resenas_productos (
  resena_id TEXT,
  producto_id TEXT,
  usuario_id TEXT,
  calificacion INTEGER,
  comentario TEXT,
  fecha_resena TIMESTAMP
);

CREATE TABLE IF NOT EXISTS raw.historial_pagos (
  pago_id TEXT,
  orden_id TEXT,
  fecha_pago TIMESTAMP,
  monto NUMERIC,
  estado TEXT
);

-- staging and marts will be created by ETL scripts/dbt
