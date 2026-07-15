import unittest

from src.modelo import Producto


class TestProducto(unittest.TestCase):
    def test_crear_producto_correctamente(self):
        producto = Producto("Teclado", 500, 10)

        self.assertEqual(producto.nombre, "Teclado")
        self.assertEqual(producto.precio, 500)
        self.assertEqual(producto.stock, 10)

    def test_precio_negativo_lanza_value_error(self):
        with self.assertRaisesRegex(
            ValueError,
            "El precio debe ser mayor a 0"
        ):
            Producto("Mouse", -50, 5)

    def test_stock_negativo_lanza_value_error(self):
        with self.assertRaisesRegex(
            ValueError,
            "El stock no puede ser negativo"
        ):
            Producto("Monitor", 3500, -1)


if __name__ == "__main__":
    unittest.main()