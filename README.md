# Frozen Inventory [WIP]

## Introducción

 Frozen Inventory es un sistema de inventario para una empresa, que permite llevar un control de los productos que se encuentran en el almacén, así como de los productos que se encuentran en tránsito. Además, permite llevar un control de los pedidos que se han realizado a los proveedores y de los pedidos que se han realizado a los clientes.




## Tecnologías utilizadas

- Python
- FastAPI
- Next.js
- TypeScript
- PostgreSQL
- Alembic

## Instalación


### Instalación de dependencias

Para instalar las dependencias del backend, ejecutar el siguiente comando:

```bash
cd back
pip install -r requirements.txt
```

Para instalar las dependencias del frontend, ejecutar el siguiente comando:

```bash
cd front
npm install
```

### Configuración de la base de datos

Para configurar la base de datos, se debe crear un archivo `.env` en la carpeta `back` con el siguiente contenido:

```bash
DB_HOST=
DB_PORT=
DB_USER=
DB_PASSWORD=
DB_NAME=
```

### Ejecución

Para ejecutar el backend, ejecutar el siguiente comando:

```bash
cd back/app
uvicorn main:app --reload
```

Para ejecutar el frontend, ejecutar el siguiente comando:

```bash
cd front
npm run dev
```

## Colaboradores

- [Lucas Oyarzún](https://github.com/LucasOyarzun)
- [Cristóbal Saldías](https://github.com/CherryStopher)



<!-- 
Para crear una migración, utlizar el comando `alembic revision -m "migration name"`

Para cargar toda la base de datos, utilizar el comando `alembic upgrade head`

Para hacer rollback de la base de datos, utilizar el comando `alembic downgrade -1` -->