from sqlalchemy import create_engine
import pandas as pd
from utils.custom_error import CustomError

class Database:
  def __init__(self, user, password, db_name, file, table_name, host = "localhost"):
    self.user = user
    self.password = password
    self.db_name = db_name
    self.host = host
    self.file = pd.read_csv(file)
    self.table_name = table_name
    self.engine = None
    self.custom_error = CustomError()
    
  def create_db_on_postgres(self):
    self.engine = create_engine(f'postgresql+psycopg2://{self.user}:{self.password}@{self.host}:5432/{self.db_name}')
    
    try:
      self.__transform_to_sql(self.engine)
    except:
      return self.custom_error.error("Error on db creation");
    
  def create_db_on_mysql(self):
    pass
    
  def create_db_on_sql_server(self):
    pass
    
  def create_db_on_sqlite(self):
    pass
    
  def create_db_on_oracle(self):
    pass
  
  def __transform_to_sql(self, engine):
    self.file.to_sql(self.table_name, engine, index=False, if_exists='fail')
    
  def test_conn(self, engine_selection):
    if engine_selection == "Postgres":
      self.engine = create_engine(f'postgresql+psycopg2://{self.user}:{self.password}@{self.host}:5432/{self.db_name}')
    
    try:
      conn = self.engine.connect()
      conn.close()
      return True
    except:
      return False