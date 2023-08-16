from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import engine, meta_data

trailers = Table("trailer", meta_data,
              Column("id", Integer, primary_key=True),
              Column("trailer_type", String(255), nullable=False),
              Column("number_plate", String(50), nullable=False),
              Column("capacity", String(50), nullable=False),
              Column("status", String(50), nullable=False),
              Column("cargo_type", String(255), nullable=False))

meta_data.create_all(engine)