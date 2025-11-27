\
        \"\"\"Extract step: copy CSVs from local Windows paths into project data/raw/ folder.
        Adjust source paths if needed.
        \"\"\"
        import os
        import shutil

        RAW_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'raw')
        os.makedirs(RAW_DIR, exist_ok=True)

        # List of source files (user-provided). Update if paths differ.
        sources = [
            r"C:\Users\luisb\Desktop\DE M2-0\1.Usuarios.csv",
            r"C:\Users\luisb\Desktop\DE M2-0\2.Categorias.csv",
            r"C:\Users\luisb\Desktop\DE M2-0\3.Productos.csv",
            r"C:\Users\luisb\Desktop\DE M2-0\4.ordenes.csv",
            r"C:\Users\luisb\Desktop\DE M2-0\5.detalle_ordenes.csv",
            r"C:\Users\luisb\Desktop\DE M2-0\6.direcciones_envio.csv",
            r"C:\Users\luisb\Desktop\DE M2-0\7.carrito.csv",
            r"C:\Users\luisb\Desktop\DE M2-0\8.metodos_pago.csv",
            r"C:\Users\luisb\Desktop\DE M2-0\9.ordenes_metodospago.csv",
            r"C:\Users\luisb\Desktop\DE M2-0\10.resenas_productos.csv",
            r"C:\Users\luisb\Desktop\DE M2-0\11.historial_pagos.csv"
        ]

        for src in sources:
            if os.path.exists(src):
                dst = os.path.join(RAW_DIR, os.path.basename(src))
                shutil.copy2(src, dst)
                print(f'Copied {src} -> {dst}')
            else:
                print(f'NOT FOUND: {src}')
        print('Extract step finished.')
