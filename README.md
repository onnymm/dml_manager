## Manejador de transacciones con PostgreSQL

Esta librería realiza las transacciones de `CREATE`, `SELECT`, `UPDATE` y `DELETE` así como algunos otros métodos comunes útiles para la gestión del CRUD en una aplicación.

Instalación:
```bash
pip install git+https://github.com/onnymm/dml_manager.git
```

### Uso
Primeramente se deben inicializar los modelos de tabla adecuados y los siguientes campos
comunes en la clase `_Base`:
```py
from sqlalchemy.orm import DeclarativeBase, ...

class _Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(Integer, primary_key= True)
    create_date: Mapped[DateTime] = mapped_column(DateTime, default= datetime.now)
    write_date: Mapped[DateTime] = mapped_column(DateTime, default= datetime.now, onupdate=datetime.now)

class Users(_Base):
    __tablename__ = 'users'
    user: Mapped[str] = mapped_column(String(24), nullable= False, unique= True)
    name: Mapped[str] = mapped_column(String(60), nullable= False)
```

Después se crea una instancia de conexión:
```py
db_connection = DMLManager(
    'postgresql+psycopg2://postgres:somepassword123@my-database-url.com:5432/production_database',
    _Base,
)
```

La conexión también se puede inicializar utilizando variables de entorno
usando los siguientes nombres:
```env
DB_HOST = my-database-url.com
DB_PORT = 5432
DB_NAME = production_database
DB_USER = postgres
DB_PASSWORD = somepassword123
```

Posteriormente creando la instancia de la siguiente forma:
```py
db_connection = DMLManager(
    'env',
    _Base,
)
```

Finalmente también se puede proporcionar un diccionario que contenga las
credenciales de conexión:
```py
db_credentials = {
    'host': 'my-database-url.com',
    'port': 5432,
    'db_name': 'production_database',
    'user': 'postgres',
    'password': 'somepassword123',
}

db_connection = DMLManager(
    db_credentials,
    _Base,
)
```
