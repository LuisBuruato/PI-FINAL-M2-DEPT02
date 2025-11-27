\
        \"\"\"Transform step: read raw CSVs with pandas, clean/normalize, and write staging CSVs.
        \"\"\"
        import os
        import pandas as pd

        BASE = os.path.dirname(os.path.dirname(__file__))
        RAW = os.path.join(BASE, 'data', 'raw')
        STAGING = os.path.join(BASE, 'data', 'staging')
        os.makedirs(STAGING, exist_ok=True)

        # Helper to load with safe names
        def load_csv(name):
            path = os.path.join(RAW, name)
            if not os.path.exists(path):
                raise FileNotFoundError(path)
            return pd.read_csv(path)

        # Usuarios -> staging/usuarios.csv (normalize column names)
        usuarios = load_csv('1.Usuarios.csv')
        usuarios.columns = usuarios.columns.str.strip().str.lower().str.replace(' ','_')
        # parse dates
        if 'fecha_registro' in usuarios.columns:
            usuarios['fecha_registro'] = pd.to_datetime(usuarios['fecha_registro'], errors='coerce')
        usuarios.to_csv(os.path.join(STAGING, 'stg_usuarios.csv'), index=False)
        print('Wrote stg_usuarios.csv')

        categorias = load_csv('2.Categorias.csv')
        categorias.columns = categorias.columns.str.strip().str.lower().str.replace(' ','_')
        categorias.to_csv(os.path.join(STAGING, 'stg_categorias.csv'), index=False)
        print('Wrote stg_categorias.csv')

        productos = load_csv('3.Productos.csv')
        productos.columns = productos.columns.str.strip().str.lower().str.replace(' ','_')
        # ensure numeric columns
        for col in ['precio','costo','stock']:
            if col in productos.columns:
                productos[col] = pd.to_numeric(productos[col], errors='coerce').fillna(0)
        productos.to_csv(os.path.join(STAGING, 'stg_productos.csv'), index=False)
        print('Wrote stg_productos.csv')

        ordenes = load_csv('4.ordenes.csv')
        ordenes.columns = ordenes.columns.str.strip().str.lower().str.replace(' ','_')
        if 'fecha_orden' in ordenes.columns:
            ordenes['fecha_orden'] = pd.to_datetime(ordenes['fecha_orden'], errors='coerce')
        ordenes.to_csv(os.path.join(STAGING, 'stg_ordenes.csv'), index=False)
        print('Wrote stg_ordenes.csv')

        detalle = load_csv('5.detalle_ordenes.csv')
        detalle.columns = detalle.columns.str.strip().str.lower().str.replace(' ','_')
        for col in ['cantidad','precio_unitario','descuento']:
            if col in detalle.columns:
                detalle[col] = pd.to_numeric(detalle[col], errors='coerce').fillna(0)
        detalle.to_csv(os.path.join(STAGING, 'stg_detalle_ordenes.csv'), index=False)
        print('Wrote stg_detalle_ordenes.csv')

        # Other files: direcciones, carrito, metodos_pago, ordenes_metodospago, resenas, historial_pagos
        for fname in ['6.direcciones_envio.csv','7.carrito.csv','8.metodos_pago.csv','9.ordenes_metodospago.csv','10.resenas_productos.csv','11.historial_pagos.csv']:
            df = load_csv(fname)
            df.columns = df.columns.str.strip().str.lower().str.replace(' ','_')
            df.to_csv(os.path.join(STAGING, 'stg_' + fname.replace('.csv','').replace('.','_') + '.csv'), index=False)
            print('Wrote', 'stg_' + fname.replace('.csv','').replace('.','_') + '.csv')

        print('Transform step finished.')
