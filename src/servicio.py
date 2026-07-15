from src.dao import ProductoDAO
from src.excepciones import (
    CantidadInvalidaError,
    ProductoNoEncontradoError,
    StockInsuficienteError
)


class InventarioService:
    def __init__(self, producto_dao: ProductoDAO):
        self.producto_dao = producto_dao

    def vender(self, producto_id: int, cantidad: int):
        if cantidad <= 0:
            raise CantidadInvalidaError(
                "La cantidad de venta debe ser mayor a 0"
            )

        producto = self.producto_dao.buscar_por_id(producto_id)

        if producto is None:
            raise ProductoNoEncontradoError(
                f"No existe un producto con id {producto_id}"
            )

        if cantidad > producto.stock:
            raise StockInsuficienteError(
                f"Stock insuficiente. Disponible: {producto.stock}, "
                f"solicitado: {cantidad}"
            )

        producto.stock -= cantidad
        self.producto_dao.actualizar(producto)

        return producto