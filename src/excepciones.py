class InventarioError(Exception):
    """Excepción base para errores del inventario."""


class ProductoNoEncontradoError(InventarioError):
    """Se lanza cuando el producto solicitado no existe."""


class CantidadInvalidaError(InventarioError):
    """Se lanza cuando la cantidad de venta no es válida."""


class StockInsuficienteError(InventarioError):
    """Se lanza cuando no hay suficiente stock."""