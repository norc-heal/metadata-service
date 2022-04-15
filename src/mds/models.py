from gino.ext.starlette import Gino
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy import Integer, Sequence

from . import config

db = Gino(
    dsn=config.DB_DSN,
    pool_min_size=config.DB_POOL_MIN_SIZE,
    pool_max_size=config.DB_POOL_MAX_SIZE,
    echo=config.DB_ECHO,
    ssl=config.DB_SSL,
    use_connection_for_request=config.DB_USE_CONNECTION_FOR_REQUEST,
    retry_limit=config.DB_RETRY_LIMIT,
    retry_interval=config.DB_RETRY_INTERVAL,
)


class Metadata(db.Model):
    __tablename__ = "metadata"

    id_sec = Sequence(__tablename__ + "_id_seq")
    guid = db.Column(db.Unicode(), primary_key=True)
    id = db.Column(Integer, id_sec, server_default=id_sec.next_value())
    data = db.Column(JSONB())
