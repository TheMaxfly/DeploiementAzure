# from sqlmodel import create_engine, Session
# import sqlmodel

# # Define the database URL
# DATABASE_URL = "sqlite:///./app/db.sqlite3"

# # Create a database engine
# engine = create_engine(DATABASE_URL, echo=True, connect_args={"check_same_thread": False})

# def get_db():
#     """
#     Provides a database session for dependency injection.

#     Yields:
#         Session: A database session.
#     """
#     with Session(engine) as session:
#         yield session

from sqlmodel import SQLModel, create_engine, Session
import os
from dotenv import load_dotenv
import sqlmodel

# Charger les variables d'environnement
load_dotenv()

DB_SERVER = os.getenv('DB_SERVER')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')

# Chaîne de connexion MSSQL pour SQLModel
DATABASE_URL = f"mssql+pyodbc://{DB_USER}:{DB_PASSWORD}@{DB_SERVER}/{DB_NAME}?driver=ODBC+Driver+18+for+SQL+Server"
print(DATABASE_URL)

# Création du moteur SQLAlchemy compatible avec SQLModel
engine = create_engine(DATABASE_URL, echo=True)

# Fonction de dépendance FastAPI pour obtenir une session
def get_db():
    with Session(engine) as session:
        yield session