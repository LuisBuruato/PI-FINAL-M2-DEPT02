{% snapshot snapshot_cliente %}

{{
    config(
        target_schema='dbo',
        unique_key='id_usuario',
        strategy='check',
        check_cols=['nombre_usuario', 'email_usuario', 'fecha_registro']
    )
}}

select *
from {{ ref('stg_usuarios') }}

{% endsnapshot %}









