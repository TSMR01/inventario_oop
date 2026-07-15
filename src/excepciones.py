class InventarioError(Exception):
    """Excepción base para errores relacionados con el inventario."""


class ProductoNoEncontradoError(InventarioError):
    """Se produce cuando no existe el producto solicitado."""


class CantidadInvalidaError(InventarioError):
    """Se produce cuando la cantidad de venta no es válida."""


class StockInsuficienteError(InventarioError):
    """Se produce cuando no existe stock suficiente para una venta."""