import unittest
from unittest.mock import Mock

from src.excepciones import (
    CantidadInvalidaError,
    StockInsuficienteError
)
from src.modelo import Producto
from src.servicio import InventarioService


class TestInventarioService(unittest.TestCase):
    def setUp(self):
        self.dao_mock = Mock()
        self.servicio = InventarioService(self.dao_mock)

    def test_vender_producto_correctamente(self):
        producto = Producto(
            producto_id=1,
            nombre="Mouse",
            precio=250,
            stock=5
        )

        self.dao_mock.buscar_por_id.return_value = producto

        resultado = self.servicio.vender(1, 2)

        self.assertEqual(resultado.stock, 3)
        self.dao_mock.actualizar.assert_called_once_with(producto)

    def test_vender_mas_del_stock_lanza_excepcion(self):
        producto = Producto(
            producto_id=1,
            nombre="Mouse",
            precio=250,
            stock=3
        )

        self.dao_mock.buscar_por_id.return_value = producto

        with self.assertRaises(StockInsuficienteError):
            self.servicio.vender(1, 10)

        self.dao_mock.actualizar.assert_not_called()

    def test_vender_cantidad_cero_lanza_excepcion(self):
        with self.assertRaises(CantidadInvalidaError):
            self.servicio.vender(1, 0)

        self.dao_mock.buscar_por_id.assert_not_called()


if __name__ == "__main__":
    unittest.main()