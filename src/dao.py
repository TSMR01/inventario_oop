import sqlite3

from src.db import get_connection
from src.modelo import Producto


class ProductoDAO:
    def guardar(self, producto: Producto) -> Producto:
        consulta = """
            INSERT INTO productos (nombre, precio, stock)
            VALUES (?, ?, ?)
        """

        try:
            with get_connection() as conexion:
                cursor = conexion.execute(
                    consulta,
                    (
                        producto.nombre,
                        producto.precio,
                        producto.stock
                    )
                )

                conexion.commit()
                producto.id = cursor.lastrowid

            return producto

        except sqlite3.Error as error:
            raise sqlite3.DatabaseError(
                f"No fue posible guardar el producto: {error}"
            ) from error

    def buscar_por_id(self, producto_id: int) -> Producto | None:
        consulta = """
            SELECT id, nombre, precio, stock
            FROM productos
            WHERE id = ?
        """

        try:
            with get_connection() as conexion:
                fila = conexion.execute(
                    consulta,
                    (producto_id,)
                ).fetchone()

            if fila is None:
                return None

            return Producto(
                producto_id=fila["id"],
                nombre=fila["nombre"],
                precio=fila["precio"],
                stock=fila["stock"]
            )

        except sqlite3.Error as error:
            raise sqlite3.DatabaseError(
                f"No fue posible buscar el producto: {error}"
            ) from error

    def actualizar(self, producto: Producto) -> None:
        consulta = """
            UPDATE productos
            SET nombre = ?, precio = ?, stock = ?
            WHERE id = ?
        """

        try:
            with get_connection() as conexion:
                cursor = conexion.execute(
                    consulta,
                    (
                        producto.nombre,
                        producto.precio,
                        producto.stock,
                        producto.id
                    )
                )

                if cursor.rowcount == 0:
                    raise ValueError(
                        f"No existe un producto con id {producto.id}"
                    )

                conexion.commit()

        except sqlite3.Error as error:
            raise sqlite3.DatabaseError(
                f"No fue posible actualizar el producto: {error}"
            ) from error