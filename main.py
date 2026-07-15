import sqlite3

from src.dao import ProductoDAO
from src.db import crear_tabla
from src.excepciones import (
    CantidadInvalidaError,
    ProductoNoEncontradoError,
    StockInsuficienteError
)
from src.modelo import Producto
from src.servicio import InventarioService


def ejecutar_demo() -> None:
    crear_tabla()

    dao = ProductoDAO()
    servicio = InventarioService(dao)

    try:
        producto = Producto(
            nombre="Mouse",
            precio=250,
            stock=3
        )

        dao.guardar(producto)

        print("Producto guardado:")
        print(producto)

        print("\nIntentando vender 10 unidades...")
        servicio.vender(producto.id, 10)

    except StockInsuficienteError as error:
        print(f"Excepción de negocio: {error}")

    except ProductoNoEncontradoError as error:
        print(f"Producto no encontrado: {error}")

    except CantidadInvalidaError as error:
        print(f"Cantidad inválida: {error}")

    except ValueError as error:
        print(f"Valor inválido: {error}")

    except sqlite3.Error as error:
        print(f"Error de base de datos: {error}")

    except Exception as error:
        print(f"Error inesperado: {error}")


if __name__ == "__main__":
    ejecutar_demo()