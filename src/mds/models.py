from datetime import datetime
from gino.ext.starlette import Gino
from sqlalchemy import BigInteger, Column, DateTime, String
from sqlalchemy.dialects.postgresql import ARRAY, JSONB

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

    guid = Column(db.Unicode(), primary_key=True)
    data = Column(JSONB())


# TODO https://ctds-planx.atlassian.net/browse/PXP-6555 add DRS fields
class FileObject(db.Model):
    __tablename__ = "file_objects"

    did = Column(String, primary_key=True)
    baseid = Column(String, index=True)
    rev = Column(String)
    form = Column(String)
    size = Column(BigInteger, index=True)
    created_date = Column(DateTime, default=datetime.utcnow)
    updated_date = Column(DateTime, default=datetime.utcnow)
    file_name = Column(String, index=True)
    version = Column(String, index=True)
    uploader = Column(String, index=True)
    urls = Column(ARRAY(String))
    urls_metadata = Column(JSONB())
    acl = Column(ARRAY(String))
    authz = Column(ARRAY(String))
    hashes = Column(JSONB())
    metadata = Column(JSONB())

    # TODO alias array
    # name = Column(String, primary_key=True, unique=True)
