from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import config

db_connection_string = "mysql+pymysql://{}:{}@{}:{}/{}".format(
    config.get('DB_USER'),
    config.get('DB_PASS'),
    config.get('DB_HOST'),
    config.get('DB_PORT'),
    config.get('DB_NAME'))

engine = create_engine(db_connection_string, convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()
