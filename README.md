{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "5483f2c3",
   "metadata": {},
   "source": [
    "# 🏗️ Diseño del Modelo Dimensional (Star Schema)\n",
    "\n",
    "## 1️⃣ Definición del Proceso de Negocio\n",
    "El proceso principal del e-commerce es:  \n",
    "**Registrar ventas de productos realizadas por clientes en fechas específicas y con ciertos atributos asociados.**\n",
    "\n",
    "- **Tabla de hechos:** `HechoVentas`  \n",
    "- **Tablas de dimensiones:**\n",
    "  - `DimProducto`\n",
    "  - `DimCliente`\n",
    "  - `DimTiempo`\n",
    "  - `DimCategoria` (si aplica)\n",
    "  - `DimEstadoOrden / DimEstatus` (opcional)\n",
    "\n",
    "---\n",
    "\n",
