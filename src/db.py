import os
import sqlite3
from pathlib import Path

from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

DB_NAME = os.getenv("DB_NAME", "inventario.db")
DB_PATH = BASE_DIR / DB_NAME


def get_connection() -> sqlite3.Connection:
    conexion = sqlite3.connect(DB_PATH)
    conexion.row_factory = sqlite3.Row
    return conexion


def crear_tabla() -> None:
    consulta = """
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            precio REAL NOT NULL CHECK (precio > 0),
            stock INTEGER NOT NULL CHECK (stock >= 0)
        )
    """

    with get_connection() as conexion:
        conexion.execute(consulta)
        conexion.commit()