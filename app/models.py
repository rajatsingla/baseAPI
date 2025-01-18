import os
from urllib.parse import urlparse
from apphelpers.db.peewee import create_pgdb_pool, create_base_model
from apphelpers.db.peewee import created, dbtransaction
from converge import settings

# Below import is required
import peeweedbevolve


db_url = os.environ.get('DATABASE_URL')
if db_url:
    result = urlparse(db_url)
    db = create_pgdb_pool(
        database=result.path[1:],
        host=result.hostname,
        user=result.username,
        password=result.password,
        max_connections=settings.DB_MAXCONNECTIONS,
    )
else:
    db = create_pgdb_pool(
        database=settings.DB_NAME,
        host=settings.DB_HOST,
        user=settings.DB_USER,
        password=settings.DB_PASSWORD,
        max_connections=settings.DB_MAXCONNECTIONS,
    )


dbtransaction = dbtransaction(db)
BaseModel = create_base_model(db)


class CommonModel(BaseModel):
    created = created()

    class Meta:
        legacy_table_names = False

