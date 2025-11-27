# Base image
FROM python:3.11-slim

# Evitar preguntas durante la instalación
ENV DEBIAN_FRONTEND=noninteractive

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y --no-install-recommends \
        curl \
        gnupg \
        apt-transport-https \
        unixodbc-dev \
        gcc \
        g++ \
        git \
        lsb-release \
    && rm -rf /var/lib/apt/lists/*

# Importar la llave pública de Microsoft para los repositorios
RUN mkdir -p /usr/share/keyrings
RUN curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > /usr/share/keyrings/microsoft-prod.gpg

# Agregar repositorio Microsoft y actualizar
RUN curl https://packages.microsoft.com/config/debian/12/prod.list > /etc/apt/sources.list.d/mssql-release.list
RUN apt-get update

# Instalar ODBC Driver 18 para SQL Server
RUN ACCEPT_EULA=Y apt-get install -y msodbcsql18

# Instalar dbt-core y adaptador SQL Server
RUN pip install --upgrade pip
RUN pip install dbt-core dbt-sqlserver

# Crear directorio de trabajo
WORKDIR /usr/app

# Copiar el proyecto dbt
COPY . /usr/app

# Configurar dbt como entrypoint
ENTRYPOINT ["dbt"]









